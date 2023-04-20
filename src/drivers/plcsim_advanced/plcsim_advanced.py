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

# class EPrimitiveDataType(int, Enum):
#     Unspecific = 0,
#     Struct = 1,
#     Bool = 2,
#     Int8 = 3,
#     Int16 = 4,
#     Int32 = 5,
#     Int64 = 6,
#     UInt8 = 7,
#     UInt16 = 8,
#     UInt32 = 9,
#     UInt64 = 10,
#     Float = 11,
#     Double = 12,
#     Char = 13,
#     WChar = 14
# class EOperatingState(int, Enum):
#     InvalidOperatingState = 0
#     Off = 1
#     Booting = 2
#     Stop = 3
#     Startup = 4
#     Run = 5
#     Freeze = 6
#     ShuttingDown = 7

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
        from Siemens.Simatic.Simulation.Runtime import SimulationRuntimeManager, SDataValue, SDataValueByName, EOperatingState, EPrimitiveDataType
except:
    pass

class plcsim_advanced(driver):
    '''
    Driver that can be used together with a local PLCSim Advanced Instance, using the Simulation Runtime API.
    Parameters:
    instanceName : The name of the PLC Sim Advanced Instance
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
                        self._connection = SimulationRuntimeManager.CreateInterface(self.instanceName)
                        if self._connection.get_OperatingState() == EOperatingState.Run:
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
        self._connection.UpdateTagList()

        for var_id in list(variables.keys()):
            try:
                var_data = dict(variables[var_id])
                var_data['SDataValueByName'] = SDataValueByName()
                var_data['SDataValueByName'].Name = var_id
                var_data['SDataValueByName'].DataValue = self._connection.Read(var_data['SDataValueByName'].Name)
                var_data['PrimitiveDataType'] = var_data['SDataValueByName'].DataValue.Type
                var_data['value'] = None
                self.variables[var_id] = var_data
            except Exception as e:
                print(e)
                self.sendDebugVarInfo(('SETUP: Bad variable definition: {}'.format(var_id), var_id))
    

    def readVariables(self, variables: list) -> list:
        """ Read given variable values. In case that the read is not possible or generates an error BAD quality should be returned.
        : param variables: List of variable ids to be read. 
        : returns: list of tupples including (var_id, var_value, VariableQuality)
        """
        signals = []
        res = []

        try:
            for var_id in variables:
                signals.append(self.variables[var_id]['SDataValueByName'])
        
            signals = self._connection.ReadSignals(signals)
            for signal in signals:
                var_id = signal.Name
                if signal.DataValue.Type == EPrimitiveDataType.Bool:
                    value = signal.DataValue.Bool
                elif signal.DataValue.Type == EPrimitiveDataType.Int8:
                    value = signal.DataValue.Int8
                elif signal.DataValue.Type == EPrimitiveDataType.Int16:
                    value = signal.DataValue.Int16
                elif signal.DataValue.Type == EPrimitiveDataType.Int32:
                    value = signal.DataValue.Int32
                elif signal.DataValue.Type == EPrimitiveDataType.Int64:
                    value = signal.DataValue.Int64
                elif signal.DataValue.Type == EPrimitiveDataType.UInt8:
                    value = signal.DataValue.UInt8
                elif signal.DataValue.Type == EPrimitiveDataType.UInt16:
                    value = signal.DataValue.UInt16
                elif signal.DataValue.Type == EPrimitiveDataType.UInt32:
                    value = signal.DataValue.UInt32
                elif signal.DataValue.Type == EPrimitiveDataType.UInt64:
                    value = signal.DataValue.UInt64
                elif signal.DataValue.Type == EPrimitiveDataType.Float:
                    value = signal.DataValue.Float
                elif signal.DataValue.Type == EPrimitiveDataType.Double:
                    value = signal.DataValue.Double
                elif signal.DataValue.Type == EPrimitiveDataType.Char:
                    value = signal.DataValue.Char
                res.append((var_id, value, VariableQuality.GOOD))  
        except Exception as e:
            res = []
            for var_id in variables:
                res.append((var_id, None, VariableQuality.BAD))

        return res

    def writeVariables(self, variables: list) -> list:
        """ Write given variable values. In case that the write is not possible or generates an error BAD quality should be returned.
        : param variables: List of tupples with variable ids and the values to be written (var_id, var_value). 
        : returns: list of tupples including (var_id, var_value, VariableQuality)
        """
        res = []
        signals = []
        for (var_id, value) in variables:
            try:
                sdatavalue = SDataValue()
                sdatavalue.Type = self.variables[var_id]['PrimitiveDataType']
                
                if sdatavalue.Type == EPrimitiveDataType.Bool:
                    sdatavalue.Bool = value
                elif sdatavalue.Type == EPrimitiveDataType.Int8:
                    sdatavalue.Int8 = value
                elif sdatavalue.Type == EPrimitiveDataType.Int16:
                    sdatavalue.Int16 = value
                elif sdatavalue.Type == EPrimitiveDataType.Int32:
                    sdatavalue.Int32 = value
                elif sdatavalue.Type == EPrimitiveDataType.Int64:
                    sdatavalue.Int64 = value
                elif sdatavalue.Type == EPrimitiveDataType.UInt8:
                    sdatavalue.UInt8 = value    
                elif sdatavalue.Type == EPrimitiveDataType.UInt16:
                    sdatavalue.UInt16 = value
                elif sdatavalue.Type == EPrimitiveDataType.UInt32:
                    sdatavalue.UInt32 = value
                elif sdatavalue.Type == EPrimitiveDataType.UInt64:
                    sdatavalue.UInt64 = value
                elif sdatavalue.Type == EPrimitiveDataType.Float:
                    sdatavalue.Float = value  
                elif sdatavalue.Type == EPrimitiveDataType.Double:
                    sdatavalue.Double = value    
                elif sdatavalue.Type== EPrimitiveDataType.Char:
                    sdatavalue.Char = value


                self.variables[var_id]['SDataValueByName'].DataValue = sdatavalue
                signals.append(self.variables[var_id]['SDataValueByName'])
                        
            except Exception as e:
                res.append((var_id, None, VariableQuality.BAD))
            else:
                res.append((var_id, value, VariableQuality.GOOD))  

        try:
            self._connection.WriteSignals(signals)
        except Exception as e:
            res = []
            for var_id in variables:
                res.append((var_id, None, VariableQuality.BAD))
                
        return res
