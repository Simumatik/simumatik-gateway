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

import sys 
import os
import clr
from enum import Enum

from multiprocessing import Pipe
from typing import Optional

from ..driver import driver, VariableQuality

class EPrimitiveDataType(int, Enum):
    Unspecific = 0,
    Struct = 1,
    Bool = 2,
    Int8 = 3,
    Int16 = 4,
    Int32 = 5,
    Int64 = 6,
    UInt8 = 7,
    UInt16 = 8,
    UInt32 = 9,
    UInt64 = 10,
    Float = 11,
    Double = 12,
    Char = 13,
    WChar = 14
class EOperatingState(int, Enum):
    InvalidOperatingState = 0
    Off = 1
    Booting = 2
    Stop = 3
    Startup = 4
    Run = 5
    Freeze = 6
    ShuttingDown = 7

try:
    if os.name == 'nt':# Just try on windows
        import clr
        p = os.path.dirname(os.path.abspath(__file__))
        sys.path.append(p)
        if sys.maxsize > 2**32: # 64-Bit OS
            clr.FindAssembly("Siemens.Simatic.Simulation.Runtime.Api.x64")
            clr.AddReference("Siemens.Simatic.Simulation.Runtime.Api.x64")
        else: # 32-Bit OS
            clr.FindAssembly("Siemens.Simatic.Simulation.Runtime.Api.x86")
            clr.AddReference("Siemens.Simatic.Simulation.Runtime.Api.x86")
        from Siemens.Simatic.Simulation.Runtime import SimulationRuntimeManager
except:
    pass

class plcsim_advanced(driver):
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
        self.instanceName = "s7-1500"


    def connect(self) -> bool:
        """ Connect driver.
        
        : returns: True if connection established False if not
        """
        # Make sure to send a debug message if method returns False
        # self.sendDebugInfo('Error message here') 
        try:
            if SimulationRuntimeManager.RegisteredInstanceInfo.Length > 0:
                for instance in SimulationRuntimeManager.RegisteredInstanceInfo:
                    if instance.Name == self.instanceName:
                        self.connection = SimulationRuntimeManager.CreateInterface(self.instanceName)
                        if self.connection.OperatingState == EOperatingState.Run:
                            return True
                        self.sendDebugInfo("PLC Sim Advanced operating state is not in 'Run'")
                self.sendDebugInfo(f"No PLC Sim Advanced instance with name {self.instanceName} found")
            else: 
                self.sendDebugInfo("No PLC Sim Advanced instance running")
        except Exception as e:
            self.sendDebugInfo(f"Connection failed, {e}")
            
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
        self.connection.UpdateTagList()
        data = self.connection.TagInfos
        print(data.Length)

        for var_id in list(variables.keys()):
            var_data = dict(variables[var_id])
            for tag in self.connection.TagInfos:
                if var_id == tag.ToString():
                    print(f"{tag.ToString()} {tag.PrimitiveDataType}")
                    var_data['PrimitiveDataType'] = tag.PrimitiveDataType
                    var_data['value'] = None
                    self.variables[var_id] = var_data
                    break

            if not "PrimitiveDataType" in var_data:
                self.sendDebugVarInfo(('SETUP: Bad variable definition: {}'.format(var_id), var_id))
                print('SETUP: Bad variable definition: {}'.format(var_id))
    

    def readVariables(self, variables: list) -> list:
        """ Read given variable values. In case that the read is not possible or generates an error BAD quality should be returned.
        : param variables: List of variable ids to be read. 
        : returns: list of tupples including (var_id, var_value, VariableQuality)
        """
        res = []

        for var_id in variables:
            try:
                data_type = self.variables[var_id]['PrimitiveDataType'] 
                if data_type == EPrimitiveDataType.Bool:
                    value = self.connection.ReadBool(var_id)
                elif data_type == EPrimitiveDataType.Int8:
                    value = self.connection.ReadInt8(var_id)
                elif data_type == EPrimitiveDataType.Int16:
                    value = self.connection.ReadInt16(var_id)
                elif data_type == EPrimitiveDataType.Int32:
                    value = self.connection.ReadInt32(var_id)
                elif data_type == EPrimitiveDataType.Int64:
                    value = self.connection.ReadInt64(var_id)    
                elif data_type == EPrimitiveDataType.UInt8:
                    value = self.connection.ReadUInt8(var_id)
                elif data_type == EPrimitiveDataType.UInt16:
                    value = self.connection.ReadUInt16(var_id)
                elif data_type == EPrimitiveDataType.UInt32:
                    value = self.connection.ReadUInt32(var_id)
                elif data_type == EPrimitiveDataType.UInt64:
                    value = self.connection.ReadUInt64(var_id)
                elif data_type == EPrimitiveDataType.Float:
                    value = self.connection.ReadFloat(var_id)
                elif data_type == EPrimitiveDataType.Double:
                    value = self.connection.ReadDouble(var_id)
                elif data_type == EPrimitiveDataType.Char:
                    value = self.connection.ReadChar(var_id)
            except Exception as e:
                res.append((var_id, None, VariableQuality.BAD))
            else:
                res.append((var_id, value, VariableQuality.GOOD))    

        return res


    def writeVariables(self, variables: list) -> list:
        """ Write given variable values. In case that the write is not possible or generates an error BAD quality should be returned.
        : param variables: List of tupples with variable ids and the values to be written (var_id, var_value). 
        : returns: list of tupples including (var_id, var_value, VariableQuality)
        """
        res = []

        for (var_id, value) in variables:
            try:
                data_type = self.variables[var_id]['PrimitiveDataType']
                if data_type == EPrimitiveDataType.Bool:
                    self.connection.WriteBool(var_id, value)
                elif data_type == EPrimitiveDataType.Int8:
                    self.connection.WriteInt8(var_id, value)
                elif data_type == EPrimitiveDataType.Int16:
                    self.connection.WriteInt16(var_id, value)
                elif data_type == EPrimitiveDataType.Int32:
                    self.connection.WriteInt32(var_id, value)
                elif data_type == EPrimitiveDataType.Int64:
                    self.connection.WriteInt64(var_id, value)
                elif data_type == EPrimitiveDataType.UInt8:
                    self.connection.WriteUInt8(var_id, value)    
                elif data_type == EPrimitiveDataType.UInt16:
                    self.connection.WriteUInt16(var_id, value)
                elif data_type == EPrimitiveDataType.UInt32:
                    self.connection.WriteUInt32(var_id, value)
                elif data_type == EPrimitiveDataType.UInt64:
                    self.connection.WriteUInt64(var_id, value)
                elif data_type == EPrimitiveDataType.Float:
                    self.connection.WriteFloat(var_id, value)  
                elif data_type == EPrimitiveDataType.Double:
                    self.connection.WriteDouble(var_id, value)    
                elif data_type== EPrimitiveDataType.Char:
                    self.connection.WriteChar(var_id, value) 
            except:
                res.append((var_id, None, VariableQuality.BAD))
            else:
                res.append((var_id, value, VariableQuality.GOOD))    

        return res
