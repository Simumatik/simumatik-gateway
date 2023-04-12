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

import sys
import os
import winreg

# Import SDK
ABB_SDK_FOUND = False

try:
    if os.name == 'nt':# Just try on windows
        reg = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
        main_key = winreg.OpenKey(reg, r"SOFTWARE\WOW6432Node\ABB\Robotics IT\Applications")
        
        i = 0
        while True:
            result = winreg.EnumKey(main_key, i)
            i += 1

            if "RobotStudio" in result:
                key = winreg.OpenKey(main_key, result)
                robotstudio_path = winreg.QueryValueEx(key, "InstallDir")[0] + "Bin"
                sys.path.append(robotstudio_path) # Add path to system path

                import clr
                clr.FindAssembly("ABB.Robotics.Controllers.PC")
                clr.AddReference("ABB.Robotics.Controllers.PC")
                from ABB.Robotics.Controllers.Discovery import NetworkScanner
                from ABB.Robotics.Controllers import ControllerFactory, UserInfo, IOSystemDomain

                ABB_SDK_FOUND = True
                break
except:
    pass

SIGNAL_ANALOGINPUT = 0
SIGNAL_ANALOGOUTPUT = 1
SIGNAL_DIGITALINPUT = 2
SIGNAL_DIGITALOUTPUT = 3
SIGNAL_GROUPINPUT = 4
SIGNAL_GROUPOUTPUT = 5
SIGNAL_UNKNOWN = 6

# Driver that connects to robotware
class robotware(driver):
    '''
    This driver uses the RobotWare API to connect to a robot controller.
    
    The driver will always provide access to the robot axis through the variable called "Axis" (float[6]).
    Optional variable definitions are used to access Input and Output signals to be read or written by the driver.

    controller: str
        Robot name in RobotWare. Default = '', will take the first that founds.
    '''

    def __init__(self, name: str, pipe: Optional[Pipe] = None, params:dict = None):
        """
        :param name: (optional) Name for the driver
        :param pipe: (optional) Pipe used to communicate with the driver thread. See gateway.py
        """
        # Inherit
        driver.__init__(self, name, pipe, params)

        # Parameters
        self.controller = ''


    def connect(self) -> bool:
        """ Connect driver.
        
        : returns: True if connection established False if not
        """
        try:
            if not ABB_SDK_FOUND:
                raise Exception('ABB RobotWare SDK not found')

            # Scan network
            scanner = NetworkScanner()
            if scanner:
                scanner.Scan()

                # Get controllers
                controllers = scanner.GetControllers()

                for controller in controllers:
                    # Check if there is a controller with same name or take the first one
                    if (str(controller.SystemName) == self.controller) or (self.controller == ""):
                        # Save name if not defined
                        if self.controller == '': self.controller = str(controller.SystemName)
                        
                        # Create controller
                        self._connection = ControllerFactory.CreateFrom(controller)
                        
                        # Logon and connect
                        if self._connection:
                            # Log on
                            self._connection.Logon(UserInfo.DefaultUser)
                            # Done
                            return True
                        else:
                            self.sendDebugInfo(f'Cannot connect to -> {self.controller}.')
                else:
                    # Controller not found
                    self.sendDebugInfo(f'Controller not found {self.controller}.')

        except Exception as e:
            self.sendDebugInfo('Exception '+str(e))

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
        # Check variable elements
        for var_id, var_data in variables.items():
            try:
                if var_id == 'Axis':
                    var_data['value'] = [None for i in range(var_data['size'])]
                    self.variables[var_id] = var_data
                    continue
                else:
                    signal = self._connection.IOSystem.GetSignal(var_id)
                    if signal:
                        value = self.get_signal_value(signal, var_data['datatype'])
                        if value is not None:
                            var_data['signal'] = signal
                            var_data['value'] = None # Force first update
                            self.variables[var_id] = var_data
                            self.sendDebugVarInfo((f'SETUP: Variable found {var_id}', var_id))
                    continue
            except:
                pass

            self.sendDebugVarInfo((f'SETUP: Variable not found {var_id}', var_id))


    def readVariables(self, variables: list) -> list:
        """ Read given variable values. In case that the read is not possible or generates an error BAD quality should be returned.
        : param variables: List of variable ids to be read. 

        : returns: list of tupples including (var_id, var_value, VariableQuality)
        """
        res = []
        for var_id in variables:
            try:
                if var_id == 'Axis':
                    mecunit = self._connection.MotionSystem.ActiveMechanicalUnit
                    # robot axis rotations [Rax_1, Rax_2, Rax_3, Rax_4, Rax_5, Rax_6]
                    pos = mecunit.GetPosition()
                    new_value = [pos.RobAx.Rax_1, pos.RobAx.Rax_2, pos.RobAx.Rax_3, pos.RobAx.Rax_4, pos.RobAx.Rax_5, pos.RobAx.Rax_6]
                    # Round
                    new_value = [round(x,3) for x in new_value]
                    res.append((var_id, new_value, VariableQuality.GOOD))
                else:
                    new_value = self.get_signal_value(self.variables[var_id]['signal'], self.variables[var_id]['datatype'])
                    if new_value is not None:
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
            try:
                self.set_signal_value(self.variables[var_id]['signal'], new_value, self.variables[var_id]['datatype'])
                res.append((var_id, new_value, VariableQuality.GOOD))
            except:
                res.append((var_id, new_value, VariableQuality.BAD))
                     
        return res

    # Helper methods

    def get_signal_value(self, signal, datatype):
        # Return value
        if signal:
            if signal.Type in [
                SIGNAL_DIGITALOUTPUT, SIGNAL_DIGITALINPUT, # Older RobotStudio
                IOSystemDomain.SignalType.DigitalInput, IOSystemDomain.SignalType.DigitalOutput # From RobotStudio 2022
                ]:
                return bool(signal.Value)
            elif signal.Type in [
                SIGNAL_ANALOGINPUT, SIGNAL_ANALOGOUTPUT, 
                IOSystemDomain.SignalType.AnalogInput, IOSystemDomain.SignalType.AnalogOutput
                ]:
                return signal.Value
            elif signal.Type in [
                SIGNAL_GROUPOUTPUT, SIGNAL_GROUPINPUT, 
                IOSystemDomain.SignalType.GroupInput, IOSystemDomain.SignalType.GroupOutput
                ]:
                return signal.GroupValue
        return None

    def set_signal_value(self, signal, new_value, datatype):
        # Return value
        if signal:
            if signal.Type in [
                SIGNAL_DIGITALINPUT, SIGNAL_DIGITALOUTPUT, SIGNAL_ANALOGINPUT, SIGNAL_ANALOGOUTPUT, # Older RobotStudio
                IOSystemDomain.SignalType.DigitalInput, IOSystemDomain.SignalType.DigitalOutput, # From RobotStudio 2022
                IOSystemDomain.SignalType.AnalogInput, IOSystemDomain.SignalType.AnalogOutput
                ]:
                signal.Value = new_value
                return True
            elif signal.Type in [
                SIGNAL_GROUPOUTPUT, SIGNAL_GROUPINPUT, 
                IOSystemDomain.SignalType.GroupInput, IOSystemDomain.SignalType.GroupOutput
                ]:
                signal.WriteGroupValue(new_value)
                return True
        return False
