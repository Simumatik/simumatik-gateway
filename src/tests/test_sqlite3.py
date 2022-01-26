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

''' 
TEST sqlite3 driver
------------------------

This test does not have any requirement.
Just execute the script to create the generic driver and test the diferent actions against a SQLite database.
You can use a DB browser to see the inputs value change and modify the output values.
For the test DB Browser fo SQLite was used.
'''

import sys
from os import path
import time
import sqlite3
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from drivers.sqlite3_conn.sqlite3_conn import sqlite3_conn
from drivers.driver import VariableOperation, VariableDatatype

VARIABLES = {
    'inputs':{'datatype': VariableDatatype.BYTE, 'size': 1, 'operation': VariableOperation.WRITE},
    'outputs':{'datatype': VariableDatatype.BYTE, 'size': 1, 'operation': VariableOperation.READ},
    }

ADDRESS = 'C:\TEMP\mydb.db'

# Create table if does not exist
connection = sqlite3.connect(ADDRESS)
cursor = connection.cursor()
cursor.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name='variables'")
if cursor.fetchone()[0] != 1:
    cursor.execute('''CREATE TABLE variables (name TEXT, value TEXT)''')		
    cursor.execute('''INSERT INTO variables (name, value) VALUES ('inputs', '0')''')		
    cursor.execute('''INSERT INTO variables (name, value) VALUES ('outputs', '11')''')		
connection.commit()
connection.close()

d = sqlite3_conn('test', None)
if d._setup({'parameters':{'address':ADDRESS}}):
    d.addVariables(VARIABLES)

    counter = 0
    start = time.perf_counter()
    while time.perf_counter() < 50+start:
        d.writeVariables([('inputs', counter)])
        print(d.readVariables(['outputs']))
        time.sleep(0.1)
        counter += 1

    d.disconnect()