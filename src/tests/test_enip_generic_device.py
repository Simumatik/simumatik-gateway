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

from drivers.enip_generic_device.enip_generic_device import enip_generic_device
from drivers.driver import VariableOperation, VariableDatatype

# Define your I/O variables here
VARIABLES = {
    'IB0':{'datatype': VariableDatatype.BYTE, 'size': 1, 'operation': VariableOperation.WRITE},
    'IB1':{'datatype': VariableDatatype.BYTE, 'size': 1, 'operation': VariableOperation.WRITE},
    'IW1':{'datatype': VariableDatatype.WORD, 'size': 1, 'operation': VariableOperation.WRITE},
    'ID1':{'datatype': VariableDatatype.DWORD, 'size': 1, 'operation': VariableOperation.WRITE},
    'ID2':{'datatype': VariableDatatype.FLOAT, 'size': 1, 'operation': VariableOperation.WRITE},
    'QB0':{'datatype': VariableDatatype.BYTE, 'size': 1, 'operation': VariableOperation.READ},
    'QB1':{'datatype': VariableDatatype.BYTE, 'size': 1, 'operation': VariableOperation.READ},
    'QW1':{'datatype': VariableDatatype.WORD, 'size': 1, 'operation': VariableOperation.READ},
    'QD1':{'datatype': VariableDatatype.DWORD, 'size': 1, 'operation': VariableOperation.READ},
    'QD2':{'datatype': VariableDatatype.FLOAT, 'size': 1, 'operation': VariableOperation.READ},
    }

# Add your custom logic in this test.
d = enip_generic_device(None, 'test')
d.ip = "192.168.0.250"
d.read_size = 12
d.write_size = 12

if d.connect():
    d.addVariables(VARIABLES)

    counter = 0
    last_sec = int(time.perf_counter())
    while True: #time.perf_counter() < 100:
        d.loop()
        d.writeVariables([
            ('IB0', counter % 256),
            ('IB1', (counter+1) % 256),
            ('IW1', counter),
            ('ID1', counter),
            ('ID2', counter/3-100),
            ])
        res = d.readVariables(['QB0','QB1','QW1','QD1','QD2'])
        print(res)
        if int(time.perf_counter())!=last_sec:
            counter += 1 
            last_sec = int(time.perf_counter())

    d.disconnect()
