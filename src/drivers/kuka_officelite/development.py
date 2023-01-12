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
from py_openshowvar import openshowvar

def axis_act_to_list(read_data):
    '''
    Formats $AxisAct struct to list of floats with axis positions.
    '''
    result = read_data.decode()

    result = result.replace("{E6AXIS:", "")
    result = result.replace("}", "")

    data = result.split(',')
    return [float(x[4:]) for x in data[:6]]

class development(driver):
    '''
    Driver that can be used for development. The driver can be used on a component just assigning the driver type "development".
    Feel free to add your code in the methods below.
    Parameters:
    myparam: int
        This is just an example of a driver parameter. Default = 3
    '''

    def __init__(self, name: str, pipe: Optional[Pipe] = None, params:dict = None):
        """
        :param name: (optional) Name for the driver
        :param pipe: (optional) Pipe used to communicate with the driver thread. See gateway.py
        """
        # Inherit
        driver.__init__(self, name, pipe, params)

        # Parameters
        self.ip = '192.168.138.128'
        self.port = 7000

    def connect(self) -> bool:
        """ Connect driver.
        
        : returns: True if connection established False if not
        """
        # Make sure to send a debug message if method returns False
        # self.sendDebugInfo('Error message here') 

        self._connection = openshowvar(self.ip, self.port)
        if not self._connection.can_connect:
            self.sendDebugInfo('Cannot connect to KRC4') 
            print("self.sendDebugInfo('Cannot connect to KRC4')")

        return self._connection.can_connect


    def disconnect(self):
        """ Disconnect driver.
        """
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
        print("add")
        for var_id in list(variables.keys()):
            var_data = dict(variables[var_id])
            try:
                var_value = self._connection.read(var_id, debug=False)
                if var_id == '$AXIS_ACT':
                    var_value = axis_act_to_list(var_value)

                var_data['value'] = None    
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
                var_value = self._connection.read(var_id, debug=False)
                if var_id == '$AXIS_ACT':
                    var_value = axis_act_to_list(var_value)
            except:
                res.append((var_id, var_value, VariableQuality.BAD))
            else:
                res.append((var_id, var_value, VariableQuality.GOOD))

        return res


    def writeVariables(self, variables: list) -> list:
        """ Write given variable values. In case that the write is not possible or generates an error BAD quality should be returned.
        : param variables: List of tupples with variable ids and the values to be written (var_id, var_value). 
        : returns: list of tupples including (var_id, var_value, VariableQuality)
        """
        res = []

        for (var_id, new_value) in variables:
            try:
                self._connection.write(var_id, str(new_value), debug=False)
            except Exception as e:
                res.append((var_id, new_value, VariableQuality.BAD))
            else:
                res.append((var_id, new_value, VariableQuality.GOOD))

        return res
