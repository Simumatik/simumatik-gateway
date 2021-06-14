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

from ..driver import driver, VariableOperation, VariableQuality

# This driver is based on the RTDE provided by Universal Robots:
# https://www.universal-robots.com/how-tos-and-faqs/how-to/ur-how-tos/real-time-data-exchange-rtde-guide-22229/
from .rtde import rtde

import logging
logging.getLogger('rtde').setLevel(logging.CRITICAL)

# Driver that connects to robodk
class universal_robots(driver):
    '''
    This driver is based on the RTDE provided by Universal Robots:
    https://www.universal-robots.com/how-tos-and-faqs/how-to/ur-how-tos/real-time-data-exchange-rtde-guide-22229/
    
    host: str
        Controller IP address
    port: int
        Controller Port address
    frequency: int
        Data writting interval
    '''

    def __init__(self, name: str, pipe: Optional[Pipe] = None):
        """
        :param name: (optional) Name for the driver
        :param pipe: (optional) Pipe used to communicate with the driver thread. See gateway.py
        """
        # Inherit
        driver.__init__(self, name, pipe)

        # Parameters
        self.host = 'localhost'
        self.port = 30004
        self.frequency = 125
        # Variables
        self.inputs_data = None
        self.inputs_setup = None
        self.outputs_setup = None


    def connect(self) -> bool:
        """ Connect driver.
        
        : returns: True if connection stablished False if not
        """
        try:
            self._connection = rtde.RTDE(self.host, self.port)
            self._connection.connect()
            self.sendDebugInfo(f'SETUP: Driver UR Connected to {self.host}')
            return True
        except Exception as e:
            self.sendDebugInfo('SETUP failed: Exception '+str(e))
        
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
        input_vars = {}
        output_vars = {}  

        for var_id, var_data in variables.items():
            try:
                if var_data['size'] == 1:
                    ur_type = self.convert_type(var_data['datatype'])
                    var_data['value'] = None
                elif var_data['size'] == 3:
                    ur_type = "VECTOR3D"
                    var_data['value'] = [None for i in range(var_data['size'])]
                elif var_data['size'] == 6:
                    ur_type = "VECTOR6D"
                    var_data['value'] = [None for i in range(var_data['size'])]
                else:
                    ur_type = None

                if ur_type is not None:
                    if var_data['operation'] == VariableOperation.WRITE:
                        self._connection.send_input_setup([var_id], [ur_type])
                        input_vars[var_id] = ur_type
                    else:
                        self._connection.send_output_setup([var_id], [ur_type], frequency = self.frequency)
                        output_vars[var_id] = ur_type

                    self.variables[var_id] = var_data
                    self.sendDebugVarInfo((f'SETUP: Variable found {var_id}', var_id))
                else:
                    self.sendDebugVarInfo((f'SETUP: Variable type not valid {var_data["datatype"]}', var_id))
            except:
                self.sendDebugVarInfo((f'SETUP: Variable not found {var_id}', var_id))

                  
        if input_vars:
            # Support multiplexing
            if self.inputs_setup:
                input_vars.update(self.inputs_setup)

            self.inputs_data = self._connection.send_input_setup(list(input_vars.keys()), list(input_vars.values()))
            if self.inputs_data:
                # Necessary to avoid error "Exception during variable transmission: Uninitialized parameter"
                for input_var in self.inputs_data.__dict__.keys():
                    if self.inputs_data.__dict__[input_var] == None:
                        self.inputs_data.__dict__[input_var] = 0

                # Save inputs setup data
                self.inputs_setup = input_vars
            else:
                self.sendDebugInfo(f'SETUP: Unable to configure inputs')

        if output_vars:
            # Support multiplexing
            if self.outputs_setup:
                output_vars.update(self.outputs_setup)

            result = self._connection.send_output_setup(list(output_vars.keys()), list(output_vars.values()), frequency = self.frequency)
            if result:
                # Save outputs setup data
                self.outputs_setup = output_vars
            else:
                self.sendDebugInfo(f'SETUP: Unable to configure outputs')

        if not self._connection.send_start():
            self.sendDebugInfo(f'SETUP: Unable to start synchronization')

    def readVariables(self, variables: list) -> list:
        """ Read given variable values. In case that the read is not possible or generates an error BAD quality should be returned.
        : param variables: List of variable ids to be read. 

        : returns: list of tupples including (var_id, var_value, VariableQuality)
        """
        ur_data = self._connection.receive()
        res = []
        self.sendDebugInfo(ur_data.__dict__)
        for var_id in variables:
            try:
                new_value = ur_data.__dict__[var_id]

                if new_value:
                    if self.variables[var_id]['size'] > 1:
                        new_value = [round(x,3) for x in new_value]
                    else:
                        new_value = self.getValueFromString(self.variables[var_id]['datatype'], str(new_value))
                
                res.append((var_id, new_value, VariableQuality.GOOD))
            except:
                res.append((var_id, self.variables[var_id]['value'], VariableQuality.BAD))
            
        return res


    def writeVariables(self, variables: list) -> list:
        """ Write given variable values. In case that the write is not possible or generates an error BAD quality should be returned.
        : param variables: List of tupples with variable ids and the values to be written (var_id, var_value). 

        : returns: list of tupples including (var_id, var_value, VariableQuality)
        """
        res = []
        self.sendDebugInfo(self.inputs_data.__dict__)
        for (var_id, new_value) in variables:
            self.inputs_data.__dict__[var_id] = new_value
            
            if self._connection.send(self.inputs_data):
                res.append((var_id, new_value, VariableQuality.GOOD))
            else:
                self.inputs_data.pop(var_id)
                res.append((var_id, new_value, VariableQuality.BAD))
           
        return res

    #Helper method
    def convert_type(self, type_name):
        switcher = {
            'byte' : 'UINT8',
            'dword' : 'UINT32',
            'qword' : 'UINT64',
            'float' : 'DOUBLE',
            'bool' : 'BOOL',
            'int' : 'INT32',
            'double' : 'DOUBLE'
        }
        return switcher.get(type_name, None)
