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

from drivers.omron_nexsocket.omron_nexsocket import omron_nexsocket
from drivers.driver import VariableOperation, VariableDatatype

VARIABLES = {
    'Out_BOOL':{'datatype': VariableDatatype.BOOL, 'size': 1, 'operation': VariableOperation.READ},
    'Out_BYTE':{'datatype': VariableDatatype.BYTE, 'size': 1, 'operation': VariableOperation.READ},
    'Out_WORD':{'datatype': VariableDatatype.WORD, 'size': 1, 'operation': VariableOperation.READ},
    'Out_DWORD':{'datatype': VariableDatatype.DWORD, 'size': 1, 'operation': VariableOperation.READ},
    'Out_QWORD':{'datatype': VariableDatatype.QWORD, 'size': 1, 'operation': VariableOperation.READ},
    'Out_INTEGER':{'datatype': VariableDatatype.INTEGER, 'size': 1, 'operation': VariableOperation.READ},
    'Out_FLOAT':{'datatype': VariableDatatype.FLOAT, 'size': 1, 'operation': VariableOperation.READ},
    'In_BOOL':{'datatype': VariableDatatype.BOOL, 'size': 1, 'operation': VariableOperation.WRITE},
    'In_BYTE':{'datatype': VariableDatatype.BYTE, 'size': 1, 'operation': VariableOperation.WRITE},
    'In_WORD':{'datatype': VariableDatatype.WORD, 'size': 1, 'operation': VariableOperation.WRITE},
    'In_DWORD':{'datatype': VariableDatatype.DWORD, 'size': 1, 'operation': VariableOperation.WRITE},
    'In_QWORD':{'datatype': VariableDatatype.QWORD, 'size': 1, 'operation': VariableOperation.WRITE},
    'In_INTEGER':{'datatype': VariableDatatype.INTEGER, 'size': 1, 'operation': VariableOperation.WRITE},
    'In_FLOAT':{'datatype': VariableDatatype.FLOAT, 'size': 1, 'operation': VariableOperation.WRITE},

    }

d = omron_nexsocket(None, 'test')

if d.connect():
    d.addVariables(VARIABLES)
    counter = 0
    t = time.perf_counter()
    while time.perf_counter()-t < 10:

        res = d.readVariables(['Out_BOOL','Out_BYTE','Out_WORD','Out_DWORD','Out_QWORD','Out_INTEGER','Out_FLOAT'])
        print(res, counter)
        d.writeVariables([
            ('In_BOOL', counter%2),
            ('In_BYTE', counter%256),
            ('In_WORD', counter),
            ('In_DWORD', counter),
            ('In_QWORD', counter),
            ('In_INTEGER', counter-1000),
            ('In_FLOAT', counter/3)])
        counter += 1
    d.disconnect()
