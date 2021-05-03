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
import datetime
from enum import Enum
import json
from multiprocessing import Pipe, Process
import os
import random
import socket
import sys
from threading import Thread
import time

# Specific libraries
from drivers import *
from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket

#Logging
import logging
FORMAT = '%(asctime)-15s %(levelname)s %(name)s: %(message)s'
logging.basicConfig(filename="gateway_logs.txt",
                    filemode='w',
                    level=logging.DEBUG, 
                    format=FORMAT)
logger = logging.getLogger('GATEWAY')
if ('debug' in sys.argv):
    logger.disabled = False
else:
    logger.disabled = True

# Version
version = "2.0.3"

# Settings
poll_time = 1 # seconds

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
        # UDP Telegrams
        self.udp_socket = None
        self.message_id = 0
        self.last_poll_sent = 0
        self.last_poll_received = 0
        # Emulation
        self.emulation_running = False
        # Drivers
        self.drivers = {}
        self.status = GatewayStatus.STANDBY
        self.error_msg = ''
        
    def get_datetime(self):
        ''' returns actual date and time as string.'''
        t = datetime.datetime.now()
        return t.strftime('%Y-%m-%d %H:%M:%S,%f')[:-3]

    def get_new_message_id(self):
        ''' Provides a new message id.'''
        self.message_id += 1
        return self.message_id
    
    def get_new_driver_id(self):
        ''' Provides a new driver id.'''
        id = 1
        while True:
            if f"driver_{id}" not in self.drivers:
                return f"driver_{id}"
            else:
                id += 1
    
    def run(self, ip:str='127.0.0.1', port:int=2323):
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

            #------------------------------
            # Websocket interface
            #------------------------------
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
                                    res_data = {"status": "error", "message": "Connection with ip " + self.server_address[0] + " cannot be stablished"}
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

            #------------------------------
            # Do actions
            #------------------------------
            # Driver running
            if self.status == GatewayStatus.CONNECTED:
                sleep_time = self.doRun()
            else:
                sleep_time = 1e-2 

            #------------------------------
            # Sleep if required
            #------------------------------
            if len(self.drivers) == 0 and sleep_time > 0:
                time.sleep(sleep_time)
    

    def close(self):
        ''' Exit Gateway'''
        self.status = GatewayStatus.EXIT


    def doConnect(self):
        """ Executed to connect the gateway to the server."""
        try:
            # Create UDP socket
            self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            #self.udp_socket.bind(('127.0.0.1', 4844))
            self.udp_socket.settimeout(poll_time*4)

            # Get implemented driver list
            drivers_list = {}
            for driver_name, (_, driver_version) in registered_drivers.items():
                drivers_list.update({driver_name:{'version':driver_version}})

            # Generate request telegram
            register_id = self.get_new_message_id()
            register_request = {
                "ID": register_id,
                "REGISTER": {
                    "server_key": 'server key obtained from the user',
                    "gateway": {
                        "version": version,
                        "heartbeat": poll_time,
                    },
                    "drivers": drivers_list
                }
            }

            # Send register request
            self.udp_socket.sendto(json.dumps(register_request).encode('utf8'), self.server_address)

        except Exception as e:
            self.doCleanup()
            self.status = GatewayStatus.ERROR
            self.error_msg = 'Exception during setup: '+str(e)
            logger.error(self.error_msg)
            raise Exception(self.error_msg)

        # Get response before defined timeout (4 x poll_time)
        try:
            data, address = self.udp_socket.recvfrom(4096)
            if data != None and address == self.server_address:
                response_json = json.loads(data.decode('utf-8'))
                if response_json["ID"] == register_id:
                    # Connection succeded
                    if (response_json["REGISTER"] == 'Success'):
                        # From now on, no timeout is set in the socket
                        self.udp_socket.setblocking(0)
                        self.last_poll_sent = time.time()
                        self.last_poll_received = time.time()
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
        except Exception as e:
            logger.error('Exception during cleanup: '+str(e))
            

    def doRun(self):
        """ Executed while gateway is connected."""
        # Default sleep time to return if nothing is done
        sleep_time = 1e-3
        # Send polling message within the interval
        if (time.time()-self.last_poll_sent) >= poll_time:
            try:
                polling_request = {
                    "ID": self.get_new_message_id(),
                    "POLLING": 'null'
                }
                self.udp_socket.sendto(json.dumps(polling_request).encode('utf8'), self.server_address)
                self.last_poll_sent = time.time()
            except:
                self.status = GatewayStatus.ERROR
                self.error_msg = 'Exception sending polling telegram'
                logger.error(self.error_msg)
                return 0 # No need of sleep if an error

        # Check incomming telegrams
        try:
            data, address = self.udp_socket.recvfrom(4096)
            # Process data if data received and address is valid 
            if (data != None and address == self.server_address):
                request_json = json.loads(data.decode('utf-8'))
                if ('SETUP' in request_json):
                    self.do_driver_setup(request_json)
                elif ('DELETE' in request_json):
                    self.do_driver_delete(request_json)
                elif ('UPDATE' in request_json):
                    self.do_driver_update(request_json)
                elif ('POLLING' in request_json):
                    self.last_poll_received = time.time()
                sleep_time = 0 # No need of sleep if data received
        except:
            # No data received
            pass

        # Check receiving poll messages
        if (time.time()-self.last_poll_received)>(4*poll_time):
            self.status = GatewayStatus.ERROR
            self.error_msg = "Polling msg was not received on time"
            logger.error(self.error_msg)
            return 0 # No need of sleep if an error

        # Check updates from drivers
        try:
            for driver_id, (driver, pipe)  in self.drivers.items():
                if driver.is_alive() and pipe:
                    if pipe.poll():
                        action, data = json.loads(pipe.recv()).popitem()
                        if action == DriverActions.UPDATE:
                            self.send_driver_update(driver_id, data)
                            logger.debug('Driver {} output data updated: {}'.format(driver_id, data))
                        elif action == DriverActions.STATUS:
                            self.send_driver_status(driver_id, data)
                            logger.debug('Driver {} status changed: {}'.format(driver_id, data))
                        elif action == DriverActions.INFO:
                            self.send_driver_info(driver_id, data)
                            logger.debug('Driver {} debug info: {}'.format(driver_id, data))
                        sleep_time = 0 # No need of sleep if data sent

        except Exception as e:
            self.status = GatewayStatus.ERROR
            self.error_msg = 'Exception during run: '+str(e)
            logger.error(self.error_msg)
            return 0 # No need of sleep if an error
        
        return sleep_time


    def do_driver_delete(self, request_json):
        request_id = request_json["ID"]
        driver_id = request_json['DRIVER']
        if (driver_id == 'all'):
            self.clean_drivers()
            response_json = {   
                "ID": request_id,
                "DELETE": 'Success',
                "DRIVER": 'all'
            }
        else:
            try:
                (driver, pipe) = self.drivers.pop(driver_id)
                self.clean_driver(driver_id, driver, pipe)
                response_json = {   
                    "ID": request_id,
                    "DELETE": 'Success',
                    "DRIVER": driver_id
                }
            except:
                response_json = {   
                    "ID": request_id,
                    "DELETE": 'Failed',
                    "DRIVER": driver_id
                }
                logger.debug("Driver " + driver_id + " not found")
        self.udp_socket.sendto(json.dumps(response_json).encode('utf8'), self.server_address)
        logger.info(f"Driver {driver_id} deleted")
        

    def send_driver_update(self, driver_id, driver_data):
        update_msg = {   
            "ID": self.get_new_message_id(),
            "UPDATE": driver_data,
            "DRIVER": driver_id
        }
        self.udp_socket.sendto(json.dumps(update_msg).encode('utf8'), self.server_address)
        

    def send_driver_status(self, driver_id, driver_status):
        update_msg = {   
            "ID": self.get_new_message_id(),
            "STATUS": driver_status,
            "DRIVER": driver_id
        }
        self.udp_socket.sendto(json.dumps(update_msg).encode('utf8'), self.server_address)
        

    def send_driver_info(self, driver_id, driver_info):
        update_msg = {   
            "ID": self.get_new_message_id(),
            "INFO": driver_info,
            "DRIVER": driver_id
        }
        self.udp_socket.sendto(json.dumps(update_msg).encode('utf8'), self.server_address)
        

    def do_driver_setup(self, request_json):
        # Create driver pipe and get new id
        pipe, driver_pipe = Pipe()
        driver_id = self.get_new_driver_id()
        driver_type = request_json["DRIVER"]
        status = "Success"

        # registered requested
        if (driver_type in registered_drivers):
            # Create driver
            driver_class, _ = registered_drivers[driver_type]
            driver = driver_class(driver_id, driver_pipe)
            driver.setDaemon(True)
            driver.start()
            pipe.send(json.dumps({DriverActions.SETUP:request_json["SETUP"]}))
            self.drivers[driver_id] = (driver, pipe)
            logger.info(f'New {driver_type} driver: {driver_id}')        

        # Wrong driver type requested
        else:
            status = "Failed"
            driver_id = None

        # Send response
        response_json = {   
            "ID": request_json["ID"],
            "SETUP": status,
            "DRIVER": driver_id
        }

        self.udp_socket.sendto(json.dumps(response_json).encode('utf8'), self.server_address)
        #TODO: Handle errors


    def do_driver_update(self, request_json):
        try:
            driver_id = request_json["DRIVER"]
            (_, pipe) = self.drivers[driver_id]
            update_data = request_json["UPDATE"]
            if pipe:
                if update_data:
                    pipe.send(json.dumps({DriverActions.UPDATE:update_data}))
                    logger.debug(f"Driver {driver_id}: input_data_updated = {update_data}")
            else:
                logger.debug(f"Driver {driver_id}: Pipe is not active")
        except:
            logger.debug(f"Driver {driver_id} not found")


    def clean_drivers(self):
        """ Close all drivers."""
        while self.drivers:
            driver_id, (driver, pipe) = self.drivers.popitem()
            self.clean_driver(driver_id, driver, pipe)


    def clean_driver(self, driver_id, driver, pipe):
        """ Clean specific driver. """
        logger.debug('Cleaning driver: {}'.format(driver_id))
        pipe.send(json.dumps({DriverActions.EXIT: None}))
        logger.info(f"Driver {driver_id} removed.")


# Testing
if __name__ == '__main__':
    g = gateway()
    g.run(ip='127.0.0.1', port=2323)
