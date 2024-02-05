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

import socket
from multiprocessing import Pipe
from typing import Optional
from ..driver import VariableQuality, VariableDatatype

import fins.udp
from ..driver import driver


class omron_fins(driver):
    '''
    Driver to communicate with Omron CPUs using FINS protocol.

    Parameters:
    ip: str
        IP address of the controller that want to connect to. Default = '192.168.0.1'
    
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
            self._connection.connect('192.168.0.1')
            self._connection.dest_node_add=1
            self._connection.srce_node_add=25

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
            area = getAreaFromString(var_id, var_data['datatype'])
            if area is not (None, None):
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
            (area, address) = self.variables[var_id]['area']
            response = self._connection.memory_area_read(area, address)
            value = int.from_bytes(response[-2:], "big")
            if True:
                res.append((var_id, value, VariableQuality.GOOD))
            else:
                res.append((var_id, 0, VariableQuality.BAD))
        return res


    def writeVariables(self, variables: list) -> list:
        """ Write given variable values. In case that the write is not possible or generates an error BAD quality should be returned.
        : param variables: List of tupples with variable ids and the values to be written (var_id, var_value). 

        : returns: list of tupples including (var_id, var_value, VariableQuality)
        """
        res = []
        for (var_id, new_value) in variables:
            (area, address) = self.variables[var_id]['area']
            response = self._connection.memory_area_write(area, address, new_value.to_bytes(2, 'big'), 1)
            if True:
                res.append((var_id, new_value, VariableQuality.GOOD))
            else:
                res.append((var_id, 0, VariableQuality.BAD))
        return res


def getAreaFromString(self, vaddress, vdtype):
    """ Get an area info tupple from a string."""
    try:
        # Get area
        if vaddress[:3] == "CIO":
            if vaddress[3:].find('.') and vdtype == VariableDatatype.BOOL:
                area = fins.FinsPLCMemoryAreas().CIO_BIT
                [word, bit] = [int(i) for i in vaddress[3:].split('.',2)]
            else:
                area = fins.FinsPLCMemoryAreas().CIO_WORD
                word = int(vaddress[3:])
                bit = 0
        elif vaddress[0] == "D":
            if vaddress[1:].find('.') and vdtype == VariableDatatype.BOOL:
                area = fins.FinsPLCMemoryAreas().DATA_MEMORY_BIT
                [word, bit] = [int(i) for i in vaddress[1:].split('.',2)]
            else:
                area = fins.FinsPLCMemoryAreas().DATA_MEMORY_WORD
                word = int(vaddress[3:])
                bit = 0
        elif vaddress[0] == "H":
            if vaddress[1:].find('.') and vdtype == VariableDatatype.BOOL:
                area = fins.FinsPLCMemoryAreas().HOLDING_BIT
                [word, bit] = [int(i) for i in vaddress[1:].split('.',2)]
            else:
                area = fins.FinsPLCMemoryAreas().HOLDING_WORD   
                word = int(vaddress[3:])
                bit = 0
        elif vaddress[0] == "W":
            if vaddress[1:].find('.') and vdtype == VariableDatatype.BOOL:
                area = fins.FinsPLCMemoryAreas().WORK_BIT
                [word, bit] = [int(i) for i in vaddress[1:].split('.',2)]
            else:
                area = fins.FinsPLCMemoryAreas().WORK_WORD
                word = int(vaddress[3:])
                bit = 0
        else:
            return (None, None)
        address = word.to_bytes(2, 'big')+ bit.to_bytes(2, 'big')
        return (area, address)

    except Exception as e:
        return (None, None) 