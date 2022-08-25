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

from multiprocessing import Pipe
import socket
import time
import json
from typing import Optional

from ..driver import VariableOperation, driver, VariableQuality, DriverStatus 


class matlab_udp(driver):
    """
    This driver is a generic driver to communicate using UDP.

    Parameters:
    ip: str
        IP address of the controller that want to connect to. Default = '127.0.0.1'
    
    port: int
        Port number for the socket connection. Default = 8400

    polling: int
        Polling interval in s to detect connection loss. Default = 1

    max_size: int
        Max telegram size (bytes). Default = 1024
    """

    def __init__(self, name: str, pipe: Optional[Pipe] = None, params:dict = None):
        """
        :param name: (optional) Name for the driver
        :param pipe: (optional) Pipe used to communicate with the driver thread. See gateway.py
        """
        # Inherit
        driver.__init__(self, name, pipe, params)

        # Parameters
        self.ip = '127.0.0.1'
        self.port = 8400
        self.polling = 1
        self.max_size = 1024
        self.has_received = False
        self.variables_to_send = {}


    def connect(self) -> bool:
        """ Connect driver.
        
        : returns: True if connection established False if not
        """
        try:   
            self.polling = int(self.polling)
            self.max_size = int(self.max_size)

            self._connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self._connection.settimeout(self.polling*2)

            sec_now = int(time.perf_counter())
            data = {"poll": sec_now}
            self._connection.sendto(json.dumps(data).encode('utf8'), (self.ip, int(self.port)))

            data, address = self._connection.recvfrom(self.max_size)
            if (data != None and address == (self.ip, int(self.port))):
                self.has_received = True
                self.variables_to_send.clear()
                self._connection.settimeout(0)
                self._last_recv_poll = sec_now
                return True

        except Exception as e:
            self.sendDebugInfo(f'Connection failed: {e}')
        
        return False


    def disconnect(self):
        """ Disconnect driver.
        """
        if self._connection:
            self._connection.close()


    def addVariables(self, variables: dict):
        """ Add variables to the driver. Correctly added variables will be added to internal dictionary 'variables'.
        Any error adding a variable should be communicated to the server using sendDebugInfo() method.

        : param variables: Variables to add in a dict following the setup format. (See documentation) 
        
        """
        self.variables.update(variables)
        for var_id in self.variables:
            self.variables[var_id]['value'] = self.defaultVariableValue(self.variables[var_id]['datatype'], self.variables[var_id]['size'])


    def readVariables(self, variables: list) -> list:
        """ Read given variable values. In case that the read is not possible or generates an error BAD quality should be returned.
        : param variables: List of variable ids to be read. 

        : returns: list of tupples including (var_id, var_value, VariableQuality)
        """
        _recv_data = {}
        try:
            while True:
                _data, address = self._connection.recvfrom(self.max_size)
                if (_data != None and address == (self.ip, int(self.port))):
                    _data = json.loads(_data.decode('utf-8'))
                    _recv_data.update(_data)
        except:
            pass

        if _recv_data != {}:
            self._last_recv_poll = int(time.perf_counter())
            self.has_received = True

        if (int(time.perf_counter()) - self._last_recv_poll) > (2 * self.polling):
            self.changeStatus(DriverStatus.ERROR)
            self.sendDebugInfo("No response for {} seconds".format(2 * self.polling))

        res = []
        for var_id in variables:
            if var_id in _recv_data:
                new_value = _recv_data.pop(var_id)
                new_value = self.getValueFromString(self.variables[var_id]['datatype'], new_value)
                if new_value is not None:
                    res.append((var_id, new_value, VariableQuality.GOOD)) 
                else:
                    res.append((var_id, new_value, VariableQuality.BAD)) 
            else:
                res.append((var_id, self.variables[var_id]['value'], VariableQuality.GOOD))
        return res


    def writeVariables(self, variables: list) -> list:
        """ Write given variable values. In case that the write is not possible or generates an error BAD quality should be returned.
        : param variables: List of tupples with variable ids and the values to be written (var_id, var_value). 

        : returns: list of tupples including (var_id, var_value, VariableQuality)
        """
        _send_data = {}
        res = []
        for (var_id, new_value) in variables:
            _send_data.update({var_id: new_value})

        if _send_data:
            try:
                self.variables_to_send.update(_send_data)
                for (var_id, new_value) in variables:
                    res.append((var_id, new_value, VariableQuality.GOOD))
            except:
                for (var_id, new_value) in variables:
                    res.append((var_id, new_value, VariableQuality.BAD))

        return res

    def loop(self):
        """ Runs every iteration while the driver is active."""
        if self.has_received and self._connection:
            self._connection.sendto(json.dumps(self.variables_to_send).encode('utf8'), (self.ip, int(self.port)))
            self.variables_to_send.clear()
            self.has_received = False
        
