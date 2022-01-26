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

from drivers.simit.simit import simit
from drivers.driver import VariableOperation, VariableDatatype

# Define your I/O variables here
VARIABLES = {
    'MW4':{'datatype': VariableDatatype.WORD, 'size': 1, 'operation': VariableOperation.WRITE},
    'MW0':{'datatype': VariableDatatype.WORD, 'size': 1, 'operation': VariableOperation.READ},
    }

# Add your custom logic in this test.
d = simit(None, 'test')
d.SHM_name = "SIMITShared Memory"
d.big_endian = False

if d.connect():
    d.addVariables(VARIABLES)

    counter = 0
    while counter < 5:
        d.writeVariables([('MW4', counter)])

        time.sleep(1)

        print(d.readVariables(['MW0']))

        counter += 1

    d.disconnect()
