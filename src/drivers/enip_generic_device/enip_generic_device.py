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

import multiprocessing
import socket
import struct
import enum 
import time

from .enip import EnipPacket, EnipIOpacket, RegisterSessionData, SendRRData, CMitem, CM_SocketAddressInfo
from ..driver import driver, VariableDatatype, VariableOperation, VariableQuality

MAX_TELEGRAM_SIZE = 4096
DEFAULT_ENIP_PORT = 44818
MAX_CIP_COUNTER = 0xffff

class STATE(str, enum.Enum):
    WAITING_CONNECTION = 'Waiting connection'
    REGISTERING_SESSION = 'Rregistering session'
    CONNECTTION_STABLISHED = 'Connection stablished'
    CONNECTION_RUNNING = 'Connection running'
    RESET = 'reset'

class enip_generic_device(driver):
    '''
    TODO: Document
    Parameters:
    ip: int
        IP Address used by the device. Default = '127.0.0.1'
    read_size: int
        Size in bytes of the data sent from the PLC to the Device.
    write_size: int
        Size in bytes of the data sent from the Device to the PLC.
    '''

    def __init__(self, name: str, pipe: multiprocessing.Pipe = None, params:dict = None):
        """
        :param name: (optional) Name for the driver
        :param pipe: (optional) Pipe used to communicate with the driver thread. See gateway.py
        """
        # Inherit
        driver.__init__(self, name, pipe, params)

        # Parameters
        self.ip = '127.0.0.1'
        self.read_size = 1
        self.write_size = 1
        self.rpi = 0

        # Object variables
        self.udp_socket = None
        self.plc_socket = None
        self.cip_counter = 0
        self.connection_timeout = 2
        self.plc_address = ""
        self.last_package_time = None
        self.change_state(STATE.RESET)

        # Enip IO packet variables
        self.id_io = 0
    
    def change_state(self, newstate):
        if newstate in STATE:
            self._state = newstate
            self.sendDebugInfo(f'{self._state}')

    def connect(self) -> bool:
        """ Connect driver.
        
        : returns: True if connection established False if not
        """
        try:
            # Create TCP socket
            self._connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self._connection.bind((self.ip, DEFAULT_ENIP_PORT))
            self._connection.listen(1)
            self._connection.settimeout(1)
            self.sendDebugInfo(f'Listening for connections at {self.ip}:{DEFAULT_ENIP_PORT}')
            self._handle = int(self.ip.split('.')[3])
            self.rpi = 0 # Force RPI to 0 because we want the loop wo be as fast as possible, no sleep
            return True

        except Exception as e:
            self.sendDebugInfo(f'Exception while setting up TCP socket at {self.ip}:{DEFAULT_ENIP_PORT}: {e}')
            return False


    def disconnect(self):
        """ Disconnect driver.
        """
        if self._connection:
            self._connection.close()


    def loop(self):
        """ Runs every iteration while the driver is active. Only use if strictly necessary.
        """
        if self._state == STATE.RESET:
            if self.udp_socket:
                self.udp_socket.close()
                self.udp_socket = None
            if self.plc_socket:
                self.plc_socket.close()
                self.plc_socket = None
            self.write_data = self.write_size*bytes.fromhex('00')
            self.read_data = self.read_size*bytes.fromhex('00')
            self.change_state(STATE.WAITING_CONNECTION)

        elif self._state == STATE.WAITING_CONNECTION:
            try:
                (self.plc_socket, self.plc_address) = self._connection.accept()
                self.plc_address = self.plc_address[0]
                self.sendDebugInfo(f'Status {self._state}: {self.plc_address}')
                self.last_package_time = time.perf_counter()
                self.change_state(STATE.REGISTERING_SESSION)
            except:
                pass

        elif self._state in [STATE.REGISTERING_SESSION, STATE.WAITING_CONNECTION]:
            # TCP Connection handler
            try:
                message = self.plc_socket.recv(MAX_TELEGRAM_SIZE)
                assert message, 'no request'
                package = EnipPacket.process(message)
                #print("UCMM Request:\n", package)
                if isinstance(package.specific_data, RegisterSessionData):
                    reply = package.reply(self._handle)
                elif isinstance(package.specific_data, SendRRData):
                    # Add CMItems
                    package.specific_data.encapsulated_packet.items.append(CMitem(0x8000, 16, CM_SocketAddressInfo(2, 2222, 0, 0).hex()))
                    plc_ip = 0
                    plc_address = self.plc_address.split('.')
                    plc_address.reverse()
                    for sip in plc_address:
                        plc_ip = plc_ip*256+int(sip) 
                    package.specific_data.encapsulated_packet.items.append(CMitem(0x8001, 16, CM_SocketAddressInfo(2, 2222, plc_ip, 0).hex()))
                    reply = package.reply(self._handle)
                    # TODO: Check if somethings needs to be done for Multicast
                    self.udp_address = self.plc_address
                    # TODO: Modify vendor data
                    # Extract T-O ID
                    self.id_io = package.specific_data.encapsulated_packet.items[1].data.id_t_o
                    # Extract connection TimeOut: Actual Time Out value = 2^time_tick x Time_out_tick
                    tick = package.specific_data.encapsulated_packet.items[1].data.prio_tick
                    timeout = package.specific_data.encapsulated_packet.items[1].data.timeout
                    self.connection_timeout = 2**tick * timeout * 1e-3
                    if self._state != STATE.CONNECTION_RUNNING:
                        self.change_state(STATE.CONNECTTION_STABLISHED)
                #print("UCMM Reply:\n", package)
                self.plc_socket.send(reply)
                self.last_package_time = time.perf_counter()
            except Exception as e:
                pass
    
        elif self._state == STATE.CONNECTTION_STABLISHED:
            try:
                self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                self.udp_socket.bind((self.ip, 2222))
                self.udp_socket.settimeout(0.0)
                self.io_seq = 1
                self.cip_counter = 1
                self.udp_socket.sendto(EnipIOpacket(self.write_data, self.cip_counter, self.id_io, self.io_seq), (self.udp_address, 2222))
                self.last_package_time = time.perf_counter()
                self.change_state(STATE.CONNECTION_RUNNING)
            except Exception as e:
                if time.perf_counter() - self.last_package_time > self.connection_timeout:
                    self.change_state(STATE.RESET)
    
        elif self._state == STATE.CONNECTION_RUNNING:
            try:
                while True: # Try to receive as many telegrams as possible and answer them 
                    # Receive data
                    message = self.udp_socket.recv(4096)
                    packet_hex = message.hex() # Convert from \x00 to 00
                    assert len(packet_hex)>8+self.read_size*2, 'Wrong telegram size'
                    assert packet_hex[4:8] == "0280", 'Invalid package header'
                    payload = packet_hex[-(self.read_size*2):] # The data may be preceed of status info
                    self.read_data = bytes.fromhex(payload)
                    # Send data
                    self.io_seq += 1
                    self.udp_socket.sendto(EnipIOpacket(self.write_data, self.cip_counter, self.id_io, self.io_seq), (self.udp_address, 2222))
                    self.last_package_time = time.perf_counter()
            except Exception as e:
                if time.perf_counter() - self.last_package_time > self.connection_timeout:
                    self.change_state(STATE.RESET)


    def addVariables(self, variables: dict):
        """ Add variables to the driver. Correctly added variables will be added to internal dictionary 'variables'.
        Any error adding a variable should be communicated to the server using sendDebugInfo() method.
        : param variables: Variables to add in a dict following the setup format. (See documentation) 
        
        """
        # TODO: Size is not considered
        for var_id, var_data in variables.items():
            try:
                if var_id[1]=="B":
                    assert var_data['datatype'] == VariableDatatype.BYTE, "B should be used for BYTE type variables."
                    byte_size = 1
                elif var_id[1]=="W":
                    assert var_data['datatype'] in [VariableDatatype.WORD, VariableDatatype.INTEGER], "W should be used for WORD or INTEGER type variables."
                    byte_size = 2
                elif var_id[1]=="D":
                    assert var_data['datatype'] in [VariableDatatype.DWORD, VariableDatatype.FLOAT], "D should be used for DWORD or FLOAT type variables."
                    byte_size = 4
                index = var_id[2:]
                assert index.isnumeric(), 'Variable name has incorrect address.'
                index = int(index)*byte_size
                if var_id[0]=="I":
                    assert var_data['operation']==VariableOperation.WRITE, "I variables should be defined to write operations."
                    assert self.write_size>=index+byte_size, "Address out of bounds."
                elif var_id[0]=="Q":
                    assert self.read_size>=index+byte_size, "Address out of bounds."
                else:
                    assert False, "Variable name should start with I or Q" 
                var_data['index'] = index
                var_data['byte_size'] = byte_size
                var_data['value'] = self.defaultVariableValue(var_data['datatype'], var_data['size'])
                self.variables[var_id] = dict(var_data)
            except Exception as e:
                self.sendDebugVarInfo((f'SETUP: Variable definition is wrong: {var_id}, {e}', var_id))


    def readVariables(self, variables: list) -> list:
        """ Read given variable values. In case that the read is not possible or generates an error BAD quality should be returned.
        : param variables: List of variable ids to be read. 
        : returns: list of tupples including (var_id, var_value, VariableQuality)
        """
        res = []
        for var_id in variables:
            try:
                var_data = self.variables[var_id]
                index = var_data['index']
                byte_size = var_data['byte_size']
                value_hex = self.read_data[index:index+byte_size]
                if var_data['datatype'] == VariableDatatype.BYTE:
                    value = struct.unpack('B', value_hex)[0]
                elif var_data['datatype'] in [VariableDatatype.WORD, VariableDatatype.INTEGER]:
                    value = struct.unpack('H', value_hex)[0]
                elif var_data['datatype'] == VariableDatatype.FLOAT:
                    value = struct.unpack('f', value_hex)[0]
                elif var_data['datatype'] == VariableDatatype.DWORD:
                    value = struct.unpack('I', value_hex)[0]
                else:
                    assert False
                res.append((var_id, value, VariableQuality.GOOD))
                #print(var_id, value, value_hex)
            except Exception as e:
                res.append((var_id, var_data['value'], VariableQuality.BAD))
        return res


    def writeVariables(self, variables: list) -> list:
        """ Write given variable values. In case that the write is not possible or generates an error BAD quality should be returned.
        : param variables: List of tupples with variable ids and the values to be written (var_id, var_value). 
        : returns: list of tupples including (var_id, var_value, VariableQuality)
        """
        res = []
        for (var_id, new_value) in variables:
            try:
                var_data = self.variables[var_id]
                index = var_data['index']
                byte_size = var_data['byte_size']
                if var_data['datatype'] == VariableDatatype.BYTE:  
                    value_hex = struct.pack('B', new_value)
                elif var_data['datatype'] in [VariableDatatype.WORD, VariableDatatype.INTEGER]:  
                    value_hex = struct.pack('H', new_value)
                elif var_data['datatype'] == VariableDatatype.FLOAT:  
                    value_hex = struct.pack('f', new_value)
                elif var_data['datatype'] == VariableDatatype.DWORD:  
                    value_hex = struct.pack('I', new_value)
                else:
                    assert False
                self.write_data = self.write_data[:index]+value_hex+self.write_data[index+byte_size:]
                res.append((var_id, new_value, VariableQuality.GOOD))
            except Exception as e:
                res.append((var_id, new_value, VariableQuality.BAD))
        if self.cip_counter<MAX_CIP_COUNTER: 
            self.cip_counter += 1 # Very important to trigger the update in the controller
        else:
            self.cip_counter = 1
        return res
    