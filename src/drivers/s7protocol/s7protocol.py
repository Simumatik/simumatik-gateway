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

from .iso_on_tcp import (getAreaFromString, PDULengthRequest, PDUReadAreas, PDUWriteAreas, connectPLC)
from ..driver import driver


class s7protocol(driver):
    '''
    Driver to communicate with Siemens PLCs using S7Protocol (ISO over TCP).
    Compatible with S-300, S-400 and LOGO! PLC

    Parameters:
    ip: str
        IP address of the controller that want to connect to. Default = '192.168.0.1'
    
    rack: int
        Rack number of the CPU. Default = 0
    
    slot: int
        Slot number of the CPU. Default = 2
    '''

    # CONSTANTS
    MaxPDULength    = 1920
    PDU_COUNTER     = 0
    MAX_PDU_COUNTER = 65535
    MAX_ITEMS       = 10 # Number of elements that can be read or write at the time

    def __init__(self, name: str, pipe: Optional[Pipe] = None, params:dict = None):
        """
        :param name: (optional) Name for the driver
        :param pipe: (optional) Pipe used to communicate with the driver thread. See gateway.py
        """
        # Inherit
        driver.__init__(self, name, pipe, params)

        # Parameters
        self.ip = '192.168.0.1'
        self.rack = 0
        self.slot = 2
        

    def connect(self) -> bool:
        """ Connect driver.
        
        : returns: True if connection established False if not
        """
        try:
            self._connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self._connection.settimeout(2)
            self._connection.connect((self.ip, 102))
        except Exception as e:
            self.sendDebugInfo(f"Socket connection with {self.ip} cannot be established.")
            return False

        if connectPLC(self._connection, rack=self.rack, slot=self.slot):
            self.PDU_COUNTER = self.PDU_COUNTER + 1 if self.PDU_COUNTER < self.MAX_PDU_COUNTER else 1
            PDULength = PDULengthRequest(self._connection, self.PDU_COUNTER)
            if (self.MaxPDULength > PDULength): self.MaxPDULength = PDULength
            self.sendDebugInfo("New PDU Max length set to: "+str(self.MaxPDULength))
            return True

        self.sendDebugInfo(f"S7 Connection with PLC cannot be established.")
        return False


    def disconnect(self):
        """ Disconnect driver.
        """
        if self._connection:
            self._areas = {}
            self._connection.close()


    def addVariables(self, variables: dict):
        """ Add variables to the driver. Correctly added variables will be added to internal dictionary 'variables'.
        Any error adding a variable should be communicated to the server using sendDebugInfo() method.

        : param variables: Variables to add in a dict following the setup format. (See documentation) 
        
        """
        # TODO: Size is not considered
        for var_id in list(variables.keys()):
            var_data = dict(variables[var_id])
            area = getAreaFromString(var_id, var_data['datatype'])
            if area is not None:
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
        varray = []
        for var_id in variables:
            varray.append((var_id, self.variables[var_id]['area']))

        res = []
        if len(varray)>0:
            
            while len(varray):
                if len(varray) >= self.MAX_ITEMS:
                    rarray = varray[:self.MAX_ITEMS]
                    del varray[:self.MAX_ITEMS]
                else:
                    rarray = varray[:]
                    varray = []

                self.PDU_COUNTER = self.PDU_COUNTER + 1 if self.PDU_COUNTER < self.MAX_PDU_COUNTER else 1
                for (vname, vvalue, quality) in PDUReadAreas(self._connection, self.PDU_COUNTER, rarray):
                    res.append((vname, vvalue, quality))
        return res


    def writeVariables(self, variables: list) -> list:
        """ Write given variable values. In case that the write is not possible or generates an error BAD quality should be returned.
        : param variables: List of tupples with variable ids and the values to be written (var_id, var_value). 

        : returns: list of tupples including (var_id, var_value, VariableQuality)
        """
        varray = []
        for (var_id, new_value) in variables:
            if new_value != None:
                varray.append((var_id, self.variables[var_id]['area'], new_value))

        res = []
        if len(varray)>0:
            while len(varray):
                if len(varray) >= self.MAX_ITEMS:
                    warray = varray[:self.MAX_ITEMS]
                    del varray[:self.MAX_ITEMS]
                else:
                    warray = varray[:]
                    varray = []
                
                self.PDU_COUNTER = self.PDU_COUNTER + 1 if self.PDU_COUNTER < self.MAX_PDU_COUNTER else 1
                for (vname, vvalue, quality) in PDUWriteAreas(self._connection, self.PDU_COUNTER, warray):
                    res.append((vname, vvalue, quality))

        return res    
