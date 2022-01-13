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
import numpy as np
from typing import Optional

from ..driver import VariableQuality, driver
#from ..s7protocol.iso_on_tcp import (getAreaFromString, PDULengthRequest, PDUReadAreas, PDUWriteAreas, connectPLC)

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
        self.SHM_name = "SIMITShared Memory"
        self.header_length = 4
        self.SHM_array = None


    def connect(self) -> bool:
        """ Connect driver.
        
        : returns: True if connection stablished False if not
        """
        try:
            self._connection = shared_memory.SharedMemory(name=self.SHM_name)
            self.SHM_array = np.ndarray((int(self._connection.size/2),), dtype=np.int16, buffer=self._connection.buf)
        except Exception as e:
            self.sendDebugInfo(f"SETUP: Connection with {self.SHM_name} cannot be established. ({e})")
            return False
        return True


    def disconnect(self):
        """ Disconnect driver.
        """
        self._connection.close()
        self.SHM_array = None




    def addVariables(self, variables: dict):
        """ Add variables to the driver. Correctly added variables will be added to internal dictionary 'variables'.
        Any error adding a variable should be communicated to the server using sendDebugInfo() method.
        : param variables: Variables to add in a dict following the setup format. (See documentation) 
        
        """
        def adress_to_byte_bit(adr:str):
            type = ""

            # Get the type (I, IB, IW, ID, Q, QB, QW, QD, M, MB, MW, MD..)
            if adr[:2].isalpha():
                type = adr[:2]
                adr = adr[2:]
            elif adr[:1].isalpha():
                type = adr[:1]
                adr = adr[1:]

            if '.' in adr:
                adr = adr.split('.')
                return {"type" : "bool", "byte" : int(adr[0]), "bit" : int(adr[1])}
            else:
                return {"type" : type, "byte" : int(adr[0])}

        for var_id in list(variables.keys()):
            var_data = dict(variables[var_id])

            area = adress_to_byte_bit(var_id)
            # area = getAreaFromString(var_id, var_data['datatype'])

            if area is not None:
                var_data['area'] = area
                var_data['value'] = 0
                self.variables[var_id] = var_data
            else:
                self.sendDebugVarInfo(('SETUP: Bad variable definition: {}'.format(var_id), var_id))



    def readVariables(self, variables: list) -> list:
        """ Read given variable values. In case that the read is not possible or generates an error BAD quality should be returned.
        : param variables: List of variable ids to be read. 
        : returns: list of tupples including (var_id, var_value, VariableQuality)
        """
        res = []
        for var_id in variables:
            byte = self.header_length + self.variables[var_id]['area']
            value = int(self.SHM_array[int(byte/2)])
            res.append((var_id, value, VariableQuality.GOOD))

        return res


    def writeVariables(self, variables: list) -> list:
        """ Write given variable values. In case that the write is not possible or generates an error BAD quality should be returned.
        : param variables: List of tupples with variable ids and the values to be written (var_id, var_value). 
        : returns: list of tupples including (var_id, var_value, VariableQuality)
        """
        res = []
        for (var_id, value) in variables:
            byte = self.header_length + self.variables[var_id]['area']
            self.SHM_array[int(byte/2)] = value
            res.append((var_id, value, VariableQuality.GOOD))



