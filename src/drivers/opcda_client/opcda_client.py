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
import win32com.client
import win32com.server.util
import win32event
import pythoncom

from ..driver import VariableOperation, VariableQuality, driver

OPC_CLASS_LIST = [
    'Graybox.OPC.DAWrapper.1',
    'OPC.Automation',
    'RSI.OPCAutomation',
    'Matrikon.OPC.Automation.1',
    'HSCOPC.Automation']
OPC_CLIENT = 'Simumatik'

class GroupEvents:
    def __init__(self):
        self.callback_data = {} 
        
    def OnDataChange(self, TransactionID, NumItems, ClientHandles, ItemValues, Qualities, TimeStamps):
        for i in range(NumItems):
            self.callback_data[ClientHandles[i]] = ItemValues[i]


class opcda_client(driver):
    '''
    Driver that can be used to connect to OPC-DA (Classic) servers. The functionality is similar to the newer OPCUA, but will work just in Windows because it makes use of COM objects.
    Parameters:
    server: string
        This is the server name of the OPC DA Server
    
    async_connection: bool
        This variable can be set to true to use async reading (subscription). Default = False
    '''

    def __init__(self, name: str, pipe: multiprocessing.Pipe = None, params:dict = None):
        """
        :param name: (optional) Name for the driver
        :param pipe: (optional) Pipe used to communicate with the driver thread. See gateway.py
        """
        # Inherit
        driver.__init__(self, name, pipe, params)

        # Parameters
        self.server = 'Matrikon.OPC.Simulation.1'
        self.async_connection = False
        self.client_class = ''
        self.data_source = 2 # SOURCE_CACHE = 1, SOURCE_DEVICE = 2

        # Internal
        self.read_group = None
        self.write_group = None
        self.handle_num = 0

        # Async connection
        self._tx_id = 1
        self._event = None


    def connect(self) -> bool:
        """ Connect driver.
        
        : returns: True if connection established False if not
        """
        pythoncom.CoInitialize()

        ''' Rows below are copied from OpenOPC'''
        self._connection = None
        if self.client_class == '':
            client_list = list(OPC_CLASS_LIST)
        else:
            client_list = [self.client_class]
        for self.client_class in client_list:
            try:
                self._connection = win32com.client.Dispatch(self.client_class, 0)
                self.sendDebugInfo(f"Using OPC COM object: {self.client_class}")
                break
            except Exception as e:
                pass          
    
        if self._connection is None:
            self.sendDebugInfo(f"Could not get OPC COM object: {self.client_class}")
            return False

        if self.async_connection:
            self._event = win32event.CreateEvent(None,0,0,None)
        
        try:
            servers = self._connection.GetOPCServers('localhost')
            self.sendDebugInfo(f"Available servers: {servers}")

            self._connection.Connect(self.server, 'localhost')
            self._connection.ClientName = OPC_CLIENT

            # Only SYNC read and write, that is, no Update rate at server side.
            if self.async_connection:
                self._connection.OPCGroups.DefaultGroupUpdateRate = self.rpi 
            else:
                self._connection.OPCGroups.DefaultGroupUpdateRate = -1

            # Create a group for reading variables (outputs)
            self.read_group = self._connection.OPCGroups.Add('READ')
            if self.async_connection:
                self.read_group.IsSubscribed = 1
                self.read_callback = win32com.client.WithEvents(self.read_group, GroupEvents)
            else:
                self.read_group.IsSubscribed = 0
            self.read_group.IsActive = 1

            # Create a group for writing variables (inputs)
            self.write_group = self._connection.OPCGroups.Add('WRITE')
            self.write_group.IsSubscribed = 0
            self.write_group.IsActive = 1

            self.sendDebugInfo(f"{self.client_class} Connected to OPC DA server: {self.server}")
            return True
        except Exception as e:
            self.sendDebugInfo(f"Could not connect to OPC DA server: {self.server}")
            return False


    def disconnect(self):
        """ Clean up groups and disconnect client.
        """
        if self._connection is not None:
            self._connection.OPCGroups.Remove('WRITE')
            self._connection.OPCGroups.Remove('READ')
            self._connection.Disconnect()


    def addVariables(self, variables: dict):
        """ Add variables to the driver. Correctly added variables will be added to internal dictionary 'variables'.
        Any error adding a variable should be communicated to the server using sendDebugInfo() method.
        : param variables: Variables to add in a dict following the setup format. (See documentation) 
        
        """
        for var_id, var_data in variables.items():
            # Add client handle to variables dict
            self.handle_num += 1
            variables[var_id]['client_handle'] = self.handle_num

            try:
                # Add variables to the read/write groups
                if var_data['operation'] == VariableOperation.READ:
                    server_handles, errors = self.read_group.OPCItems.AddItems(1, [0,var_id], [0,self.handle_num])
                    if self.async_connection:
                        self._tx_id = self._tx_id+1 if self._tx_id< 0xFFFF else 0
                        self.read_group.AsyncRefresh(self.data_source, self._tx_id)       
                else:
                    server_handles, errors = self.write_group.OPCItems.AddItems(1, [0,var_id], [0,self.handle_num])
                if errors[0] == 0:
                    variables[var_id]['server_handle'] = server_handles[0]
                    if var_data['operation'] == VariableOperation.READ:
                        variables[var_id]['value'] = None # Force first update
                    else:
                        variables[var_id]['value'] = self.defaultVariableValue(variables[var_id]['datatype'], variables[var_id]['size'])
                    self.variables[var_id] = variables[var_id]
                else:
                    self.sendDebugVarInfo((f"Variable not found: {var_id}!", var_id))
            except Exception as e:
                self.sendDebugInfo(f'exception adding variable {var_id}: {e}')



    def readVariables(self, variables: list) -> list:
        """ Read given variable values. In case that the read is not possible or generates an error BAD quality should be returned.
        : param variables: List of variable ids to be read. 
        : returns: list of tupples including (var_id, var_value, VariableQuality)
        """
        res = []

        if self.async_connection:      
            for var_id in variables:
                ch = self.variables[var_id]['client_handle']
                if ch in self.read_callback.callback_data:
                    res.append((var_id, self.read_callback.callback_data[ch], VariableQuality.GOOD))
                else:
                    res.append((var_id, self.variables[var_id]['value'], VariableQuality.BAD))
                    self.read_callback.callback_data[ch] = self.variables[var_id]['value']

        else:
            names = []
            handles = []
            for var_id in variables:
                # Only read variables that have been added successfully
                if var_id in self.variables:
                    handles.append(self.variables[var_id]['server_handle'])
                    names.append(var_id)
            if handles:
                try:
                    values, errors, _, _ = self.read_group.SyncRead(self.data_source, len(handles), [0]+handles)
                    for i, error in enumerate(errors):
                        if error == 0:
                            res.append((names[i], values[i], VariableQuality.GOOD))
                        else:
                            self.sendDebugVarInfo((f"Variable {names[i]} read error! {self._connection.GetErrorString(error)}", names[i]))
                            res.append((names[i], values[i], VariableQuality.BAD))
                except Exception as e:
                    self.sendDebugInfo(f'exception reading variable values: {e}, {names}, {handles}')

        return res


    def writeVariables(self, variables: list) -> list:
        """ Write given variable values. In case that the write is not possible or generates an error BAD quality should be returned.
        : param variables: List of tupples with variable ids and the values to be written (var_id, var_value). 
        : returns: list of tupples including (var_id, var_value, VariableQuality)
        """
        res = []
        names = []
        handles = []
        values = []
        for (var_id, value) in variables:
            # Only write variables that have been added successfully
            if var_id in self.variables:
                names.append(var_id)
                values.append(value)
                handles.append(self.variables[var_id]['server_handle'])
        if handles:
            try:
                errors = self.write_group.SyncWrite(len(handles), [0]+handles, [0]+values)
                for i, error in enumerate(errors):
                    if error == 0:
                        res.append((names[i], values[i], VariableQuality.GOOD))
                    else:
                        self.sendDebugVarInfo((f"Variable {names[i]} write error! {self._connection.GetErrorString(error)}", names[i]))
                        res.append((names[i], values[i], VariableQuality.BAD))
            except Exception as e:
                self.sendDebugInfo(f'exception reading variable values: {e}, {names}, {handles}')
        
        return res