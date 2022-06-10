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

from ..driver import driver, VariableQuality, VariableDatatype, VariableOperation

from multiprocessing import Pipe
from typing import Optional

from pyModbusTCP.client import ModbusClient
    

class modbustcp_master(driver):
    '''
    Driver that creates a Modbus TCP master (client) to communicate with ModBus TCP slaves (servers).
    The Modbus protocol exchanges information using a request-reply mechanism between a master (client) and a slave (server). 
    The master-slave principle is a model for a communication protocol in which one device (the master) controls one or more other devices (the slaves). 

    Uses the library pyModbusTCP.

    | Register Numbers  | Type          | Function Code | Name                                  | Data Type | Example Value |
    |-------------------|---------------|---------------|---------------------------------------|-----------|---------------|
    | 1-9999            | Read-Write	| 1	            | Status/Coil (State controls)	        | bool      | 0 or 1        |
    | 10001-19999       | Read-Only	    | 2	            | Input Contact (State information)	    | bool      | 0 or 1        |
    | 30001-39999       | Read-Only	    | 4	            | Input Registers (Numerical values)    | int, word | 0 to 32767    |
    | 40001-49999       | Read-Write	| 3	            | Holding Registers (Numerical values)  | int, word | 0 to 32767    |

    Parameters:
    host            : String    : the slave ip address, default 127.0.0.1
    port            : Int       : the slave port to connect to, default 502
    '''

    def __init__(self, name: str, pipe: Optional[Pipe] = None):
        """
        :param name: (optional) Name for the driver
        :param pipe: (optional) Pipe used to communicate with the driver thread. See gateway.py
        """
        # Inherit
        driver.__init__(self, name, pipe)
        
        self.host = '127.0.0.1'
        self.port = 502


    def connect(self) -> bool:
        """ Connect driver.
        
        : returns: True if connection established False if not
        """
        # Create connection
        try:
            self._connection = ModbusClient(host=self.host, auto_open=True, auto_close=False)
        except Exception as e:
            self.sendDebugInfo(f"Connection with {self.host} cannot be established.")
            return False

        return True

    def disconnect(self):
        """ Disconnect driver.
        """
        if self._connection:
            self._connection.close()


    def addVariables(self, variables: dict):
        """ Add variables to the driver. Correctly added variables will be added to internal dictionary 'variables'.
        Any error adding a variable should be communicated to the server using sendDebugInfo() method.
        : param variables: Variables to add in a dict following the setup format. (See documentation) 
        """
        for var_id in list(variables.keys()):
            var_data = dict(variables[var_id])
            try:
                reg_number = int(var_id)
                # Status/Coil
                if 0<reg_number<10000:
                    assert var_data['datatype'] == VariableDatatype.BOOL, f'Datatype must be boolean.' 
                    if var_data['operation']==VariableOperation.WRITE:
                        assert self._connection.write_single_coil(reg_number, False), f'Error accessing coil.'
                        var_data['value'] = False
                    elif var_data['operation']==VariableOperation.READ:
                        res = self._connection.read_coils(reg_number)
                        assert res is not None, f'Error accessing coil.'
                        var_data['value'] = res[0]
                    
                # Input Contact
                elif 10000<reg_number<20000:
                    assert var_data['datatype'] == VariableDatatype.BOOL, f'Datatype must be boolean.'
                    assert var_data['operation'] == VariableOperation.READ, f'Only read operations allowed with Input Contacts.'
                    res = self._connection.read_discrete_inputs(reg_number-10000)
                    assert res is not None, f'Error accessing Input Contact.'
                    var_data['value'] = res[0]

                # Input Registers
                elif 30000<reg_number<40000:
                    assert var_data['datatype'] in [VariableDatatype.WORD, VariableDatatype.INTEGER], f'Datatype must be word or integer.'
                    assert var_data['operation'] == VariableOperation.READ, f'Only read operations allowed with Input Register.'
                    res = self._connection.read_input_registers(reg_number-30000)
                    assert res is not None, f'Error accessing Input Register.'
                    var_data['value'] = res[0]
                    
                # Holding Registers
                elif 40000<reg_number<50000:
                    assert var_data['datatype'] in [VariableDatatype.WORD, VariableDatatype.INTEGER], f'Datatype must be word or integer.' 
                    if var_data['operation']==VariableOperation.WRITE:
                        assert self._connection.write_single_register(reg_number-40000, 0), f'Error accessing Holding Registers.'
                        var_data['value'] = 0
                    elif var_data['operation']==VariableOperation.READ:
                        res = self._connection.read_holding_registers(reg_number-40000)
                        assert res is not None, f'Error accessing coil.'
                        var_data['value'] = res[0]

                self.variables[var_id] = var_data 
            except Exception as e:
                self.sendDebugVarInfo((f'SETUP: Bad variable definition: {e}', var_id))
                
                
    def readVariables(self, variables: list) -> list:
        """ Read given variable values. In case that the read is not possible or generates an error BAD quality should be returned.
        : param variables: List of variable ids to be read. 
        : returns: list of tupples including (var_id, var_value, VariableQuality)
        """
        res = []
        for var_id in variables:
            reg_number = int(var_id)
            value = None
            if 0<reg_number<10000:
                value = self._connection.read_coils(reg_number-1)
            elif 10000<reg_number<20000:
                value = self._connection.read_discrete_inputs(reg_number-10001)
            elif 30000<reg_number<40000:
                value = self._connection.read_input_registers(reg_number-30001)
            elif 40000<reg_number<50000:
                value = self._connection.read_holding_registers(reg_number-40001)
            if value is not None:
                res.append((var_id, value[0], VariableQuality.GOOD))
            else:
                res.append((var_id, None, VariableQuality.BAD))

        return res


    def writeVariables(self, variables: list) -> list:
        """ Write given variable values. In case that the write is not possible or generates an error BAD quality should be returned.
        : param variables: List of tupples with variable ids and the values to be written (var_id, var_value). 
        : returns: list of tupples including (var_id, var_value, VariableQuality)
        """
        res = []

        for (var_id, new_value) in variables:
            reg_number = int(var_id)
            success = False
            if 0<reg_number<10000:
                success = self._connection.write_single_coil(reg_number-1, new_value)
            elif 40000<reg_number<50000:
                success = self._connection.write_single_register(reg_number-40001, new_value)
            if success:
                res.append((var_id, new_value, VariableQuality.GOOD))
            else:
                res.append((var_id, new_value, VariableQuality.BAD))

        return res