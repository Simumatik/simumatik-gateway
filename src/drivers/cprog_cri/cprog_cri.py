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

import socket
import time
from multiprocessing import Pipe
from typing import Optional

from ..driver import VariableDatatype, driver, VariableQuality


class cprog_cri(driver):
    '''
    This driver implements the CRI Interface communication protocol for COMMONPLACE ROBOTICS GmbH CPRog software
    Has been tested with version V902-11-024, 2/4/2021
    IMPORTANT: It requires activating CRI Interface:
      - In CPRog open a robot project
      - Go to File->Configure Interfaces
      - Select "CRI Interface".
      - If you want to use default 'ip' parameter value check "Force IP address".
      - Click on Start. Now you can go back to the editor.
    
    REFERENCE: https://cpr-robots.com/download/CRI/CPR_RobotInterfaceCRI.pdf
    
    The driver will always provide access to the next variables:
    - "Axis" (float[1..16]): robot joint positions in degrees.
    - "DIN" (byte,word,dword,qword): robot digital inputs. WARNING! Not supported yet
    - "DOUT" (byte,word,dword,qword): robot digital outputs.
    - "GSIG" (byte,word,dword,qword): robot General signals outputs.
    - "GRIPPERSTATE" (float[1..3]): robot gripper status. It may have up to three values.
    
    Parameters:
    ip: str
        CPRog CRI Interface Server IP. It is the IP of the machine running CPRog. Default = '127.0.0.1'
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

        # Internal variables
        self._counter = 0
        self._mem_reply = ''


    def connect(self) -> bool:
        """ Connect driver.
        
        : returns: True if connection stablished False if not
        """
        # Force rpi to max 50ms, CPROG updates are every 100ms
        self.rpi = min(50, self.rpi) 
        
        try:
            self._connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
            self._connection.settimeout(1)
            self._connection.connect((self.ip, 3920))
            
            self.send_CRI_CMD( "ALIVEJOG", '0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0')
            sec_now = int(time.perf_counter())
            self._last_sent_poll = sec_now

            return True

        except Exception as e:
            self.sendDebugInfo('SETUP failed: Exception '+str(e))

        return False


    def disconnect(self):
        """ Disconnect driver.
        """
        pass


    def addVariables(self, variables: dict):
        """ Add variables to the driver. Correctly added variables will be added to internal dictionary 'variables'.
        Any error adding a variable should be communicated to the server using sendDebugInfo() method.
        : param variables: Variables to add in a dict following the setup format. (See documentation) 
        
        """
        for var_id, var_data in variables.items():
            if var_id in ['Axis', 'DIN', 'DOUT', 'GSIG', 'GRIPPERSTATE']:
                var_data['value'] = self.defaultVariableValue(var_data['datatype'], var_data['size'])
                self.variables[var_id] = var_data
            else:
                self.sendDebugVarInfo((f'SETUP: Variable not suported: {var_id}', var_id))
        pass


    def readVariables(self, variables: list) -> list:
        """ Read given variable values. In case that the read is not possible or generates an error BAD quality should be returned.
        : param variables: List of variable ids to be read. 
        : returns: list of tupples including (var_id, var_value, VariableQuality)
        """
        read_variables = {}
        try:
            # Send Alive telegram every 1 sec to keep communication alive
            sec_now = int(time.perf_counter())
            if self._last_sent_poll != sec_now:
                self._last_sent_poll = sec_now
                self.send_CRI_CMD("ALIVEJOG", '0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0')
                       
            # Read telegram until we read a STATUS one (2 every 5?: RUNSTATE, GRIPPERSTATE, GSIG and STATUS x 2)
            while True:
                (CMD, data) = self.recv_CRI_CMD()
                if CMD == 'STATUS':
                    if 'Axis' in variables:
                        values = data[20:20+self.variables['Axis']['size']] # Robot joint positions
                        read_variables['Axis'] = [float(v) for v in values]
                    if 'DOUT' in variables:
                        output_values = int(data[52])
                        output_type = self.variables['DOUT']['datatype']
                        if output_type == VariableDatatype.BYTE:
                            output_values &= int('ff',16)
                        elif output_type == VariableDatatype.WORD:
                            output_values &= int('ffff',16)
                        elif output_type == VariableDatatype.DWORD:
                            output_values &= int('ffffffff',16)
                        elif output_type == VariableDatatype.QWORD:
                            output_values &= int('ffffffffffffffff',16)
                        read_variables['DOUT'] = output_values
                elif CMD == 'GSIG':
                    if 'GSIG' in variables:
                        output_values = int(data[0])
                        output_type = self.variables['GSIG']['datatype']
                        if output_type == VariableDatatype.BYTE:
                            output_values &= int('ff',16)
                        elif output_type == VariableDatatype.WORD:
                            output_values &= int('ffff',16)
                        elif output_type == VariableDatatype.DWORD:
                            output_values &= int('ffffffff',16)
                        elif output_type == VariableDatatype.QWORD:
                            output_values &= int('ffffffffffffffff',16)
                        read_variables['GSIG'] = output_values
                elif CMD == 'GRIPPERSTATE':
                    if 'GRIPPERSTATE' in variables:
                        gripper_size = self.variables['GRIPPERSTATE']['size']
                        if gripper_size>1:
                            read_variables['GRIPPERSTATE'] = [float(data[i]) for i in range(gripper_size)] 
                        else:
                            read_variables['GRIPPERSTATE'] = float(data[0])
                elif CMD == 'RUNSTATE':
                    # Move on every update cycle
                    break
                #else:
                #    print(CMD, data)
        except Exception as e:
            print(e)
        
        res = []
        for var_id in variables:
            if var_id in read_variables:
                res.append((var_id, read_variables[var_id], VariableQuality.GOOD))
            else:
                res.append((var_id, self.variables[var_id]['value'], VariableQuality.BAD))
        return res


    def writeVariables(self, variables: list) -> list:
        """ Write given variable values. In case that the write is not possible or generates an error BAD quality should be returned.
        : param variables: List of tupples with variable ids and the values to be written (var_id, var_value). 
        : returns: list of tupples including (var_id, var_value, VariableQuality)
        """
        res = []
        for (var_id, new_value) in variables:

            if var_id == 'DIN':
                # TODO: DIN write not supported yet, coomand missing in CRI
                res.append((var_id, new_value, VariableQuality.BAD))

            elif var_id == 'GSIG':
                set_value = new_value
                gsig_number = 0
                output_type = self.variables['GSIG']['datatype']
                if output_type == VariableDatatype.BYTE:
                    gsig_max_number = 8
                elif output_type == VariableDatatype.WORD:
                    gsig_max_number = 16
                elif output_type == VariableDatatype.DWORD:
                    gsig_max_number = 32
                elif output_type == VariableDatatype.QWORD:
                    gsig_max_number = 64
                while gsig_number<gsig_max_number:
                    if set_value % 2:
                        self.send_CRI_CMD("CMD GSIG", f'{gsig_number} true')
                    else:
                        self.send_CRI_CMD("CMD GSIG", f'{gsig_number} false')
                    set_value >>= 1    
                    gsig_number += 1    
                res.append((var_id, new_value, VariableQuality.GOOD))

            else:
                res.append((var_id, new_value, VariableQuality.BAD))     

        return res


    def send_CRI_CMD(self, command:str, message:str):
        self._counter += 1
        request = f'CRISTART {self._counter} {command} {message} CRIEND'
        res = self._connection.send(request.encode('utf8'))
        assert (res == len(request)), "Error sending CRI command"
        

    def recv_CRI_CMD(self)->tuple:
        try:
            while True:
                recv = self._connection.recv(256)
                self._mem_reply += recv.decode('utf8')
                # Check if complete telegram received
                i = self._mem_reply.find('CRIEND')
                if i>0:
                    telegram = self._mem_reply[:i+6]
                    self._mem_reply = self._mem_reply[i+6:]
                    telegram = telegram.split(' ')
                    return (telegram[2], telegram[3:-1])
                
        except Exception as e:
            return (None,None)
