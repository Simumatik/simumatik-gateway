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

from ..driver import VariableQuality, driver

import OpenOPC
import pywintypes # To avoid timeout error
pywintypes.datetime=pywintypes.TimeType

class development(driver):
    '''
    Driver that can be used for development. The driver can be used on a component just assigning the driver type "development".
    Feel free to add your code in the methods below.
    Parameters:
    server: string
        This is the server name of the OPC DA Server
    '''

    def __init__(self, name: str, pipe: Optional[Pipe] = None):
        """
        :param name: (optional) Name for the driver
        :param pipe: (optional) Pipe used to communicate with the driver thread. See gateway.py
        """
        # Inherit
        driver.__init__(self, name, pipe)

        # Parameters
        self.server = 'Matrikon.OPC.Simulation.1'


    def connect(self) -> bool:
        """ Connect driver.
        
        : returns: True if connection stablished False if not
        """
        # Make sure to send a debug message if method returns False
        # self.sendDebugInfo('Error message here') 

        self._connection = OpenOPC.client()

        if self.server in self._connection.servers():
            try:
                self._connection.connect(self.server)
            except:
                self.sendDebugInfo("Could not connect to OPC DA server.")
                return False
            else:
                return True
        else:
            self.sendDebugInfo(f'OPC DA server "{self.server}" not found.')
            return False


    def disconnect(self):
        """ Disconnect driver.
        """
        if self._connection is not None:
            self._connection.close()


    def loop(self):
        """ Runs every iteration while the driver is active. Only use if strictly necessary.
        """
        pass


    def addVariables(self, variables: dict):
        """ Add variables to the driver. Correctly added variables will be added to internal dictionary 'variables'.
        Any error adding a variable should be communicated to the server using sendDebugInfo() method.
        : param variables: Variables to add in a dict following the setup format. (See documentation) 
        
        """
        for var_id in list(variables.keys()):
            var_data = dict(variables[var_id])
            try:
                var_data['value'] = self._connection[var_id]
            except Exception as e:
                self.sendDebugInfo(f'SETUP: {e} \"{var_id}\"')
            else:
                self.variables[var_id] = var_data 



    def readVariables(self, variables: list) -> list:
        """ Read given variable values. In case that the read is not possible or generates an error BAD quality should be returned.
        : param variables: List of variable ids to be read. 
        : returns: list of tupples including (var_id, var_value, VariableQuality)
        """
        res = []
        for var_id in variables:
            try:
                value, quality, time = self._connection.read(var_id)    
            except Exception as e:
                res.append((var_id, None, VariableQuality.ERROR))
                self.sendDebugVarInfo(f'readVariables exception: {e}')
            else:
                if quality == 'Good':
                    res.append(var_id, value, VariableQuality.GOOD)
                else:
                    res.append(var_id, value, VariableQuality.BAD)

        return res


    def writeVariables(self, variables: list) -> list:
        """ Write given variable values. In case that the write is not possible or generates an error BAD quality should be returned.
        : param variables: List of tupples with variable ids and the values to be written (var_id, var_value). 
        : returns: list of tupples including (var_id, var_value, VariableQuality)
        """
        res = []

        for (var_id, var_value) in variables:
            try:
                write_result = self._connection.write((var_id, var_value))
            except Exception as e:
                res.append((var_id, None, VariableQuality.ERROR))
                self.sendDebugVarInfo(f'writeVariables exception: {e}')
            else:
                if write_result == "Success":
                    res.append(var_id, var_value, VariableQuality.GOOD)
                else:
                    res.append(var_id, var_value, VariableQuality.BAD)
        
        return res