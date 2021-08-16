'''
Created on Sep 3, 2013

@author: ayam
'''

import struct
from collections import namedtuple
from .ConnectionManager import sendUnconnectedMessage
from .CIP import ROUTER_PATH, CM_PATH, BACKPLANE_DATA_PATH

FORWARD_CLOSE           = 0x4e
UNCONNECTED_SEND        = 0x52
FORWARD_OPEN            = 0x54
GET_CONNECTION_DATA     = 0x56
SEARCH_CONNECTION_DATA  = 0x57
EX_FORWARD_OPEN         = 0x59
GET_CONNECTION_OWNER    = 0x5a


""" MESSAGE ROUTER PACKET """
MR_Request_Paquet = namedtuple('MR_Request_Paquet', ['Service',             # (UBYTE)
                                                     'Request_Path_Size',   # (UBYTE)
                                                     'Request_Path',        # (Array of BYTE)
                                                     'Request_Data'])       # (Array of BYTE)

MR_Reply_Paquet = namedtuple('MR_Reply_Paquet', ['Service',                 # (UBYTE)
                                                 'Reserved',                # (UBYTE)
                                                 'General_Status',          # (UBYTE)
                                                 'Aditional_Status_Size',   # (UBYTE)
                                                 'Aditional_Status',        # (Array of BYTE)
                                                 'Response_Data'])          # (Array of BYTE)

Connection = namedtuple('Connection', ['OT_NetConnID',                      # (U32)
                                       'TO_NetConnID',                      # (U32)
                                       'ConnSerialNumber',                  # (U16)
                                       'OriginatorVendorID',                # (U16)
                                       'OriginatorSerialNumber',            # (U32)
                                       'OT_API',                            # (U32)
                                       'TO_API',                            # (U32)
                                       'ConectionPath'])                    # Array of BYTE)


def formatMR_request(request):
    """ Returns the Message Router packet formated."""
    if request:
        packet = struct.pack('BB',
                             request.Service,
                             request.Request_Path_Size)
        return packet + request.Request_Path + request.Request_Data
    else:
        return None

def getMR_reply(data):
    """ Returns the Message Router Reply Packet from the given data."""
    try:
        # Item Count
        service, reserved, general_status, aditional_status_size = struct.unpack('BBBB',data[:4])
        # Address 
        data_pos = 4 + aditional_status_size*2
        if aditional_status_size > 0:
            aditional_status = data[4:data_pos]
        else:
            aditional_status = ''
        # Data 
        if len(data)>data_pos:
            response_data = data[data_pos:]
        else:
            response_data = ''
        # Format
        packet = MR_Reply_Paquet(Service = service,
                                 Reserved = reserved,
                                 General_Status = general_status,
                                 Aditional_Status_Size = aditional_status_size,
                                 Aditional_Status = aditional_status,
                                 Response_Data = response_data)
        return packet
    except:
        return None

def sendMRPaquet(socket, sessionhandle, service, path, request_data):
    """ Sends a Message Router packet and gives the response."""
    if socket:
        # create MR Request
        MR_request = MR_Request_Paquet(Service = service,
                                       Request_Path_Size = int(len(path)/2),
                                       Request_Path = path,
                                       Request_Data = request_data)
        # Format request
        mr_request = formatMR_request(MR_request)
        # Send request
        mr_reply = sendUnconnectedMessage(socket, sessionhandle, mr_request)
        # Get reply
        MR_reply = getMR_reply(mr_reply)
        # Reply get
        if MR_reply:
            # Return MRResponsePacket
            return MR_reply.Response_Data
    # No reply
    return None

def getConnetion(data, path):
    """ Gets connection structure from ForwardOpen reply."""
    if data:
        if len(data)>=24: #Successful Response minimum length
            connection = Connection._make(struct.unpack('!IIHHIII',data[:24])+(path,))
            return connection
    return None

def forwardOpen(socket, session_handle, PLCpath, TO_NetConnID, ConnSerialNumber, RPI, Parameters):
    """ Send a Forward_Open Service packet."""
    if socket:
        """ Send a Message Router Forward Open Paquet."""
        mr_path = struct.pack('BB',PLCpath[0],PLCpath[1])
        mr_path += struct.pack('BBBB', ROUTER_PATH[0],ROUTER_PATH[1],ROUTER_PATH[2],ROUTER_PATH[3])
        mr_path_len = int(len(mr_path)/2)
        mr_data = struct.pack('!bBIIHHIBbbbIHIHBB',  # b/B:1, h/H:2, i/I:4
                              0x07,                 # (BYTE) Priority
                              0x05,                 # (UBYTE) Timeout_Ticks
                              0x00000000,           # (U32) OT_NetConnID
                              TO_NetConnID,         # (U32)
                              ConnSerialNumber,     # (U16)
                              0x6789,               # (U16) OriginatorVendorID
                              0x00001234,           # (U32) OriginatorSerialNumber
                              0x01,                 # (UBYTE) ConnTimeoutMultiplier
                              0x00, 0x00, 0x00,     # Reserved
                              RPI*1000,             # (U32) OT_RPI
                              Parameters,           # (U16) OT_NetConnParam
                              RPI*1000,             # (U32) TO_RPI
                              Parameters,           # (U16) TO_NetConnParam
                              0xA3,                 # (BYTE) TransportType
                              mr_path_len)          # (UBYTE)
        cm_path = struct.pack('BBBB',CM_PATH[0],CM_PATH[1],CM_PATH[2],CM_PATH[3])
        request_data = mr_data+mr_path
        reply_data = sendMRPaquet(socket, session_handle, FORWARD_OPEN, cm_path, request_data)
        connection = getConnetion(reply_data, mr_path)
        if connection:
            return connection

    # No Connection
    return None

def forwardClose(socket, session_handle, connection):
    """ Send a Forward_Close Service packet."""
    if socket and connection:
        mr_path_len = int(len(connection.ConectionPath)/2)
        mr_data = struct.pack('!bBHHIbB',
                              0x0A,                                     # (BYTE) Priority
                              0x05,                                     # (UBYTE) Timeout_Ticks
                              connection.ConnSerialNumber,              # (U16)
                              connection.OriginatorVendorID,            # (U16)
                              connection.OriginatorSerialNumber,        # (U32) 
                              mr_path_len,                              # (UBYTE) 
                              0)                                        # (BYTE) Reserved
        cm_path = "".join(map(chr, CM_PATH))
        reply_data = sendMRPaquet(socket, session_handle, FORWARD_CLOSE, cm_path, (mr_data+connection.ConectionPath))
        if len(reply_data)>=10:
            return True
        else:
            return False
    return False
