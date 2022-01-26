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
import threading
import socket
import numpy as np

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from drivers.hokuyo_uam.hokuyo_uam import hokuyo_uam
from drivers.driver import VariableOperation, VariableDatatype

""" Test client to communicate with driver"""
def client(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (ip, port)

    print(f'Client starting, connecting to {server_address}')
    sock.connect(server_address)
    print(f'Connected to {server_address}')

    while True:
        message = b'\x02000EAR01B19B\x03'
        sock.send(message)
        # Wait for response
        try:
            t1 = time.perf_counter()
            response = sock.recv(9000)
            resp_time = round((time.perf_counter() - t1)*1000)
            print(f'Client received {len(response)} bytes of data after {resp_time} ms')
        except Exception as e:
            print(e)
            sock.close()
            print('Client disconnected')
            break
""" ------------------------------------"""

_client = threading.Thread(target=client, args=("127.0.0.1", 10940))
_client.start()

VARIABLES = {
    '0_134': {'datatype': VariableDatatype.INTEGER, 'size': 135, 'operation': VariableOperation.WRITE},
    '135_269': {'datatype': VariableDatatype.INTEGER, 'size': 135, 'operation': VariableOperation.WRITE},
    '270_404': {'datatype': VariableDatatype.INTEGER, 'size': 135, 'operation': VariableOperation.WRITE},
    '405_539': {'datatype': VariableDatatype.INTEGER, 'size': 135, 'operation': VariableOperation.WRITE},
    '540_674': {'datatype': VariableDatatype.INTEGER, 'size': 135, 'operation': VariableOperation.WRITE},
    '675_809': {'datatype': VariableDatatype.INTEGER, 'size': 135, 'operation': VariableOperation.WRITE},
    '810_944': {'datatype': VariableDatatype.INTEGER, 'size': 135, 'operation': VariableOperation.WRITE},
    '945_1080': {'datatype': VariableDatatype.INTEGER, 'size': 136, 'operation': VariableOperation.WRITE},
    }


# Curve that the points will follow during test
def f(t):
    y = [0] * 1081
    for x in range(1081):
        y[x] = np.sin(t*2 - x/40)*1000+1500
        y[x] = int(y[x])
    return y


d = hokuyo_uam(None, 'test')
if d.connect():
    d.addVariables(VARIABLES)

    start_time = time.perf_counter()
    last_update = 0
    while True:
        now = time.perf_counter()
        if now - start_time > 5:
            break

        # Simulate running the loop
        d.loop()
        # Update sensor readings every 100 ms
        if now - last_update > 0.1:
            points = f(now - start_time)
            # Write the new points separated into 8 variables
            updated_vars = []
            for var_id in VARIABLES:
                [first, last] = map(int, var_id.split('_'))
                updated_vars.append((var_id, points[first:last+1]))
            d.writeVariables(updated_vars)
            last_update = now
        
        time.sleep(1e-3)

    d.disconnect()