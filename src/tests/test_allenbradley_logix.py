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

from drivers.allenbradley_logix.allenbradley_logix import allenbradley_logix
from drivers.driver import VariableOperation, VariableDatatype

# Define your I/O variables here
VARIABLES = {
    'inputs_BOOL':{'datatype': VariableDatatype.BOOL, 'size': 1, 'operation': VariableOperation.WRITE},
    'outputs_BOOL':{'datatype': VariableDatatype.BOOL, 'size': 1, 'operation': VariableOperation.READ},
    'inputs_BYTE':{'datatype': VariableDatatype.BYTE, 'size': 1, 'operation': VariableOperation.WRITE},
    'outputs_BYTE':{'datatype': VariableDatatype.BYTE, 'size': 1, 'operation': VariableOperation.READ},
    'inputs_WORD':{'datatype': VariableDatatype.WORD, 'size': 1, 'operation': VariableOperation.WRITE},
    'outputs_WORD':{'datatype': VariableDatatype.WORD, 'size': 1, 'operation': VariableOperation.READ},
    'inputs_DWORD':{'datatype': VariableDatatype.DWORD, 'size': 1, 'operation': VariableOperation.WRITE},
    'outputs_DWORD':{'datatype': VariableDatatype.DWORD, 'size': 1, 'operation': VariableOperation.READ},
    'inputs_INT':{'datatype': VariableDatatype.INTEGER, 'size': 1, 'operation': VariableOperation.WRITE},
    'outputs_INT':{'datatype': VariableDatatype.INTEGER, 'size': 1, 'operation': VariableOperation.READ},
    'inputs_FLOAT':{'datatype': VariableDatatype.FLOAT, 'size': 1, 'operation': VariableOperation.WRITE},
    'outputs_FLOAT':{'datatype': VariableDatatype.FLOAT, 'size': 1, 'operation': VariableOperation.READ},
    }

# Add your custom logic in this test.
d = allenbradley_logix(None, 'test')
d.ip = "192.168.1.246"

if d.connect():
    d.addVariables(VARIABLES)

    counter = 0
    while time.perf_counter() < 100:
        d.writeVariables([
            ('inputs_BOOL', counter%2),
            ('inputs_BYTE', counter),
            ('inputs_WORD', counter),
            ('inputs_DWORD', counter*2),
            ('inputs_INT', counter*6),
            ('inputs_FLOAT', counter*2.3),
            ])
        d.readVariables(['outputs_BOOL', 'outputs_BYTE', 'outputs_WORD', 'outputs_DWORD', 'outputs_INT', 'outputs_FLOAT'])
        time.sleep(0.1)
        counter += 1

    d.disconnect()
