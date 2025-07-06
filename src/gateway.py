# Simumatik Gateway - Simumatik 3rd party integration tool
# Copyright (C) 2021 Simumatik AB
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import logging
import multiprocessing
import enum
import sys
import threading
import time
import socket
import os

DEBUG_DRIVER_MANAGER = False
if DEBUG_DRIVER_MANAGER:
    # Make sure to uninstall the driver-manager package when testing against the local commit
    # Remove package: pip uninstall simumatik-driver-manager
    # Clone repo: git clone https://github.com/Simumatik/simumatik-driver-manager.git
    # Reinstall package: pip install --upgrade -r .\requirements
    sys.path.append("simumatik-driver-manager")
    
from driver_manager.driver_manager import RunDriverManager, DriverMgrCommands
from gateway_ws_interface import GatewayWsInterface, GatewayWsCommands
from workspace_udp_interface import WorkspaceUDPInterface, WorkspaceCommand, MINIMUM_SYNC_PERIOD, STANDBY_SYNC_PERIOD

# Version
version = "6.0.4"

MAX_PIPE_LOOPS = 10
'''
ACTUAL_PATH = os.path.dirname(os.path.abspath(__file__))
USER_PATH = os.path.expanduser('~')
if USER_PATH in ACTUAL_PATH:
    LOCAL_FOLDER = os.path.dirname(ACTUAL_PATH) # Works for different branches
else:
    LOCAL_FOLDER =  f"{USER_PATH}/Simumatik"
logging.basicConfig(filename=f"{LOCAL_FOLDER}/gateway.log",
                    filemode='w',
                    level=logging.ERROR, 
                    #format=FORMAT
                    )
'''

class GatewayStatus(str, enum.Enum):
    STANDBY = 'standby'
    CONNECTED = 'connected'
    ERROR = 'error'
    EXIT = 'exit'

class gateway():

    def __init__(self, use_processes:bool=False, log_level:int=logging.ERROR, status_file_path:str=''):
        """
        :param use_processes: Allows to use processes instead of threads for drivers.
            it will have impact in performance and used resources

        :param log_level: Sets the logging level.

        Simumatik Communication Gateway
        """
        self._logger = logging.getLogger('Gateway')
        self._logger.setLevel(log_level)
        if not self._logger.handlers: self._logger.addHandler(logging.StreamHandler())
        self._log_level = log_level
        self._status_file_path = status_file_path
        self._use_processes = use_processes
        self._connected_workspace_ip = None
        self._workspace_interface = None
        self._ws_interface = None
        self._driver_manager = None
        self._DM_stats = {'SLEEP_TIME':0}
        
    def run(self, ws_ip:str='0.0.0.0', ws_port:int=2323):
        ''' 
        Main loop
        '''
        self._logger.info(f"Gateway version {version} started. (Using processes={self._use_processes})")
        self.status = GatewayStatus.STANDBY
        self.error_msg = ''
        if not self.startWSInterface(ws_ip, ws_port):
            self.status = GatewayStatus.EXIT
        while self.status != GatewayStatus.EXIT:
            self.wsStateMahine()
            if self.status == GatewayStatus.CONNECTED:
                can_sleep = True
                # INCOMMING TELEGRAMS FROM WORKSPACE
                counter = 0
                for (telegram_id, command, data) in self._workspace_interface.receive_telegrams(MINIMUM_SYNC_PERIOD if self._driver_manager is not None else STANDBY_SYNC_PERIOD):
                    if WorkspaceCommand.SETUP == command:
                        if self._driver_manager is None: self.startDriverManager()
                        self._DM_pipe.send((DriverMgrCommands.SETUP_DRIVERS, data))
                    elif WorkspaceCommand.SYNC == command:
                        if self._driver_manager and data:
                            self._pending_writes.update(data)
                    elif WorkspaceCommand.CLEAN == command:
                        if self._driver_manager is not None: self.stopDriverManager()
                        self._workspace_interface.send_telegram(telegram_id=telegram_id, command=WorkspaceCommand.CLEAN, data='SUCCESS')
                    else:
                        self._logger.error(f"Gateway: Unknown command received: {command} -> {data}")
                    can_sleep = False
                    counter += 1
                    if counter >= MAX_PIPE_LOOPS: break                    
                # INCOMING/OUTGOING DATA FROM/TO DRIVER MANAGER
                if self._driver_manager:
                    if self._pending_writes:
                        self._DM_pipe.send((DriverMgrCommands.UPDATES, self._pending_writes))
                        self._pending_writes = {}
                    counter = 0
                    while self._DM_pipe.poll():
                        (command, data) = self._DM_pipe.recv()
                        if command == DriverMgrCommands.SETUP_DRIVERS:
                            self._workspace_interface.send_telegram(command=WorkspaceCommand.SETUP, data=data)
                        if command == DriverMgrCommands.UPDATES:
                            self._pending_reads.update(data)
                        elif command == DriverMgrCommands.STATUS:
                            self._workspace_interface.send_telegram(command=WorkspaceCommand.STATUS, data=data)                     
                        elif command == DriverMgrCommands.INFO:
                            self._workspace_interface.send_telegram(command=WorkspaceCommand.INFO, data=data)
                        elif command == DriverMgrCommands.VAR_INFO:
                            self._workspace_interface.send_telegram(command=WorkspaceCommand.VAR_INFO, data=data)
                        elif command == DriverMgrCommands.STATS:
                            self._DM_stats.update(data)
                            self._DM_stats['CPU_USSAGE'] = round((1-self._DM_stats['SLEEP_TIME'])*100,2)
                            self._DM_stats['SLEEP_TIME'] = 0
                        can_sleep = False
                        counter += 1
                        if counter >= MAX_PIPE_LOOPS: break                                  
                # OUTGOING TELEGRAMS TO WORKSPACE                             
                if self._workspace_interface.ready_for_sync_telegram():
                    if self._driver_manager:
                        self._workspace_interface.send_sync_telegram(self._pending_reads)
                        self._pending_reads = {}
                        can_sleep = False
                    else:
                        self._workspace_interface.send_sync_telegram()
                # SLEEP TO RELEASE CPU
                if can_sleep:
                    start = time.perf_counter()
                    time.sleep(1e-3)
                    self._DM_stats['SLEEP_TIME'] += (time.perf_counter() - start)
                # CHECK CONNECTION
                connected, self.error_msg = self._workspace_interface.check_connection(self._DM_stats)
                if not connected:
                    self.status = GatewayStatus.ERROR
            else:
                time.sleep(1e-3)
        self.stopWSInterface()
       
    def startWorkspaceInterface(self, ip:str='127.0.0.1') -> bool:
        """ 
        Starts Workspace UDP Connection
        
        :param ip: Workspace ip address.
        """  
        if self._workspace_interface is None:      
            self._workspace_interface = WorkspaceUDPInterface(disable_poll_check=False, log_level=self._log_level)
            if self._workspace_interface.connect(ip=ip, port=4844, version=version):
                self._connected_workspace_ip = ip
                return True
        self._connected_workspace_ip = None
        return False
    
    def stopWorkspaceInterface(self):
        """ 
        Stops Workspace UDP Connection
        """        
        if self._workspace_interface is not None:
            self._workspace_interface.disconnect()
        self._workspace_interface = None
        self._connected_workspace_ip = None
    
    def startDriverManager(self):
        """ 
        Starts Driver Manager
        """       
        if self._driver_manager is None:
            self._DM_pipe, pipe = multiprocessing.Pipe()
            self._DM_stats = {'SLEEP_TIME':0}
            self._driver_manager = threading.Thread(target=RunDriverManager, args=(pipe, self._use_processes, self._status_file_path,), daemon=True)
            self._driver_manager.start()
            self._pending_writes = {}
            self._pending_reads = {}
        else:
            self._logger.error("Gateway: DriverManager start requested when already started")
        
    def stopDriverManager(self):
        """ 
        Stops Driver Manager
        """
        if self._driver_manager is not None:
            self._logger.debug("Gateway: Cleaning request sent to DriverManager...")
            self._DM_pipe.send((DriverMgrCommands.CLEAN, None))
            while True:
                (command, result) = self._DM_pipe.recv()
                if command == DriverMgrCommands.CLEAN:
                    self._logger.debug(f"Gateway: Cleaning response received from DriverManager -> {result}")
                    break
            self._driver_manager = None
            self._DM_pipe = None
            self._logger.debug("Gateway: Cleaned up, DriverManager closed")
        else:
            self._logger.error("Gateway: DriverManager stop requested when already stopped")

    def startWSInterface(self, ip:str, port:int):
        """ 
        Starts Gateway WS Interface for getting messages from the App.
        
        :param ip: WS Server IP.

        :param port: WS Server Port.
        """        
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.bind((ip, port))
            s.close()
            self._logger.debug("Gateway: WS IP and Port check OK! Launching Websocket server...")
            self._WS_pipe, pipe = multiprocessing.Pipe()
            self._ws_interface = threading.Thread(target=GatewayWsInterface, args=(ip, port, pipe, self._log_level,), daemon=True)
            self._ws_interface.start()
            return True
        except Exception as e:
            # Log
            self._logger.error(f"Gateway: Exception opening {ip}:{port}: {e}")
            self._ws_interface = None 
            return False       
    
    def stopWSInterface(self):
        """ 
        Stops Gateway WS Interface.
        """
        if self._ws_interface:
            self._ws_interface = None

    def wsStateMahine(self) -> None:
        """ 
        Gateway WS Interface State machine.
        """
        if self._WS_pipe:
            if self._WS_pipe.poll():
                (command, req_data) = self._WS_pipe.recv()
                resp_data = {"status": "Wrong command"} 
                if command == GatewayWsCommands.CONNECT:
                    if self.status == GatewayStatus.STANDBY:
                        if self.startWorkspaceInterface(ip=req_data.get('url', '127.0.0.1')):
                            self.status = GatewayStatus.CONNECTED
                            resp_data = {"status": self.status, "ip": self._connected_workspace_ip}
                        else:
                            self.status = GatewayStatus.ERROR
                            self._workspace_interface = None
                            resp_data = {"status": self.status, "message": f"Connection with ip {self._connected_workspace_ip} cannot be established"}
                    else:
                        resp_data = {"status": "error", "message": "Gateway status is not STANDBY"}
                elif command == GatewayWsCommands.DISCONNECT:
                    if self.status == GatewayStatus.CONNECTED:
                        if self._driver_manager is not None: self.stopDriverManager()  
                        self.stopWorkspaceInterface()
                        self.status = GatewayStatus.STANDBY
                        resp_data = {"status": self.status}
                    else:
                        resp_data = {"status": self.status, "message": "Gateway status is not CONNECTED"}
                elif (command == GatewayWsCommands.RESET):
                    if self.status == GatewayStatus.ERROR:
                        if self._driver_manager is not None: self.stopDriverManager()
                        self.stopWorkspaceInterface()
                        self.status = GatewayStatus.STANDBY
                        self.error_msg = ''
                        resp_data = {"status": self.status}
                    else:
                        resp_data = {"status": self.status, "message": "Gateway status is not ERROR"}
                elif (command == GatewayWsCommands.STATUS):
                    resp_data = {"status": self.status, "ip": self._connected_workspace_ip if self._connected_workspace_ip != None else ""}
                    if self.status == GatewayStatus.ERROR:
                        resp_data.update({"message": self.error_msg})
                elif (command == GatewayWsCommands.VERSION):
                    resp_data = {"status": str(version)}
                if command is not None:
                    self._WS_pipe.send((command, resp_data))    

if __name__ == '__main__':
    multiprocessing.freeze_support()
    #print(sys.argv)
    STATUS_FILE_PATH = os.path.dirname(os.path.abspath(__file__))+'/Driver_Manager_status.txt'
    g = gateway(use_processes=False, log_level=logging.INFO, status_file_path=STATUS_FILE_PATH)
    g.run(ws_ip='0.0.0.0', ws_port=2323)