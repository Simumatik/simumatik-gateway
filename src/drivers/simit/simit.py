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

from multiprocessing import Pipe, shared_memory
import struct
from typing import Optional

from ..driver import VariableDatatype, VariableQuality, driver

SIMIT_BOOL = 0
SIMIT_BYTE = 8
SIMIT_WORD = 9
SIMIT_INT = 10
SIMIT_DWORD = 11
SIMIT_DINT = 12
SIMIT_REAL = 13

BIG_ENDIAN = '>'
LITTLE_ENDIAN = '<'

def adress_to_area(vaddress:str, big_endian:bool, vdtype:VariableDatatype):
    if big_endian:
        format= BIG_ENDIAN
    else:
        format = LITTLE_ENDIAN

    if vaddress[:2].isalpha():
        type_letter = vaddress[1]
        byte = int(vaddress[2:])

        if type_letter.upper() == 'B':
            type = SIMIT_BYTE
            len = 1
            format = 'B' #Overwrites (not +=) endian information written above, since byte has no endian information
        elif type_letter.upper() == 'W' and vdtype == VariableDatatype.WORD:
            type = SIMIT_WORD
            format += 'H'
            len = 2
        elif type_letter.upper() == 'W' and vdtype == VariableDatatype.INTEGER:
            type = SIMIT_INT
            format += 'h'
            len = 2
        elif type_letter.upper() == 'D' and vdtype == VariableDatatype.DWORD:
            type = SIMIT_DWORD
            format += 'I'
            len = 4
        elif type_letter.upper() == 'D' and vdtype == VariableDatatype.INTEGER:
            type = SIMIT_DINT
            format += 'i'
            len = 4
        elif type_letter.upper() == 'D' and vdtype == VariableDatatype.FLOAT:
            type = SIMIT_REAL
            format += 'f'
            len = 4
        else:
            return None
        
        return (type, format, len, byte)

    # BOOL
    elif vaddress[:1].isalpha():
        type = SIMIT_BOOL #adr[:1]
        vaddress = vaddress[1:]

    if '.' in vaddress:
        vaddress = vaddress.split('.')
        return {"type" : type, "byte" : int(vaddress[0]), "bit" : int(vaddress[1])}
    else:
        return None
        

class simit(driver):
    '''
    Driver that can be used to connect with simit using shared memory.
    Parameters:
        SHM_name : Name of the shared memory
        big_endian : True if big endian, else little endian
    '''

    def __init__(self, name: str, pipe: Optional[Pipe] = None, params:dict = None):
        """
        :param name: (optional) Name for the driver
        :param pipe: (optional) Pipe used to communicate with the driver thread. See gateway.py
        """
        # Inherit
        driver.__init__(self, name, pipe, params)

        # Parameters
        self.SHM_name = "SIMITShared Memory"
        self.big_endian = False

        self.memory_size = 4096
        self.header_size = 8

        self.bytes = b''


    def connect(self) -> bool:
        """ Connect driver.
        
        : returns: True if connection established False if not
        """
        try:
            self._connection = shared_memory.SharedMemory(name=self.SHM_name)
        except Exception as e:
            self.sendDebugInfo(f"SETUP: Connection with {self.SHM_name} cannot be eestablished. ({e})")
            return False
        else:
            self.bytes = self._connection.buf.tobytes()
            self.memory_size, self.header_size = struct.unpack('II', self.bytes[:8])
            return True


    def disconnect(self):
        """ Disconnect driver.
        """
        self._connection.close()
        self.bytes = b''


    def addVariables(self, variables: dict):
        """ Add variables to the driver. Correctly added variables will be added to internal dictionary 'variables'.
        Any error adding a variable should be communicated to the server using sendDebugInfo() method.
        : param variables: Variables to add in a dict following the setup format. (See documentation) 
        
        """
        for var_id in list(variables.keys()):
            var_data = dict(variables[var_id])

            type, format, len, byte = adress_to_area(var_id, self.big_endian, var_data["datatype"])

            if type is not None:
                var_data['type'] = type
                var_data['format'] = format
                var_data['len'] = len
                var_data['byte'] = byte
                var_data['value'] = 0
                self.variables[var_id] = var_data
            else:
                self.sendDebugVarInfo(('SETUP: Bad variable definition: {}'.format(var_id), var_id))


    def readVariables(self, variables: list) -> list:
        """ Read given variable values. In case that the read is not possible or generates an error BAD quality should be returned.
        : param variables: List of variable ids to be read. 
        : returns: list of tupples including (var_id, var_value, VariableQuality)
        """
        self.bytes = self._connection.buf[:self.memory_size].tobytes()

        res = []
        for var_id in variables:
            byte_adress = self.header_size + self.variables[var_id]['byte']
            format = self.variables[var_id]['format']
            len = self.variables[var_id]['len']

            try:
                values = self.bytes[byte_adress:byte_adress+len] 
                value = struct.unpack(format,values)[0]

                if self.variables[var_id]['type'] == SIMIT_REAL:
                    value = round(value, 3)
            except:
                res.append((var_id, value, VariableQuality.ERROR))
            else:
                res.append((var_id, value, VariableQuality.GOOD))

        return res


    def writeVariables(self, variables: list) -> list:
        """ Write given variable values. In case that the write is not possible or generates an error BAD quality should be returned.
        : param variables: List of tupples with variable ids and the values to be written (var_id, var_value). 
        : returns: list of tupples including (var_id, var_value, VariableQuality)
        """
        res = []

        for (var_id, value) in variables:
            byte_adress = self.header_size + self.variables[var_id]['byte']
            format = self.variables[var_id]['format']
            len = self.variables[var_id]['len']

            try:
                self._connection.buf[byte_adress:byte_adress + len] = struct.pack(format,value)
            except:
                res.append((var_id, value, VariableQuality.ERROR))
            else:
                res.append((var_id, value, VariableQuality.GOOD))
        return res