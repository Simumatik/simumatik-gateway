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

import enum
from multiprocessing import Pipe
import socket
import struct
import time
import fastcrc
from typing import Optional

from ..driver import driver, VariableQuality, VariableOperation, VariableDatatype

CMD_TOT_LEN = 14
CMD_FORMAT = 'c 4s 2s 2s 4s c'

STX = '\x02'
ETX = '\x03'

def UAM_decode(bytes):
    string = bytes.decode()
    decimal_res = []
    for i in range(0, len(string), 4):
        ascii = [ord(c) for c in string[i:i+4]]
        ascii_d = [c-0x30 if c<0x40 else c-0x37 for c in ascii]
        binary = ''.join([format(d, '04b') for d in ascii_d])
        decimal_res.append(int(binary, 2))
    return decimal_res

def UAM_encode(decimal_list):
    ascii_str = ''
    for decimal in decimal_list:
        if decimal < 0:
            decimal = 65535
        binary = format(decimal, '016b')
        decimal = [int(binary[i:i+4], 2) for i in range(0, 16, 4)]
        ascii_d = [d+0x30 if d<10 else d+0x37 for d in decimal]
        ascii_str += ''.join([chr(a) for a in ascii_d])
    return ascii_str.encode()

def calc_crc(bytes):
    crc16 = fastcrc.crc16.kermit(bytes)
    return str(hex(crc16))[2:].upper().encode()

class development(driver):
    '''
    Driver that can be used for development. The driver can be used on a component just assigning the driver type "development".
    Feel free to add your code in the methods below.
    Parameters:
    myparam: int
        This is just an example of a driver parameter. Default = 3
    '''

    def __init__(self, name: str, pipe: Optional[Pipe] = None):
        """
        :param name: (optional) Name for the driver
        :param pipe: (optional) Pipe used to communicate with the driver thread. See gateway.py
        """
        # Inherit
        driver.__init__(self, name, pipe)

        # Parameters
        self.port = 10940
        self.transmit_interval = 0.1

        # Internal
        self._last_transmit_time = 0
        self.data = [65534] * 1081 + [0] * 1081
        self.encoded_data = UAM_encode(self.data)

    
    def loop(self):
        dt = time.perf_counter() - self._last_transmit_time
        if dt > self.transmit_interval:
            self._last_transmit_time = time.perf_counter()
            try:
                # Receive commands
                data = self._connection.recv(CMD_TOT_LEN)
                s = struct.Struct(CMD_FORMAT)

                _, cmd_size, header, sub_header, crc, _ = s.unpack(data)
                # print(cmd_size, header, sub_header, crc)

                if header + sub_header == b'AR01':
                    # Transmit stored data
                    # Build data from sensor readings
                    msg_len = b'21FF'
                    area_num = b'07'
                    timestamp = b'005A2F4F'
                    data = UAM_encode(self.data)
                    print(len(data))
                    UAM_msg = msg_len + b'AR01000' + area_num + b'11701111000000000000' + timestamp + b'00000000' + data
                    UAM_crc = calc_crc(UAM_msg)
                    UAM_msg = b'\x02' + UAM_msg + UAM_crc + b'\x03'
                    self._connection.sendall(UAM_msg)
            except Exception as e:
                self.disconnect()
                self.connect()
                print(e)
        


    def connect(self) -> bool:
        """ Connect driver.
        
        : returns: True if connection stablished False if not
        """
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_address = ("0.0.0.0", self.port)
            sock.bind(server_address)
            sock.listen()
            self._connection, self.client_address = sock.accept()
        except Exception as e:
            self.sendDebugInfo(f'Could not connect: {e}') 
            return False
        return True


    def disconnect(self):
        """ Disconnect driver.
        """
        try:
            self._connection.close()
        except:
            pass


    def addVariables(self, variables: dict):
        """ Add variables to the driver. Correctly added variables will be added to internal dictionary 'variables'.
        Any error adding a variable should be communicated to the server using sendDebugInfo() method.
        : param variables: Variables to add in a dict following the setup format. (See documentation) 
        
        """
        for var_id, var_data in variables.items():
            try:
                var_data['value'] = None # Force first update
                self.variables[var_id] = var_data
                self.sendDebugVarInfo((f'SETUP: Variable added {var_id}', var_id))
                continue
            except:
                pass
            
            self.sendDebugVarInfo((f'SETUP: Variable not added {var_id}', var_id))


    def readVariables(self, variables: list) -> list:
        """ Read given variable values. In case that the read is not possible or generates an error BAD quality should be returned.
        : param variables: List of variable ids to be read. 
        : returns: list of tupples including (var_id, var_value, VariableQuality)
        """
        res = []
        # try:
        #     values = self._connection.
        # except:
        #     for var_id in variables:
        #         res.append((var_id, None, VariableQuality.BAD))
        # else:
        #     for var_id in values:
        #         res.append((var_id, values[var_id], VariableQuality.GOOD))

        return res


    def writeVariables(self, variables: list) -> list:
        """ Write given variable values. In case that the write is not possible or generates an error BAD quality should be returned.
        : param variables: List of tupples with variable ids and the values to be written (var_id, var_value). 
        : returns: list of tupples including (var_id, var_value, VariableQuality)
        """
        res = []
        for (var_id, var_value)  in variables: 
            if var_value == None or len(var_value)<100:
                continue
            try:
                [first, last] = map(int, var_id.split('_'))
                self.data = self.data[:first] + var_value + self.data[last:]
                res.append((var_id, var_value, VariableQuality.GOOD))
            except Exception as e:
                res.append((var_id, var_value, VariableQuality.BAD))
                print(e)

        return res