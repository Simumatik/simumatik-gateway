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

from drivers.twincat_ads.twincat_ads import twincat_ads
from drivers.driver import VariableOperation, VariableDatatype

# Define your I/O variables here
VARIABLES = {
    'GVL.ByteIn':{'datatype': VariableDatatype.BYTE, 'size': 1, 'operation': VariableOperation.WRITE},
    'GVL.ByteOut':{'datatype': VariableDatatype.BYTE, 'size': 1, 'operation': VariableOperation.READ},
    'GVL.BoolIn':{'datatype': VariableDatatype.BOOL, 'size': 1, 'operation': VariableOperation.WRITE},
    'GVL.BoolOut':{'datatype': VariableDatatype.BOOL, 'size': 1, 'operation': VariableOperation.READ},
    'GVL.WordIn':{'datatype': VariableDatatype.WORD, 'size': 1, 'operation': VariableOperation.WRITE},
    'GVL.WordOut':{'datatype': VariableDatatype.WORD, 'size': 1, 'operation': VariableOperation.READ},
    'GVL.IntIn':{'datatype': VariableDatatype.INTEGER, 'size': 1, 'operation': VariableOperation.WRITE},
    'GVL.IntOut':{'datatype': VariableDatatype.INTEGER, 'size': 1, 'operation': VariableOperation.READ},
    'GVL.DWordIn':{'datatype': VariableDatatype.DWORD, 'size': 1, 'operation': VariableOperation.WRITE},
    'GVL.DWordOut':{'datatype': VariableDatatype.DWORD, 'size': 1, 'operation': VariableOperation.READ},
    'GVL.DIntIn':{'datatype': VariableDatatype.INTEGER, 'size': 1, 'operation': VariableOperation.WRITE},
    'GVL.DIntOut':{'datatype': VariableDatatype.INTEGER, 'size': 1, 'operation': VariableOperation.READ},
    'GVL.RealIn':{'datatype': VariableDatatype.FLOAT, 'size': 1, 'operation': VariableOperation.WRITE},
    'GVL.RealOut':{'datatype': VariableDatatype.FLOAT, 'size': 1, 'operation': VariableOperation.READ},
}

# Add your custom logic in this test.
d = twincat_ads(None, 'test')
d.net_id = "192.168.1.125.1.1"
d.port = 851

if d.connect():
    print("Connected")
    d.addVariables(VARIABLES)

    counter = 0
    while counter < 5:
        d.writeVariables([('GVL.ByteIn', counter)])
        d.writeVariables([('GVL.BoolIn', counter%2)])
        d.writeVariables([('GVL.WordIn', counter)])
        d.writeVariables([('GVL.IntIn', -counter)])
        d.writeVariables([('GVL.DWordIn', counter)])
        d.writeVariables([('GVL.DIntIn', -16*counter)])
        d.writeVariables([('GVL.RealIn', 3.1415*counter)])

        time.sleep(1)

        print(d.readVariables(['GVL.ByteOut']))
        print(d.readVariables(['GVL.BoolOut']))
        print(d.readVariables(['GVL.WordOut']))
        print(d.readVariables(['GVL.IntOut']))
        print(d.readVariables(['GVL.DWordOut']))
        print(d.readVariables(['GVL.DIntOut']))
        print(d.readVariables(['GVL.RealOut']))

        counter += 1

    d.disconnect()
