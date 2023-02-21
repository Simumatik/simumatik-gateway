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

import struct
from collections import namedtuple
from ..driver import VariableQuality, VariableDatatype


# ISO on TCP
ISO_CMD         = 0x0300
ISO_EXCHANGE    = b'\x02\xF0\x80'
ISO_HEADER_LEN  = 4

# Functions
CMD_READ    = 0x04
CMD_WRITE   = 0x05

# Areas
AREA_SYSINFO    = 0x03        # System info of 200 family 
AREA_SYSFLAGS   = 0x05        # System flags of 200 family 
AREA_ANAIN      = 0x06        # analog inputs of 200 family 
AREA_ANAOUT     = 0x07        # analog outputs of 200 family 
AREA_P          = 0x80        # direct peripheral access 
AREA_INPUT      = 0x81
AREA_OUTPUT     = 0x82
AREA_FLAG       = 0x83
AREA_DB         = 0x84
AREA_DI         = 0x85        # instance data blocks 
AREA_LOCAL      = 0x86        # local data (should not be accessible over network) 
AREA_V          = 0x87        # previous (Vorgaenger) local data (should not be accessible over network)  
AREA_COUNTER    = 28          # S7 counters 
AREA_TIMER      = 29          # S7 timers 
AREA_COUNTER200 = 30          # IEC counters (200 family) 
AREA_TIMER200   = 31          # IEC timers (200 family) 

# Data Type
S7_Bit          = 1
S7_Byte         = 2
S7_Char         = 3
S7_Word         = 4
S7_Int          = 5
S7_DoubleWord   = 6
S7_DoubleInt    = 7
S7_Real         = 8

# Transport sizes in data
DATA_TRANSPORT_SIZE_NULL     = 0
DATA_TRANSPORT_SIZE_BBIT     = 3           # bit access, len is in bits 
DATA_TRANSPORT_SIZE_BBYTE    = 4           # byte/word/dword acces, len is in bits 
DATA_TRANSPORT_SIZE_BINT     = 5           # integer access, len is in bits
DATA_TRANSPORT_SIZE_BDINT    = 6           # integer access, len is in bytes
DATA_TRANSPORT_SIZE_BREAL    = 7           # real access, len is in bytes
DATA_TRANSPORT_SIZE_BSTR     = 9           # octet string, len is in bytes

# Others
DATA_OK     = 0xFF

# DataArea
DataArea = namedtuple('DataArea', ['Area', 'Start', 'Count', 'Type', 'DB','Formated'])

DEBUGG = False


"""
 PDU Telegrams
"""
PDU = namedtuple('PDU', ['Command',     # (U8) Specific for type of PDU
                         'Type',        # (U8) Type
                         'DestRef',     # (U16)
                         'SourceRef',   # (U16)
                         'ParamLength', # (U16) Parameter data length
                         'DataLength',  # (U16) Data length
                         'Params',      # (String with Parameter data)
                         'Data'])       # (String containing Data)

def formatPDU(tpdu):
    """ Returns the CIP request packet formated."""
    if tpdu:
        mess = struct.pack('!BBHHHH',
                           tpdu.Command,
                           tpdu.Type,
                           tpdu.DestRef,
                           tpdu.SourceRef,
                           tpdu.ParamLength,
                           tpdu.DataLength)
        # Type 2 and 3 PDUs have 12 byte header
        if tpdu.Type in [2,3]:
            mess += b'\x00\x00'
        # Add Parameters
        if tpdu.ParamLength:
            mess += tpdu.Params
        # Add Data
        if tpdu.DataLength:
            mess += tpdu.Data
        return mess
    else:
        return None

def getPDU(message):
    """ Gets a pdu from a string."""
    try:
        spdu = struct.unpack('!BBHHHH',message[:10])
        point = 12 if int(spdu[1]) in [2,3] else 10
        params = message[point : (point+spdu[4])] if spdu[4] else ""
        data = message[(point+spdu[4]) : (point+spdu[4]+spdu[5])] if spdu[5] else ""
        tpdu = PDU._make(spdu+(params,data))
        return tpdu
    except Exception as e:
        if DEBUGG: print("Driver S7Siemens"+"Error! Can't get PDU."+str(e))
    return None

def PDULengthRequest(socket, PDU_id): 
    """ Send a specific PDU to request length."""
    if socket is not None:
        PARAMS = b'\xF0\x00\x00\x01\x00\x01\x03\xC0'
        request = PDU(Command = 0x32,
                        Type = 0x01,
                        DestRef = 0x0000,
                        SourceRef = PDU_id,
                        ParamLength = len(PARAMS),
                        DataLength = 0x00,                  
                        Params = PARAMS,
                        Data = b'')
        reply = exchangePDU(socket, request)
        if reply:
            param, dummy, PDULength = struct.unpack('!HIH',reply.Params)
            return PDULength


def PDU_from_ReadAreas(PDU_id:int, areas:list):
    PARAMS = struct.pack("BB", CMD_READ, len(areas))
    for (_, area) in areas:
        PARAMS += area.Formated
        
    return PDU(
        Command = 0x32,
        Type = 0x01,
        DestRef = 0x0000,
        SourceRef = PDU_id,
        ParamLength = len(PARAMS),
        DataLength = 0x00,                  
        Params = PARAMS,
        Data = b'')

def ReadAreas_from_PDU(pdu:PDU, areas:list):
    results = []
    if pdu:
        if pdu.Data:
            point = 0
            for (name, area) in areas:
                # Result data is OK
                res, typelength, length = struct.unpack('!BBH',pdu.Data[point:point+4])
                if res == DATA_OK:
                    if typelength in [4,5]: # Length in Bits
                        length >>= 3
                    elif typelength in [3,9]: # Length in Bytes
                        pass
                    # Check count
                    dataend = point+4+length
                    # Return Data
                    if area.Type == S7_Bit:
                        value = (0,) if (pdu.Data[point+4:dataend] == b'\x00') else (1,)
                    if area.Type == S7_Byte:
                        value = struct.unpack('B',pdu.Data[point+4:dataend])
                    elif area.Type == S7_Word:
                        value = struct.unpack('!H',pdu.Data[point+4:dataend])
                    elif area.Type == S7_Int:
                        value = struct.unpack('!h',pdu.Data[point+4:dataend])
                    elif area.Type == S7_DoubleWord:
                        value = struct.unpack('!I',pdu.Data[point+4:dataend])
                    elif area.Type == S7_DoubleInt:
                        value = struct.unpack('!i',pdu.Data[point+4:dataend])
                    elif area.Type == S7_Real:
                        value = struct.unpack('!f',pdu.Data[point+4:dataend])
                    results.append((name, value[0], VariableQuality.GOOD))
                    # Value has an extra bit if not even length
                    point = dataend+dataend%2
                else:
                    # Data not OK
                    results.append((name, None, VariableQuality.BAD))
    return results

def PDU_from_WriteAreas(PDU_id:int, areadata:list):
    PARAMS = struct.pack("BB", CMD_WRITE, len(areadata))
    DATA = b''
    for (name, area, value) in areadata:
        PARAMS += area.Formated
        # Attach data
        if area.Type == S7_Bit:
            DATA += struct.pack('!BBHB', 0, DATA_TRANSPORT_SIZE_BBIT, area.Count, value) #Different code for Bits (3)
            # Adds an empty byte if data length is odd
            if area.Count%2:
                DATA += b'\x00'
        elif area.Type == S7_Byte:
            DATA += struct.pack('!BBHB', 0, DATA_TRANSPORT_SIZE_BBYTE, area.Count*8, value)
            # Adds an empty byte if data length is odd
            if area.Count%2:
                DATA += b'\x00'
        elif area.Type == S7_Word:
            DATA += struct.pack('!BBHH', 0, DATA_TRANSPORT_SIZE_BBYTE, area.Count*16, value) 
        elif area.Type == S7_Int:
            DATA += struct.pack('!BBHh', 0, DATA_TRANSPORT_SIZE_BINT, area.Count*16, value) 
        elif area.Type == S7_DoubleWord:
            DATA += struct.pack('!BBHI', 0, DATA_TRANSPORT_SIZE_BBYTE, area.Count*32, value)
        elif area.Type == S7_DoubleInt:
            DATA += struct.pack('!BBHi', 0, DATA_TRANSPORT_SIZE_BINT, area.Count*32, value)
        elif area.Type == S7_Real:
            DATA += struct.pack('!BBHf', 0, DATA_TRANSPORT_SIZE_BREAL, area.Count*4, value)
        
    return PDU(Command = 0x32,
        Type = 0x01,
        DestRef = 0x0000,
        SourceRef = PDU_id,
        ParamLength = len(PARAMS),
        DataLength = len(DATA),                  
        Params = PARAMS,
        Data = DATA)    

def WriteAreas_from_PDU(pdu:PDU, areas:list):
    results = []
    # Check reply
    reply_OK = False
    if pdu:
        if (pdu.Params and pdu.Data):
            res, reply_len = struct.unpack('!BB',pdu.Params)
            # All area status returned
            if len(areas) == reply_len:
                reply_OK = True
    for i in range(len(areas)):
        (name, area, value) = areas[i]
        if reply_OK:
            # Result data is OK
            if pdu.Data[i] == DATA_OK:
                results.append((name, value, VariableQuality.GOOD))
            else:
                results.append((name, None, VariableQuality.BAD))
        # Not all area status returned
        else:
            results.append((name, None, "Error"))
    return results

def PDUReadAreas(socket, PDU_id, areas = []):
    """ Send a read data PDU request.
        areas (Array of AreaData): [(Area, Start, Count, Type, DB)]
    """
    results = []
    if socket and len(areas):
        request = PDU_from_ReadAreas(PDU_id, areas)
        reply = exchangePDU(socket, request)
        results = ReadAreas_from_PDU(reply, areas)
    return results

def PDUWriteAreas(socket, PDU_id, areas=[]):
    """ Send a read data PDU request.
        areadata (Array of (AreaData, value)): [((Area, Start, Count, Type, DB), value)]
    """
    results = []
    if socket and len(areas):            
        request = PDU_from_WriteAreas(PDU_id, areas)
        reply = exchangePDU(socket, request)
        results = WriteAreas_from_PDU(reply, areas)
    return results

"""
 ISO-on-TCP TELEGRAMS
"""
def ISOSend(socket, message=""):
    """ Send a message encapsulated into a ISO telegram throw the socket.
                       -------------------------------
        ISO TELEGRAM: | CMD | TOTAL LENGTH | MESSAGE |
                      -------------------------------
    """
    if socket:
        # Send telegram
        reply = struct.pack('!HH', ISO_CMD, len(message)+ISO_HEADER_LEN) + message
        res = socket.send(reply)
        if (res == len(reply)):
            # Telegram sent
            if DEBUGG: print("ISO send:", reply)
            return True
    # Message not send
    return False
    
def ISOReceive(socket):
    """ Receive message from socket.
                       -------------------------------
        ISO TELEGRAM: | CMD | TOTAL LENGTH | MESSAGE |
                      -------------------------------
    """
    if socket:
        # Read reply
        try:
            reply_header = socket.recv(ISO_HEADER_LEN)
        except Exception as e:
            if DEBUGG: print("Driver S7Siemens Error! Timeout, ISO response not received. "+str(e))
            return None
        # Check header length
        if len(reply_header) == ISO_HEADER_LEN:
            mess_head, mess_len = struct.unpack('!HH',reply_header)
            # Check header
            if mess_head == ISO_CMD:
                try:
                    reply_data = socket.recv(mess_len-ISO_HEADER_LEN)
                except socket.error as e:
                    if DEBUGG: print("Driver S7Siemens Error! ISO response not completed. "+str(e))
                    return None
                # Extract data
                if len(reply_data) == mess_len-ISO_HEADER_LEN:
                    if DEBUGG: print("ISO read:", reply_header+reply_data)
                    # Return removing 
                    return reply_data    
        # Wrong header
        if DEBUGG: print("Error! ISO response incorrect.")
        return None
    # No telegram
    if DEBUGG: 
        print("Error! No ISO response.")
        
    return None
    
def ISOConnect(socket, message=""):
    """ Send ISO Connect telegram."""
    if socket:
        # Send telegram
        if (ISOSend(socket, message)):   
            # Read response
            return ISOReceive(socket)    
    # Nothing to return
    return False

def ISOExchange(socket, message=""):  
    """ Send an ISO data Exchange telegram, adding the header to the given message."""
    """ If sent, Read reply, returning the received data without the header."""    
    if socket:
        # Send telegram with exchange extra data
        if (ISOSend(socket, ISO_EXCHANGE + message)):   
            # Telegram sent, read response
            response = ISOReceive(socket)
            # Check response
            return response[3:] if response is not None else response

    # Nothing to return
    return None



""" 
CIP ENCAPSULATION PACKET 
"""

def connectPLC(socket, rack=0, slot=0):
    """ Sends a packet to connect the PLC."""
    if socket:
        # Send specific telegram
        request = b''
        params = [[b'\xC1',b'\x01\x00'],
                  [b'\xC2',struct.pack('BB', rack+1, slot)],
                  [b'\xC0',b'\x09']]
        for param in params:
            request += param[0] + struct.pack('B', len(param[1])) + param[1]
        # References    
        request = struct.pack('!HHb',0, 1, 0) + request
        # Command
        request = struct.pack('BB',len(request)+1,0xE0) + request
        
        if DEBUGG: print("PDU send:", request)
        reply = ISOConnect(socket, request)
        if reply:
            if DEBUGG: print("PDU read:", reply)
            return True
    # Not connected
    return False

def exchangePDU(socket, pdu):  
    """ Send a PDU."""
    if socket:
        # Parameters
        request = formatPDU(pdu)
        if request:
            if DEBUGG: print("PDU send:", request)
            reply = ISOExchange(socket, request)   
            if len(reply):
                if DEBUGG: print("PDU read:", reply)
                # Format PDU and return
                return getPDU(reply)
    # No reply
    return None



""" 
 OTHERS
"""
def getAreaFromString(vaddress, vdtype):
    """ Get an area info tupple from a string."""
    try:
        # Get area
        p = 0
        if vaddress[p] == "I":
            area = AREA_INPUT
            p = 1
        elif vaddress[p] == "L":
            area = AREA_LOCAL
            p = 1
        elif vaddress[p] == "Q":
            area = AREA_OUTPUT
            p = 1
        elif vaddress[p] == "M":
            area = AREA_FLAG
            p = 1
        else:
            return None

        # Get DataType
        # TODO: Some datatypes are missing
        if vaddress[p] == "B" and vdtype == VariableDatatype.BYTE:
            datatype = S7_Byte
            p = 2
        elif vaddress[p] == "W" and vdtype == VariableDatatype.WORD:
            datatype = S7_Word
            p = 2
        elif vaddress[p] == "W" and vdtype == VariableDatatype.INTEGER:
            datatype = S7_Int
            p = 2
        elif vaddress[p] == "D" and vdtype == VariableDatatype.DWORD:
            datatype = S7_DoubleWord
            p = 2
        elif vaddress[p] == "D" and vdtype == VariableDatatype.INTEGER:
            datatype = S7_DoubleInt
            p = 2
        elif vaddress[p] == "D" and vdtype == VariableDatatype.FLOAT:
            datatype = S7_Real
            p = 2
        elif vaddress[p:].find('.') and vdtype == VariableDatatype.BOOL:
            datatype = S7_Bit
        else:
            return None
        # Get Start
        if datatype in [S7_Byte, S7_Word, S7_Int, S7_DoubleWord, S7_DoubleInt, S7_Real]:
            start = int(vaddress[p:])
        elif datatype in [S7_Bit]:
            start_H, start_L = vaddress[p:].split('.')
            start = int(start_H)*8+int(start_L)
            
        # Format area
        areaformated = b'\x12\x0A\x10'
        # Calculate Start address
        if datatype == S7_Bit:      
            tstart = start
        elif datatype in [S7_Byte, S7_Word, S7_Int, S7_DoubleWord, S7_DoubleInt, S7_Real]:         
            tstart = start * 8
        # Fill parameter data
        areaformated += struct.pack('!BHHBBH',
                            datatype,
                            1,
                            0,
                            area,
                            int(tstart/0x1000),
                            int(tstart%0x1000))

        # 'Area', 'Start', 'Count', 'Type', 'DB', 'Formated'
        return DataArea(Area=area, Type=datatype, DB=0, Start=start, Count=1, Formated=areaformated)

    except Exception as e:
        return None      
