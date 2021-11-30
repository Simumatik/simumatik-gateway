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
import pythoncom, win32com.client

from ..driver import driver, VariableQuality, VariableOperation, VariableDatatype

# CONSTANTS
frJointDisplayType = 0
frJoint = 9
frDInType  = 1
frDOutType = 2
frAInType = 3
frAOutType = 4
frPLCInType = 6
frPLCOutType = 7
frRDInType = 8
frRDOutType = 9
frGPInType = 18
frGPOutType = 19

class fanuc_roboguide(driver):
    '''
    Driver that can be used to connect with Roboguide. 
    It makes use of the FANUC Robotics Controller Interface COM object. Requires the pywin32 library.
    
    Parameters:
    ip: str
        This parameter is used to define where the Roboguide instance is running. Default = "127.0.0.1"
    '''

    def __init__(self, name: str, pipe: Optional[Pipe] = None):
        """
        :param name: (optional) Name for the driver
        :param pipe: (optional) Pipe used to communicate with the driver thread. See gateway.py
        """
        # Inherit
        driver.__init__(self, name, pipe)

        # Parameters
        self.ip = '127.0.0.1'
        self.joint_group = None
        self.joint_positions = None


    def connect(self) -> bool:
        """ Connect driver.
        
        : returns: True if connection stablished False if not
        """
        try:
            pythoncom.CoInitialize()
            self._connection = win32com.client.Dispatch("FRRobot.FRCRobot")
        except Exception as e:
            self.sendDebugInfo(f"RoboGuide COM Interface not found! {e}")
            return False

        # Connect
        try:
            self._connection.ConnectEx(HostName=self.ip, NoWait=False, NumRetries=1, Period=1)
            assert self._connection.IsConnected, f"Connection failed! Client not found at: {self.ip}"
        except Exception as e:
            self.sendDebugInfo(e)
            return False
        self.sendDebugInfo(f"Connected to Host: {self._connection.HostName}")

        try:
            # Add pointers
            mobjCurPos = self._connection.CurPosition
            assert mobjCurPos.NumGroups>0, f"Connection failed! Axis group not found"
            self.joint_group = mobjCurPos.Group(1, frJointDisplayType)
            self.joint_positions = self.joint_group.Formats(frJoint)
        except Exception as e:
            self.sendDebugInfo(e)
            return False

        return True


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
                    if var_id[:2]=="DI" and var_data['datatype']==VariableDatatype.BOOL and var_data['operation']==VariableOperation.WRITE:
                        var_data['area'] = frDInType
                    elif var_id[:2]=="DO" and var_data['datatype']==VariableDatatype.BOOL and var_data['operation']==VariableOperation.READ:
                        var_data['area'] = frDOutType
                    elif var_id[:2]=="RI" and var_data['datatype']==VariableDatatype.BOOL and var_data['operation']==VariableOperation.WRITE:
                        var_data['area'] = frRDInType
                    elif var_id[:2]=="RO" and var_data['datatype']==VariableDatatype.BOOL and var_data['operation']==VariableOperation.READ:
                        var_data['area'] = frRDOutType
                    elif var_id[:2]=="GI" and var_data['datatype'] in [VariableDatatype.BYTE,VariableDatatype.WORD] and var_data['operation']==VariableOperation.WRITE:
                        var_data['area'] = frGPInType
                    elif var_id[:2]=="GO" and var_data['datatype'] in [VariableDatatype.BYTE,VariableDatatype.WORD] and var_data['operation']==VariableOperation.READ:
                        var_data['area'] = frGPOutType
                    elif var_id[:2]=="AI" and var_data['datatype']==VariableDatatype.WORD and var_data['operation']==VariableOperation.WRITE:
                        var_data['area'] = frAInType
                    elif var_id[:2]=="AO" and var_data['datatype']==VariableDatatype.WORD and var_data['operation']==VariableOperation.READ:
                        var_data['area'] = frAOutType
                    else:
                        self.sendDebugVarInfo((f'SETUP: Variable definition is wrong: {var_id}', var_id))
                        continue
                    try:
                        var_data['port'] = int(var_id[2:])
                        assert var_data['port']>0, "Variable port number is wrong"
                    except:
                        self.sendDebugVarInfo((f'SETUP: Variable port number is wrong: {var_id}', var_id))
                        continue
                    # Prepare input signals to be written (simulated)
                    if var_data['operation']==VariableOperation.WRITE:
                        self._connection.IOTypes(var_data['area']).Signals(var_data['port']).Simulate = True
                    var_data['value'] = None # Force first update
                    self.variables[var_id] = var_data
                    self.sendDebugVarInfo((f'SETUP: Variable found {var_id}', var_id))
                    continue
            except Exception as e:
                self.sendDebugVarInfo((f'SETUP: Error setting up variable: {var_id}, {e}', var_id))
                pass
            
            self.sendDebugVarInfo((f'SETUP: Variable not found {var_id}', var_id))
        pass


    def readVariables(self, variables: list) -> list:
        """ Read given variable values. In case that the read is not possible or generates an error BAD quality should be returned.
        : param variables: List of variable ids to be read. 
        : returns: list of tupples including (var_id, var_value, VariableQuality)
        """
        res = []
        for var_id in variables:
            try:
                if var_id == 'Axis':
                    self.joint_group.Refresh()
                    new_value = []
                    for i in range(self.variables[var_id]['size']):
                        val = self.joint_positions.Item(i+1)
                        new_value.append(round(val,3))
                    res.append((var_id, new_value, VariableQuality.GOOD))

                else:
                    new_value = self._connection.IOTypes(self.variables[var_id]['area']).Signals(self.variables[var_id]['port']).Value
                    res.append((var_id, new_value, VariableQuality.GOOD))
            except Exception as e:
                res.append((var_id, self.variables[var_id]['value'], VariableQuality.BAD))
            
        return res


    def writeVariables(self, variables: list) -> list:
        """ Write given variable values. In case that the write is not possible or generates an error BAD quality should be returned.
        : param variables: List of tupples with variable ids and the values to be written (var_id, var_value). 
        : returns: list of tupples including (var_id, var_value, VariableQuality)
        """
        res = []
        for (var_id, new_value) in variables:
            try:
                self._connection.IOTypes(self.variables[var_id]['area']).Signals(self.variables[var_id]['port']).Value = new_value
                res.append((var_id, new_value, VariableQuality.GOOD))
            except:
                res.append((var_id, new_value, VariableQuality.BAD))
                     
        return res
