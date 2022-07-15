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

from drivers.modbustcp_master.modbustcp_master import modbustcp_master
from drivers.driver import VariableOperation, VariableDatatype

VARIABLES = {
    '1':{'datatype': VariableDatatype.BOOL, 'size': 1, 'operation': VariableOperation.WRITE},
    '201':{'datatype': VariableDatatype.BOOL, 'size': 1, 'operation': VariableOperation.WRITE},
    '10001':{'datatype': VariableDatatype.BOOL, 'size': 1, 'operation': VariableOperation.READ},
    '10301':{'datatype': VariableDatatype.BOOL, 'size': 1, 'operation': VariableOperation.READ},
    '30001':{'datatype': VariableDatatype.WORD, 'size': 1, 'operation': VariableOperation.READ},
    '30031':{'datatype': VariableDatatype.WORD, 'size': 1, 'operation': VariableOperation.READ},
    '40001':{'datatype': VariableDatatype.WORD, 'size': 1, 'operation': VariableOperation.WRITE},
    '40041':{'datatype': VariableDatatype.WORD, 'size': 1, 'operation': VariableOperation.WRITE},
    }

d = modbustcp_master(None, 'test')
d.host = 'localhost'
d.port = 502

if d.connect():
    res = d.addVariables(VARIABLES)
    print(d.variables)

    counter = 0
    start = time.perf_counter()
    while time.perf_counter()-start < 5:
        d.writeVariables([('1', counter%2), ('40001', counter)])
        print(d.readVariables(['10001', '30001']))
        #time.sleep(0.1)
        counter += 1

    d.disconnect()
