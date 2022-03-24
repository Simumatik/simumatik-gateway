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
import numpy as np

from ..driver import driver, VariableQuality

CMD_FORMAT = 'c 4s 2s 2s 4s c'
CMD_TOT_LEN = struct.calcsize(CMD_FORMAT)

def UAM_encode(decimal_list, format_str='!H'):
    ascii_str = ''
    for decimal in decimal_list:
        # Value -1 from component means nothing is detected
        if decimal < 0:
            decimal = 65535 # 65535 for 'object not detected'
        hex_val = struct.pack(format_str, decimal)
        ascii_str += str(hex_val.hex()).upper()

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
        Time in seconds to detect connection loss. Default = 30ms
    '''

    def __init__(self, name: str, pipe: Optional[Pipe] = None):
        """
        :param name: (optional) Name for the driver
        :param pipe: (optional) Pipe used to communicate with the driver thread. See gateway.py
        """
        # Inherit
        driver.__init__(self, name, pipe)

        # Parameters
        self.force_write = 0 # No need to force, this driver writes on demand
        self.ip = "0.0.0.0"
        self.port = 10940
        self.transmit_interval = 0.03
        self.data_size = 1080 # Probably could be used as parameter

        # Internal
        self.area_num = '06'
        self.intensity_data = b'0000'*(self.data_size+1) # Constant for now
        self.last_transmit_time = 0
        self.data = np.full((self.data_size+1), 65535) # Initialize to nothing detected
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
            if var_value is not None:
                [first, last] = map(int, var_id.split('_'))
                if (last-first)+1 == len(var_value):                   
                    self.data[first:last+1] = np.asarray(var_value, np.int16)
                    res.append((var_id, var_value, VariableQuality.GOOD))
                else:
                    res.append((var_id, var_value, VariableQuality.BAD))
                    self.sendDebugInfo(f'Bad variable data: {var_id}')
        
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
            # Check new request
            try:
                request = self._client.recv(CMD_TOT_LEN)
                if len(request) == CMD_TOT_LEN:
                    _, _, header, sub_header, _, _ = struct.Struct(CMD_FORMAT).unpack(request)

                    # AR01 request response
                    if header + sub_header == b'AR01':
                        self.last_transmit_time = time.perf_counter()
                        self.encoded_data = UAM_encode(self.data)
                        self._client.sendall(self.AR01_telegram())
                        
            except:  
                pass
            
            # Check connection lost
            if (time.perf_counter() - self.last_transmit_time) > self.transmit_interval * 4:
                self.sendDebugInfo(f'Connection Interrupted')
                self._client.close()
                self._client = None


    def AR01_telegram(self):
        # Build data from sensor readings
        time_ms = int(time.perf_counter()*1000) # Seconds elapsed since detection in protection area
        timestamp = UAM_encode([time_ms], format_str="!I")
        UAM_msg = b'21FFAR01000' + self.area_num.encode() + b'00001111000000000000' + timestamp + b'00000000' + self.encoded_data + self.intensity_data
        res = b'\x02' + UAM_msg + calc_crc(UAM_msg) + b'\x03'
        return res