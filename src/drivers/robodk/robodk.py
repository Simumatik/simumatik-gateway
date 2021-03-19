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

import sys
import os
from os import path
import winreg

# Import SDK
ROBODK_SDK_FOUND = False

try:
    if os.name == 'nt':# Just try on windows
        reg = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
        key = winreg.OpenKey(reg, r"SOFTWARE\RoboDK")

        robodk_path = winreg.QueryValueEx(key, "INSTDIR")[0] + "\Python"
        sys.path.append(robodk_path) # Add path to system path

        from robolink import Robolink, ITEM_TYPE_ROBOT
        ROBODK_SDK_FOUND = True
except:
    pass

# Driver that connects to robodk
class robodk(driver):
    '''
    This driver uses the RoboDK API to connect to a robot controller. It is based on the Robodk API (https://robodk.com/offline-programming).
    
    The driver will always provide access to the robot axis through the variable called "Axis" (float[6]).
    Optional variable definitions are used to access Station Parameters in RobotDK to be read or written by the driver.

    controller: str
        Robot name in RoboDK. Default = '', will take the first that founds.
    '''

    def __init__(self, name: str, pipe: Optional[Pipe] = None):
        """
        :param name: (optional) Name for the driver
        :param pipe: (optional) Pipe used to communicate with the driver thread. See gateway.py
        """
        # Inherit
        driver.__init__(self, name, pipe)

        # Parameters
        self.controller = ''


    def connect(self) -> bool:
        """ Connect driver.
        
        : returns: True if connection stablished False if not
        """
        if not ROBODK_SDK_FOUND:
            return False

        try:
            self._connection = Robolink()
            if self._connection:
                self.sendDebugInfo('SETUP: Driver RoboDK Scanning...')
                self.robot = self._connection.Item(self.controller)
                if self.robot:
                    if self.robot.Valid() and self.robot.Type() == ITEM_TYPE_ROBOT:
                        self.sendDebugInfo(f'SETUP: Driver RoboDK Connected to {self.controller}...')
                        return True
                else:
                    self.sendDebugInfo(f'Item {self.controller} not found!')

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
        for var_id, var_data in variables.items():
            try:
                if var_id == 'Axis':
                    var_data['value'] = [None for i in range(var_data['size'])]
                    self.variables[var_id] = var_data
                    continue
                else:
                    value = self._connection.getParam(var_id)
                    if value is not None:
                        var_data['value'] = None # Force first update
                        self.variables[var_id] = var_data
                        self.sendDebugInfo(f'SETUP: Variable found {var_id}')
                        continue
            except:
                pass
            
            self.sendDebugInfo(f'SETUP: Variable not found {var_id}')


    def readVariables(self, variables: list) -> list:
        """ Read given variable values. In case that the read is not possible or generates an error BAD quality should be returned.
        : param variables: List of variable ids to be read. 

        : returns: list of tupples including (var_id, var_value, VariableQuality)
        """
        res = []
        for var_id in variables:
            try:
                if var_id == 'Axis':
                    new_value = self.robot.Joints().tr().rows[0] # robot joint rotations [Rax_1, Rax_2, Rax_3, Rax_4, Rax_5, Rax_6]
                    new_value = [round(x,3) for x in new_value]
                    res.append((var_id, new_value, VariableQuality.GOOD))
                    continue
                else:
                    new_value = self._connection.getParam(var_id)
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
                self._connection.setParam(var_id, new_value)
                res.append((var_id, new_value, VariableQuality.GOOD))
            except:
                res.append((var_id, new_value, VariableQuality.BAD))
                     
        return res
