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

CMD_FORMAT = 'c 4s 2s 2s 4s c'
CMD_TOT_LEN = struct.calcsize(CMD_FORMAT)

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

class hokuyo_uam(driver):
    '''
    Driver that can be used for development. The driver can be used on a component just assigning the driver type "development".
    Feel free to add your code in the methods below.
    Parameters:
    ip: str
        Ip address to listen for commands on. Default = "0.0.0.0"
    port: int
        Port to listen for commands on. Default = 10940
    transmit_interval: float
        Time in seconds to wait between transmitting data to client. Default = 30ms
    '''

    def __init__(self, name: str, pipe: Optional[Pipe] = None):
        """
        :param name: (optional) Name for the driver
        :param pipe: (optional) Pipe used to communicate with the driver thread. See gateway.py
        """
        # Inherit
        driver.__init__(self, name, pipe)

        # Parameters
        self.ip = "0.0.0.0"
        self.port = 10940
        self.transmit_interval = 0.03

        # Internal
        self.area_num = '06'
        self.last_transmit_time = 0
        self.data = [65534] * 1081
        self._data_changed = True
        self._client = None


    def connect(self) -> bool:
        """ Connect driver.
        
        : returns: True if connection stablished False if not
        """
        try:
            self._connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self._connection.bind((self.ip, self.port))
            self._connection.listen()
            self._connection.setblocking(False)
        except Exception as e:
            self.sendDebugInfo(f'Could not connect: {e}') 
            return False

        self.sendDebugInfo(f'Waiting for connection at {self.ip}:{self.port}')
        return True


    def disconnect(self):
        """ Disconnect driver.
        """
        try:
            if self._client:
                self._client.close()
        except:
            pass
        self._client = None
        
        try:
            if self._connection:
                self._connection.close()
        except:
            pass
        


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
                self.data = self.data[:first] + var_value + self.data[last+1:]
                res.append((var_id, var_value, VariableQuality.GOOD))
                self._data_changed = True
            except Exception as e:
                res.append((var_id, var_value, VariableQuality.BAD))
                self.sendDebugInfo(e)
    
        return res


    def loop(self):
        """ Runs every iteration while the driver is active. Only use if strictly necessary.
        """
        # Get new connections
        if self._client is None:
            try:
                self._client, client_address = self._connection.accept()
                self.sendDebugInfo(f'Connection stablished with: {client_address}')
            except:
                pass

        # Process actual connections
        else:
            now = time.perf_counter()
            dt = now - self.last_transmit_time
            if dt > self.transmit_interval:
                self.last_transmit_time = now

                if self._data_changed:
                    self.encoded_data = UAM_encode(self.data)
                    self._data_changed = False
                    
                try:
                    data = self._client.recv(CMD_TOT_LEN)
                    assert len(data)>0
                    response = self.process_telegram(data)
                    if response:
                        self._client.sendall(response)

                except:  
                    self.sendDebugInfo(f'Connection Interrupted')
                    self._client.close()
                    self._client = None


    def process_telegram(self, data):
        s = struct.Struct(CMD_FORMAT)
        if len(data) == CMD_TOT_LEN:
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
                return UAM_msg
        return None