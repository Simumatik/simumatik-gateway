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
import os, sys, winreg

# Import SDK
MATLAB_SDK_FOUND = False

def add_matlab_path():
    if os.name == 'nt':# Just try on windows
        reg = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)

        # Get registry key to the latest version of MATLAB installed
        key = winreg.OpenKey(reg, "SOFTWARE\\MathWorks\\MATLAB")
        matlab_version = winreg.EnumKey(key, 0)
        key = winreg.OpenKey(reg, "SOFTWARE\\MathWorks\\MATLAB\\" + matlab_version)
        
        # Path to python engine relative to MATLABROOT
        matlab_path = winreg.QueryValueEx(key, "MATLABROOT")[0] + "\\extern\\engines\\python"
        assert os.path.isdir(matlab_path + "\\build\\lib"), "Matlab engine not built"
        sys.path.append(matlab_path + "\\build\\lib") # Add path to system path 

        
        MATLAB_SDK_FOUND = True

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
        self.session_id = None


    def connect(self) -> bool:
        """ Connect driver.

        : returns: True if connection stablished False if not
        """
        try:
            if not MATLAB_SDK_FOUND:
                add_matlab_path()
                import matlab.engine
            
            # Get list of shared matlab sessions
            sessions = matlab.engine.find_matlab()
            assert sessions, "No shared matlab sessions found"
            if self.session_id:
                # id specified, try connecting to that session
                self._connection = matlab.engine.connect_matlab(self.session_id)
            else:
                self._connection = matlab.engine.connect_matlab(sessions[0])
            return True

        except Exception as e:
            self.sendDebugInfo('SETUP failed: ' + str(e))

        return False


    def disconnect(self):
        """ Disconnect driver.
        """
        self._connection.exit()


    def addVariables(self, variables: dict):
        """ Add variables to the driver. Correctly added variables will be added to internal dictionary 'variables'.
        Any error adding a variable should be communicated to the server using sendDebugInfo() method.
        : param variables: Variables to add in a dict following the setup format. (See documentation)

        """
        self.variables.update(variables)
        for var_id in self.variables:
            self.variables[var_id]['value'] = self.defaultVariableValue(self.variables[var_id]['datatype'], self.variables[var_id]['size'])


    def readVariables(self, variables: list) -> list:
        """ Read given variable values. In case that the read is not possible or generates an error BAD quality should be returned.
        : param variables: List of variable ids to be read.
        : returns: list of tupples including (var_id, var_value, VariableQuality)
        """
        res = []
        for var_id in variables:
            try:
                new_value = self._connection.workspace[var_id]
                if self.variables[var_id]['size'] > 1:
                    new_value = [self.getValueFromString(self.variables[var_id]['datatype'], i) for i in new_value[0]]
                else:
                    new_value = self.getValueFromString(self.variables[var_id]['datatype'], new_value)
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
        for (var_id, new_value) in variables:
            self._connection.workspace[var_id] = new_value
            res.append((var_id, new_value, VariableQuality.GOOD))
        return res
