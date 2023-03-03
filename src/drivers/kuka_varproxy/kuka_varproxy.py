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

from ..driver import VariableQuality, VariableDatatype, driver
import socket
import struct
import random

def axis_act_to_list(read_data):
    '''
    Formats $AxisAct struct to list of floats with axis positions.
    '''
    result = read_data.decode()

    result = result.replace("{E6AXIS:", "")
    result = result.replace("}", "")

    data = result.split(',')
    return [float(x[4:]) for x in data]

def pack_read_request(var_id, msg_id):
    var_id_len = len(var_id)
    flag = 0
    req_len = var_id_len + 3

    return struct.pack(
        '!HHBH'+str(var_id_len)+'s',
            msg_id,
            req_len,
            flag,
            var_id_len,
            var_id
    ) 

def pack_write_request(var_id, value, msg_id):
    var_id_len = len(var_id)
    value_len = len(value)
    flag = 1
    req_len = var_id_len + 3 + 2 + value_len
    
    return struct.pack(
        '!HHBH'+str(var_id_len)+'s'+'H'+str(value_len)+'s',
        msg_id,
        req_len,
        flag,
        var_id_len,
        var_id,
        value_len,
        value
        )

def read_response(response, msg_id):
    if response is not None:
        value_len = len(response) - struct.calcsize('!HHBH') - 3
        result = struct.unpack('!HHBH'+str(value_len)+'s'+'3s', response)
        recieved_msg_id, body_len, flag, value_len, value, isok = result
        if recieved_msg_id == msg_id and result[-1].endswith(b'\x01'):
            return value
    return None


class kuka_varproxy(driver):
    '''
    Driver that can be used for communication with a Kuka Varproxy server, installed on a KUKA Robot Controller
    Parameters:
    ip: string
        The IP-address of the KukaVarProxy server. Default = '192.168.138.1'
    port: int
        The port number used to communicate with KukaVarProxy server. Default = 7000
    '''

    def __init__(self, name: str, pipe: Optional[Pipe] = None, params:dict = None):
        """
        :param name: (optional) Name for the driver
        :param pipe: (optional) Pipe used to communicate with the driver thread. See gateway.py
        """
        # Inherit
        driver.__init__(self, name, pipe, params)
        
        # Parameters
        self.ip = '192.168.138.1'
        self.port = 7000


    def connect(self) -> bool:
        """ Connect driver.
        : returns: True if connection established False if not
        """
        self.msg_id = random.randint(1, 100)
        self._connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            ret = self._connection.connect_ex((self.ip, self.port))
            return ret == 0
        except socket.error:
            self.sendDebugInfo('Cannot connect to KRC4') 
            return False


    def disconnect(self):
        """ Disconnect driver.
        """
        self._connection.close()


    def addVariables(self, variables: dict):
        """ Add variables to the driver. Correctly added variables will be added to internal dictionary 'variables'.
        Any error adding a variable should be communicated to the server using sendDebugInfo() method.
        : param variables: Variables to add in a dict following the setup format. (See documentation) 
        
        """
        for var_id in list(variables.keys()):
            var_data = dict(variables[var_id])
            try:
                self.msg_id = (self.msg_id + 1) % 65536
                self._connection.send(pack_read_request(var_id.encode(), self.msg_id))
                read_response(self._connection.recv(256), self.msg_id)
                var_data['value'] = None    
                self.variables[var_id] = var_data 
            except Exception as e:
                self.sendDebugInfo(f'SETUP: {e} \"{var_id}\"')


    def readVariables(self, variables: list) -> list:
        """ Read given variable values. In case that the read is not possible or generates an error BAD quality should be returned.
        : param variables: List of variable ids to be read. 
        : returns: list of tupples including (var_id, var_value, VariableQuality)
        """
        res = []
        for var_id in variables:
            try:
                self.msg_id = (self.msg_id + 1) % 65536
                self._connection.send(pack_read_request(var_id.encode(), self.msg_id))
                var_value = read_response(self._connection.recv(256), self.msg_id)
                if var_id == '$AXIS_ACT':
                    var_value = axis_act_to_list(var_value)
                elif self.variables[var_id]['datatype'] in [VariableDatatype.INTEGER, VariableDatatype.BYTE, VariableDatatype.WORD, VariableDatatype.DWORD, VariableDatatype.QWORD]:
                    var_value = int(var_value)
                elif self.variables[var_id]['datatype'] == VariableDatatype.FLOAT:
                    var_value = float(var_value)
            except Exception as e:
                res.append((var_id, var_value, VariableQuality.BAD))
            else:
                res.append((var_id, var_value, VariableQuality.GOOD))
        return res


    def writeVariables(self, variables: list) -> list:
        """ Write given variable values. In case that the write is not possible or generates an error BAD quality should be returned.
        : param variables: List of tupples with variable ids and the values to be written (var_id, var_value). 
        : returns: list of tupples including (var_id, var_value, VariableQuality)
        """
        res = []
        for (var_id, new_value) in variables:
            try:
                self.msg_id = (self.msg_id + 1) % 65536
                self._connection.send(pack_write_request(var_id.encode(), str(new_value).encode(), self.msg_id))
                read_response(self._connection.recv(256), self.msg_id)
            except Exception as e:
                res.append((var_id, new_value, VariableQuality.BAD))
            else:
                res.append((var_id, new_value, VariableQuality.GOOD))
        return res