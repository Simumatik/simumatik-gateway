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

import multiprocessing
import time
import enum

class DriverStatus(str, enum.Enum):
    STANDBY = 'STANDBY'
    RUNNING = 'RUNNING'
    ERROR = 'ERROR'
    EXIT = 'EXIT'

class DriverActions(str, enum.Enum):
    ADD_VARIABLES = 'ADD_VARIABLES'
    UPDATE = 'UPDATE'
    STATUS = 'STATUS'
    INFO = 'INFO'
    VAR_INFO = 'VAR_INFO'
    RESET = 'RESET'
    EXIT = 'EXIT'

class VariableQuality(str, enum.Enum):
    GOOD = 'GOOD'
    BAD = 'BAD'
    ERROR = 'ERROR'

class VariableDatatype(str, enum.Enum):
    BOOL = 'bool'
    BYTE = 'byte'
    INTEGER = 'int'
    WORD = 'word'
    DWORD = 'dword'
    QWORD = 'qword'
    FLOAT = 'float'
    STRING = 'str'

class VariableOperation(str, enum.Enum):
    READ = 'read'
    WRITE = 'write'
    BOTH = 'both'

class driver():
    """

    Parameters:

    rpi: int
        Requested Packet Interval (in ms), how often variables are read and write. Default = 50
        Set rpi to 0 to continuously read and write variables
    
    force_write: float
        Used to periodically (in sec) re-write variables. Default = 1
    
    auto_reset: float
        Used to define the time (in sec) to try reset the driver when the state is ERROR. Default = 5.0
    
    """

    def __init__(self, name: str, pipe: multiprocessing.Pipe = None, params:dict = None):
        """
        :param name: (optional) Name for the driver
        :param pipe: (optional) Pipe used to communicate with the driver thread. See gateway.py
        """
        # Standard parameters
        self.rpi = 50
        self.force_write = 1 
        self.auto_reset = 5.0

        # Initialize
        self.name = name
        self.pipe = pipe
        self.params = params
        self.handles = []
        self._connection = None
        self.last_read = time.perf_counter() # last read package sent
        self.last_write = time.perf_counter() # last write package sent
        self.last_forced_write = time.perf_counter() # last read package sent
        self.last_status_change = time.perf_counter() # last status changed timestamp
        
        # Driver internal data
        self.variables = {} # Dictionary to store variable data (definition and additional data specific to each driver)
        self.raw_variables_def = {} # Dictionary to store raw variable definition data, used to reset the driver
        self.pending_updates = {} # Pending variable updates to write on the driver {var_name: var_value}

        if self.pipe is None: 
            self.changeStatus(DriverStatus.EXIT)
        else:
            self.changeStatus(DriverStatus.STANDBY)
    

    def run(self):
        """ Run loop."""
        if self._setup(self.params):
            self.changeStatus(DriverStatus.RUNNING)
        else:
            self.changeStatus(DriverStatus.ERROR)

        while self.status != DriverStatus.EXIT:

            try:
                while self.pipe.poll():
                    (action, data) = self.pipe.recv()
                    
                    try:
                        # Action EXIT
                        if action == DriverActions.EXIT:
                            self._cleanup()
                            self.changeStatus(DriverStatus.EXIT)

                        # Action RESET
                        elif action == DriverActions.RESET:
                            if self.status == DriverStatus.ERROR: 
                                if self._cleanup():
                                    self.changeStatus(DriverStatus.STANDBY)
                                else:
                                    self.sendDebugInfo('RESET action failed! Cleanup not completed.')
                            else:
                                self.sendDebugInfo('RESET action failed! Actual status is not ERROR.')

                        # Action ADD VARIABLES
                        elif action == DriverActions.ADD_VARIABLES:
                            self.raw_variables_def.update(data)
                            if self.status == DriverStatus.RUNNING: 
                                if not self._addVariables(data):
                                    self.sendDebugInfo('ADD_VARIABLES action failed!')

                        # Action UPDATE
                        elif action == DriverActions.UPDATE:
                            if self.status == DriverStatus.RUNNING: 
                                if isinstance(data, dict):
                                    for var_name, var_value in data.items():
                                        if var_name in self.variables:
                                            if self.variables[var_name]['operation'] in [VariableOperation.WRITE, VariableOperation.BOTH]:
                                                self.pending_updates.update({var_name:var_value})
                                            else:
                                                self.sendDebugVarInfo(('UPDATE action failed! Variable defined operation is not write: ' + var_name, var_name))
                                        else:
                                            self.sendDebugVarInfo(('UPDATE action failed! Variable not defined: ' + var_name, var_name))
                                else:
                                    self.sendDebugVarInfo(('UPDATE action failed! Data format is wrong: ' + var_name, var_name))
                            else:
                                self.sendDebugInfo('UPDATE action failed! Actual status is not RUNNING.')

                    except Exception as e:
                        self.changeStatus(DriverStatus.ERROR)
                        self.sendDebugInfo('Exception executing action: ' + str(e))
                
            except Exception as e:
                self.sendDebugInfo('Exception parsing pipe message: '+str(e))

            # Driver running
            if self.status == DriverStatus.RUNNING:
                if not self._transmitVariables():
                    self.changeStatus(DriverStatus.ERROR)

            # Auto reset
            elif self.status == DriverStatus.ERROR and self.auto_reset>0:
                if time.perf_counter() - self.last_status_change >= self.auto_reset: 
                    if self.raw_variables_def: # Check if previously the driver had some variables set up
                        self._cleanup()
                        if self._setup(self.params):
                            self.changeStatus(DriverStatus.RUNNING)
                            if not self._addVariables(self.raw_variables_def):
                                self.sendDebugInfo('ADD_VARIABLES action failed!')
                        else:
                            self.changeStatus(DriverStatus.ERROR)
                    else:
                        self.changeStatus(DriverStatus.ERROR)

            # Driver loop
            self.loop()

            # Sleep
            if self.rpi > 0:
                time.sleep(self.rpi*5e-4) # Sleep 1/2 rpi in seconds


    def loop(self):
        """ Runs every iteration while the driver is active. Only use if strictly necessary.
        """
        pass

                
    def changeStatus(self, new_status:DriverStatus):
        """ Change driver status.

        :param new_status: Status to be changed
        """
        try:
            self.status = new_status
            self.last_status_change = time.perf_counter()
            if self.pipe:
                self.pipe.send((DriverActions.STATUS, self.status))
        except:
            pass


    def sendDebugInfo(self, debug_info:str):
        """ Send debug telegram to server.

        :param debug_info: message sent in the telegram
        """
        try:
            if self.pipe:
                self.pipe.send((DriverActions.INFO, debug_info))
        except:
            pass

    def sendDebugVarInfo(self, debug_info:tuple):
        """ Send variable debug telegram to server.

        :param debug_info: message sent in the telegram
        """
        try:
            if self.pipe:
                self.pipe.send((DriverActions.VAR_INFO, debug_info))
        except:
            pass


    def sendUpdate(self, data:dict):
        """ Send update telegram to server. 

        :param data: data to be sent to the server {address: value}
        """
        try:
            if self.pipe:
                self.pipe.send((DriverActions.UPDATE, data))
        except:
            pass


    def _setup(self, param_data: dict) -> bool:
        """ Executed to setup the driver. This method calls the specific driver connect(). Variables need to be add with the ADD VARIABLES action. 

        :param param_data: Setup specific data including parameters. (See documentation)

        :returns: True if setup is completed or False if not
        """
        try:
            if param_data:
                self.__dict__.update(param_data)
                return self.connect()
                
        except Exception as e:
            self.sendDebugInfo('Exception during setup: '+str(e))
        
        return False


    def _addVariables(self, variable_data: dict) -> bool:
        """ Executed when setup is already done but new variables want to be added. 

        :param variable_data: Variable specific data. (See documentation)

        :returns: True if variables are added or False if not
        """
        try:
            if variable_data is not None and self._connection is not None:
                self.addVariables(variable_data)
                return True
                
        except Exception as e:
            self.sendDebugInfo('Exception during addVariables: '+str(e))
        
        return False


    def _cleanup(self):
        """ Executed to cleanup the driver. This method calls the specific disconnect() method.
        """
        try:
            self.disconnect()
            self.variables = {}        
        except Exception as e:
            self.sendDebugInfo('Exception during cleanup: '+str(e)) 
        finally:
            self._connection = None


    def _transmitVariables(self) -> bool:
        """ This is the internal loop code. This method calls the specific writeVariables() and readVariables() method on demand.
        
        :returns: True if transmission is completed or False if not
        """

        now = time.perf_counter()
        try:
            assert self._connection, "Connection not valid!"

            # Write variables from the server following the rpi
            if (now - self.last_write) >= (self.rpi*1e-3):
                self.last_write = now
                pending_writes = [(var_id, new_value) for var_id, new_value in self.pending_updates.items()]

                # Force write if necesary
                if (self.force_write > 0) and (now - self.last_forced_write >= self.force_write):
                    self.last_forced_write = now

                    # Loop all variables and set actual value to the pending writes if necessary
                    for var_id, var_data  in self.variables.items():
                        if var_data['operation'] in [VariableOperation.WRITE, VariableOperation.BOTH]:
                            if var_id not in self.pending_updates:
                                pending_writes.append((var_id, var_data['value']))

                # Call write variables
                if pending_writes:
                    for (var_id, value, quality) in self.writeVariables(pending_writes):
                        if var_id in self.pending_updates:
                            self.pending_updates.pop(var_id)
                            if quality == VariableQuality.GOOD:
                                self.variables[var_id]['value'] = value
                            else:
                                self.sendDebugInfo(f'Variable {var_id} write quality is {quality}')
            
            # Read variables from the driver following the rpi and send them to the server
            if (now - self.last_read) >= (self.rpi*1e-3):
                self.last_read = now
                pending_reads = []
                
                for var_id, var_data  in self.variables.items():
                    if var_data['operation'] in [VariableOperation.READ, VariableOperation.BOTH]:
                        pending_reads.append(var_id)

                if pending_reads:
                    updates = {}
                    for (var_id, value, quality) in self.readVariables(pending_reads):
                        if (quality == VariableQuality.GOOD):
                            if (self.variables[var_id]['value'] != value):
                                self.variables[var_id]['value'] = value
                                updates[var_id] = value
                        elif self.variables[var_id]['value'] != None:
                            self.sendDebugInfo(f'Variable {var_id} read quality is {quality}')
                            self.variables[var_id]['value'] = None

                    if updates:
                        self.sendUpdate(updates)

            return True
        
        except Exception as e:
            self.sendDebugInfo(f'Exception during variable transmission: {e}')
        
        return False


    def getValueFromString(self, datatype:VariableDatatype, str_value:str) -> any:
        """ Returns a potential variable value converted from string to the correct datatype.

        : param datatype: Variable datatype
        : param str_value: Variable value in string format

        : returns: the variable value in specific format or back as str by default. None if conversion not possible.
        """
        try:
            if datatype == VariableDatatype.BOOL:
                if isinstance(str_value, str):
                    return str_value in ['True','true']
                else:    
                    return bool(str_value)

            elif datatype in [VariableDatatype.BYTE, VariableDatatype.INTEGER, VariableDatatype.WORD, VariableDatatype.DWORD, VariableDatatype.QWORD]:
                return int(str_value)

            elif datatype == VariableDatatype.FLOAT:
                return float(str_value)

            else:
                return str_value

        except Exception as e:
            return None


    def defaultVariableValue(self, datatype: VariableDatatype, size:int=1) -> any:
        """ Returns the default variable value depending on the datatype.

        : param datatype: Variable datatype 
        : param size: Variable size: 0,1: single, >1: list (array)

        : returns: the default variable value for the datatype
        """
        if datatype == VariableDatatype.BOOL:
            def_value = False
        elif datatype in [VariableDatatype.BYTE, VariableDatatype.INTEGER, VariableDatatype.WORD, VariableDatatype.DWORD, VariableDatatype.QWORD]:
            def_value = 0
        elif datatype == VariableDatatype.FLOAT:
            def_value = 0.0
        else:
            def_value = ""

        if size > 1:
            return [def_value for i in range(size)]
        else:
            return def_value

    """ VIRTUAL METHODS TO BE IMPLEMENTED IN EACH DRIVER """

    def connect(self) -> bool:
        """ Connect driver.
        
        : returns: True if connection established False if not
        """
        return True


    def disconnect(self):
        """ Disconnect driver.
        """
        pass


    def addVariables(self, variables: dict):
        """ Add variables to the driver. Correctly added variables will be added to internal dictionary 'variables'.
        Any error adding a variable should be communicated to the server using sendDebugInfo() method.

        : param variables: Variables to add in a dict following the setup format. (See documentation) 
        
        """
        pass


    def readVariables(self, variables: list) -> list:
        """ Read given variable values. In case that the read is not possible or generates an error BAD quality should be returned.
        : param variables: List of variable ids to be read. 

        : returns: list of tupples including (var_id, var_value, VariableQuality)
        """
        return []


    def writeVariables(self, variables: list) -> list:
        """ Write given variable values. In case that the write is not possible or generates an error BAD quality should be returned.
        : param variables: List of tupples with variable ids and the values to be written (var_id, var_value). 

        : returns: list of tupples including (var_id, var_value, VariableQuality)
        """
        return []
