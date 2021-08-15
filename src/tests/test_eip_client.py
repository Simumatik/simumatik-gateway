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

from drivers.eip_client.eip_client import eip_client
from drivers.driver import VariableOperation, VariableDatatype

VARIABLES = {
    'IB0':{'datatype': VariableDatatype.BYTE, 'size': 1, 'operation': VariableOperation.WRITE},
    'QB0':{'datatype': VariableDatatype.BYTE, 'size': 1, 'operation': VariableOperation.READ},
    }

# Create Driver
d = eip_client(None, 'test')
d.ip = "127.0.0.1"
d.rack = 1
d.slot = 1
if d.connect():
    # Register session
    res = d.registerSession()
    if res:
        # list services
        d.listServices()
        # Connect to PLC
        connection = d.ConnectToLogixPLC(path=(1,1)) #(Backplane port of 1756-ENET, CPU Slot)
        if connection:
            # Read Data
            cont = 0
            #while (time.clock() < 10.0):
            d.ReadPLCData(connection, 'rate')#['rate','ButtonClose'])
            cont += 1
            # Disconnect from PLC
            d.DisconnectFromLogixPLC(connection)
        # Unregister Session
        d.unregisterSession()
# Close session
d.close()