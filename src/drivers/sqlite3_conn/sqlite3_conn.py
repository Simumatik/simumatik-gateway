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
import sqlite3

from ..driver import driver, VariableOperation, VariableQuality


class sqlite3_conn(driver):
    '''
    Driver that can read and write on an SQLite3 database table. 
    The table should include at least two TEXT columns including the name and value of the variables.
    The value in TEXT format will be converted by the driver to the defined datatype.

    Parameters:
    address: str
        This is the path of the database. Default = "mydb.db"
    table: str
        This is the name of the database table where the variables are located. Default = "variables"
    variable_column: str
        This is the name of the column which includes the variable names. Default = "name"
    value_column: str
        This is the name of the column which includes the variable values. Default = "value"
    '''

    def __init__(self, name: str, pipe: Optional[Pipe] = None, params:dict = None):
        """
        :param name: (optional) Name for the driver
        :param pipe: (optional) Pipe used to communicate with the driver thread. See gateway.py
        """
        # Inherit
        driver.__init__(self, name, pipe, params)

        # Parameters
        self.address = "mydb.db"
        self.table = "variables"
        self.variable_column = "name"
        self.value_column = "value"


    def connect(self) -> bool:
        """ Connect driver.
        
        : returns: True if connection established False if not
        """
        try:
            self._connection = sqlite3.connect(self.address)
            cursor = self._connection.cursor()

            # Check if table exists
            cursor.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name=?", (self.table,))
            if cursor.fetchone()[0] != 1:
                self.sendDebugInfo(f"SETUP: Table {self.table} does not exist.")
                return False
            
            # Check if columns exist
            cursor.execute('SELECT * from variables')
            columns = [description[0] for description in cursor.description]
            if self.variable_column not in columns:
                self.sendDebugInfo(f"SETUP: Table {self.table} does not contain column {self.variable_column}.")
                return False
            if self.value_column not in columns:
                self.sendDebugInfo(f"SETUP: Table {self.table} does not contain column {self.value_column}.")
                return False
            
            self._connection.commit()

        except Exception as e:
            self.sendDebugInfo(f"SETUP: Connection with {self.address} cannot be established.")
            return False
        
        return True


    def disconnect(self):
        """ Disconnect driver.
        """
        if self._connection:
            self._connection.close()
            self._connection = None


    def addVariables(self, variables: dict):
        """ Add variables to the driver. Correctly added variables will be added to internal dictionary 'variables'.
        Any error adding a variable should be communicated to the server using sendDebugInfo() method.
        : param variables: Variables to add in a dict following the setup format. (See documentation) 
        
        """
        cursor = self._connection.cursor()
        for var_id, var_data in variables.items():
            cursor.execute("SELECT value FROM variables WHERE name=?", (var_id,))
            res = cursor.fetchall()
            if res:
                var_data['value'] =  self.getValueFromString(var_data['datatype'], res[0][0])
                self.variables[var_id] = var_data
            else:
                self.sendDebugVarInfo(('SETUP: Variable NOT found {}'.format(var_id), var_id))


    def readVariables(self, variables: list) -> list:
        """ Read given variable values. In case that the read is not possible or generates an error BAD quality should be returned.
        : param variables: List of variable ids to be read. 
        : returns: list of tupples including (var_id, var_value, VariableQuality)
        """
        res = []
        cursor = self._connection.cursor()
        for var_id in variables:
            cursor.execute("SELECT value FROM variables WHERE name=?", (var_id,))
            new_value = cursor.fetchall()
            if new_value:
                new_value = self.getValueFromString(self.variables[var_id]['datatype'], new_value[0][0])
                res.append((var_id, new_value, VariableQuality.GOOD))
            else:
                res.append((var_id, None, VariableQuality.BAD))
        return res



    def writeVariables(self, variables: list) -> list:
        """ Write given variable values. In case that the write is not possible or generates an error BAD quality should be returned.
        : param variables: List of tupples with variable ids and the values to be written (var_id, var_value). 
        : returns: list of tupples including (var_id, var_value, VariableQuality)
        """
        res = []
        cursor = self._connection.cursor()
        for (var_id, new_value) in variables:
            try:
                str_new_value = str(new_value)
                cursor.execute("UPDATE variables SET value=? WHERE name=?", (str_new_value, var_id,))
                self._connection.commit()
                res.append((var_id, new_value, VariableQuality.GOOD))
            except:
                res.append((var_id, new_value, VariableQuality.BAD))           
        return res
