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

"""
TEST opcua_client driver
------------------------

This test requires a running opcua server in the given url (opc.tcp://localhost:4840), including both tags (MotorOn and SensorActive).
Just execute the script to create the generic driver and test the diferent actions.

To test this driver you just need to get access to a opcua server. If you do not have one, you can try using some online servers.

__NOTE! It is important that the server has no security configuration so the access is open.__

## Test with Codesys

The driver is able to read any variable and and write just on writeable vartiables inside the Objects->DeviceSet node. 

1. Create a project for a OPCUA compatible CPU (Control Win V3 is fine) and add a Global Variable List (GVL).
2. Add the variables you want to read or write to the GVL.
3. Right click on the GVL object and open the properties. Check Build->Link Always option.
4. Add a Symbol Configuration object to the project and check the 'Support OPC UA Features' option.
5. Build it and check the variables from the GVL you want to share through OPCUA.
6. Login to the controller and download the project.
7. Variables are now accesible for any OPCUA client.

If using Control Win V3, configure the 'url' parameter as 'opc.tcp://localhost:4840' and set the variable names as addresses, i.e:

```
    setup_data = {'parameters': {'url':"opc.tcp://localhost:4840", 'rpi':10},
                  'variables': {'MotorOn': {'datatype':'bool', 'size':1, 'operation':'read'},
                                'SensorActive': {'datatype':'bool', 'size':1, 'operation':'write'}}
                 }
```
"""

import sys
from os import path
import time
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from drivers.opcua_client.opcua_client import opcua_client
from drivers.driver import VariableOperation, VariableDatatype

VARIABLES = {
    'inputs':{'datatype': VariableDatatype.BYTE, 'size': 1, 'operation': VariableOperation.WRITE},
    'outputs':{'datatype': VariableDatatype.BYTE, 'size': 1, 'operation': VariableOperation.READ},
    }

d = opcua_client(None, 'test')
if d.connect():
    d.addVariables(VARIABLES)

    counter = 0
    while time.perf_counter() < 5:
        d.writeVariables([('inputs', counter)])
        print(d.readVariables(['outputs']))
        time.sleep(0.1)
        counter += 1

    d.disconnect()
