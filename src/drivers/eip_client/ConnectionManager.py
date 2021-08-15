'''
Created on Sep 3, 2013

@author: ayam
'''

import struct
from collections import namedtuple
from .EthernetIP import sendRRData, sendUnitData

ItemId_Null                 = 0x0000 # used for UCMM messages
ItemId_ListIdentityResponse = 0x000C
ItemId_ConnectionBased      = 0x00A1 # used for connected messages
ItemId_ConnectedTP          = 0x00B1 # connected transport packet
ItemId_UCM                  = 0x00B2 # unconnected message
ItemId_ListServiceResponse  = 0x0100
ItemId_OTSocketInfo         = 0x8000 # originator to target socket info
ItemId_TOSocketInfo         = 0x8001 # target to originator socket info
ItemId_Sequenced            = 0x8002 # sequenced adress item



""" CONNECTION MANAGER PACKET / COMMON PACKET FORMAT"""
Common_Paquet = namedtuple('Common_Paquet', ['Item_Count',          # (U16)
                                             'Address_TypeID',      # (U16)
                                             'Address_Length',      # (U16)
                                             'Address_Data',        # (Array of BYTE)
                                             'DataItem_TypeID',     # (U16)
                                             'DataItem_Length',     # (U16)
                                             'DataItem_Data',       # (Array of BYTE)
                                             'Aditional_Items'])    # (Array of BYTE)

def formatCommonPacket(packet):
    """ Returns the Common Format packet formated."""
    if packet:
        data = struct.pack('HHH', packet.Item_Count, packet.Address_TypeID, packet.Address_Length)
        if packet.Address_Data:
            data += packet.Address_Data
        data += struct.pack('HH', packet.DataItem_TypeID, packet.DataItem_Length)
        if packet.DataItem_Data:
            data += packet.DataItem_Data
        if packet.Aditional_Items:
            data += packet.Aditional_Items
        return data
    else:
        return None

def getCommonPacket(data):
    """ Returns the Common Format Packet from the given data."""
    try:
        # Item Count and Address 
        item_count,address_typeid, address_length = struct.unpack('HHH',data[:6])
        dataitem_pos = 6 + address_length
        if address_length > 0:
            address_data = data[6:dataitem_pos]
        else:
            address_data = ''
        # Data Item
        dataitem_typeid, dataitem_length = struct.unpack('HH',data[dataitem_pos:(dataitem_pos+4)])
        additional_pos = dataitem_pos + 4 + dataitem_length
        if dataitem_length > 0:
            dataitem_data = data[(dataitem_pos+4):additional_pos]
        else:
            dataitem_data = ''
        # Additional Items
        if len(data)>additional_pos:
            Additional_Items = data[additional_pos:]
        else:
            Additional_Items = ''
        # Format
        packet = Common_Paquet(Item_Count = item_count,
                               Address_TypeID = address_typeid,
                               Address_Length = address_length,
                               Address_Data = address_data,
                               DataItem_TypeID = dataitem_typeid,
                               DataItem_Length = dataitem_length,
                               DataItem_Data = dataitem_data,
                               Aditional_Items = Additional_Items)
        return packet
    except:
        return None
        
def sendUnconnectedMessage(socket, sessionhandle, MRRequestPacket):
    """ Send a unconnected Message."""
    if socket:
        # create CM Request
        CM_request = Common_Paquet(Item_Count = 2,
                                   Address_TypeID = ItemId_Null,
                                   Address_Length = 0,
                                   Address_Data = '',
                                   DataItem_TypeID = ItemId_UCM,
                                   DataItem_Length = len(MRRequestPacket),
                                   DataItem_Data = MRRequestPacket,
                                   Aditional_Items = '')
        # Format request
        cm_request = formatCommonPacket(CM_request)
        # Send request
        #print "CM: Unconnected Message Request sent:", CM_request
        cm_reply = sendRRData(socket, sessionhandle, cm_request)
        # Get reply
        CM_reply = getCommonPacket(cm_reply)
        # Reply get
        if CM_reply:
            #print "CM: Unconnected Message Reply received:", CM_reply
            # Return MRResponsePacket
            return CM_reply.DataItem_Data
    # No reply
    return None
            
def sendConnectedMessage(socket, sessionhandle, connection, transportpacket):
    """ Send a unconnected Message."""
    if socket:
        # create CM Request
        CM_request = Common_Paquet(Item_Count = 2,
                                   Address_TypeID = ItemId_ConnectionBased,
                                   Address_Length = 4,
                                   Address_Data = struct.pack('!I',connection.OT_NetConnID),
                                   DataItem_TypeID = ItemId_ConnectedTP,
                                   DataItem_Length = len(transportpacket),
                                   DataItem_Data = transportpacket,
                                   Aditional_Items = '')
        # Format request
        cm_request = formatCommonPacket(CM_request)
        # Send request
        #print "CM: Unit Data Message Request sent:", CM_request
        cm_reply = sendUnitData(socket, sessionhandle, cm_request)
        # Get reply
        CM_reply = getCommonPacket(cm_reply)
        # Reply get
        if CM_reply:
            #print "CM: Unit Data Message Reply received:", CM_reply
            # Return MRResponsePacket
            return CM_reply.DataItem_Data
    # No reply
    return None
            
            
        
        
        
        

