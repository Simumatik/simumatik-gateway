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

import roslibpy
import json
import multiprocessing

from ..driver import driver, VariableOperation, VariableQuality

class rosbridge(driver):
    '''
    This driver uses the rosbridge_suite with the python client (roslibpy) 
    to allow topic publishing and subscribing in a running ROS device.
    http://wiki.ros.org/rosbridge_suite
    https://github.com/gramaziokohler/roslibpy

    Parameters:
    host: str
        ROS host name. Default = 'localhost'
    
    port: int
        Port assigned to ros_bridge. Default = 9090

    '''

    def __init__(self, name: str, pipe: multiprocessing.Pipe = None, params:dict = None):
        """
        :param name: (optional) Name for the driver
        :param pipe: (optional) Pipe used to communicate with the driver thread. See gateway.py
        """
        # Inherit
        driver.__init__(self, name, pipe, params)

        # Parameters
        self.host = 'localhost'
        self.port = 9090
        self.request_telegram_var = 'ros_message_request'
        self.response_telegram_var = 'ros_message_response'

        # Interal vars
        self.new_values = {}
        self.telegram_topics = {}
        self.pending_telegram_response = {}


    def connect(self) -> bool:
        """ Connect driver.
        
        : returns: True if connection established False if not
        """
        try:
            self.port = int(self.port)

            self._connection = roslibpy.Ros(self.host , self.port)
            self._connection.run()

        except Exception as e:
            self.sendDebugInfo(f"Connection with {self.host}:{self.port} cannot be established.")
            return False
        
        return True


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
        for var_id, var_data in variables.items():
            try:
                # For telegram variables, skip adding the ros topic publisher/subscriber
                if var_id in [self.request_telegram_var, self.response_telegram_var]:
                    var_data['value'] = None
                    self.variables[var_id] = var_data
                    continue

                # For specific message type and field, it's indicated in the datatype.
                # The use of '/' is compulsory to avoid mistakes.
                if '/' in var_data['datatype']:
                    message_type = var_data['datatype']
                    message_field = var_data['field']
                else:
                    # Get the correct message type from simumatik type
                    message_type = self.message_type_convertion(var_data['datatype'],var_data['size'])
                    # Use 'data' as the value field for all std_msgs
                    message_field = 'data'

                var_data['value'] = self.defaultVariableValue(var_data['datatype'], var_data['size'])
                self.new_values[var_id] = var_data['value']

                if var_data['operation'] == VariableOperation.WRITE:
                    var_data['publisher'] = roslibpy.Topic(self._connection, var_id, message_type)
                if var_data['operation'] == VariableOperation.READ:
                    # Create a subscriber for the variable
                    var_data['subscriber'] = roslibpy.Topic(self._connection, var_id, message_type)
                    # Define callback function with fixed name and field
                    callback_lambda = lambda message, name = var_id, field = message_field : self.callback(message, name, field)
                    # Subscribe using the callback function
                    var_data['subscriber'].subscribe(callback_lambda)

                if var_id in self.variables:
                    if self.variables[var_id]['operation'] != var_data['operation']:
                        var_data['operation'] = VariableOperation.BOTH

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
            if var_id == self.response_telegram_var:
                res.append((var_id, json.dumps(self.pending_telegram_response), VariableQuality.GOOD))
                self.pending_telegram_response = {}
            elif var_id in self.new_values:
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
        for (var_id, new_value) in variables:
            try:
                if var_id == self.request_telegram_var:
                    if new_value:
                        self.supervise_request_telegram(new_value)
                elif '/' in self.variables[var_id]['datatype']:
                    self.variables[var_id]['publisher'].publish(roslibpy.Message({self.variables[var_id]['field'] : new_value}))
                else:
                    self.variables[var_id]['publisher'].publish(roslibpy.Message({'data' : new_value}))

                res.append((var_id, new_value, VariableQuality.GOOD))
            except Exception as e:
                print(e)
                res.append((var_id, new_value, VariableQuality.BAD))
                     
        return res


    def callback(self, msg, var_id, field):
        # Callback function called when the subscriber recieves a message
        # If the datatype is float, round.
        if  isinstance(msg[field], float):
            value = round(msg[field], 3)
        elif isinstance(msg[field], list) and isinstance(msg[field][0], float):
            value = [round(x,3) for x in msg[field]]
        else:
            value = msg[field]
        
        if self.variables[var_id]['value'] != value:
            self.new_values[var_id] = value


    def message_type_convertion(self, type_name, size):
        # Function used to extract the message type from simumatik types.

        # There is a distinction depending on the size
        if size == 1:
            switcher = {
                'bool'  : 'std_msgs/Bool',
                'byte'  : 'std_msgs/Byte',
                'int'   : 'std_msgs/Int32', # Can be changed to Int64
                'word'  : 'std_msgs/UInt16',
                'dword' : 'std_msgs/UInt32',
                'qword' : 'std_msgs/UInt64',
                'float' : 'std_msgs/Float32', # Can be changed to Float64
                'str'   : 'std_msgs/String',
                'string': 'std_msgs/String'
            }

            return switcher.get(type_name, "Invalid type")

        else:
            switcher = {
                # Bool of size different than 1 is not valid
                'byte'  : 'std_msgs/ByteMultiArray',
                'int'   : 'std_msgs/Int32MultiArray', # Can be changed to Int64
                'word'  : 'std_msgs/UInt16MultiArray',
                'dword' : 'std_msgs/UInt32MultiArray',
                'qword' : 'std_msgs/UInt64MultiArray',
                'float' : 'std_msgs/Float32MultiArray', # Can be changed to Float64
                # String of size different than 1 is not valid
            }
            
            return switcher.get(type_name, "Invalid type")
    

    def supervise_request_telegram(self, telegram_data):
        topic_updates = json.loads(telegram_data)
        for topic, data in topic_updates.items():
            if not topic in self.telegram_topics:
                self.telegram_topics[topic] = {}
                self.telegram_topics[topic]['msg'] = data['msg']
                self.telegram_topics[topic]['payload'] = {}
                self.telegram_topics[topic]['ros_topic'] = roslibpy.Topic(self._connection, topic, data['msg'])

            if 'subscribe' in data:
                if data['subscribe'] == True:
                    callback_lambda = lambda message, topic = topic : self.telegram_subscriber_callback(message, topic)
                    self.telegram_topics[topic]['ros_topic'].subscribe(callback_lambda)
                else:
                    ... # Remove subscriber (if there is one)

            self.telegram_topics[topic]['id'] = data.get('id', 0)
            if 'payload' in data:
                # Update stored topic values
                self.telegram_topics[topic]['payload'].update(data['payload'])
                # Publish new data
                msg = self.telegram_topics[topic]['payload']
                self.telegram_topics[topic]['ros_topic'].publish(roslibpy.Message(msg))

    def telegram_subscriber_callback(self, message, topic):
        self.telegram_topics[topic]['payload'].update(message)
        self.pending_telegram_response[topic] = {}
        self.pending_telegram_response[topic]['payload'] = self.telegram_topics[topic]['payload']
        self.pending_telegram_response[topic]['id'] = self.telegram_topics[topic]['id'] + 1
