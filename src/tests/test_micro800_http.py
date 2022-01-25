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

from drivers.micro800_http.micro800_http import micro800_http
from drivers.driver import VariableOperation, VariableDatatype

VARIABLES = {
    '_IO_EM_DI_00':{'datatype': VariableDatatype.BOOL, 'size': 1, 'operation': VariableOperation.WRITE},
    '_IO_EM_DO_00':{'datatype': VariableDatatype.BOOL, 'size': 1, 'operation': VariableOperation.READ},
    }

d = micro800_http(None, 'test')
d.port = '65173'

if d.connect():
    d.addVariables(VARIABLES)

    value = False
    while time.perf_counter() < 5:
        d.writeVariables([('_IO_EM_DI_00', value)])
        print(d.readVariables(['_IO_EM_DO_00']))
        time.sleep(0.1)
        value = not value

    d.disconnect()
