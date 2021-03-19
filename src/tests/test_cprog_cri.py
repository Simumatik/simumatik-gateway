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

from drivers.cprog_cri.cprog_cri import cprog_cri
from drivers.driver import VariableOperation, VariableDatatype, VariableQuality

# Define your I/O variables here
VARIABLES = {
    'Axis':{'datatype': VariableDatatype.FLOAT, 'size': 6, 'operation': VariableOperation.READ},
    'DOUT':{'datatype': VariableDatatype.BYTE, 'size': 1, 'operation': VariableOperation.READ},
    'GSIG':{'datatype': VariableDatatype.BYTE, 'size': 1, 'operation': VariableOperation.WRITE},
    'GRIPPERSTATE':{'datatype': VariableDatatype.FLOAT, 'size': 1, 'operation': VariableOperation.READ},
    }

# Add your custom logic in this test.
d = cprog_cri(None, 'test')
#d.ip = '192.168.0.233'
if d.connect():
    d.addVariables(VARIABLES)

    signal = 0
    old_signal = None
    last = int(time.perf_counter())
    while True:

        if signal != old_signal:
            res = d.writeVariables([('GSIG', signal)])
            for (var_id, write_value, quality) in res:
                if quality == VariableQuality.GOOD:
                    d.variables[var_id]['value'] = write_value
            old_signal = signal 

  
        res = d.readVariables(['Axis', 'DOUT', 'GRIPPERSTATE'])
        for (var_id, read_value, quality) in res:
            if quality == VariableQuality.GOOD:
                d.variables[var_id]['value'] = read_value
                if var_id == 'DOUT':
                    signal = read_value
                elif var_id == 'Axis':
                    print('Axis', read_value)
        
        time.sleep(d.rpi*1e-3)

    d.disconnect()
