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

from drivers.kuka_varproxy.kuka_varproxy import kuka_varproxy
from drivers.driver import VariableOperation, VariableDatatype

# Define your I/O variables here
VARIABLES = {
    'Out_BOOL':{'datatype': VariableDatatype.BOOL, 'size': 1, 'operation': VariableOperation.READ},
    'Out_INTEGER':{'datatype': VariableDatatype.BYTE, 'size': 1, 'operation': VariableOperation.READ},
    'Out_FLOAT':{'datatype': VariableDatatype.FLOAT, 'size': 1, 'operation': VariableOperation.READ},
    'In_BOOL':{'datatype': VariableDatatype.BOOL, 'size': 1, 'operation': VariableOperation.WRITE},
    'In_INTEGER':{'datatype': VariableDatatype.BYTE, 'size': 1, 'operation': VariableOperation.WRITE},
    'In_FLOAT':{'datatype': VariableDatatype.FLOAT, 'size': 1, 'operation': VariableOperation.WRITE},
    '$AXIS_ACT': {'datatype': VariableDatatype.FLOAT, 'size': 6, 'operation': VariableOperation.READ},
    }

# Add your custom logic in this test.

d = kuka_varproxy(None, 'test')
d.ip = '192.168.138.128'

if d.connect():
    d.addVariables(VARIABLES)
    counter = 0
    t = time.perf_counter()
    while time.perf_counter()-t < 10:

        res = d.readVariables(['Out_BOOL','Out_INTEGER','Out_FLOAT', '$AXIS_ACT'])
        print(res, counter)
        d.writeVariables([
            ('In_BOOL', True if counter%2 == 0 else False),
            ('In_INTEGER', counter-200),
            ('In_FLOAT', counter/3),
            ])
        counter += 1
    d.disconnect()
print('')