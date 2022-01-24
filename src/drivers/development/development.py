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
import time
import fastcrc

from ..driver import driver, VariableQuality

CMD_TOT_LEN = 14
CMD_FORMAT = 'c 4s 2s 2s 4s c'

def UAM_encode(decimal_list):
    ascii_str = ''
    # Loop through distance values
    for decimal in decimal_list:
        if decimal < 0:
            decimal = 65535 # 65535 for 'object not detected'
        binary = format(decimal, '016b')
        decimal = [int(binary[i:i+4], 2) for i in range(0, 16, 4)]
        ascii_d = [d+0x30 if d<10 else d+0x37 for d in decimal]
        ascii_str += ''.join([chr(a) for a in ascii_d])

    return ascii_str.encode()

def calc_crc(bytes):
    crc16 = fastcrc.crc16.kermit(bytes)
    ascii_crc = str(hex(crc16))[2:].upper()

    return ('0' * (4 - len(ascii_crc)) + ascii_crc).encode()

class development(driver):
    '''
    Driver that can be used for development. The driver can be used on a component just assigning the driver type "development".
    Feel free to add your code in the methods below.
    Parameters:
    port: int
        Port to listen for commands on. Default = 10940
    transmit_interval: float
        Time in seconds to wait between transmitting data to client. Default = 10940
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
        self.transmit_interval = 0.03
        self.area_num = '06'

        # Internal
        self.last_transmit_time = 0
        self.data = [65534] * 1081
        self.encoded_data = UAM_encode(self.data)

    
    def loop(self):
        dt = time.perf_counter() - self.last_transmit_time
        if dt > self.transmit_interval:
            try:
                # Receive commands
                data = self._connection.recv(CMD_TOT_LEN)
                s = struct.Struct(CMD_FORMAT)
                
                if len(data) == struct.calcsize(CMD_FORMAT):
                    _, cmd_size, header, sub_header, crc, _ = s.unpack(data)

                    if header + sub_header == b'AR01':
                        # Transmit stored data
                        # Build data from sensor readings
                        msg_len = b'21FF'
                        area_num = self.area_num.encode()
                        timestamp = b'005A2F4F' # Seconds elapsed since detection in protection area
                        data = self.encoded_data + b'0000'*1081 # Add intensity values
                        UAM_msg = msg_len + b'AR01000' + area_num + b'00001111000000000000' + timestamp + b'00000000' + data
                        UAM_crc = calc_crc(UAM_msg)
                        UAM_msg = b'\x02' + UAM_msg + UAM_crc + b'\x03'
                        self._connection.sendall(UAM_msg)

            except Exception as e:
                # Wait for a new connection
                self.disconnect()
                self.connect()
                self.sendDebugInfo(e)
            
            finally:
                self.last_transmit_time = time.perf_counter()


    def connect(self) -> bool:
        """ Connect driver.
        
        : returns: True if connection stablished False if not
        """
        try:
            server_address = ("0.0.0.0", self.port)
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind(server_address)
            sock.listen()
            self.sendDebugInfo(f'Waiting for connection')
            self._connection, self.client_address = sock.accept()
        except Exception as e:
            print(e)
            self.sendDebugInfo(f'Could not connect: {e}') 
            return False

        self.sendDebugInfo(f'Connected to: {self.client_address}') 
        return True


    def disconnect(self):
        """ Disconnect driver.
        """
        try:
            self._connection.close()
        except:
            pass
        finally:
            self._connection = None


    def addVariables(self, variables: dict):
        """ Add variables to the driver. Correctly added variables will be added to internal dictionary 'variables'.
        Any error adding a variable should be communicated to the server using sendDebugInfo() method.
        : param variables: Variables to add in a dict following the setup format. (See documentation) 
        
        """
        for var_id, var_data in variables.items():
            var_data['value'] = None # Force first update
            self.variables[var_id] = var_data


    def readVariables(self, variables: list) -> list:
        """ Read given variable values. In case that the read is not possible or generates an error BAD quality should be returned.
        : param variables: List of variable ids to be read. 
        : returns: list of tupples including (var_id, var_value, VariableQuality)
        """
        res = []

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
                self.sendDebugInfo(e)
    
        # Encode new data, unless there is a pending transmit
        if time.perf_counter() - self.last_transmit_time < 0.03:
            self.encoded_data = UAM_encode(self.data)

        return res