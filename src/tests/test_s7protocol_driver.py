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

from drivers.s7protocol.s7protocol import s7protocol
from drivers.driver import VariableOperation, VariableDatatype

VARIABLES = {
    'DB11.DBB0':{'datatype': VariableDatatype.BYTE, 'size': 1, 'operation': VariableOperation.WRITE},
    'DB5.DBD68':{'datatype': VariableDatatype.BYTE, 'size': 1, 'operation': VariableOperation.READ},
    }
'''
'IB0':{'datatype': VariableDatatype.BYTE, 'size': 1, 'operation': VariableOperation.WRITE},
'QB0':{'datatype': VariableDatatype.BYTE, 'size': 1, 'operation': VariableOperation.READ},
'I1.2':{'datatype': VariableDatatype.BOOL, 'size': 1, 'operation': VariableOperation.WRITE},
'Q1.2':{'datatype': VariableDatatype.BOOL, 'size': 1, 'operation': VariableOperation.READ},
'IW2':{'datatype': VariableDatatype.WORD, 'size': 1, 'operation': VariableOperation.WRITE},
'QW2':{'datatype': VariableDatatype.WORD, 'size': 1, 'operation': VariableOperation.READ},
'IW4':{'datatype': VariableDatatype.INTEGER, 'size': 1, 'operation': VariableOperation.WRITE},
'QW4':{'datatype': VariableDatatype.INTEGER, 'size': 1, 'operation': VariableOperation.READ},
'ID10':{'datatype': VariableDatatype.DWORD, 'size': 1, 'operation': VariableOperation.WRITE},
'QD10':{'datatype': VariableDatatype.DWORD, 'size': 1, 'operation': VariableOperation.READ},
'ID14':{'datatype': VariableDatatype.INTEGER, 'size': 1, 'operation': VariableOperation.WRITE},
'QD14':{'datatype': VariableDatatype.INTEGER, 'size': 1, 'operation': VariableOperation.READ},
'ID18':{'datatype': VariableDatatype.FLOAT, 'size': 1, 'operation': VariableOperation.WRITE},
'QD18':{'datatype': VariableDatatype.FLOAT, 'size': 1, 'operation': VariableOperation.READ},
'''


d = s7protocol(None, 'test')
d.ip = '192.168.1.250'
# For S-1200
d.rack = 0
d.slot = 1
# For Logo!
#d.rack = 0
#d.slot = 2
if True:#d.connect():
    d.addVariables(VARIABLES)
    counter = 0
    t = time.perf_counter()
    while time.perf_counter()-t < 10:

        res = d.readVariables(['DB5.DBD68'])#'QB0','Q1.2','QW2','QD10','QW4','QW10000','QD18'])
        print(res, counter)
        d.writeVariables([
            ('DB11.DBB0', counter%2),
            #('I1.2', counter%2),
            #('IB0', counter%256),
            #('IW2', counter),
            #('ID10', counter),
            #('IW4', counter-1000),
            #('ID18', counter/3)]
            ])
        counter += 1
    d.disconnect()
