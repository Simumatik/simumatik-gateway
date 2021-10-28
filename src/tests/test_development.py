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

from drivers.development.development import development
from drivers.driver import VariableOperation, VariableDatatype

# Define your I/O variables here
VARIABLES = {
    'GVL.Digital_In1':{'datatype': VariableDatatype.BOOL, 'size': 1, 'operation': VariableOperation.WRITE},
    'GVL.Digital_Out1':{'datatype': VariableDatatype.BOOL, 'size': 1, 'operation': VariableOperation.READ},
    }

# Add your custom logic in this test.
d = development(None, 'test')
d.net_id = "192.168.1.160.1.1"
d.port = 851

if d.connect():
    d.addVariables(VARIABLES)

    counter = 0
    while time.perf_counter() < 5:
        d.writeVariables([('GVL.Digital_In1', counter%2)])
        print(d.readVariables(['GVL.Digital_Out1']))
        time.sleep(0.1)
        counter += 1

    d.disconnect()
