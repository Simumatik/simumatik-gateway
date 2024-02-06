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
from os import path
import time
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from drivers.omron_fins.omron_fins import omron_fins
from drivers.driver import VariableOperation, VariableDatatype

# Define your I/O variables here
VARIABLES = {
    'd0':{'datatype': VariableDatatype.WORD, 'size': 1, 'operation': VariableOperation.WRITE},
    'd1':{'datatype': VariableDatatype.INTEGER, 'size': 1, 'operation': VariableOperation.WRITE},
    'd2':{'datatype': VariableDatatype.DWORD, 'size': 1, 'operation': VariableOperation.WRITE},
    'd4':{'datatype': VariableDatatype.QWORD, 'size': 1, 'operation': VariableOperation.WRITE},
    'd8':{'datatype': VariableDatatype.FLOAT, 'size': 1, 'operation': VariableOperation.WRITE},
    'd10':{'datatype': VariableDatatype.WORD, 'size': 1, 'operation': VariableOperation.READ},
    'd11':{'datatype': VariableDatatype.INTEGER, 'size': 1, 'operation': VariableOperation.READ},
    'd12':{'datatype': VariableDatatype.DWORD, 'size': 1, 'operation': VariableOperation.READ},
    'd14':{'datatype': VariableDatatype.QWORD, 'size': 1, 'operation': VariableOperation.READ},
    'd18':{'datatype': VariableDatatype.FLOAT, 'size': 1, 'operation': VariableOperation.READ},
    }

# Add your custom logic in this test.
d = omron_fins(None, 'test')
d.ip = "192.168.0.1"
d.dest_node_add = 1
d.srce_node_add = 25

if d.connect():
    d.addVariables(VARIABLES)

    counter = 0
    start = time.perf_counter()
    while time.perf_counter()-start < 10:
        d.writeVariables([
            ('d0', counter),
            ('d1', counter*2),
            ('d2', counter*3),
            ('d4', counter*4),
            ('d8', counter*1.1),
            ])
        res = d.readVariables(['d10', 'd11', 'd12', 'd14', 'd18'])
        for (var_id, value, quality) in res: 
            print(f"{var_id}: {value}")
        time.sleep(0.1)
        counter += 1

    d.disconnect()
