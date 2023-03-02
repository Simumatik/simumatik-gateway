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

from ..driver import driver, VariableQuality, VariableDatatype

import sys
import os
import winreg

# Import SDK
epson_rcapi_FOUND = False

try:
    if os.name == 'nt':# Just try on windows
        reg = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
        main_key = winreg.OpenKey(reg, r"SOFTWARE\WOW6432Node\SEIKO EPSON CORPORATION")
        
        i = 0
        while True:
            result = winreg.EnumKey(main_key, i)
            i += 1
            if "EPSON RC+ 7.0" in result:
                sub_key = winreg.OpenKey(main_key, result)
                while True: 
                    result = winreg.EnumKey(sub_key, i)
                    i += 1
                    if "Install" in result:
                        key = winreg.OpenKey(sub_key, result)
                        dll_path = winreg.QueryValueEx(key, "EPSON RC+ 7.0")[0] + "\\exe"
                        sys.path.append(dll_path) # Add path to system pat

                        import clr
                        clr.FindAssembly("RCAPINet")
                        clr.AddReference("RCAPINet")
                        #clr.AddReference("System")
                        #clr.AddReference("System.Collections")
                        import RCAPINet

                        epson_rcapi_FOUND = True
                        break
except:
    pass

# Driver that connects to epson_rcapi
class epson_rcapi(driver):
    '''
    This driver uses the Yaskawa plci API to connect to a controller.
    If the variable path is not specified with the @ character, the driver will assume is a global variable and will add the prefix "@GlobalVariables.".
    
    connection_name: str
        Connection name in Epson RC. Default = '', will take the first non-usb connection.
    '''

    def __init__(self, name: str, pipe: Optional[Pipe] = None, params:dict = None):
        """
        :param name: (optional) Name for the driver
        :param pipe: (optional) Pipe used to communicate with the driver thread. See gateway.py
        """
        # Inherit
        driver.__init__(self, name, pipe, params)

        # Parameters
        self.connection_name = ''


    def connect(self) -> bool:
        """ Connect driver.
        
        : returns: True if connection established False if not
        """
        try:
            if not epson_rcapi_FOUND:
                raise Exception('Yaskawa Plci DLL not found')

            self._connection = RCAPINet.Spel()
            self._connection.Initialize()
            res = self._connection.GetConnectionInfo()
            for i in res:
                if (i.ConnectionName == self.connection_name) or (self.connection_name=="" and i.ConnectionName!="USB"):
                    self._connection.Connect(i.ConnectionNumber)
                    self.sendDebugInfo(f'Connected to {i.ConnectionName}')
                    return True

        except Exception as e:
            self.sendDebugInfo('Exception '+str(e))

        return False

    def disconnect(self):
        """ Disconnect driver.
        """
        if self._connection:
            self._connection.Disconnect()
            self._connection.Dispose()

    def addVariables(self, variables: dict):
        """ Add variables to the driver. Correctly added variables will be added to internal dictionary 'variables'.
        Any error adding a variable should be communicated to the server using sendDebugInfo() method.

        : param variables: Variables to add in a dict following the setup format. (See documentation) 
        
        """
        # Check variable elements
        try:
            for var_id, var_data in variables.items():
                path = var_id if '@' in var_id else "@GlobalVariables."+var_id
                varList = List[System.String]()
                varList.Add(path)
                res = self._service.ReadVariables(varList)
                for value in res:
                    if value is not None:
                        var_data['value'] = None # Force first update
                        var_data['path'] = path 
                        self.variables[var_id] = var_data
                        self.sendDebugVarInfo((f'SETUP: Variable found {var_id}', var_id))
                    else:
                        self.sendDebugVarInfo((f'SETUP: Variable not found {var_id}', var_id))
        except Exception as e:
            self.sendDebugInfo('Exception '+str(e))
                 

    def readVariables(self, variables: list) -> list:
        """ Read given variable values. In case that the read is not possible or generates an error BAD quality should be returned.
        : param variables: List of variable ids to be read. 

        : returns: list of tupples including (var_id, var_value, VariableQuality)
        """
        res = []
        try:
            varList = List[System.String]()
            for var_id in variables:
                varList.Add(self.variables[var_id]['path'])
            if varList.Count>0:
                new_values = self._service.ReadVariables(varList)
                for i, new_value in enumerate(new_values):
                    if new_value is not None:
                        res.append((variables[i], new_value, VariableQuality.GOOD))
                    else:
                        res.append((variables[i], new_value, VariableQuality.BAD))
        except:
            pass
        return res

    def writeVariables(self, variables: list) -> list:
        """ Write given variable values. In case that the write is not possible or generates an error BAD quality should be returned.
        : param variables: List of tupples with variable ids and the values to be written (var_id, var_value). 

        : returns: list of tupples including (var_id, var_value, VariableQuality)
        """
        res = []
        try:
            varList = List[System.String]()
            valueList = List[System.Object]()
            for (var_id, new_value) in variables:
                varList.Add(self.variables[var_id]['path'])
                if self.variables[var_id]['datatype'] == VariableDatatype.BOOL:
                    valueList.Add(System.Boolean(new_value))
                elif self.variables[var_id]['datatype'] == VariableDatatype.BYTE:
                    valueList.Add(System.Byte(new_value))
                elif self.variables[var_id]['datatype'] == VariableDatatype.INTEGER:
                    valueList.Add(System.Int32(new_value))
                elif self.variables[var_id]['datatype'] == VariableDatatype.WORD:
                    valueList.Add(System.UInt16(new_value))
                elif self.variables[var_id]['datatype'] == VariableDatatype.DWORD:
                    valueList.Add(System.UInt32(new_value))
                elif self.variables[var_id]['datatype'] == VariableDatatype.QWORD:
                    valueList.Add(System.UInt64(new_value))
                elif self.variables[var_id]['datatype'] == VariableDatatype.FLOAT:
                    valueList.Add(System.Double(new_value))
                else:
                    assert False, "Not supported datatype!"
            if varList.Count>0:
                self._service.WriteVariables(varList, valueList)
                for (var_id, new_value) in variables:
                    res.append((var_id, new_value, VariableQuality.GOOD))
        except:
            pass
        return res