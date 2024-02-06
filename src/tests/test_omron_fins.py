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
    'CIO0.0':{'datatype': VariableDatatype.BOOL, 'size': 1, 'operation': VariableOperation.WRITE},
    'CIO1.0':{'datatype': VariableDatatype.BOOL, 'size': 1, 'operation': VariableOperation.READ},
    'CIO2':{'datatype': VariableDatatype.WORD, 'size': 1, 'operation': VariableOperation.WRITE},
    'CIO3':{'datatype': VariableDatatype.WORD, 'size': 1, 'operation': VariableOperation.READ},
    'D0.0':{'datatype': VariableDatatype.BOOL, 'size': 1, 'operation': VariableOperation.WRITE},
    'D1.0':{'datatype': VariableDatatype.BOOL, 'size': 1, 'operation': VariableOperation.READ},
    'D2':{'datatype': VariableDatatype.WORD, 'size': 1, 'operation': VariableOperation.WRITE},
    'D3':{'datatype': VariableDatatype.WORD, 'size': 1, 'operation': VariableOperation.READ},
    'H0.0':{'datatype': VariableDatatype.BOOL, 'size': 1, 'operation': VariableOperation.WRITE},
    'H1.0':{'datatype': VariableDatatype.BOOL, 'size': 1, 'operation': VariableOperation.READ},
    'H2':{'datatype': VariableDatatype.WORD, 'size': 1, 'operation': VariableOperation.WRITE},
    'H3':{'datatype': VariableDatatype.WORD, 'size': 1, 'operation': VariableOperation.READ},
    'W0.0':{'datatype': VariableDatatype.BOOL, 'size': 1, 'operation': VariableOperation.WRITE},
    'W1.0':{'datatype': VariableDatatype.BOOL, 'size': 1, 'operation': VariableOperation.READ},
    'W2':{'datatype': VariableDatatype.WORD, 'size': 1, 'operation': VariableOperation.WRITE},
    'W3':{'datatype': VariableDatatype.WORD, 'size': 1, 'operation': VariableOperation.READ},
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
    while time.perf_counter()-start < 100:
        d.writeVariables([
            ('CIO0.0', counter%2),
            ('CIO2', counter),
            ('D0.0', counter%2),
            ('D2', counter),
            ('H0.0', counter%2),
            ('H2', counter),
            ('W0.0', counter%2),
            ('W2', counter),
            ])
        d.readVariables(['CIO1.0', 'CIO3', 'D1.0', 'D3', 'H1.0', 'H3', 'W1.0', 'W3'])
        time.sleep(0.1)
        counter += 1

    d.disconnect()
