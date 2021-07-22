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
TEST Simulink driver
------------------------

This test requires MATLAB running in the same machine, also make sure that
the MATLAB session is shared by running 'matlab.engine.shareEngine' in MATLAB.
Just execute the script to create the driver and test the different actions.
'''

import sys
from os import path
import time
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from drivers.simulink.simulink import simulink
from drivers.driver import VariableOperation, VariableDatatype

port_number = 1

VARIABLES = {
    port_number:{'datatype': VariableDatatype.FLOAT, 'size': 1, 'operation': VariableOperation.READ},
    }

d = simulink('test', None)
d.autorun_simulink = True
d.simulink_block = "simulink_test1/Test_Block"
if d.connect():
    d.addVariables(VARIABLES)

    counter = 0
    while time.perf_counter() < 10:
        # TODO: Figure out how to write to input ports..
        # The commented line below gives an error
        # d.writeVariables([('1', counter)])
        print(d.readVariables([port_number]))
        time.sleep(0.1)
        counter += 1

    d.disconnect()
