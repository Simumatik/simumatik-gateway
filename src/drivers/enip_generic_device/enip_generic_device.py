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

from multiprocessing import Pipe
from typing import Optional
import socket
import struct
from enum import Enum 
import time
from .enip import EnipPacket, CMitemResData00b2, EnipIOpacket

from ..driver import driver, VariableDatatype, VariableOperation, VariableQuality


MAX_TELEGRAM_SIZE = 4096
DEFAULT_ENIP_PORT = 44818
CONNECTION_TIMEOUT = 1

class STATE(str, Enum):
    WAITING_CONNECTION = 'waiting connection'
    REGISTERING_SESSION = 'registering session'
    COMMUNICATION_MANAGER = 'communication manager setup'
    CONNECTTION_STABLISHED = 'connection stablished'
    CONNECTION_RUNNING = 'connection running'
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

    def __init__(self, name: str, pipe: Optional[Pipe] = None, params:dict = None):
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
        self.device_id = "41370000"

        # Object variables
        self.udp_socket = None
        self.plc_socket = None
        self.plc_address = ""
        self.last_package_time = None

        # Enip IO packet variables
        self.io_seq = 0
        self.cip_counter = 0
        self.id_io = ""

    def connect(self) -> bool:
        """ Connect driver.
        
        : returns: True if connection established False if not
        """
        try:
            # Create TCP socket
            self._connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self._connection.bind((self.ip, DEFAULT_ENIP_PORT))
            self._connection.listen(1)
            self._connection.settimeout(CONNECTION_TIMEOUT)
            self.sendDebugInfo(f'Listening for connections at {self.ip}:{DEFAULT_ENIP_PORT}')
            self._state = STATE.RESET
            return True

        except Exception as e:
            print("Exception in doSetup"+ str(e))
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
        if self._state == STATE.WAITING_CONNECTION:
            try:
                (self.plc_socket, self.plc_address) = self._connection.accept()
                self.plc_address = self.plc_address[0]
                self.sendDebugInfo(f'Status {self._state}: {self.plc_address}')
                self.last_package_time = time.perf_counter()
                self._state = STATE.REGISTERING_SESSION
            except:
                pass

        elif self._state == STATE.REGISTERING_SESSION:
            try:
                message = self.plc_socket.recv(MAX_TELEGRAM_SIZE)
                assert message, 'no request'
                req_register_session = message.hex()
                register_session_packet = EnipPacket.unpack(req_register_session)
                register_session_packet.encapsulation_header.set_session_handle(int(self.ip.split('.')[3]))
                self.plc_socket.send(bytes.fromhex(register_session_packet.hex()))
                self.last_package_time = time.perf_counter()
                self._state = STATE.COMMUNICATION_MANAGER
            except:
                if time.perf_counter() - self.last_package_time > CONNECTION_TIMEOUT:
                    self._state = STATE.WAITING_CONNECTION
            
        elif self._state == STATE.COMMUNICATION_MANAGER:
            try:
                message = self.plc_socket.recv(4096)
                assert message, 'no request'
                req_connection_manager = message.hex()
                connection_manager_packet = EnipPacket.unpack(req_connection_manager)
                for item in connection_manager_packet.specific_data.item_list:
                    if item.id == 'b200':
                        self.id_io = item.CM_item_data.id_t_o
                        # Create second item data from request and introduce it. TODO: Do not hardcode id_o_t
                        item.CM_item_data = CMitemResData00b2(self.device_id, item.CM_item_data.id_t_o, item.CM_item_data.conn_serial_num,
                                                            item.CM_item_data.orig_vendor_id, item.CM_item_data.orig_serial_num, item.CM_item_data.rpi_o_t, item.CM_item_data.rpi_t_o)
                    elif item.id == '0080':
                        # TODO: Modify third item to match response (from O->T to T->O)
                        #connection_manager_packet.specific_data.item_list[2].id = "0080"
                        #connection_manager_packet.specific_data.item_list[2].CM_item_data.sin_addr = "00000000"
                        pass
                self.plc_socket.send(bytes.fromhex(connection_manager_packet.hex()))
                self.last_package_time = time.perf_counter()
                self._state = STATE.CONNECTTION_STABLISHED
            except:
                if time.perf_counter() - self.last_package_time > CONNECTION_TIMEOUT:
                    self._state = STATE.WAITING_CONNECTION
        
        elif self._state == STATE.CONNECTTION_STABLISHED:
            try:
                self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                self.udp_socket.bind((self.ip, 2222))
                self.udp_socket.settimeout(1.0)
                # Send data
                packet = EnipIOpacket(self.write_data, self.io_seq, self.id_io, self.cip_counter).pack()
                self.udp_socket.sendto(packet, (self.plc_address, 2222))
                self.io_seq += 1
                self.last_package_time = time.perf_counter()
                self._state = STATE.CONNECTION_RUNNING
            except:
                if time.perf_counter() - self.last_package_time > CONNECTION_TIMEOUT:
                    self._state = STATE.WAITING_CONNECTION
        
        elif self._state == STATE.CONNECTION_RUNNING:
            try:
                # Receive data
                message = self.udp_socket.recv(4096)
                packet_hex = message.hex() # Convert from \x00 to 00
                assert len(packet_hex)>8, 'Wrong telegram size'
                assert packet_hex[4:8] == "0280", 'Invalid package header'
                self.read_data = packet_hex[-(self.read_size*2):]
                #print("Read:", self.read_data)
                # Send data
                packet = EnipIOpacket(self.write_data, self.io_seq, self.id_io, self.cip_counter).pack()
                self.udp_socket.sendto(packet, (self.plc_address, 2222))
                self.io_seq += 1
                #print("Write:", self.write_data)
                self.last_package_time = time.perf_counter()
            except:
                try:
                    self.plc_socket.recv(1, socket.MSG_PEEK | socket.MSG_DONTWAIT)
                except:
                    self._state = STATE.RESET

        elif self._state == STATE.CONNECTION_RUNNING:
            if self.udp_socket:
                self.udp_socket.close()
            if self.plc_socket:
                self.plc_socket.close()
            self._state = STATE.WAITING_CONNECTION

        else:
            self.write_data = self.write_size*bytes.fromhex('00')
            self.read_data = self.read_size*bytes.fromhex('00')
            self._state = STATE.WAITING_CONNECTION


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
                    assert var_data['datatype'] in [VariableDatatype.WORD], "W should be used for WORD type variables."
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
            var_data = self.variables[var_id]
            index = var_data['index']
            if var_data['datatype'] == VariableDatatype.BYTE:
                value = struct.unpack('B', self.write_data[index:index+1])
            elif var_data['datatype'] == VariableDatatype.WORD:
                value = struct.unpack('H', self.write_data[index:index+2])
            elif var_data['datatype'] == VariableDatatype.FLOAT:
                value = struct.unpack('f', self.write_data[index:index+4])
            elif var_data['datatype'] == VariableDatatype.DWORD:
                value = struct.unpack('I', self.write_data[index:index+4])
            else:
                res.append((var_id, var_data['value'], VariableQuality.BAD))
                continue
            res.append((var_id, value, VariableQuality.GOOD))
        return res


    def writeVariables(self, variables: list) -> list:
        """ Write given variable values. In case that the write is not possible or generates an error BAD quality should be returned.
        : param variables: List of tupples with variable ids and the values to be written (var_id, var_value). 
        : returns: list of tupples including (var_id, var_value, VariableQuality)
        """
        res = []
        for (var_id, new_value) in variables:
            var_data = self.variables[var_id]
            index = var_data['index']
            if var_data['datatype'] == VariableDatatype.BYTE:  
                self.write_data = self.write_data[:index]+struct.pack('B', new_value)+self.write_data[index+1:]
            elif var_data['datatype'] == VariableDatatype.WORD:  
                self.write_data = self.write_data[:index]+struct.pack('H', new_value)+self.write_data[index+2:]
            elif var_data['datatype'] == VariableDatatype.FLOAT:  
                self.write_data = self.write_data[:index]+struct.pack('f', new_value)+self.write_data[index+4:]
            elif var_data['datatype'] == VariableDatatype.DWORD:  
                self.write_data = self.write_data[:index]+struct.pack('I', new_value)+self.write_data[index+4:]
            else:
                res.append((var_id, new_value, VariableQuality.BAD))
                continue
            res.append((var_id, new_value, VariableQuality.GOOD))
        self.cip_counter += 1 # Very important to trigger the update in the controller
        return res
    