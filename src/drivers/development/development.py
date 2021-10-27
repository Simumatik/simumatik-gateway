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

from ..driver import driver, VariableQuality 
import pyads


class development(driver):
    '''
    Driver that can be used for development. The driver can be used on a component just assigning the driver type "development".
    Feel free to add your code in the methods below.

    Parameters:
    net_id  : String    : the Beckhoff twincat route to the PLC
    port    : Int       : port to connect to
    '''

    def __init__(self, name: str, pipe: Optional[Pipe] = None):
        """
        :param name: (optional) Name for the driver
        :param pipe: (optional) Pipe used to communicate with the driver thread. See gateway.py
        """
        # Inherit
        driver.__init__(self, name, pipe)
        
        self.net_id = '192.168.0.1.1.1'
        self.port = pyads.PORT_TC3PLC1


    def connect(self) -> bool:
        """ Connect driver.
        
        : returns: True if connection stablished False if not
        """
        # Create connection
        try:
            self._connection = pyads.Connection(self.net_id, self.port)
            self._connection.open()
        except Exception as e:
            self.sendDebugInfo(f"SETUP: Connection with {self.net_id} cannot be stablished. ({e})")
            return False

        # Check connection status.
        state = self._connection.read_state()
        if state[0] == pyads.ADSSTATE_RUN:
            self.sendDebugInfo("SETUP: Driver connected") 
            return True
        else:
            self.sendDebugInfo(f"SETUP: Driver not connected, ADS state = {state[0]}") 
            return False

    def disconnect(self):
        """ Disconnect driver.
        """
        if self._connection:
            self._connection.close()


    def addVariables(self, variables: dict):
        """ Add variables to the driver. Correctly added variables will be added to internal dictionary 'variables'.
        Any error adding a variable should be communicated to the server using sendDebugInfo() method.
        : param variables: Variables to add in a dict following the setup format. (See documentation) 
        """
        for var_id in list(variables.keys()):
            var_data = dict(variables[var_id])
            try:
                var_data['value'] = self._connection.read_by_name(var_id)
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
                var_value = self._connection.read_by_name(var_id)
                res.append((var_id, var_value, VariableQuality.GOOD))
            except Exception as e:
                res.append((var_id, None, VariableQuality.ERROR))
                self.sendDebugInfo(f'SETUP: Cannot read variable \"{var_id}\" ({e})')
                 
        return res
        

    def writeVariables(self, variables: list) -> list:
        """ Write given variable values. In case that the write is not possible or generates an error BAD quality should be returned.
        : param variables: List of tupples with variable ids and the values to be written (var_id, var_value). 
        : returns: list of tupples including (var_id, var_value, VariableQuality)
        """
        res = []
        for (var_id, var_value)  in variables: 
            try:
                self._connection.write_by_name(var_id, var_value)
                res.append((var_id, var_value, VariableQuality.GOOD))
            except Exception as e:
                res.append((var_id, var_value, VariableQuality.BAD))
                self.sendDebugInfo(f'SETUP: Cannot write variable \"{var_id}\" ({e})')

        return res