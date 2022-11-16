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
import os
import sys

from ..driver import driver, VariableQuality, VariableOperation, VariableDatatype

ROBOT_INTERFACE_FOUND = False
try:
    if os.name == 'nt':# Just try on windows
        import clr
        p = os.path.dirname(os.path.abspath(__file__))
        sys.path.append(p)
        clr.FindAssembly("RobotInterfaceDotNet")
        clr.AddReference("RobotInterfaceDotNet")
        from System import Array, Int16, Int32, Double
        from FRRJIf import Core, FRIF_DATA_TYPE

        ROBOT_INTERFACE_FOUND = True
except:
    pass

class fanuc_roboguide(driver):
    '''
    Driver that can be used to connect with Roboguide. 
    It makes use of the FANUC Robot Interface. Requires the clr library and RobotInterfaceDotNet.dll.

    Parameters:
    hostname: str
        This parameter is used to define where the Roboguide instance is running. Default = "127.0.0.1"
    
    motion_group: int
        This parameter is used to select the motion group nuimber
    '''

    def __init__(self, name: str, pipe: Optional[Pipe] = None, params:dict = None):
        """
        :param name: (optional) Name for the driver
        :param pipe: (optional) Pipe used to communicate with the driver thread. See gateway.py
        """
        # Inherit
        driver.__init__(self, name, pipe, params)

        # Parameters
        self.hostname = '127.0.0.1'
        self.motion_group = 1
        self.port = None


    def connect(self) -> bool:
        """ Connect driver.
        
        : returns: True if connection established False if not
        """
        try:
            self._connection = Core()
            if self.port:
                self._connection.PortNumber = self.port
            self._datatable = self._connection.get_DataTable()
            self._curpos = self._datatable.AddCurPosUF(FRIF_DATA_TYPE.CURPOS, self.motion_group, 1)
            if self._curpos.Valid:
                if self._connection.Connect(self.hostname):
                    return True
                else:
                    self.sendDebugInfo(f"Error connecting to host.")
            else:
                self.sendDebugInfo(f"Error getting current position")
        except Exception as e:
            self.sendDebugInfo(f"Robot Interface initialization error.")
        
        return False


    def disconnect(self):
        """ Disconnect driver.
        """
        self._connection.Disconnect()


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
                        var_data['area'] = "DI"
                    elif var_id[:2]=="DO" and var_data['datatype']==VariableDatatype.BOOL and var_data['operation']==VariableOperation.READ:
                        var_data['area'] = "DO"
                    elif var_id[:2]=="GI" and var_data['datatype'] in [VariableDatatype.BYTE,VariableDatatype.WORD,VariableDatatype.DWORD] and var_data['operation']==VariableOperation.WRITE:
                        var_data['area'] = "GI"
                    elif var_id[:2]=="GO" and var_data['datatype'] in [VariableDatatype.BYTE,VariableDatatype.WORD,VariableDatatype.DWORD] and var_data['operation']==VariableOperation.READ:
                        var_data['area'] = "GO"
                    else:
                        self.sendDebugVarInfo((f'SETUP: Variable definition is wrong: {var_id}', var_id))
                        continue
                    try:
                        var_data['port'] = int(var_id[2:])
                        assert var_data['port']>0, "Variable port number is wrong"
                    except:
                        self.sendDebugVarInfo((f'SETUP: Variable port number is wrong: {var_id}', var_id))
                        continue
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
        self._datatable.Refresh()
        for var_id in variables:
            size = self.variables[var_id]['size']
            if var_id == 'Axis':
                joints = self.createBuffer(Double, 9)
                quality = self._curpos.GetValue(
                    Array.CreateInstance(Double, 9), 
                    Array.CreateInstance(Double, 7), 
                    joints, 
                    Int16(0), Int16(0), Int16(0), Int16(0)
                    )
                if quality[0]==True:
                    new_value = []
                    for i in range(size):
                        new_value.append(round(joints[i], 3))
                    res.append((var_id, new_value, VariableQuality.GOOD))
                else:
                    res.append((var_id, self.variables[var_id]['value'], VariableQuality.BAD))

            else:
                port = self.variables[var_id]['port']
                if self.variables[var_id]['area'] == "DO":
                    buff = self.createBuffer(Int16, size)
                    (quality, read_value) = self._connection.ReadSDO(port, buff, size)
                elif self.variables[var_id]['area'] == "GO":
                    buff = self.createBuffer(Int32, size)
                    (quality, read_value) = self._connection.ReadGO(port, buff, size)
                if quality is True:
                    new_value = self.readBuffer(read_value)
                    res.append((var_id, new_value, VariableQuality.GOOD))
                else:
                    res.append((var_id, self.variables[var_id]['value'], VariableQuality.BAD))
            
        return res


    def writeVariables(self, variables: list) -> list:
        """ Write given variable values. In case that the write is not possible or generates an error BAD quality should be returned.
        : param variables: List of tupples with variable ids and the values to be written (var_id, var_value). 
        : returns: list of tupples including (var_id, var_value, VariableQuality)
        """
        res = []
        for (var_id, new_value) in variables:
            size = self.variables[var_id]['size']
            port = self.variables[var_id]['port']
            if self.variables[var_id]['area'] == "DI":
                buff = self.createBuffer(Int16, size)
                self.writeBuffer(buff, new_value)
                quality = self._connection.WriteSDI(port, buff, size)
            else:
                buff = self.createBuffer(Int32, size)
                self.writeBuffer(buff, new_value)
                quality = self._connection.WriteGI(port, buff, size)
            if quality == True:
                res.append((var_id, new_value, VariableQuality.GOOD))
            else:
                res.append((var_id, new_value, VariableQuality.BAD))
                     
        return res
    

    def createBuffer(self, datatype, size):
        return Array.CreateInstance(datatype, size)
    

    def writeBuffer(self, buffer, data):
        if isinstance(data, list):
            for i in range(len(data)):
                buffer[i] = data[i]
        else:
            buffer[0] = data
    

    def readBuffer(self, buffer):
        if buffer.Length>1:
            return [buffer[i] for i in range(buffer.Length)]
        elif buffer.Length==1:
            return buffer[0]
        else:
            return 0
                

