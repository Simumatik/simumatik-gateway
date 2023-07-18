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

''' User manual

To test this driver you just need to get access to a Ethernet/IP master, which can be emulated by using for example Codesys.

## Test with Codesys

1. Create a project with Control Win V3 or the RPI equivalent.
2. Add an Ethernet (Ethernet) module from Ethernet/IP section as a new device.
3. Inside the Ethernet module, add an Ethernet_IP_Scanner module.
4. Inside the Ethernet_IP_Scanner module, add an Generic_Ethernet_IP_device.
5. Be aware that Codesys gateway is enabled and connected (double click on Control Win V3 device to verify).
6. Double click on the Ethernet module, and select the interface you are using, such as wifi or ethernet.
7. Double click on the Generic_Ethernet_IP_device, set the IP of the ENIP driver, set Strict Compatiblity Check, and uncheck every check in the general tab.
8. Still in the Generic_Ethernet_IP_device, choose the Connections tab and click add connections. 
9. In connection-path add '20 04 2C 66 2C 6C'. Set O->T and T->O bytes to '1'. Set Connection type in both cases to 'Point to point' and to 'Fixed'. In the left, set the data to '32 bits run/idle', and in the right to 'pure data'
10. Now you can compile, go online, and run the driver with the following config:


setup = {DriverActions.SETUP: {'parameters': {'driver_ip':'<IP_ADDRESS>', 'connection_path':'', 'read_size':1, 'write_size':1},
                                'data': {'input_data': {'datatype':'str', 'size':1, 'operation':'write'},
                                         'output_data': {'datatype':'str', 'size':1, 'operation':'read'}
                                        }
                              }
        }
'''

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
d.ip = "192.168.1.100"
d.read_size = 2
d.write_size = 2

if d.connect():
    d.addVariables(VARIABLES)

    counter = 0
    last_sec = int(time.perf_counter())
    while True: #time.perf_counter() < 100:
        d.loop()
        '''
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
        '''

    d.disconnect()
