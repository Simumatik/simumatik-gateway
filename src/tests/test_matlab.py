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
TEST MATLAB driver
------------------------

This test requires MATLAB running in the same machine, also make sure that
the MATLAB session is shared by running 'matlab.engine.shareEngine' in MATLAB.
Just execute the script to create the driver and test the diferent actions.
'''

import sys
from os import path
import time
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from drivers.matlab.matlab import matlab
from drivers.driver import VariableOperation, VariableDatatype

VARIABLES = {
    'input_int':{'datatype': VariableDatatype.INTEGER, 'size': 1, 'operation': VariableOperation.WRITE},
    'output_int':{'datatype': VariableDatatype.INTEGER, 'size': 1, 'operation': VariableOperation.READ},
    'input_float_arr':{'datatype': VariableDatatype.FLOAT, 'size': 3, 'operation': VariableOperation.WRITE},
    'output_float_arr':{'datatype': VariableDatatype.FLOAT, 'size': 3, 'operation': VariableOperation.READ},
    }

d = matlab('test', None)
if d.connect():
    d.addVariables(VARIABLES)

    counter = 0
    while time.perf_counter() < 10:
        d.writeVariables([('input_int', counter),('input_float_arr',[counter/10, counter/100, counter/1000])])
        print(d.readVariables(['output_int', 'output_float_arr']))
        time.sleep(0.1)
        counter += 1

    d.disconnect()
