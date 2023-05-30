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

from drivers.plcsim.plcsim import plcsim
from drivers.driver import VariableOperation, VariableDatatype

VARIABLES = {
    'IB0':{'datatype': VariableDatatype.BYTE, 'size': 1, 'operation': VariableOperation.WRITE},
    'QB0':{'datatype': VariableDatatype.BYTE, 'size': 1, 'operation': VariableOperation.READ},
    'I1.2':{'datatype': VariableDatatype.BOOL, 'size': 1, 'operation': VariableOperation.WRITE},
    'Q1.2':{'datatype': VariableDatatype.BOOL, 'size': 1, 'operation': VariableOperation.READ},
    'IW2':{'datatype': VariableDatatype.WORD, 'size': 1, 'operation': VariableOperation.WRITE},
    'QW2':{'datatype': VariableDatatype.WORD, 'size': 1, 'operation': VariableOperation.READ},
    'IW10000':{'datatype': VariableDatatype.WORD, 'size': 1, 'operation': VariableOperation.WRITE},
    'QW10000':{'datatype': VariableDatatype.WORD, 'size': 1, 'operation': VariableOperation.READ},
    'IW4':{'datatype': VariableDatatype.INTEGER, 'size': 1, 'operation': VariableOperation.WRITE},
    'QW4':{'datatype': VariableDatatype.INTEGER, 'size': 1, 'operation': VariableOperation.READ},
    'ID10':{'datatype': VariableDatatype.DWORD, 'size': 1, 'operation': VariableOperation.WRITE},
    'QD10':{'datatype': VariableDatatype.DWORD, 'size': 1, 'operation': VariableOperation.READ},
    'ID14':{'datatype': VariableDatatype.INTEGER, 'size': 1, 'operation': VariableOperation.WRITE},
    'QD14':{'datatype': VariableDatatype.INTEGER, 'size': 1, 'operation': VariableOperation.READ},
    'ID18':{'datatype': VariableDatatype.FLOAT, 'size': 1, 'operation': VariableOperation.WRITE},
    'QD18':{'datatype': VariableDatatype.FLOAT, 'size': 1, 'operation': VariableOperation.READ},
    'DB12.DBB0':{'datatype': VariableDatatype.BYTE, 'size': 1, 'operation': VariableOperation.WRITE},
    'DB12.DBB1':{'datatype': VariableDatatype.BYTE, 'size': 1, 'operation': VariableOperation.READ},
    'DB12.DBX2.0':{'datatype': VariableDatatype.BOOL, 'size': 1, 'operation': VariableOperation.WRITE},
    'DB12.DBX2.1':{'datatype': VariableDatatype.BOOL, 'size': 1, 'operation': VariableOperation.READ},
    'DB12.DBW4':{'datatype': VariableDatatype.WORD, 'size': 1, 'operation': VariableOperation.WRITE},
    'DB12.DBW6':{'datatype': VariableDatatype.WORD, 'size': 1, 'operation': VariableOperation.READ},
    'DB12.DBW8':{'datatype': VariableDatatype.INTEGER, 'size': 1, 'operation': VariableOperation.WRITE},
    'DB12.DBW10':{'datatype': VariableDatatype.INTEGER, 'size': 1, 'operation': VariableOperation.READ},
    'DB12.DBD12':{'datatype': VariableDatatype.DWORD, 'size': 1, 'operation': VariableOperation.WRITE},
    'DB12.DBD14':{'datatype': VariableDatatype.DWORD, 'size': 1, 'operation': VariableOperation.READ},
    'DB12.DBD20':{'datatype': VariableDatatype.INTEGER, 'size': 1, 'operation': VariableOperation.WRITE},
    'DB12.DBD24':{'datatype': VariableDatatype.INTEGER, 'size': 1, 'operation': VariableOperation.READ},
    'DB12.DBD28':{'datatype': VariableDatatype.FLOAT, 'size': 1, 'operation': VariableOperation.WRITE},
    'DB12.DBD32':{'datatype': VariableDatatype.FLOAT, 'size': 1, 'operation': VariableOperation.READ},  
    }

d = plcsim(None, 'test')
d.ip = '192.168.1.250'
d.rack = 0
d.slot = 1
#d.mode = 'TIA'

if d.connect():
    d.addVariables(VARIABLES)

    counter = 0
    t = time.perf_counter()
    while time.perf_counter()-t < 10:

        res = d.readVariables(['DB12.DBB1', 'DB12.DBX2.1', 'DB12.DBW6', 'DB12.DBW10', 'DB12.DBD14', 'DB12.DBD24', 'DB12.DBD32', 'QB0','Q1.2','QW2','QW4','QD10','QD14','QD18', 'QW10000'])
        print(res[0], counter, end="\r")
        d.writeVariables([
            ('DB12.DBB0', counter%256),
            ('DB12.DBX2.0', counter%2),
            ('DB12.DBW4', counter),
            ('DB12.DBW8', counter-500),
            ('DB12.DBD12', counter+0xFFFF),
            ('DB12.DBD20', counter-40000),
            ('DB12.DBD28', counter/3),
            ('IB0', counter%256),
            ('I1.2', counter%2),
            ('IB0', counter%256),
            ('IW2', counter),
            ('IW4', counter-1000),
            ('ID10', counter+0xFFFF),
            ('ID14', counter-40000),
            ('ID18', counter/3),
            ('IW10000', counter),
            ])
        counter += 1

    d.disconnect()
