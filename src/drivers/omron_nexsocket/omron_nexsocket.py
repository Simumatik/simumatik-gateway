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
import sys
import winreg
import struct
import ctypes

from ..driver import driver, VariableDatatype, VariableQuality

NEXSOCKET_PORT = 7000
SOCKET_ERROR = -1
REC_SIZE = 5000

class omron_nexsocket(driver):
    '''
    Driver that can be used to communicate with the Omron NEX Simulator. It is based on the NexSocket.dll
    The variable names in Simumatik need to match exactly with the name in the Global Variables at Sysmac Studio.
    Parameters:
    ip: str
        IP address of the Sysmac Simulator. Default = '127.0.0.1'
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


    def connect(self) -> bool:
        """ Connect driver.
        
        : returns: True if connection established False if not
        """
        try:
            self._handle = None
            self._res_buffer = ctypes.create_string_buffer(REC_SIZE)
            reg = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
            main_key = winreg.OpenKey(reg, r"SOFTWARE\Omron")
            i = 0
            while True:
                result = winreg.EnumKey(main_key, i)
                i += 1
                if "Sysmac Studio" in result:
                    key = winreg.OpenKey(main_key, result)
                    OmronSysmac_path = winreg.QueryValueEx(key, "INSTALLPATH")[0]
                    break

            self._connection = ctypes.WinDLL(OmronSysmac_path+'\\MATLAB\\Win32\\NexSocket.dll')
            res = self._connection.NexSock_initialize()
            assert res>0, f'NexSocket initialization failed.'
            self._handle = ctypes.c_short()
            res = self._connection.NexSockClient_connect(ctypes.byref(self._handle), self.ip.encode('utf-8'), ctypes.c_int16(NEXSOCKET_PORT))     
            assert res>0, f'Connection with {self.ip}:{NEXSOCKET_PORT}'   
            assert self._handle.value>0, f'Connection did not return valid handle ({self._handle}).'
            return True
        except Exception as e:
            self.sendDebugInfo('Error during connection: {e}') 
        return False


    def disconnect(self):
        """ Disconnect driver.
        """
        if self._connection:
            if self._handle:
                self._connection.NexSock_close(self._handle.value)
            self._connection.NexSock_terminate()


    def addVariables(self, variables: dict):
        """ Add variables to the driver. Correctly added variables will be added to internal dictionary 'variables'.
        Any error adding a variable should be communicated to the server using sendDebugInfo() method.
        : param variables: Variables to add in a dict following the setup format. (See documentation) 
        
        """
        for var_id in list(variables.keys()):
            try:
                var_data = dict(variables[var_id])
                (response, error) = self.process_request(f'GetVarAddrText 1 VAR://{var_id}')
                assert error is None and len(response)==3, error
                tagRevision = response[0].decode('utf-8')
                address = response[2].decode('utf-8')[:-1] # For some reason there is an extra space
                bit_size = int(address.split(',')[-1])
                byte_size = int(bit_size/8)
                if var_data['datatype']==VariableDatatype.BOOL:
                    assert byte_size==0 and bit_size==1, 'Wrong datatype definition in controller.'
                elif var_data['datatype']==VariableDatatype.BYTE:
                    assert byte_size==1, 'Wrong datatype definition in controller.'
                elif var_data['datatype']==VariableDatatype.WORD:
                    assert byte_size==2, 'Wrong datatype definition in controller.'
                elif var_data['datatype']==VariableDatatype.INTEGER:
                    assert byte_size==2, 'Wrong datatype definition in controller.'
                elif var_data['datatype']==VariableDatatype.DWORD:
                    assert byte_size==4, 'Wrong datatype definition in controller.'
                elif var_data['datatype']==VariableDatatype.QWORD:
                    assert byte_size==8, 'Wrong datatype definition in controller.'
                elif var_data['datatype']==VariableDatatype.FLOAT:
                    assert byte_size==4, 'Wrong datatype definition in controller.'
                var_data['tagRevision'] = tagRevision
                var_data['address'] = address
                var_data['byte_size'] = byte_size
                var_data['value'] = self.defaultVariableValue(var_data['datatype'], var_data['size'])
                self.variables[var_id] = var_data
            except Exception as e:
                self.sendDebugVarInfo((f'SETUP: Bad variable definition: {var_id}, {e}', var_id))


    def readVariables(self, variables: list) -> list:
        """ Read given variable values. In case that the read is not possible or generates an error BAD quality should be returned.
        : param variables: List of variable ids to be read. 
        : returns: list of tupples including (var_id, var_value, VariableQuality)
        """
        res = []
        payload = ''
        for var_id in variables:
            tagRevision = self.variables[var_id]['tagRevision']
            tag_address = self.variables[var_id]['address']
            if payload == '':
                payload = f'AsyncReadMemText {tagRevision} {len(variables)}'
            payload += f' {tag_address},2'
        if variables:
            (response, error) = self.process_request(payload)
            if error is None and len(response)==1:
                var_values = response[0]
                for var_id in variables:
                    datatype = self.variables[var_id]['datatype']
                    size = max(1,self.variables[var_id]['byte_size']) # TO receive booleans
                    value_hex = var_values[:size]
                    var_values = var_values[size:]
                    if datatype==VariableDatatype.BOOL:
                        value = value_hex == b'\x01'
                    elif datatype==VariableDatatype.BYTE:
                        value = struct.unpack('B',value_hex)[0]
                    elif datatype==VariableDatatype.WORD:
                        value = struct.unpack('H',value_hex)[0]
                    elif datatype==VariableDatatype.INTEGER:
                        value = struct.unpack('h',value_hex)[0]
                    elif datatype==VariableDatatype.DWORD:
                        value = struct.unpack('L',value_hex)[0]
                    elif datatype==VariableDatatype.QWORD:
                        value = struct.unpack('Q',value_hex)[0]
                    elif datatype==VariableDatatype.FLOAT:
                        value = struct.unpack('f',value_hex)[0]
                    res.append((var_id, value, VariableQuality.GOOD))
            else:
                res.append((var_id, None, VariableQuality.BAD))
        return res


    def writeVariables(self, variables: list) -> list:
        """ Write given variable values. In case that the write is not possible or generates an error BAD quality should be returned.
        : param variables: List of tupples with variable ids and the values to be written (var_id, var_value). 
        : returns: list of tupples including (var_id, var_value, VariableQuality)
        """
        res = []
        payload = ''
        for (var_id, new_value) in variables:
            tagRevision = self.variables[var_id]['tagRevision']
            tag_address = self.variables[var_id]['address']
            datatype = self.variables[var_id]['datatype']
            if datatype==VariableDatatype.BOOL:
                value_hex = b'\x01' if new_value else b'\x00'
            elif datatype==VariableDatatype.BYTE:
                value_hex = struct.pack('B',new_value)
            elif datatype==VariableDatatype.WORD:
                value_hex = struct.pack('H',new_value)
            elif datatype==VariableDatatype.INTEGER:
                value_hex = struct.pack('h',new_value)
            elif datatype==VariableDatatype.DWORD:
                value_hex = struct.pack('L',new_value)
            elif datatype==VariableDatatype.QWORD:
                value_hex = struct.pack('Q',new_value)
            elif datatype==VariableDatatype.FLOAT:
                value_hex = struct.pack('f',new_value)
            if payload == '':
                payload = f'AsyncWriteMemText {tagRevision} {len(variables)}'
            payload += f' {tag_address},2,'+value_hex.hex() 
        if variables:
            (response, error) = self.process_request(payload)
            for (var_id, new_value) in variables: 
                if error is not None:
                    res.append((var_id, new_value, VariableQuality.BAD))
                else:
                    res.append((var_id, new_value, VariableQuality.GOOD))
        return res

    def process_request(self, request):
        res = []
        error = None
        try:
            sent_length = self._connection.NexSock_send(self._handle, request.encode('utf-8'), len(request))
            assert sent_length>0, 'NexSocket connection error sending data.'
            while True:
                response_length = self._connection.NexSock_receive(self._handle, self._res_buffer, REC_SIZE)
                if response_length == 0: # response end
                    break
                elif response_length < 0: # response error
                    error = self._res_buffer.value.decode('utf-8')
                else: # response payload
                    res.append(self._res_buffer[:response_length])
        except Exception as e:
            error = e
        return (res, error)