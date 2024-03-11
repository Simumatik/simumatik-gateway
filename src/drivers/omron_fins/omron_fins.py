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
from ..driver import VariableQuality, VariableDatatype

import fins.udp
from ..driver import driver


class omron_fins(driver):
    '''
    Driver to communicate with Omron CPUs using FINS protocol.

    The following memory areas can be used:
        * WORK (w)
        * CIO (c)
        * DATA_MEMORY (d)
        * HOLDING (h)

    Parameters:
    ip: str
        IP address of the target controller for connection. Default = '192.168.0.1'
    
    dest_node_add: int
        Destination node address. Default = 0
    
    srce_node_add: int
        Source node address. Default = 0
    '''

    def __init__(self, name: str, pipe: Optional[Pipe] = None, params:dict = None):
        """
        :param name: (optional) Name for the driver
        :param pipe: (optional) Pipe used to communicate with the driver thread. See gateway.py
        """
        # Inherit
        driver.__init__(self, name, pipe, params)

        # Parameters
        self.ip = '192.168.0.1'
        self.dest_node_add = 0
        self.srce_node_add = 0
        

    def connect(self) -> bool:
        """ Connect driver.
        
        : returns: True if connection established False if not
        """
        try:
            self._connection = fins.udp.UDPFinsConnection()
            self._connection.dest_node_add=1
            self._connection.srce_node_add=25
            self._connection.connect('192.168.0.1')
            self._connection.cpu_unit_status_read()

        except Exception as e:
            self.sendDebugInfo(f"Socket connection with {self.ip} cannot be established.")
            return False
        
        return True


    def disconnect(self):
        """ Disconnect driver.
        """
        if self._connection:
            self._connection = None


    def addVariables(self, variables: dict):
        """ Add variables to the driver. Correctly added variables will be added to internal dictionary 'variables'.
        Any error adding a variable should be communicated to the server using sendDebugInfo() method.

        : param variables: Variables to add in a dict following the setup format. (See documentation) 
        
        """
        # TODO: Size is not considered
        for var_id in list(variables.keys()):
            var_data = dict(variables[var_id])
            area = self.getAreaFromString(var_id, var_data['datatype'])
            if area != None:
                var_data['area'] = area
                var_data['value'] = None
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
            (data_type, memory_area, begin_address, word_count) = self.variables[var_id]['area']
            code = 0
            try:
                response = self._connection.get_values(data_type, memory_area, begin_address, word_count)
                if isinstance(response, bytes):
                    value = int.from_bytes(response, "big")
                else:
                    value = response
                res.append((var_id, value, VariableQuality.GOOD))
            except Exception as e:
                print("readVariables Exception:", str(e))
                res.append((var_id, 0, VariableQuality.BAD))
        return res


    def writeVariables(self, variables: list) -> list:
        """ Write given variable values. In case that the write is not possible or generates an error BAD quality should be returned.
        : param variables: List of tupples with variable ids and the values to be written (var_id, var_value). 

        : returns: list of tupples including (var_id, var_value, VariableQuality)
        """
        res = []
        for (var_id, new_value) in variables:
            (data_type, memory_area, begin_address, word_count) = self.variables[var_id]['area']
            try:
                if data_type in ['2s','4s','8s']:
                    data = new_value.to_bytes(2*word_count,'big')
                else:
                    data = new_value
                response = self._connection.set_values(data_type, memory_area, begin_address, word_count, data)
            except Exception as e:
                response = fins.FinsResponseFrame()
                print("writeVariables Exception:", str(e))
            if response.end_code == b'\x00@':
                res.append((var_id, new_value, VariableQuality.GOOD))
            else:
                res.append((var_id, 0, VariableQuality.BAD))
        return res

    def getAreaFromString(self, vaddress, vdtype):
        """ Get an area info tupple from a string."""
        try:
            # Get area
            if vaddress[0].lower() in ['w','c','d','h']:
                if vaddress[0].lower() == 'w':
                    memory_area = fins.FinsPLCMemoryAreas().WORK_WORD
                elif vaddress[0].lower() == 'c':
                    memory_area = fins.FinsPLCMemoryAreas().CIO_WORD
                elif vaddress[0].lower() == 'd':
                    memory_area = fins.FinsPLCMemoryAreas().DATA_MEMORY_WORD
                elif vaddress[0].lower() == 'h':
                    memory_area = fins.FinsPLCMemoryAreas().HOLDING_WORD
                
                if vdtype == VariableDatatype.INTEGER:
                    data_type = '>h'
                    word_count = 1
                elif vdtype == VariableDatatype.WORD:
                    data_type = '2s'
                    word_count = 1
                elif vdtype == VariableDatatype.DWORD:
                    data_type = '4s'
                    word_count = 2
                elif vdtype == VariableDatatype.QWORD:
                    data_type = f'8s'
                    word_count = 4
                elif vdtype == VariableDatatype.FLOAT:
                    data_type = '>f'
                    word_count = 2
                word_address = int(vaddress[1:])
                bit_address = 0
                begin_address = word_address.to_bytes(2, 'big') + bit_address.to_bytes(1, 'big')
                return (data_type, memory_area, begin_address, word_count)
            else:
                return None
        except Exception as e:
            return None 