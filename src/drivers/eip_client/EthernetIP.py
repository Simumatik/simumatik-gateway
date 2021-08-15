'''
Created on Sep 3, 2013

@author: ayam
'''

from collections import namedtuple
import struct
import time

EIP_PORT            = 44818
EIP_VERSION         = 0x01

# Ethernet IP commands 
EIP_NOP                    = 0x0000
#EIP_LISTTARGETS    = 0x0001 # Reserved for legacy RA
EIP_LISTSERVICES    = 0x0004
#EIP_LISTIDENTITY    = 0x0063
#EIP_LISTINTERFACES    = 0x0064
EIP_REGISTERSESSION     = 0x0065
EIP_UNREGISTERSESSION   = 0x0066
EIP_SENDRRDATA          = 0x006F
EIP_SENDUNITDATA        = 0x0070
#EIP_INDICATESTATUS    = 0x0072
#EIP_CANCEL        = 0x0073

# EIP Status code
EIP_SUCCESS                 = 0x0000
EIP_INVALID_COMMAND         = 0x0001
EIP_MEMORY                  = 0x0002
EIP_INCORRECT_DATA          = 0x0003
EIP_INVALID_SESSION_HANDLE  = 0x0064
EIP_INVALID_LENGTH          = 0x0065
EIP_UNSUPPORTED_PROTOCOL    = 0x0069

CONTEXT = 0

""" CIP ENCAPSULATION PACKET """
CIP_Paquet = namedtuple('CIP_Paquet', ['Command',   # (U16)
                                       'Length',    # (U16)
                                       'Handle',    # (U32)
                                       'Status',    # (U32)
                                       'ContextL',  # (32)
                                       'ContextH',  # (32)
                                       'Options',   # (U32)
                                       'Data'])     # (Array of BYTE)


def formatCIP_request(request):
    """ Returns the CIP request packet formated."""
    if request:
        header = struct.pack('HHIIiiI',
                             request.Command,
                             len(request.Data), # or request.Length
                             request.Handle,
                             request.Status,
                             request.ContextL,
                             request.ContextH,
                             request.Options)
        return header + request.Data
    else:
        return None

def sendCIPPaquet(socket, request):
    """ Sends a encapsulation packet and gives the response."""
    global CONTEXT
    if socket:
        request_msg = formatCIP_request(request)
        res = socket.send(request_msg)
        #CONTEXT += 1
        if res == len(request_msg):
            # CIP message sent
            #print "CIP Packet request sent:", request
            #print "CIP Data Sent: ", ':'.join(x.encode('hex') for x in request_msg)
            # Check if reply available
            if (request.Command in [EIP_REGISTERSESSION, EIP_LISTSERVICES, EIP_SENDRRDATA, EIP_SENDUNITDATA]):
                # Get reply header
                try:
                    reply_header = socket.recv(24)
                except:
                    reply_header = ''
                    reply_datalength = 0
                if len(reply_header)==24:
                    reply_command, reply_datalength = struct.unpack('HH',reply_header[:4])
                    reply_data = ''
                    # TODO: Check reply header
                    
                    # Get reply data
                    if reply_datalength>0:
                        reply_data = socket.recv(reply_datalength)
                    # Return reply
                    reply = CIP_Paquet._make(struct.unpack('HHIIiiI',reply_header)+(reply_data,))
                    #print "CIP Packet reply received:", reply
                    #print "CIP Data received: ", ':'.join(x.encode('hex') for x in (reply_header+reply_data))
                    return reply
                else:
                    return CIP_Paquet(0,0,0,0,0,0,0,'')
            else:
                return CIP_Paquet(0,0,0,0,0,0,0,'')
    return None

def sendRegisterSession(socket):
    """ Sends an specific Register session packet."""
    global CONTEXT
    if socket:
        data = struct.pack('HH', EIP_VERSION, 0)
        request = CIP_Paquet(Command = EIP_REGISTERSESSION,
                             Length = len(data),
                             Handle = 0,
                             Status = EIP_SUCCESS,
                             ContextL=CONTEXT,
                             ContextH=0,
                             Options=0,
                             Data = data)
        reply = sendCIPPaquet(socket, request)
        if reply:
            return reply.Handle
    # Not OK
    return None
    
def sendUnegisterSession(socket, sessionhandle):
    """ Sends an specific Register session packet."""
    global CONTEXT
    if socket:
        data = ''
        request = CIP_Paquet(Command = EIP_UNREGISTERSESSION,
                             Length = len(data),
                             Handle = sessionhandle,
                             Status = EIP_SUCCESS,
                             ContextL=CONTEXT,
                             ContextH=0,
                             Options=0,
                             Data = data)
        reply = sendCIPPaquet(socket, request)
        if reply:
            return True
    # Not OK
    return None

def sendListServices(socket, sessionhandle):
    """ Sends an specific Register session packet."""
    global CONTEXT
    if socket:
        data = ''
        request = CIP_Paquet(Command = EIP_LISTSERVICES,
                             Length = len(data),
                             Handle = sessionhandle,
                             Status = EIP_SUCCESS,
                             ContextL=CONTEXT,
                             ContextH=0,
                             Options=0,
                             Data = data)
        reply = sendCIPPaquet(socket, request)
        if reply:
            return reply
    # Not OK
    return None

def sendRRData(socket, sessionhandle, packet=''):
    """ Sends a RR Data packet."""
    global CONTEXT
    if socket:
        data = struct.pack('IH',0,1) + packet 
        CIP_request = CIP_Paquet(Command = EIP_SENDRRDATA,
                                 Length = len(data),
                                 Handle = sessionhandle,
                                 Status = EIP_SUCCESS,
                                 ContextL=CONTEXT,
                                 ContextH=0,
                                 Options=0,
                                 Data = data)
        CIP_reply = sendCIPPaquet(socket, CIP_request)
        if CIP_reply:
            return CIP_reply.Data[6:] # encapsulated packet
    else:
        return None
    
def sendUnitData(socket, sessionhandle, packet=''):
    """ Sends a RR Data packet."""
    global CONTEXT
    if socket:
        data = struct.pack('IH',0,1) + packet 
        CIP_request = CIP_Paquet(Command = EIP_SENDUNITDATA,
                                 Length = len(data),
                                 Handle = sessionhandle,
                                 Status = EIP_SUCCESS,
                                 ContextL=CONTEXT,
                                 ContextH=0,
                                 Options=0,
                                 Data = data)
        CIP_reply = sendCIPPaquet(socket, CIP_request)
        if CIP_reply:
            return CIP_reply.Data[6:] # encapsulated packet
    else:
        return None
    
    
    
        