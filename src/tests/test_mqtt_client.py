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
TEST mqtt driver
------------------------

This test requires a running MQTT broker, in example Mosquitto.
Just execute the script to create the generic driver and test the diferent actions against another client launched as thread.
'''

import sys
from os import path
import time
import threading
import paho.mqtt.client as mqtt
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from drivers.mqtt_client.mqtt_client import mqtt_client
from drivers.driver import VariableOperation, VariableDatatype

""" Test client to respond the driver"""
def onMessage(client, userdata, message):
    value = str(message.payload.decode("utf-8"))
    print(f"{message.topic} = {value}")


def mqtt_response_client(ip, port):
    client = mqtt.Client("Test")
    client.on_message = onMessage
    client.connect(ip, port=port, keepalive=60)
    client.loop_start()

    counter = 0
    client.publish('outputs', counter)
    client.subscribe('inputs')

    while True:
        counter += 1
        client.publish('outputs', counter)
        time.sleep(1)
""" ------------------------------------"""

x = threading.Thread(target=mqtt_response_client, args=("127.0.0.1", 1883,))
x.start()

VARIABLES = {
    'inputs':{'datatype': VariableDatatype.BYTE, 'size': 1, 'operation': VariableOperation.WRITE},
    'outputs':{'datatype': VariableDatatype.BYTE, 'size': 1, 'operation': VariableOperation.READ},
    }

d = mqtt_client('test', None)
if d.connect():
    d.addVariables(VARIABLES)

    counter = 0
    while time.perf_counter() < 5:
        d.writeVariables([('inputs', counter)])
        print(d.readVariables(['outputs']))
        time.sleep(1)
        counter += 1

    d.disconnect()
