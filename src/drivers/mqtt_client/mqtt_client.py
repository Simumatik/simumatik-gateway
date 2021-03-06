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

import paho.mqtt.client as mqtt
from multiprocessing import Pipe
from typing import Optional

from ..driver import driver, VariableOperation, VariableQuality


class mqtt_client(driver):
    '''
    This driver is a client to communicate using MQTT.

    Parameters:
    ip: str
        MQTT Broker IP adress . Default = '127.0.0.1'
    
    port: int
        MQTT Broker port. Default = 1883

    retain: bool
        Retain published topics by the driver in the MQTT Broker. Default = True
    '''

    def __init__(self, name: str, pipe: Optional[Pipe] = None):
        """
        :param name: (optional) Name for the driver
        :param pipe: (optional) Pipe used to communicate with the driver thread. See gateway.py
        """
        # Inherit
        driver.__init__(self, name, pipe)

        # Parameters
        self.ip = '127.0.0.1'
        self.port = 1883
        self.retain = True

        # Interal vars
        self.new_values = {}


    def connect(self) -> bool:
        """ Connect driver.
        
        : returns: True if connection stablished False if not
        """
        try:
            self.port = int(self.port)

            self._connection = mqtt.Client(self._name, clean_session=not self.retain)
            self._connection.on_message = self.onMessage
            #self._connection.on_log = self.onLog
            self._connection.connect(self.ip, port=int(self.port), keepalive=60)
            self._connection.loop_start()

        except Exception as e:
            self.sendDebugInfo(f"SETUP: Connection with {self.ip}:{self.port} cannot be stablished.")
            return False
        
        return True


    def disconnect(self):
        """ Disconnect driver.
        """
        if self._connection:
            self._connection.loop_stop()
            self._connection.disconnect()


    def addVariables(self, variables: dict):
        """ Add variables to the driver. Correctly added variables will be added to internal dictionary 'variables'.
        Any error adding a variable should be communicated to the server using sendDebugInfo() method.

        : param variables: Variables to add in a dict following the setup format. (See documentation) 
        
        """
        for var_id, var_data in variables.items():
            try:
                var_data['value'] = self.defaultVariableValue(var_data['datatype'], var_data['size'])
                if var_data['operation'] == VariableOperation.WRITE:
                    self._connection.publish(var_id, var_data['value'], retain=self.retain)
                if var_data['operation'] == VariableOperation.READ:
                    self._connection.subscribe(var_id)
                self.variables[var_id] = var_data
            except:
                self.sendDebugVarInfo(('SETUP: Variable NOT found {}'.format(var_id), var_id))


    def readVariables(self, variables: list) -> list:
        """ Read given variable values. In case that the read is not possible or generates an error BAD quality should be returned.
        : param variables: List of variable ids to be read. 

        : returns: list of tupples including (var_id, var_value, VariableQuality)
        """
        res = []
        for var_id in variables:
            if var_id in self.new_values:
                res.append((var_id, self.new_values[var_id], VariableQuality.GOOD))
            else:
                res.append((var_id, None, VariableQuality.BAD))
        return res


    def writeVariables(self, variables: list) -> list:
        """ Write given variable values. In case that the write is not possible or generates an error BAD quality should be returned.
        : param variables: List of tupples with variable ids and the values to be written (var_id, var_value). 

        : returns: list of tupples including (var_id, var_value, VariableQuality)
        """
        res = []
        # TODO: Possible improvement can be to send multiple at once
        for (var_id, new_value) in variables:
            try:
                self._connection.publish(var_id, new_value)
                res.append((var_id, new_value, VariableQuality.GOOD))
            except:
                res.append((var_id, new_value, VariableQuality.BAD))
                     
        return res


    def onLog(self, client, userdata, level, buf):
        """ This method is useful for testing."""
        self.sendDebugInfo(f'LOG: {buf}')


    def onMessage(self, client, userdata, message):
        var_id = message.topic
        if var_id in self.variables:
            self.new_values[var_id] = self.getValueFromString(self.variables[var_id]['datatype'], str(message.payload.decode("utf-8")))
