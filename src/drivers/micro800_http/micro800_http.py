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

from urllib import request
import json
from ..driver import VariableDatatype, driver, VariableQuality


class micro800_http(driver):
    '''
    Driver to communicate with Allen Bradley Micro800 Simulator using the HTTP API.

    Parameters:
    port: int
        Port used for the HTTP communication (shown in the simulator). Default = 51234
    '''

    def __init__(self, name: str, pipe: Optional[Pipe] = None):
        """
        :param name: (optional) Name for the driver
        :param pipe: (optional) Pipe used to communicate with the driver thread. See gateway.py
        """
        # Inherit
        driver.__init__(self, name, pipe)

        # Parameters
        self.port = 54321
                
        # Internal variables
        self._output_vars = []
        self._input_vars = []


    def connect(self) -> bool:
        """ Connect driver.
        
        : returns: True if connection stablished False if not
        """
        try:
            # Redefine URL with actual port
            self._connection = f"http://localhost:{self.port}/"

            # Get available outputs
            req = request.Request(self._connection+"/outputs", method="GET")
            r = request.urlopen(req)
            content = r.read()
            if content:
                for var_data in json.loads(content):
                    self._output_vars.append(var_data['Name'])
            else:
                self.sendDebugInfo('Output data not available.')
                return False

            # Get available inputs
            req = request.Request(self._connection+"/inputs", method="GET")
            r = request.urlopen(req)
            content = r.read()
            if content:
                for var_data in json.loads(content):
                    self._input_vars.append(var_data['Name'])
            else:
                self.sendDebugInfo('Input data not available.')
                return False
            
            return True

        except Exception as e:
            self.sendDebugInfo('Exception '+str(e))

        return False


    def disconnect(self):
        """ Disconnect driver.
        """
        pass


    def addVariables(self, variables: dict):
        """ Add variables to the driver. Correctly added variables will be added to internal dictionary 'variables'.
        Any error adding a variable should be communicated to the server using sendDebugInfo() method.
        : param variables: Variables to add in a dict following the setup format. (See documentation) 
        
        """
        for var_id, var_data in variables.items():
            if var_id in self._output_vars or var_id in self._input_vars:
                var_data['value'] = self.defaultVariableValue(var_data['datatype'], var_data['size'])
                self.variables[var_id] = var_data
            else:
                self.sendDebugVarInfo((f'SETUP: Variable not found: {var_id}', var_id))


    def readVariables(self, variables: list) -> list:
        """ Read given variable values. In case that the read is not possible or generates an error BAD quality should be returned.
        : param variables: List of variable ids to be read. 
        : returns: list of tupples including (var_id, var_value, VariableQuality)
        """
        res = []
        try:
            # Read outputs
            req = request.Request(self._connection+"/outputs", method="GET")
            r = request.urlopen(req)
            content = r.read()
            if content:
                for var_data in json.loads(content):
                    if var_data['Name'] in variables:
                        res.append((var_data['Name'], var_data['Value'], VariableQuality.GOOD))
                        variables.remove(var_data['Name'])
                    if not len(variables):
                        break

        except Exception as e:
            self.sendDebugInfo('SETUP failed: Exception '+str(e))
        
        return res


    def writeVariables(self, variables: list) -> list:
        """ Write given variable values. In case that the write is not possible or generates an error BAD quality should be returned.
        : param variables: List of tupples with variable ids and the values to be written (var_id, var_value). 
        : returns: list of tupples including (var_id, var_value, VariableQuality)
        """
        # Send POST Request
        data = []
        
        for (var_id, new_value) in variables:
            data.append({'Name':var_id, 'Value':new_value})
        try:
            data_json = json.dumps(data)
            req = request.Request(self._connection+"/inputs", method="POST")
            req.add_header('Content-Type', 'application/json')
            request.urlopen(req, data=data_json.encode())
            quality = VariableQuality.GOOD
        except Exception as e:
            quality = VariableQuality.BAD

        res = []
        for (var_id, new_value) in variables:
            res.append((var_id, new_value, quality))
        return res
