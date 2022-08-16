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

from opcua import Client, ua
from collections import deque
import os
from multiprocessing import Pipe
from typing import Optional

from ..driver import VariableOperation, driver, VariableQuality 

import logging
logging.getLogger('opcua').setLevel(logging.CRITICAL)

class SubHandler(object):

    def __init__(self):
        self.read_values = {}
        
    def datachange_notification(self, node, val, data):
        self.read_values[node] = val
    

class opcua_client(driver):
    """
    This driver is just a opcua client that can be used to access OPCUA data in a server.
    The driver is based on the opcua Client object form the python opcua library (https://github.com/FreeOpcUa/python-opcua).

    Parameters:
    url: str
        OPCUA server address. Default = 'opc.tcp://localhost:4840'

    """

    def __init__(self, name: str, pipe: Optional[Pipe] = None, params:dict = None):
        """
        :param name: (optional) Name for the driver
        :param pipe: (optional) Pipe used to communicate with the driver thread. See gateway.py
        """
        # Inherit
        driver.__init__(self, name, pipe, params)

        # Parameters
        self.url = 'opc.tcp://localhost:4840'


    def connect(self) -> bool:
        """ Connect driver.
        
        : returns: True if connection established False if not
        """
        try:   
            self._connection = Client(self.url)
            self._connection.connect()
                    
        except Exception as e:
            self.sendDebugInfo(f'Error connecting to server at {self.url}.')
            return False

        self.handler = SubHandler()
        self.subscription = self._connection.create_subscription(self.rpi, self.handler)
        return True


    def disconnect(self):
        """ Disconnect driver.
        """
        if self._connection:
            self._connection.disconnect()


    def addVariables(self, variables: dict):
        """ Add variables to the driver. Correctly added variables will be added to internal dictionary 'variables'.
        Any error adding a variable should be communicated to the server using sendDebugInfo() method.

        : param variables: Variables to add in a dict following the setup format. (See documentation) 
        
        """
        # Get Objects node
        objects = self._connection.get_objects_node()

        # Get deviceSet node
        if not objects: 
            raise Exception('Objects node not found!') 

        # Loop variables and append extra info to data dict
        var_identifiers = []
        var_paths = []
        var_names = []
        for var_id in variables.keys():
            if '=' in var_id:
                var_identifiers.append(var_id)
            elif '.' in var_id:
                var_paths.append(var_id)
            else:
                var_names.append(var_id)

        var_ident_found, var_idents_not_found = self.find_nodes_by_identifier(objects, var_identifiers)
        var_paths_found, var_paths_not_found = self.find_nodes_by_path(objects, var_paths)
        var_names_found, var_names_not_found = self.find_nodes_by_name(objects, var_names)
        vars_found = {}
        vars_found.update(var_names_found)
        vars_found.update(var_paths_found)
        vars_found.update(var_ident_found)

        for var_id, node in vars_found.items():
            # debug info
            self.sendDebugVarInfo(('SETUP: Variable found {}'.format(var_id), var_id))
            # Add node to info
            self.variables[var_id] = dict(variables[var_id])
            self.variables[var_id]['node'] = node
            # Check datatype and size
            self.variables[var_id]['variant'] = node.get_data_type_as_variant_type()
            # If write, get actual value
            if self.variables[var_id]['operation'] == VariableOperation.WRITE:
                # Save write variable values
                self.variables[var_id]['value'] = node.get_value()
            # If read, subscribe
            else:
                # read variable values do not need to be saved
                self.variables[var_id]['value'] = None
                self.subscription.subscribe_data_change(node)
                
        # Remove variables not found
        for var_id in var_idents_not_found + var_paths_not_found + var_names_not_found:
            self.sendDebugVarInfo(('SETUP: Variable NOT found {}'.format(var_id), var_id))


    def readVariables(self, variables: list) -> list:
        """ Read given variable values. In case that the read is not possible or generates an error BAD quality should be returned.
        : param variables: List of variable ids to be read. 

        : returns: list of tupples including (var_id, var_value, VariableQuality)
        """

        new_values = dict(self.handler.read_values)
        self.handler.read_values = {}

        res = []
        for var_id in variables:
            var_node = self.variables[var_id]['node']
            if var_node in new_values:
                new_value = new_values.pop(var_node)
                res.append((var_id, new_value, VariableQuality.GOOD)) 
            else:
                res.append((var_id, self.variables[var_id]['value'], VariableQuality.GOOD))
        return res


    def writeVariables(self, variables: list) -> list:
        """ Write given variable values. In case that the write is not possible or generates an error BAD quality should be returned.
        : param variables: List of tupples with variable ids and the values to be written (var_id, var_value). 

        : returns: list of tupples including (var_id, var_value, VariableQuality)
        """
        nodeids = []
        values = []
        res = []
        for (var_id, new_value) in variables:
            nodeids.append(self.variables[var_id]['node'].nodeid)
            values.append(ua.DataValue(ua.Variant(new_value, self.variables[var_id]['variant'])))
        if len(nodeids)>0:
            results = self._connection.uaclient.set_attributes(nodeids, values, ua.AttributeIds.Value)
            for i, result in enumerate(results):
                if result.is_good():
                    res.append((variables[i][0], variables[i][1], VariableQuality.GOOD))
                else:
                    res.append((variables[i][0], variables[i][1], VariableQuality.BAD))
        return res


    # Helper function
    def find_nodes_by_name(self, parent, names:list=[]):
        """ The method gets a parent node and a list of node names.
        It returns the dictionary with the node names as keys and found nodes as values."""
        res = {}
        # Check parent node
        if names:   
            name = parent.get_display_name().Text
            if name in names:
                res[name] = parent
                names.remove(name)
        # Check children nodes
        if names:
            try:
                children = parent.get_children()
            except Exception as e:
                children = []
            for child in children:
                res_child, names = self.find_nodes_by_name(child, names)
                res.update(res_child)
                if not names: break
        # Return results
        return res, names


    # Helper function
    def find_node_by_path(self, parent, path):
        node_names = deque(path.split('.'))
        if node_names:
            child_node = parent
            while node_names:
                node_name = node_names.popleft()
                for child in child_node.get_children():
                    if node_name == child.get_display_name().Text:
                        child_node = child
                        break
                else:
                    return None
            return child_node
        else:
            return None


    def find_nodes_by_path(self, parent, paths:list=[]):
        """ The method gets a parent node and a list of node paths.
        It returns the dictionary with the node paths as keys and found nodes as values.
        Node paths are node names separated by dots, i.e.:
          'DeviceSet.CODESYS Control Win V3 x64.Resources.Application.GlobalVars.GVL.inputs'
        """
        res = {}
        bad_paths = []
 
        common_path = os.path.commonprefix(paths)
        if len(common_path)>0:
            if common_path[-1] == '.': # A good common path should end with '.'
                common_node = self.find_node_by_path(parent, common_path[:-1])
                if common_node:
                    parent = common_node
                    paths = [x.replace(common_path,'') for x in paths]
            else:
                common_path = ''

        while paths:
            path = paths.pop()
            child_node = self.find_node_by_path(parent, path)

            if child_node is not None:
                res[common_path+path] = child_node
            else:
                bad_paths.append(common_path+path)
        
        return res, bad_paths

    def find_nodes_by_identifier(self, parent, identifiers:list=[]):
        """ The method gets a parent node and a list of node identifiers.
        It returns the dictionary with the node identifiers as keys and found nodes as values.
        Node identifiers should follow the OPCUA format, i.e.:
          'ns=4;s=|var|CODESYS Control Win V3 x64.Application.GVL.inputs'
        """
        res = {}
        bad_identifiers = []

        while identifiers:
            identifier = identifiers.pop()
            child_node = self._connection.get_node(identifier)
            try:
                child_node.get_attribute(ua.AttributeIds.DisplayName)
            except:
                child_node = None

            if child_node is not None:
                res[identifier] = child_node
            else:
                bad_identifiers.append(identifier)
        
        return res, bad_identifiers
