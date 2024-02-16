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

# Python functions
from logs import logger
import datetime
from enum import Enum
import json
from multiprocessing import Pipe
import socket
from threading import Thread
import time

# Specific libraries
from drivers import *
from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket


# Version
version = "4.4.1"

# Settings
poll_time = 1 # seconds
MINIMUM_SYNC_PERIOD = 0.002
STANDBY_SYNC_PERIOD = 0.1
MAX_SYNC_TELEGRAM = 10000

# Global
WebSocketConnections = []

# Gateway WebSocket Server
class WebSocket_server(WebSocket):

    # Every time a msg is received by the socket this is executed
    def handleMessage(self):
        # Log
        logger.debug('{} Message: {}'.format(self.address,self.data))
        # Send data
        self.msg_queue.append(self.data)
        
    # Every time a client is connected this is executed
    def handleConnected(self):
        # Log
        logger.debug('{} Connected'.format(self.address))
        # Append connection
        global WebSocketConnections
        WebSocketConnections.append(self)
        # Data queue
        self.msg_queue = []

    # Every time a client is disconnected this is executed
    def handleClose(self):
        # Log
        logger.debug('{} Close'.format(self.address))
        # Remove connection
        global WebSocketConnections
        WebSocketConnections.remove(self)

# WebSocket Thread method
def WebSocket_thread(ip, port):
    server = SimpleWebSocketServer(ip, port, WebSocket_server)
    server.serveforever()
    logger.error('Websocket server terminated!')

class GatewayStatus(int, Enum):
    STANDBY = 0
    CONNECTING = 1
    CONNECTED = 2
    ERROR = 5
    EXIT= 6

class gateway():
    '''
    Simumatik Communication Gateway
    '''

    def __init__(self):
        ''' Constructor '''
        # Get URL
        self.server_address = None
        self.sync_mode = False
        self.sync_period = STANDBY_SYNC_PERIOD
        self.sync_telegrams = {}
        self.sync_telegram_counter = 0
        self.sync_last_telegram = 0
        # UDP Telegrams
        self.udp_socket = None
        self.message_id = 0
        self.last_poll_sent = 0
        self.last_message_received = 0
        self.last_processed_update = 0
        self.loop_counter = 0
        # Emulation
        self.emulation_running = False
        # Drivers
        self.drivers = {} # {driver_object: pipe}
        self.handles = {} # {handle: (var_name, driver_object)}
        self.variables = {} # {driver_object: {var_name: [handles]}}
        self.driver_statuses = {} # {driver_handle: status}
        self.driver_infos = {} # {driver_handle: info}
        self.driver_updates = {} # {var_name: value}
        self.status = GatewayStatus.STANDBY
        self.error_msg = ''
        

    def get_datetime(self):
        ''' returns actual date and time as string.'''
        t = datetime.datetime.now()
        return t.strftime('%Y-%m-%d %H:%M:%S,%f')[:-3]


    def get_new_message_id(self):
        ''' Provides a new message id.'''
        if self.message_id > 1e4:
            self.message_id = 1
        else:
            self.message_id += 1
        return self.message_id


    def clean_drivers(self):
        """ Close all drivers."""
        self.handles = {}
        self.variables = {}
        self.driver_statuses = {}
        self.driver_infos = {}
        while self.drivers:
            driver_object, pipe = self.drivers.popitem()
            logger.debug('Cleaning driver: {}'.format(driver_object.name))
            pipe.send(json.dumps({DriverActions.EXIT: None}))


    def run(self, ip:str='0.0.0.0', port:int=2323):
        ''' Main loop'''

        # Launch Websocket server
        global WebSocketConnections
        try:
            # First test_cloud if port is not in use
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.bind((ip, port))
            s.close()
            # Log
            logger.debug("Port check OK! Launching Websocket server...")
            # Launch WebSocket Server
            t = Thread(target=WebSocket_thread, daemon=True, args=(ip,port, ))
            t.start()
        except Exception as e:
            # Log
            logger.error(f"Exception opening {ip}:{port}: {e}")
            raise Exception(f"Exception opening {ip}:{port}: {e}")

        # Loop
        logger.debug("SimumatikGateway " + version + " ready...")
        while self.status != GatewayStatus.EXIT:
            # Websocket interface
            self.doWebsocketInterface()
            # Driver running
            if self.status == GatewayStatus.CONNECTED:
                self.doRun()
            # Sleep
            else:
                time.sleep(1e-3)
    

    def close(self):
        ''' Exit Gateway'''
        self.status = GatewayStatus.EXIT

    def receive_telegram(self):
        data_length, address = self.udp_socket.recvfrom(4)
        data, address = self.udp_socket.recvfrom(int.from_bytes(data_length, "big"))
        #print("Message from Gateway", address, data)
        return data, address

    def send_telegram(self, telegram_id:int, command:str, data:dict=None):
        msg = {"ID": telegram_id, "COMMAND":command}
        if data is not None:
            msg.update({"DATA": data})
        telegram = json.dumps(msg).encode('utf8')
        self.udp_socket.sendto(len(telegram).to_bytes(4, 'big'), self.server_address)
        self.udp_socket.sendto(telegram, self.server_address)

    def doConnect(self):
        """ Executed to connect the gateway to the server."""
        now = time.perf_counter()
        try:
            # Create UDP socket
            self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            # Get implemented driver list
            drivers_list = {}
            for driver_name, (_, driver_version) in registered_drivers.items():
                drivers_list.update({driver_name:{'version':driver_version}})
            # Send REGISTER message
            self.send_telegram(
                telegram_id=0, 
                command="REGISTER",
                data={
                    "SERVER_KEY": 'server key obtained from the user',
                    "GATEWAY": {
                        "VERSION": version,
                        "HEARTBEAT": poll_time,
                    },
                    "DRIVERS": drivers_list
                })
        except Exception as e:
            self.doCleanup()
            self.status = GatewayStatus.ERROR
            self.error_msg = 'Exception during setup: '+str(e)
            logger.error(self.error_msg)
            raise Exception(self.error_msg)

        # Get response before defined timeout (4 x poll_time)
        self.udp_socket.settimeout(poll_time*4)
        try:
            data, address = self.receive_telegram()
            if data != None and address == self.server_address:
                response_json = json.loads(data.decode('utf-8'))
                if response_json.get("COMMAND", "") == "REGISTER" and response_json.get("DATA", 'FAILED') in ['SUCCESS', 'SUCCESS_SYNC', 'SUCCESS_ASYNC']:
                    # From now on, no timeout is set in the socket
                    self.sync_mode = response_json.get("DATA") == 'SUCCESS_SYNC'
                    self.udp_socket.setblocking(0)
                    self.last_poll_sent = now
                    self.last_message_received = now
                    self.status = GatewayStatus.CONNECTED
                    logger.debug("Gateway connected")
                    return
                else:
                    logger.debug("Datagram id or ip does not match")
        except Exception as e:
            logger.debug("Invalid json datagram received: " + str(e))
        # Connection failed
        self.status = GatewayStatus.ERROR


    def doCleanup(self):
        """ Executed to setup the driver."""
        try:
            # Clean drivers
            self.clean_drivers()
            # Clean gateway
            if self.udp_socket:
                self.udp_socket.close()
            self.udp_socket = None
            self.server_address = None
            self.message_id = 0 
            self.sync_telegrams = {}
            self.sync_period = STANDBY_SYNC_PERIOD
            self.sync_last_telegram = 0
            self.sync_telegram_counter = 0
            self.driver_updates = {}
        except Exception as e:
            logger.error('Exception during cleanup: '+str(e))
            

    def doRun(self):
        """ Executed while gateway is connected."""
        # Flag if sleep is needed
        needs_sleep = True
        self.loop_counter += 1

        # Send polling message within the interval
        if (time.perf_counter()-self.last_poll_sent) >= poll_time:
            try:
                polling_data = {
                    "LAST_PROC_UPDATE": self.last_processed_update, 
                    "SYNC_PERIOD": self.sync_period, 
                    "DRIVER_COUNT": len(self.drivers),
                    "CYCLES": round(1000/self.loop_counter,2),
                    }
                self.send_telegram(telegram_id=self.get_new_message_id(), command="POLLING", data=polling_data)
                self.last_poll_sent = time.perf_counter()
                needs_sleep = False
                self.loop_counter = 0
                #print(self.sync_period, self.sync_telegrams)
                # Clean lost sync packages
                for id in list(self.sync_telegrams.keys()):
                    if id < self.sync_telegram_counter:
                        self.sync_telegrams.pop(id)
            except:
                self.status = GatewayStatus.ERROR
                self.error_msg = 'Exception sending polling telegram'
                logger.error(self.error_msg)
                return

        # Check incomming telegrams
        try:
            while True:
                data, address = self.receive_telegram()
                # Process data if data received and address is valid 
                if (data != None and address == self.server_address):
                    self.last_message_received = time.perf_counter()
                    request_json = json.loads(data.decode('utf-8'))
                    telegram_id = request_json.get("ID")
                    telegram_command = request_json.get("COMMAND", '')
                    telegram_data = request_json.get("DATA", None)
                    if 'SETUP' == telegram_command:
                        result = self.do_driver_setup(telegram_data)
                        self.send_telegram(telegram_id=telegram_id, command='SETUP', data=result)
                    elif 'CLEAN' == telegram_command:
                        self.clean_drivers()
                        self.send_telegram(telegram_id=telegram_id, command='CLEAN', data='SUCCESS')
                        # Clean telegram pipe
                        if not self.sync_mode:
                            while True:
                                try:
                                    data, address = self.receive_telegram()
                                except:
                                    break
                    elif 'UPDATE' == telegram_command:
                        self.last_processed_update = telegram_id
                        res = self.do_driver_updates(telegram_data)
                    elif 'SYNC' == telegram_command:
                        self.last_processed_update = telegram_id
                        if telegram_id in self.sync_telegrams:
                            sent_time = self.sync_telegrams.pop(telegram_id)
                            delta = (time.perf_counter()-sent_time)
                            last_period = max(delta * 0.5, MINIMUM_SYNC_PERIOD if len(self.drivers) else STANDBY_SYNC_PERIOD)
                            #print(f"SYNC received with ID {self.sync_telegram_counter}, {delta}")
                            self.sync_period = self.sync_period * 0.9 + last_period * 0.1
                        if telegram_data:
                            res = self.do_driver_updates(telegram_data)
                    elif 'POLLING' == telegram_command:
                        pass
                    needs_sleep = False
        except:
            # No data received
            pass

        # Check receiving messages: Any received message is valid to consider connection alive
        if (time.perf_counter()-self.last_message_received)>(4*poll_time):
            self.status = GatewayStatus.ERROR
            self.error_msg = "Polling msg was not received on time"
            logger.error(self.error_msg)
            return

        # Check updates from drivers
        try:
            var_info = {}
            for driver_object, pipe in self.drivers.items():
                if driver_object.is_alive() and pipe:
                    while pipe.poll():
                        action, data = json.loads(pipe.recv()).popitem()
                        
                        if action == DriverActions.UPDATE:
                            logger.debug(f'Driver {driver_object.name} output data updated: {data}')
                            for var_name, var_value in data.items():
                                for handle in self.variables[driver_object][var_name]:
                                    self.driver_updates[handle] = var_value
                            
                        elif action == DriverActions.STATUS:
                            logger.debug(f'Driver {driver_object.name} status changed: {data}')
                            for driver_handle in driver_object.handles:
                                self.driver_statuses[driver_handle] = data                            

                        elif action == DriverActions.INFO:
                            logger.debug(f'Driver {driver_object.name} debug info: {data}')
                            for driver_handle in driver_object.handles:
                                self.driver_infos[driver_handle] = data

                        elif action == DriverActions.VAR_INFO:
                            (var_data, var_name) = data
                            logger.debug(f'Driver {driver_object.name} variable {var_name} debug info: {data}')
                            for handle in self.variables[driver_object][var_name]:
                                var_info[handle] = var_data
                            
                        needs_sleep = False

            # Send telegrams ASYNC
            if not self.sync_mode:
                if self.driver_updates:               
                    self.send_telegram(telegram_id=self.get_new_message_id(), command="UPDATE", data=self.driver_updates)
                    self.driver_updates = {}

            # Send telegrams SYNC
            if self.sync_mode and (time.perf_counter()-self.sync_last_telegram>=self.sync_period):
                if self.driver_updates:  
                    self.sync_telegram_counter = self.sync_telegram_counter + 1 if self.sync_telegram_counter<MAX_SYNC_TELEGRAM else 1             
                    self.send_telegram(telegram_id=self.sync_telegram_counter, command="SYNC" if self.sync_mode else "UPDATE", data=self.driver_updates)
                    #print(f"SYNC sent with ID {self.sync_telegram_counter}")
                    self.sync_last_telegram = time.perf_counter()
                    self.sync_telegrams[self.sync_telegram_counter] = time.perf_counter()
                    self.driver_updates = {}
                elif self.sync_mode:
                    self.sync_telegram_counter = self.sync_telegram_counter + 1 if self.sync_telegram_counter<MAX_SYNC_TELEGRAM else 1
                    self.send_telegram(telegram_id=self.sync_telegram_counter, command="SYNC", data={})
                    #print(f"SYNC sent with ID {self.sync_telegram_counter}")
                    self.sync_last_telegram = time.perf_counter()
                    self.sync_telegrams[self.sync_telegram_counter] = time.perf_counter()
            
            if self.driver_statuses: 
                self.send_telegram(telegram_id=self.get_new_message_id(), command="STATUS", data=self.driver_statuses)
                self.driver_statuses = {}
            if self.driver_infos: 
                self.send_telegram(telegram_id=self.get_new_message_id(), command="INFO", data=self.driver_infos)
                self.driver_infos = {}
            if var_info: 
                self.send_telegram(telegram_id=self.get_new_message_id(), command="VAR_INFO", data=var_info)

        except Exception as e:
            self.status = GatewayStatus.ERROR
            self.error_msg = 'Exception during run: '+str(e)
            logger.error(self.error_msg)
            return
        
        # Sleep only if nothing received or sent
        if needs_sleep:
            time.sleep(1e-3)

        
    def do_driver_setup(self, telegram_data)->dict:
        res = {}
        for driver_handle, driver_data in telegram_data.items():
            driver_type = driver_data["DRIVER"]
            driver_class, _ = registered_drivers[driver_type]
            setup_data = driver_data["SETUP"]
            parameter_data = setup_data.get("parameters", None)
            variable_data = setup_data.get("variables", None)
            logger.info(f"(Actual drivers {len(self.drivers)}), New driver requested {driver_handle}: {parameter_data}")
            # Check if requested driver type is registered
            if driver_type not in registered_drivers:
                res[driver_handle] = "Failed"                
            else:
                # Check if compatible driver already exists
                for driver_object, pipe in self.drivers.items():
                    if driver_object.__class__ == driver_class:
                        if driver_object.checkSetupCompatible(parameter_data):
                            logger.info(f"Handler {driver_handle} using compatible driver {driver_object.name}")
                            driver_object.handles.append(driver_handle)
                            # Fill up handle and variable dicts
                            if variable_data:
                                self.process_variables(driver_object, variable_data)
                                pipe.send(json.dumps({DriverActions.ADD_VARIABLES: variable_data}))
                            # Make sure we send status update
                            if driver_object.status == DriverStatus.RUNNING:
                                self.driver_statuses[driver_handle] = "RUNNING"

                            res[driver_handle] = "SUCCESS"
                            break
                        #else:
                        #    logger.info(f"Handler {driver_handle} not compatible with driver {driver_object.name}")

                else:
                    # Create new driver
                    pipe, driver_pipe = Pipe()
                    driver_object = driver_class(driver_handle, driver_pipe, parameter_data)
                    driver_object.setDaemon(True)
                    self.drivers[driver_object] = pipe
                    driver_object.handles.append(driver_handle)
                    driver_object.start()
                    if variable_data:
                        self.process_variables(driver_object, variable_data)
                        pipe.send(json.dumps({DriverActions.ADD_VARIABLES: variable_data}))
                    logger.info(f'New {driver_type} driver created: {driver_object.name}, {parameter_data}')        
                    res[driver_handle] = "SUCCESS"
        return res

    def process_variables(self, driver_object, var_datas:dict):
        # TODO: Consider a variable that already has ben setup but now is the other type (READ/WRITE) so it should be changed to BOTH
        # An option can be to store the variable type as well in the self.variables dict ([handles], var_type)
        for var_name, var_data in var_datas.items():
            var_handle = var_data['handle']
            self.handles[var_handle] = (var_name, driver_object)
            if driver_object not in self.variables:
                self.variables[driver_object] = {}
            if var_name not in self.variables[driver_object]:
                self.variables[driver_object][var_name] = [var_handle]
            else:
                self.variables[driver_object][var_name].append(var_handle)


    def do_driver_updates(self, telegram_data) -> bool:
        try:
            updates = {}
            for var_handle, var_value in telegram_data.items():
                var_name, driver_object = self.handles[var_handle]
                if driver_object not in updates:
                    updates[driver_object] = {var_name: var_value}
                else:
                    updates[driver_object].update({var_name: var_value})
            
            for driver_object, update_data in updates.items():
                pipe = self.drivers[driver_object]
                if pipe:
                    if update_data:
                        pipe.send(json.dumps({DriverActions.UPDATE:update_data}))
                        logger.debug(f"Driver {driver_object.name}: input_data_updated = {update_data}")
                else:
                    logger.debug(f"Driver {driver_object.name}: Pipe is not active")
            
            return True

        except:
            print("Error processing UPDATE telegram!")
            return False

    def doWebsocketInterface(self):
        ''' Websocket interface '''
        # Loop connections
        for connection in WebSocketConnections:
            # Check if there is a message to process
            while connection.msg_queue:
                # Get message data
                try:
                    msg = json.loads(connection.msg_queue.pop())
                except:
                    continue

                if 'request' in msg:
                    req = msg['request']
                    # Get command
                    command = req['command']
                    # Set response
                    res_data = ''
                    # connect command 
                    if (command == "connect"):
                        # Check arguments
                        if ('data' in req and 'url' in req['data']):
                            self.server_address = (req['data']['url'], 4844)
                        else:
                            self.server_address = ('127.0.0.1', 4844)
                        # Check gateway status
                        if self.status == GatewayStatus.STANDBY:
                            # Try to connect
                            self.doConnect()
                            if self.status == GatewayStatus.CONNECTED:
                                # Notify client
                                res_data = {"status": "connected", "ip": self.server_address[0]}
                            else:
                                # Notify client
                                res_data = {"status": "error", "message": "Connection with ip " + self.server_address[0] + " cannot be established"}
                        else:
                            res_data = {"status": "error", "message": "Gateway status is not STANDBY"}

                    # disconnect command 
                    elif (command == "disconnect"):
                        # Check gateway status
                        if self.status == GatewayStatus.CONNECTED:
                            # Do cleanup
                            self.doCleanup()
                            self.status = GatewayStatus.STANDBY
                            # Notify client
                            res_data = {"status": "disconnected"}
                        else:
                            res_data = {"status": "error", "message": "Gateway status is not CONNECTED"}

                    # reset command 
                    elif (command == "reset"):
                        # Check gateway status
                        if self.status == GatewayStatus.ERROR:
                            # Do cleanup
                            self.doCleanup()
                            self.status = GatewayStatus.STANDBY
                            self.error_msg = ''
                            # Notify client
                            res_data = {"status": "reset"}
                        else:
                            res_data = {"status": "error", "message": "Gateway status is not ERROR"}

                    # status command 
                    elif (command == "status"):
                        # Notify client
                        if self.status == GatewayStatus.ERROR:
                                res_data = {"status": "error", "message": str(self.error_msg), "ip": self.server_address[0] if self.server_address != None else ""}
                        else:
                            res_data = {"status": str(GatewayStatus(self.status).name), "ip": self.server_address[0] if self.server_address != None else ""}

                    # version command
                    elif (command == "version"):
                        # Notify client
                        res_data = {"status": str(version)}
                
                    # Not defined command
                    else:
                        res_data = {"status": "Unknown command"}

                    # Send response
                    connection.sendMessage(json.dumps({"response": {"id": req["id"], "command": command, "data": res_data}}))
                    logger.debug('Response sent: {}'.format(json.dumps({"response": {"id": req["id"], "command": command, "data": res_data}})))

# Testing
if __name__ == '__main__':
    g = gateway()
    g.run(ip='0.0.0.0', port=2323)