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
ACS_SPIIPLUS_FOUND = False

try:
    if os.name == 'nt':# Just try on windows
        reg = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
        main_key = winreg.OpenKey(reg, "SOFTWARE\\WOW6432Node\\Microsoft\\Windows\\CurrentVersion\\SharedDlls")
    
        i = 0
        while True:
            path,_,_ = winreg.EnumValue(main_key, i)
            i += 1
            if "SPiiPlus .NET Library\ACS.SPiiPlusNET.dll" in path:
                dll_path = '\\'.join(path.split('\\')[:-1])
                sys.path.append(dll_path) # Add path to system pat

                import clr
                clr.FindAssembly("ACS.SPiiPlusNET")
                clr.AddReference("ACS.SPiiPlusNET")
                from ACS.SPiiPlusNET import Api, EthernetCommOption
                ACS_SPIIPLUS_FOUND = True
                break
except:
    pass

# Driver that connects to ACS Motion Control using SPiiPlus
class acs_spiiplus(driver):
    '''
    Driver to communicate with ACS Motion controllers. Supports real controllers using TCP or UDP communication, as well as the simulator.
        
    ip: str
        Ip address of the ACS Controller. Default = '192.168.0.1'.
    
    comm: str
        Communication type used: tcp, udp, simulator. Default = 'tcp'.
    '''

    def __init__(self, name: str, pipe: Optional[Pipe] = None, params:dict = None):
        """
        :param name: (optional) Name for the driver
        :param pipe: (optional) Pipe used to communicate with the driver thread. See gateway.py
        """
        # Inherit
        driver.__init__(self, name, pipe, params)

        # Parameters
        self.ip = '192.168.0.1'
        self.comm = 'tcp'


    def connect(self) -> bool:
        """ Connect driver.
        
        : returns: True if connection established False if not
        """
        try:
            if not ACS_SPIIPLUS_FOUND:
                raise Exception('ACS.APiiPlusNET DLL not found')

            self._connection = Api()
            info = self._connection.GetConnectionInfo()
            if self.comm == 'simulator':
                self._connection.OpenCommSimulator()
            elif self.comm == 'tcp':
                port = int(EthernetCommOption.ACSC_SOCKET_STREAM_PORT)
                self._connection.OpenCommEthernetTCP(self.ip, port)
            elif self.comm == 'udp':
                port = int(EthernetCommOption.ACSC_SOCKET_DGRAM_PORT)
                self._connection.OpenCommEthernetUDP(self.ip, port)
            self.sendDebugInfo(f'Connected to {self.ip}')
            return True

        except Exception as e:
            self.sendDebugInfo('Exception '+str(e))

        return False

    def disconnect(self):
        """ Disconnect driver.
        """
        if self._connection:
            self._connection = None

    def addVariables(self, variables: dict):
        """ Add variables to the driver. Correctly added variables will be added to internal dictionary 'variables'.
        Any error adding a variable should be communicated to the server using sendDebugInfo() method.

        : param variables: Variables to add in a dict following the setup format. (See documentation) 
        
        """
        # Check variable elements
        try:
            for var_id, var_data in variables.items():
                try:
                    value = self._connection.ReadVariable(var_id)
                    var_data['value'] = value # Force first update
                    self.variables[var_id] = var_data
                    self.sendDebugVarInfo((f'SETUP: Variable found {var_id}', var_id))
                except:
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
            for var_id in variables:
                new_value = self._connection.ReadVariable(var_id)
                if new_value is not None:
                    res.append((var_id, new_value, VariableQuality.GOOD))
                else:
                    res.append((var_id, new_value, VariableQuality.BAD))
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
            for (var_id, new_value) in variables:
                v = self._connection.WriteVariable(new_value, var_id)
                if v is None:
                    res.append((var_id, new_value, VariableQuality.GOOD))
                else:
                    res.append((var_id, new_value, VariableQuality.BAD))
        except:
            pass
        return res