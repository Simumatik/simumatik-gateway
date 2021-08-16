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
from multiprocessing import Pipe
from typing import Optional
import time
from random import randrange
import struct
from ..driver import VariableDatatype, driver, VariableQuality
from .EthernetIP import (EIP_PORT, sendRegisterSession, sendUnegisterSession, sendListServices)
from .MessageRouter import forwardOpen, forwardClose, MR_Request_Paquet, formatMR_request
from .ConnectionManager import sendConnectedMessage
from .CIP import (CIP_DATA_READ,CIP_DATA_READ_REPLY, CIP_DATA_WRITE, CIP_DATA_WRITE_REPLY,
                 CIP_MULTIPLE_SERVICE, CIP_MULTIPLE_SERVICE_REPLY, ROUTER_PATH, CM_PATH, 
                 DATATYPE_BOOL, DATATYPE_SINT, DATATYPE_INT, DATATYPE_DINT, DATATYPE_REAL)


class eip_client(driver):
    '''
    Driver to communicate with Allen Bradley CPUs using EthernetIP protocol.
    Compatible with ControlLogix, CompactLogix and MicroLogix PLCs

    Parameters:
    ip: str
        IP address of the controller that want to connect to. Default = '192.168.0.1'
    
    slot: int
        Slot number of the CPU. Default = 1

    network_port: int
        Network port number. Default = 1
    '''

    # CONSTANTS
    MAX_ITEMS = 10

    def __init__(self, name: str, pipe: Optional[Pipe] = None):
        """
        :param name: (optional) Name for the driver
        :param pipe: (optional) Pipe used to communicate with the driver thread. See gateway.py
        """
        # Inherit
        driver.__init__(self, name, pipe)
        
        # Parameters
        self.ip = '192.168.0.1'
        self.slot = 1
        self.network_port = 1

    def connect(self) -> bool:
        """ Connect driver.
        
        : returns: True if connection stablished False if not
        """
        try:
            # Create Socket
            self._connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
            self._connection.settimeout(2)
            self._connection.connect((self.ip, EIP_PORT))
        except Exception as e:
            self.sendDebugInfo(f"SETUP: Socket connection with {self.ip} cannot be stablished.")
            return False

        try:
            # Register session
            self._handle = sendRegisterSession(self._connection)
            if self._handle:
                # Check services
                services = sendListServices(self._connection, self._handle)
                # Connect to CPU
                self._eip_connection = self.ConnectToLogixPLC(path=(self.network_port,self.slot))
                if self._eip_connection is not None:
                    return True
            else:
                self.sendDebugInfo("Error registering session.")
        
        except Exception as e:
            self.sendDebugInfo(f"SETUP: EIP connection with {self.ip} cannot be stablished.")
            
        # Not connected
        return False


    def disconnect(self):
        """ Disconnect driver.
        """
        if self._connection is not None:
            try:
                # Cleanup
                if self._handle is not None:
                    # Disconnect from controller
                    if self._eip_connection is not None:
                        self.DisconnectFromLogixPLC(self._eip_connection)
                        self._eip_connection = None
                        
                    # Unregister session
                    sendUnegisterSession(self._connection, self._handle)
                    self._handle = None
                # Close session
                self._connection.close()
            
            except Exception as e:
                self.sendDebugInfo(f"Not possible to disconnect. "+str(e))  
        return False 


    def addVariables(self, variables: dict):
        """ Add variables to the driver. Correctly added variables will be added to internal dictionary 'variables'.
        Any error adding a variable should be communicated to the server using sendDebugInfo() method.

        : param variables: Variables to add in a dict following the setup format. (See documentation) 
        
        """
        for var_id, var_data in variables.items():
            value = self.ReadPLCData(var_id)
            if value is not None:
                var_data['value'] = self.defaultVariableValue(var_data['datatype'], var_data['size'])
                self.variables[var_id] = var_data
            else:
                self.sendDebugVarInfo((f'SETUP: Variable not found: {var_id}', var_id))


    def readVariables(self, variables: list) -> list:
        """ Read given variable values. In case that the read is not possible or generates an error BAD quality should be returned.
        : param variables: List of variable ids to be read. 

        : returns: list of tupples including (var_id, var_value, VariableQuality)
        """
        """ Read given variable."""
        varray = []
        for var_id in variables:
            varray.append((var_id, self.variables[var_id]['area']))

        res = []
        if len(varray)>0:
            
            while len(varray):
                if len(varray) >= self.MAX_ITEMS:
                    rarray = varray[:self.MAX_ITEMS]
                    del varray[:self.MAX_ITEMS]
                else:
                    rarray = varray[:]
                    varray = []                    # Read
                
                res += self.MultipleReadPLCData(rarray)                
                                
        # Return list
        return res
    
    def writeVariables(self, variables: list) -> list:
        """ Write given variable values. In case that the write is not possible or generates an error BAD quality should be returned.
        : param variables: List of tupples with variable ids and the values to be written (var_id, var_value). 

        : returns: list of tupples including (var_id, var_value, VariableQuality)
        """
        # Results
        res = []
        try:
            if self._connection is not None:
                # Write
                # TODO: Multiple write
                for (vname, vvalue, vtype) in varray:
                    if self.WritePLCData(vname, vvalue, vtype):
                        res.append((vname, vvalue, "Good"))
                    else:
                        res.append((vname, None, "Error"))
                        
        except Exception as e:
            self.sendDebugInfo("Error writing data: "+str(e))
            
        # Return list
        return res


# Driver specific
# ------------------

    def ConnectToLogixPLC(self, path):
        """ Connect to a PLC in the specified path."""
        connection = forwardOpen(self._connection,
                                 self._handle,
                                 path,
                                 TO_NetConnID = randrange(0xFFFF),
                                 ConnSerialNumber = randrange(0xFFFF), # VERY IMPORTANT!!!
                                 RPI = 5000,
                                 Parameters = 0xf843) # Important the order 0xf843
        if connection is not None:
            self._packetNumber = 1
        else:
            self.sendDebugInfo("Error connecting to Logix CPU.")
        return connection
    

    def DisconnectFromLogixPLC(self, connection):
        """ Disconnect from the PLC in the given connection."""
        if forwardClose(self._connection, self._handle, connection):
            return True
        else:
            self.sendDebugInfo("Error disconnecting from Logix CPU.")
            return False


    def ReadPLCData(self, vname):
        """ Read Tag from PLC."""
        # Check connection
        if self._connection is not None:
            # Create CIP request
            request_path = struct.pack('BB',0x91,len(vname)) + vname.encode()
            if len(vname)%2 != 0:
                request_path += struct.pack('B',0x00)    
            request_data = struct.pack('H',1)
            # create MR Request
            MR_request = MR_Request_Paquet(Service = CIP_DATA_READ,
                                           Request_Path_Size = int(len(request_path)/2),
                                           Request_Path = request_path,
                                           Request_Data = request_data)
            # Format request
            packet_nb = struct.pack('H',self._packetNumber)
            mr_request = packet_nb + formatMR_request(MR_request)
            # Send request
            reply = sendConnectedMessage(self._connection, self._handle, self._eip_connection, mr_request)
            self._packetNumber = self._packetNumber + 1 if self._packetNumber<65000 else 0
            
            # Process reply
            packet_nb,service,reserved, status, ext_status_size = struct.unpack('HBBBB',reply[:6])
            if service == CIP_DATA_READ_REPLY and status == 0:
                reply_data = reply[6:]
                if len(reply_data)>2:
                    datatype = struct.unpack('H',reply_data[:2])
                    if datatype[0] == DATATYPE_BOOL:
                        value = struct.unpack('B',reply_data[2:])
                        return value[0] != 0
                    elif datatype[0] == DATATYPE_SINT:
                        value = struct.unpack('B',reply_data[2:])
                        return value[0]
                    elif datatype[0] == DATATYPE_INT:
                        value = struct.unpack('H',reply_data[2:])
                        return value[0]
                    elif datatype[0] == DATATYPE_DINT:
                        value = struct.unpack('I',reply_data[2:])
                        return value[0]
                    elif datatype[0] == DATATYPE_REAL:
                        value = struct.unpack('f',reply_data[2:])
                        return value[0]       
        # If error
        return None
        
    def WritePLCData(self, vname, vvalue, vtype):
        """ Read Tag from PLC."""
        # Check connection
        if self._connection is not None:
            # Create CIP request
            request_path = struct.pack('BB',0x91,len(vname)) + vname
            if len(vname)%2 != 0:
                request_path += struct.pack('B',0x00)    
            
            if vtype == 'Boolean':
                v = 0xFF if vvalue == True else 0x00
                request_data = struct.pack('HHB', DATATYPE_BOOL, 1, v)
            elif vtype in ['Short Integer','Byte']:
                fvalue = vvalue if vvalue < 2**7 else vvalue-2**8
                request_data = struct.pack('HHb', DATATYPE_SINT, 1, fvalue)
            elif vtype in ['Integer','Word']:
                fvalue = vvalue if vvalue < 2**15 else vvalue-2**16
                request_data = struct.pack('HHh', DATATYPE_INT, 1, fvalue)
            elif vtype in ['Double Integer', 'Double Word']:
                fvalue = vvalue if vvalue < 2**31 else vvalue-2**32
                request_data = struct.pack('HHi', DATATYPE_DINT, 1, fvalue)
            elif vtype == 'Real':
                request_data = struct.pack('HHf', DATATYPE_REAL, 1, vvalue)
            else:
                self.sendDebugInfo("Wrong data type: {0} -> {1}".format(vname, vtype))
                return False
            
            # create MR Request
            MR_request = MR_Request_Paquet(Service = CIP_DATA_WRITE,
                                           Request_Path_Size = int(len(request_path)/2),
                                           Request_Path = request_path,
                                           Request_Data = request_data)
            # Format request
            packet_nb = struct.pack('H',self._packetNumber)
            mr_request = packet_nb + formatMR_request(MR_request)
            # Send request
            reply = sendConnectedMessage(self._connection, self._handle, self._eip_connection, mr_request)
            self._packetNumber = self._packetNumber + 1 if self._packetNumber<65000 else 0
            
            # Process reply
            packet_nb,service,reserved, status, ext_status_size = struct.unpack('HBBBB',reply[:6])
            if service == CIP_DATA_WRITE_REPLY and status == 0:
                return True
        # If error
        return False

    def MultipleReadPLCData(self, varray=[]):
        """ Read Multiple Tags from PLC."""
        # Results
        res = []
        # Check connection
        if self._connection is not None:
            # Number of services
            request_data = struct.pack('H',len(varray))
            # Offsets
            offset = 2 + len(varray)*2
            offsets = ''
            requests = ''
            # loop variables
            for vname in varray:
                offsets += struct.pack('H', offset)
                tag_data = struct.pack('BB', 0x91, len(vname)) + vname
                if len(vname)%2 != 0:
                    tag_data += struct.pack('B',0x00)    
                service_request = struct.pack('BB',CIP_DATA_READ,int(len(tag_data)/2)) + tag_data + struct.pack('H',1)
                offset += len(service_request)
                requests += service_request
                
            # Request data
            request_data += offsets + requests
            # create MR Request
            MR_request = MR_Request_Paquet(Service = CIP_MULTIPLE_SERVICE,
                                           Request_Path_Size = 2,
                                           Request_Path = "".join(map(chr, ROUTER_PATH)),
                                           Request_Data = request_data)
            # Format request
            packet_nb = struct.pack('H',self._packetNumber)
            mr_request = packet_nb + formatMR_request(MR_request)
            # Send connected packet
            reply = sendConnectedMessage(self._connection, self._handle, self._eip_connection, mr_request)
            self._packetNumber = self._packetNumber + 1 if self._packetNumber<65000 else 0

            # Process reply
            packet_nb,service,reserved, status, ext_status_size = struct.unpack('HBBBB',reply[:6])
            if service == CIP_MULTIPLE_SERVICE_REPLY and status == 0:
                # Get number of services
                reply_data = reply[6:]
                if len(reply_data)>2:
                    nservices = struct.unpack('H',reply_data[:2])[0]
                    for nservice in range(nservices):
                        boffset = nservice*2+2
                        offset = struct.unpack('H',reply_data[boffset:boffset+2])[0]
                        service_reply, reply_status= struct.unpack('HH',reply_data[offset:offset+4])
                        if service_reply == CIP_DATA_READ_REPLY and reply_status == 0:
                            datatype = struct.unpack('H',reply_data[offset+4:offset+6])[0]
                            var_id = varray[nservice][0]
                            if datatype == DATATYPE_BOOL:
                                value = struct.unpack('B',reply_data[offset+6:offset+7])[0]
                                res.append((var_id, value != 0, VariableQuality.GOOD))
                            elif datatype == DATATYPE_SINT:
                                value = struct.unpack('B',reply_data[offset+6:offset+7])[0]
                                res.append((var_id, value, VariableQuality.GOOD))
                            elif datatype == DATATYPE_INT:
                                value = struct.unpack('H',reply_data[offset+6:offset+8])[0]
                                res.append((var_id, value, VariableQuality.GOOD))
                            elif datatype == DATATYPE_DINT:
                                value = struct.unpack('I',reply_data[offset+6:offset+10])[0]
                                res.append((var_id, value, VariableQuality.GOOD))
                            elif datatype == DATATYPE_REAL:
                                value = struct.unpack('f',reply_data[offset+6:offset+10])[0]
                                res.append((var_id, value, VariableQuality.GOOD))
                        else:
                            res.append((var_id, self.variables[var_id]['value'], VariableQuality.BAD))
        # Return list
        return res

    def MultipleWritePLCData(self, varray=[]):
        """ Write Multiple Tags from PLC."""
        # Results
        res = []
        # Check connection
        if self._connection is not None:
            # Number of services
            request_data = struct.pack('H',len(varray))
            # Offsets
            offset = 2 + len(varray)*2
            offsets = ''
            requests = ''
            # loop variables
            for (vname, vvalue, vtype) in varray:
                offsets += struct.pack('H', offset)
                tag_data = struct.pack('BB', 0x91, len(vname)) + vname
                if len(vname)%2 != 0:
                    tag_data += struct.pack('B',0x00)    
                service_request = struct.pack('BB',CIP_DATA_READ,int(len(tag_data)/2)) + tag_data + struct.pack('H',1)
                offset += len(service_request)
                requests += service_request
                
            # Request data
            request_data += offsets + requests
            # create MR Request
            MR_request = MR_Request_Paquet(Service = CIP_MULTIPLE_SERVICE,
                                           Request_Path_Size = 2,
                                           Request_Path = "".join(map(chr, ROUTER_PATH)),
                                           Request_Data = request_data)
            # Format request
            packet_nb = struct.pack('H',self._packetNumber)
            mr_request = packet_nb + formatMR_request(MR_request)
            # Send connected packet
            reply = sendConnectedMessage(self._connection, self._handle, self._eip_connection, mr_request)
            self._packetNumber = self._packetNumber + 1 if self._packetNumber<65000 else 0

            # Process reply
            packet_nb,service,reserved, status, ext_status_size = struct.unpack('HBBBB',reply[:6])
            if service == CIP_MULTIPLE_SERVICE_REPLY and status == 0:
                # Get number of services
                reply_data = reply[6:]
                if len(reply_data)>2:
                    nservices = struct.unpack('H',reply_data[:2])[0]
                    for nservice in range(nservices):
                        boffset = nservice*2+2
                        offset = struct.unpack('H',reply_data[boffset:boffset+2])[0]
                        service_reply, reply_status= struct.unpack('HH',reply_data[offset:offset+4])
                        if service_reply == CIP_DATA_READ_REPLY and reply_status == 0:
                            datatype = struct.unpack('H',reply_data[offset+4:offset+6])[0]
                            if datatype == DATATYPE_BOOL:
                                value = struct.unpack('B',reply_data[offset+6:offset+7])[0]
                                res.append((varray[nservice][0], value != 0, "Good"))
                            elif datatype == DATATYPE_SINT:
                                value = struct.unpack('B',reply_data[offset+6:offset+7])[0]
                                res.append((varray[nservice][0], value, "Good"))
                            elif datatype == DATATYPE_INT:
                                value = struct.unpack('H',reply_data[offset+6:offset+8])[0]
                                res.append((varray[nservice][0], value, "Good"))
                            elif datatype == DATATYPE_DINT:
                                value = struct.unpack('I',reply_data[offset+6:offset+10])[0]
                                res.append((varray[nservice][0], value, "Good"))
                            elif datatype == DATATYPE_REAL:
                                value = struct.unpack('f',reply_data[offset+6:offset+10])[0]
                                res.append((varray[nservice][0], value, "Good"))
        # Return list
        return res

