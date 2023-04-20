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

from drivers.plcsim_advanced.plcsim_advanced import plcsim_advanced
from drivers.driver import VariableOperation, VariableDatatype

# Define your I/O variables here
VARIABLES = {
    'ByteIn':{'datatype': VariableDatatype.BYTE, 'size': 1, 'operation': VariableOperation.WRITE},
    'ByteOut':{'datatype': VariableDatatype.BYTE, 'size': 1, 'operation': VariableOperation.READ},
    'BoolIn':{'datatype': VariableDatatype.BOOL, 'size': 1, 'operation': VariableOperation.WRITE},
    'BoolOut':{'datatype': VariableDatatype.BOOL, 'size': 1, 'operation': VariableOperation.READ},
    'WordIn':{'datatype': VariableDatatype.WORD, 'size': 1, 'operation': VariableOperation.WRITE},
    'WordOut':{'datatype': VariableDatatype.WORD, 'size': 1, 'operation': VariableOperation.READ},
    'WordInHighAdress':{'datatype': VariableDatatype.WORD, 'size': 1, 'operation': VariableOperation.WRITE},
    'WordOutHighAdress':{'datatype': VariableDatatype.WORD, 'size': 1, 'operation': VariableOperation.READ},
    'IntIn':{'datatype': VariableDatatype.INTEGER, 'size': 1, 'operation': VariableOperation.WRITE},
    'IntOut':{'datatype': VariableDatatype.INTEGER, 'size': 1, 'operation': VariableOperation.READ},
    'DWordIN':{'datatype': VariableDatatype.DWORD, 'size': 1, 'operation': VariableOperation.WRITE},
    'DWordOut':{'datatype': VariableDatatype.DWORD, 'size': 1, 'operation': VariableOperation.READ},
    'DIntIn':{'datatype': VariableDatatype.INTEGER, 'size': 1, 'operation': VariableOperation.WRITE},
    'DIntOut':{'datatype': VariableDatatype.INTEGER, 'size': 1, 'operation': VariableOperation.READ},
    'RealIn':{'datatype': VariableDatatype.FLOAT, 'size': 1, 'operation': VariableOperation.WRITE},
    'RealOut':{'datatype': VariableDatatype.FLOAT, 'size': 1, 'operation': VariableOperation.READ},
    }


# Add your custom logic in this test.
d = plcsim_advanced(None, 'test')
d.instanceName = "drivertest"
print("Connecting to PLC sim advanced")
if d.connect():
    d.addVariables(VARIABLES)

    #quit()

    counter = 0
    t = time.perf_counter()
    while time.perf_counter()-t < 5:
        res = d.readVariables(['ByteOut', 'BoolOut', 'WordOut', 'WordOutHighAdress', 'IntOut', 'RealOut'])
        #print(res, counter)
        d.writeVariables([
            ('BoolIn', counter%2),
            ('ByteIn', counter%256),
            ('WordIn', counter),
            ('WordInHighAdress', counter),
            ('IntIn', counter-500),
            ('RealIn', counter/3),
            ])
        counter += 1
    print(counter)
    d.disconnect()