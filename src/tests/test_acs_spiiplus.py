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

from drivers.acs_spiiplus.acs_spiiplus import acs_spiiplus
from drivers.driver import VariableOperation, VariableDatatype

VARIABLES = {
    'I0':{'datatype': VariableDatatype.INTEGER, 'size': 1, 'operation': VariableOperation.WRITE},
    'I1':{'datatype': VariableDatatype.INTEGER, 'size': 1, 'operation': VariableOperation.READ},
    'V0':{'datatype': VariableDatatype.FLOAT, 'size': 1, 'operation': VariableOperation.WRITE},
    'V1':{'datatype': VariableDatatype.FLOAT, 'size': 1, 'operation': VariableOperation.READ},
    }

d = acs_spiiplus(None, 'test')
d.ip = '192.168.240.1'
d.comm = 'simulator'

if d.connect():
    d.addVariables(VARIABLES)

    counter = 0
    t = time.perf_counter()
    while time.perf_counter()-t < 10:

        print(d.readVariables(['I1','V1']), counter)
        d.writeVariables([('I0', counter),('V0', counter/9)])
        counter += 1

    d.disconnect()
