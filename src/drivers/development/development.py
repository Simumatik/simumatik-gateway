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
import pythoncom

from ..driver import driver

FANUC_API_FOUND = True
try:
    from .fanuc_wrapper import (FRCRobot, constants)
    #import fanuc_wrapper
except Exception as e:
    print(e)
    FANUC_API_FOUND = False

assert FANUC_API_FOUND, "Fanuc is not installed"

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
        self.joint_group = None
        self.joint_positions = None
        self.input_group = None
        self.output_group = None


    def connect(self) -> bool:
        """ Connect driver.
        
        : returns: True if connection stablished False if not
        """
        try:
            # Create API Instance
            #from .fanuc_wrapper import FRCRobot
            pythoncom.CoInitialize()
            self._connection = FRCRobot()
        except Exception as e:
            print(e)
            self.sendDebugInfo("Felkod 1")
            return False

        # Connect
        ip = '127.0.0.1'
        ip2 = '127.0.0.1:9001'
        try:
            self._connection.ConnectEx(HostName=ip, NoWait=False, NumRetries=1, Period=1)#, NoWait=False)
            print(self._connection.HostName)
            print(self._connection.IsOffline)
        except:
            print("Connection failed! Client not found")
            return False
            
        assert self._connection.IsConnected, f"Cannot coonect to {ip}" 

        try:
            # Add pointers
            mobjCurPos = self._connection.CurPosition
            assert mobjCurPos.NumGroups>0, "Joint positions not available"
            print("Groups found:", mobjCurPos.NumGroups)
            self.joint_group = mobjCurPos.Group(1, constants.frJointDisplayType)
            self.joint_positions = self.joint_group.Formats(constants.frJoint)
            self.input_group = self._connection.IOTypes(constants.frDInType).Signals
            self.output_group = self._connection.IOTypes(constants.frDOutType).Signals
            self.input_group.Simulate = True
        except:
            print("Could not find joints")
            return False

        return True


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
            try:
                if var_id == 'Axis':
                    var_data[0] = [None for i in range(var_data['size'])]
                    self.variables[var_id] = var_data
                    continue
                else:
                    self.joint_group.Refresh()
                    value = self.joint_positions.Item(0)
                    if value is not None:
                        var_data['value'] = None # Force first update
                        self.variables[var_id] = var_data
                        self.sendDebugVarInfo((f'SETUP: Variable found {var_id}', var_id))
                        continue
            except:
                pass
            
            self.sendDebugVarInfo((f'SETUP: Variable not found {var_id}', var_id))
        pass


    def readVariables(self, variables: list) -> list:
        """ Read given variable values. In case that the read is not possible or generates an error BAD quality should be returned.
        : param variables: List of variable ids to be read. 
        : returns: list of tupples including (var_id, var_value, VariableQuality)
        """
        res = []
        self.joint_group.Refresh()
        self.output_group
        for var_id in variables:
            try:
                if var_id == 'Axis':
                    new_value = self.joint_positions.Item(0)
                    # new_value = [round(x,3) for x in new_value]
                    res.append((var_id, new_value, VariableQuality.GOOD))
                    continue
                else:
                    new_value = self.output_group(0).Value
                    if new_value is not None:
                        new_value = self.getValueFromString(self.variables[var_id]['datatype'], new_value)
                        res.append((var_id, new_value, VariableQuality.GOOD))
                        continue
            except:
                res.append((var_id, self.variables[var_id]['value'], VariableQuality.BAD))
            
        return res


    def writeVariables(self, variables: list) -> list:
        """ Write given variable values. In case that the write is not possible or generates an error BAD quality should be returned.
        : param variables: List of tupples with variable ids and the values to be written (var_id, var_value). 
        : returns: list of tupples including (var_id, var_value, VariableQuality)
        """

        res = []
        # TODO: Possible improvement can be to send multiple at once
        for (var_id, new_value) in variables:
            try:
                self.input_group(0).Value = new_value
                res.append((var_id, new_value, VariableQuality.GOOD))
            except:
                res.append((var_id, new_value, VariableQuality.BAD))
                     
        return res
