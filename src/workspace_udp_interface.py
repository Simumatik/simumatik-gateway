import json
import logging
import socket
import time
import enum

from drivers import *

POLL_TIME = 1 # seconds
MINIMUM_SYNC_PERIOD = 0.002
STANDBY_SYNC_PERIOD = 0.1
MAX_SYNC_TELEGRAM = 10000
MAX_TELEGRAM_LENGTH = 2**16


class WorkspaceCommand(str, enum.Enum):
    SETUP = 'SETUP'
    CLEAN = 'CLEAN'
    SYNC = 'SYNC'
    STATUS = 'STATUS'
    INFO = "INFO"
    VAR_INFO = "VAR_INFO"
    REGISTER = 'REGISTER'
    POLLING = 'POLLING'
    UNKNOWN = 'UNKNOWN'
    
class WorkspaceUDPInterface():
    
    def __init__(self, disable_poll_check:bool=False, log_level:int=logging.ERROR) -> None:
        self._logger = logging.getLogger('WorkspaceInterface')
        self._logger.setLevel(log_level)
        if not self._logger.handlers: self._logger.addHandler(logging.StreamHandler())
        self.udp_socket = None
        self.server_address = None
        self.sync_mode = False
        self.sync_period = STANDBY_SYNC_PERIOD
        self.sync_telegrams = {}
        self.sync_telegram_counter = 0
        self.sync_last_telegram = 0
        self.message_id = 0
        self.last_poll_sent = 0
        self.last_message_received = 0
        self.last_processed_update = 0
        self.loop_counter = 0
        self._disable_poll_check = disable_poll_check

    def get_new_message_id(self):
        ''' 
        Provides a new message id.
        '''
        if self.message_id > 1e4:
            self.message_id = 1
        else:
            self.message_id += 1
        return self.message_id
    
    def connect(self, ip:str, port:int, version:str):
        try:
            self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.udp_socket.settimeout(POLL_TIME*4)
            self.server_address = (ip, port)
        except Exception as e:
            self._logger.error(f'WorkspaceInterface: Exception during setup: {e}')
            self.udp_socket = None
            return False
        drivers_list = {}
        for driver_name, (_, driver_version) in registered_drivers.items():
            drivers_list.update({driver_name:{'version':driver_version}})
        self.send_telegram(
            telegram_id=0, 
            command=WorkspaceCommand.REGISTER,
            data={
                "SERVER_KEY": 'server key obtained from the user',
                "GATEWAY": {
                    "VERSION": version,
                    "HEARTBEAT": POLL_TIME,
                },
                "DRIVERS": drivers_list
            })
        try:
            for _, command, data in self.receive_telegrams():
                if command == WorkspaceCommand.REGISTER:
                    if data in ['SUCCESS', 'SUCCESS_SYNC', 'SUCCESS_ASYNC']:
                        self.udp_socket.setblocking(0)
                        self.last_poll_sent = time.perf_counter()
                        self.last_message_received = time.perf_counter()
                        self._logger.info(f'WorkspaceInterface: Gateway connected to workspace -> {self.server_address}')
                        return True
                    else:
                        self._logger.error(f'WorkspaceInterface: Workspace refused gateway connection with status: {data}')
                else:
                    self._logger.error("WorkspaceInterface: Datagram id or ip does not match")
        except Exception as e:
            self._logger.error(f"WorkspaceInterface: Invalid json datagram received: {e}")  
        return False
    
    def disconnect(self):
        if self.udp_socket:
            self.udp_socket.close()
        self._logger.info(f'WorkspaceInterface: Gateway disconnected from workspace -> {self.server_address}')
        self.udp_socket = None
    
    def check_connection(self, stats:dict={}) -> tuple:
        self.loop_counter += 1
        now = time.perf_counter()
        if (now-self.last_poll_sent) >= POLL_TIME:
            try:
                polling_data = {
                    "LAST_PROC_UPDATE": self.last_processed_update, 
                    "SYNC_PERIOD": self.sync_period, 
                    "CYCLES": round(1000/self.loop_counter,2), # Latency in ms
                    }
                polling_data.update(stats)
                self.send_telegram(telegram_id=self.get_new_message_id(), command=WorkspaceCommand.POLLING, data=polling_data)
                self.last_poll_sent = now
                self.loop_counter = 0
                for id in list(self.sync_telegrams.keys()):
                    if id < self.sync_telegram_counter:
                        self.sync_telegrams.pop(id)
            except:
                self._logger.error(f'WorkspaceInterface: Exception sending polling telegram!')
                return (False, 'Exception sending polling telegram')     
        if (now-self.last_message_received)>(4*POLL_TIME) and not self._disable_poll_check:
            self._logger.error(f'WorkspaceInterface: Polling msg was not received on time!')
            return (False, "Polling msg was not received on time")
        return (True, '')   
    
    def ready_for_sync_telegram(self) -> bool:
        return (time.perf_counter()-self.sync_last_telegram>=self.sync_period)
    
    def send_sync_telegram(self, data:dict={}):
        self.sync_telegram_counter = self.sync_telegram_counter + 1 if self.sync_telegram_counter<MAX_SYNC_TELEGRAM else 1             
        self.send_telegram(telegram_id=self.sync_telegram_counter, command="SYNC", data=data)
        self.sync_last_telegram = time.perf_counter()
        self.sync_telegrams[self.sync_telegram_counter] = self.sync_last_telegram
    
    def calculate_sync_period(self, telegram_id:int, min_sync_period:float):
        self.last_processed_update = telegram_id
        if telegram_id in self.sync_telegrams:
            sent_time = self.sync_telegrams.pop(telegram_id)
            delta = (self.last_message_received-sent_time)
            last_period = max(delta * 0.5, min_sync_period)
            self.sync_period = self.sync_period * 0.9 + last_period * 0.1

    def send_telegram(self, telegram_id:int=0, command:WorkspaceCommand=WorkspaceCommand.CLEAN, data:dict=None):
        if telegram_id == 0: telegram_id = self.get_new_message_id()
        msg = {"ID": telegram_id, "COMMAND":command}
        if data is not None:
            msg.update({"DATA": data})
        telegram = json.dumps(msg).encode('utf8')
        if len(telegram)<MAX_TELEGRAM_LENGTH:
            self.udp_socket.sendto(telegram, self.server_address)
            if data and command!=WorkspaceCommand.POLLING:
                self._logger.debug(f'WorkspaceInterface: Telegram sent to {self.server_address}: {telegram}')
        else:
            self._logger.error(f'WorkspaceInterface: Message to Workspace is too long! Length = {len(telegram)}')
    
    def receive_telegrams(self, min_sync_period:float=STANDBY_SYNC_PERIOD):
        try:
            while True:
                telegram, address = self.udp_socket.recvfrom(MAX_TELEGRAM_LENGTH)
                assert address == self.server_address
                if telegram != None:
                    self.last_message_received = time.perf_counter()
                    request_json = json.loads(telegram.decode('utf-8'))
                    command = request_json.get("COMMAND", '')
                    if command != WorkspaceCommand.POLLING:
                        telegram_id = request_json.get("ID")
                        data = request_json.get("DATA", {})
                        if command == WorkspaceCommand.SYNC:
                            self.calculate_sync_period(telegram_id, min_sync_period)
                        if data:
                            self._logger.debug(f'WorkspaceInterface: Telegram received from {address}: {telegram}')
                        yield (telegram_id, command, data)
        except:
            pass        