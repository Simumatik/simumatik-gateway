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

''' 
TEST RoboDK COM driver
------------------------

This test requires RoboDK running in the same machine, including a robot and both Station Parameters "inputs" and "outputs".
You can use the file called 'robodk_test_project.py' including all previous setup and run the program in a loop.
Just execute the script to create the driver and test the diferent actions.
'''

import sys
from os import path
import time
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from drivers.robodk_api.robodk_api import robodk_api
from drivers.driver import VariableOperation, VariableDatatype

VARIABLES = {
    'Axis':{'datatype': VariableDatatype.FLOAT, 'size': 6, 'operation': VariableOperation.READ},
    'inputs':{'datatype': VariableDatatype.BYTE, 'size': 1, 'operation': VariableOperation.WRITE},
    'outputs':{'datatype': VariableDatatype.BYTE, 'size': 1, 'operation': VariableOperation.READ},
    }

d = robodk_api('test', None)
d.controller = "robot"
if d.connect():
    d.addVariables(VARIABLES)

    counter = 0
    while time.perf_counter() < 5:
        d.writeVariables([('inputs', counter)])
        print(d.readVariables(['Axis', 'outputs']))
        time.sleep(0.1)
        counter += 1

    d.disconnect()
