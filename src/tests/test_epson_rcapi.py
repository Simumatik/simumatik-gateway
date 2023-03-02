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
TEST ABB RobotWare driver
------------------------

This test requires ABB RobotStudio running in the same machine, including a robot and both signals "inputs" and "outputs".
Just execute the script to create the driver and test the diferent actions.
'''

import sys
from os import path
import time
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from drivers.epson_rcapi.epson_rcapi import epson_rcapi
from drivers.driver import VariableOperation, VariableDatatype

VARIABLES = {
    'Axis':{'datatype': VariableDatatype.FLOAT, 'size': 6, 'operation': VariableOperation.READ},
    'inputs':{'datatype': VariableDatatype.BYTE, 'size': 1, 'operation': VariableOperation.WRITE},
    'outputs':{'datatype': VariableDatatype.BYTE, 'size': 1, 'operation': VariableOperation.READ},
    }

d = epson_rcapi('test', None)
d.connection_name = 'C4 Sample'
if d.connect():
    '''
    d.addVariables(VARIABLES)
    
    counter = 0
    '''
    while time.perf_counter() < 10:
        res = d._connection.Agl(1)
        '''
        d.writeVariables([('inputs', counter)])
        print(d.readVariables(['Axis', 'outputs']))
        '''
        time.sleep(0.1)
    
    d.disconnect()
