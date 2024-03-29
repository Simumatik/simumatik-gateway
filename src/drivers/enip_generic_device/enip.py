import struct

ENIP_HEADER_SIZE = 24 # Encapsulation_header is 24 bytes
COM_REGISTER_SESSION = 0x65
COM_SENDRRDATA = 0x6F
CM_ConnectedDataItem_Type = 0x00B1
CM_UnconnectedDataItem_Type = 0x00B2
CM_SocketAddressInfo_O_T_Type = 0x8000
CM_SocketAddressInfo_T_O_Type = 0x8001
CM_SequencedAddressItem_Type = 0x8002


class CM_NullAddressItem:
    def __init__(self):
        pass

    def __str__(self):
        return f''

    def hex(self):
        return b''
    
class CM_SocketAddressInfo():
    def __init__(self, sin_family, sin_port, sin_addr, sin_zero):
        self.sin_family = sin_family
        self.sin_port = sin_port
        self.sin_addr = sin_addr
        self.sin_zero = sin_zero

    def __str__(self):
        return f'sin_family: {hex(self.sin_family)}, sin_port: {self.sin_port}, sin_addr: {self.sin_addr}, sin_zero: {self.sin_zero}'

    def hex(self):
        packet_hex = struct.pack('!H', self.sin_family)
        packet_hex += struct.pack('!H', self.sin_port)
        packet_hex += struct.pack('I', self.sin_addr)
        packet_hex += struct.pack('Q',self.sin_zero)
        return packet_hex

    @staticmethod
    def unpack(raw_data):
        (sin_family, sin_port) = struct.unpack('!HH', raw_data[:4])
        (sin_addr,) = struct.unpack('I', raw_data[4:8])
        (sin_zero,) = struct.unpack('Q', raw_data[8:16])
        return CM_SocketAddressInfo(sin_family, sin_port, sin_addr, sin_zero)

class CM_UnconnectedDataItem():
    # Unconnected Messages
    def __init__(self, service, request_path_size, request_path, request_data):
        self.service = service
        self.request_path_size = request_path_size
        self.request_path = request_path
        self.request_data = request_data
        # Get next known data (36 bytes -> 72 hex)
        (self.prio_tick, self.timeout) = struct.unpack('BB', self.request_data[:2])
        (self.id_o_t, self.id_t_o) = struct.unpack('II', self.request_data[2:10])
        (self.conn_serial_num, self.orig_vendor_id, self.orig_serial_num) = struct.unpack('HHI', self.request_data[10:18])
        (self.timeout_mult, res_1, res_2, res_3) = struct.unpack('BBBB', self.request_data[18:22])
        (self.rpi_o_t, self.param_o_t) = struct.unpack('IH', self.request_data[22:28])
        (self.rpi_t_o, self.param_t_o) = struct.unpack('IH', self.request_data[28:34])
        (self.trigger, self.path_size) = struct.unpack('BB', self.request_data[34:36])
        # Remaining data
        self.path = self.request_data[36:36+self.path_size]
        pass

    def __str__(self):
        return f'Service: {hex(self.service)}, request path size: {self.request_path_size}, request path: {self.request_path}, request data: {self.request_data}'

    def hex(self):
        packet_hex = struct.pack('BBBB', 212, 0, 0, 0) # Reply service, reserved, status, reserved
        #packet_hex += self.request_path
        packet_hex += struct.pack('IIHHIIIBB',
                                  0x00003741,
                                  self.id_t_o,
                                  self.conn_serial_num,
                                  self.orig_vendor_id,
                                  self.orig_serial_num,
                                  self.rpi_o_t,
                                  self.rpi_t_o,
                                  0,
                                  0)
        return packet_hex

    @staticmethod
    def unpack(raw_data):
        # Get initial known data
        (service, request_path_size) = struct.unpack('BB', raw_data[:2])
        # Remove data used from raw_data
        raw_data = raw_data[2:]
        # request_path_size tell us the number of words: 1 word -> 2 bytes
        request_path = raw_data[:request_path_size*2]
        # Remove data used from raw_data
        request_data = raw_data[request_path_size*2:]
        return CM_UnconnectedDataItem(service, request_path_size, request_path, request_data)
    
class CMitem():
    def __init__(self, type_id, length, data):
        self.type_id = type_id
        self.length = length
        if (type_id == CM_UnconnectedDataItem_Type):
            self.data = CM_UnconnectedDataItem.unpack(data)
        elif type_id in [CM_SocketAddressInfo_O_T_Type, CM_SocketAddressInfo_T_O_Type]:
            self.data = CM_SocketAddressInfo.unpack(data)
        else:
            self.data = CM_NullAddressItem()

    def __str__(self):
        s = f'    CM Item:\n'
        s += f'     Type ID: {hex(self.type_id)}\n'
        s += f'     Length: {self.length}\n'
        s += f'     Data: {self.data}\n'
        return s

    def hex(self):
        data_hex = self.data.hex()
        return struct.pack('HH', self.type_id, len(data_hex)) + data_hex

class EncapsulatedPacket():
    def __init__(self, items):
        self.items = items

    def __str__(self):
        s = f'   Item count: {len(self.items)}\n'
        for item in self.items:
            s += f'{item}'
        return s
        
    def hex(self):
        packet_hex = struct.pack('H', len(self.items))
        for item in self.items:
            packet_hex += item.hex()
        return packet_hex
    
    @staticmethod
    def unpack(raw_data):
        (items_count,) = struct.unpack('H', raw_data[:2])
        raw_data = raw_data[2:]
        # List of CMitems
        items = []
        for _ in range(items_count):
            (type_id, length) = struct.unpack('HH', raw_data[:4])
            data = raw_data[4:4+length]
            items.append(CMitem(type_id, length, data))
            raw_data = raw_data[4+length:]
        return EncapsulatedPacket(items)

class EnipPacket:
    def __init__(self, encapsulation_header, specific_data):
        self.encapsulation_header = encapsulation_header
        self.specific_data = specific_data

    def __str__(self):
        return f'{self.encapsulation_header}{self.specific_data}'

    def reply(self, handle):
        self.encapsulation_header.set_session_handle(handle)
        data_hex = self.specific_data.hex()
        raw_data = self.encapsulation_header.hex(len(data_hex)) + data_hex
        return raw_data
    
    @staticmethod
    def process(raw_data):
        encapsulation_header = EncapsulationHeader.unpack(raw_data[:ENIP_HEADER_SIZE])
        if (encapsulation_header.command == COM_REGISTER_SESSION):
            specific_data = RegisterSessionData.unpack(raw_data[ENIP_HEADER_SIZE:])
        elif (encapsulation_header.command == COM_SENDRRDATA):
            specific_data = SendRRData.unpack(raw_data[ENIP_HEADER_SIZE:])
        package = EnipPacket(encapsulation_header, specific_data)
        return package

class EncapsulationHeader:
    def __init__(self, command, session_handle, status, context, options, length=0):
        self.command = command  # 2 bytes (H)
        self.length = length  # 2 bytes (H)
        self.session_handle = session_handle  # 4 bytes (I)
        self.status = status  # 4 bytes (I)
        self.context = context  # 8 bytes (Q)
        self.options = options  # 4 bytes (I)

    def __str__(self):
        s = f'Encapsulation_header:\n'
        s += f'  Command: {hex(self.command)}\n'
        s += f'  Length: {self.length}\n'
        s += f'  Session handle: {self.session_handle}\n'
        s += f'  Status: {self.status}\n'
        s += f'  Context: {self.context}\n'
        s += f'  Options: {self.options}\n'
        return s

    def set_session_handle(self, new_data):
        self.session_handle = new_data

    def hex(self, len_data_hex):
        self.length = len_data_hex
        res = struct.pack(
            'HHII', 
            self.command,
            self.length,
            self.session_handle,
            self.status)
        return res+self.context+self.options

    @staticmethod
    def unpack(raw_data):
        # For some reason this unpack requires 28 bytes
        (command, length) = struct.unpack('HH', raw_data[:4])
        (session, status) = struct.unpack('II', raw_data[4:12]) 
        context = raw_data[12:20]
        options = raw_data[20:24]
        return EncapsulationHeader(command, session, status, context, options, length)
    
class RegisterSessionData:
    def __init__(self, protocol_version, flags):
        self.protocol_version = protocol_version
        self.flags = flags

    def __str__(self):
        s = f'RegisterSessionData:\n'
        s += f'  Protocol Version: {hex(self.protocol_version)}\n'
        s += f'  Flags:{self.flags}\n'
        return s

    def hex(self):
        return struct.pack(
            'HH', 
            self.protocol_version,
            self.flags)

    @staticmethod
    def unpack(raw_data):
        (protocol_version, flags) = struct.unpack('HH', raw_data)
        return RegisterSessionData(protocol_version, flags)
    
class SendRRData():
    def __init__(self, interface_handle, timeout, encapsulated_packet):
        self.interface_handle = interface_handle
        self.timeout = timeout
        self.encapsulated_packet = encapsulated_packet

    def __str__(self):
        s = f'SendRRData:\n'
        s += f'  Interface Handle: {hex(self.interface_handle)}\n'
        s += f'  Timeout: {self.timeout}\n'
        s += f'  Encapsulated packet:\n{self.encapsulated_packet}\n'
        return s

    def hex(self):
        return struct.pack('IH', self.interface_handle, self.timeout) + self.encapsulated_packet.hex() 

    @staticmethod
    def unpack(raw_data):
        (interface_handle, timeout) = struct.unpack('IH', raw_data[:6])
        encapsulated_packet = EncapsulatedPacket.unpack(raw_data[6:])
        return SendRRData(interface_handle, timeout, encapsulated_packet)

def EnipIOpacket(data:bytes, cip_counter:int, connection_id:int, seq_count:int):
    # Item count
    res = struct.pack('H',2)   
    res += struct.pack('HHII', CM_SequencedAddressItem_Type, 8, connection_id, seq_count)
    res += struct.pack('HH', CM_ConnectedDataItem_Type, 2+len(data))
    res += struct.pack('H', cip_counter) + data
    return res