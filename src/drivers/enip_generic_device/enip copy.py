import struct

ENIP_HEADER_SIZE = 24 # Encapsulation_header is 24 bytes


class EnipPacket:
    def __init__(self, encapsulation_header, specific_data):
        self.encapsulation_header = encapsulation_header
        self.specific_data = specific_data

    def hex(self):
        data_hex = self.specific_data.hex()
        raw_data = self.encapsulation_header.hex(len(data_hex)) + data_hex
        print("Sent:", raw_data[:ENIP_HEADER_SIZE], raw_data[ENIP_HEADER_SIZE:], len(raw_data))
        return raw_data

    @staticmethod
    def process(raw_data, handle):
        print("Received:", raw_data[:ENIP_HEADER_SIZE], raw_data[ENIP_HEADER_SIZE:], len(raw_data))
        encapsulation_header = EncapsulationHeader.unpack(raw_data[:ENIP_HEADER_SIZE])
        encapsulation_header.set_session_handle(handle)
        if (encapsulation_header.command == 0x65):
            specific_data = RegisterSessionData.unpack(raw_data[ENIP_HEADER_SIZE:])
        elif (encapsulation_header.command == 0x6f):
            specific_data = SendRRData.unpack(raw_data[ENIP_HEADER_SIZE:])
        return EnipPacket(encapsulation_header, specific_data)


class EncapsulationHeader:
    def __init__(self, command, session_handle, status, context, options, length=0):
        self.command = command  # 2 bytes (H)
        self.length = length  # 2 bytes (H)
        self.session_handle = session_handle  # 4 bytes (I)
        self.status = status  # 4 bytes (I)
        self.context = context  # 8 bytes (Q)
        self.options = options  # 4 bytes (I)

    def set_session_handle(self, new_data):
        self.session_handle = new_data

    def hex(self, len_data_hex):
        self.length = len_data_hex
        return struct.pack(
            'HHIIQI', 
            self.command,
            self.length,
            self.session_handle,
            self.status,
            self.context,
            self.options
            )[:ENIP_HEADER_SIZE]# For some reason this pack will return 28 bytes

    @staticmethod
    def unpack(raw_data):
        # For some reason this unpack requires 28 bytes
        (command, length, session, status, context, options) = struct.unpack('HHIIQI', raw_data+b'\x00'*4)
        return EncapsulationHeader(command, session, status, context, options, length)
    
class RegisterSessionData:
    def __init__(self, protocol_version, flags):
        self.protocol_version = protocol_version
        self.flags = flags

    def hex(self):
        return struct.pack(
            'HH', 
            self.protocol_version,
            self.flags)

    @staticmethod
    def unpack(raw_data):
        (protocol_version, flags) = struct.unpack('HH', raw_data)
        return RegisterSessionData(protocol_version, flags)


class CMitemData0000:
    def __init__(self):
        pass

    def hex(self):
        return b''
    
class CMitemData800x():
    def __init__(self, sin_family, sin_port, sin_addr, sin_zero):
        self.sin_family = sin_family
        self.sin_port = sin_port
        self.sin_addr = sin_addr
        self.sin_zero = sin_zero

    def hex(self):
        packet_hex = struct.pack('HHIQ', 
                                 self.sin_family,
                                 self.sin_port,
                                 self.sin_addr,
                                 self.sin_zero)
        return packet_hex

    @staticmethod
    def unpack(raw_data):
        (sin_family, sin_port, sin_addr, sin_zero) = struct.unpack('HHIQ', raw_data)
        return CMitemData800x(sin_family, sin_port, sin_addr, sin_zero)

class CMitemReqData00b2():
    # Unconnected Messages
    def __init__(self, service, request_path_size, request_path, timeout, id_o_t, id_t_o, conn_serial_num, orig_vendor_id,
                 orig_serial_num, timeout_mult, reserved_1, reserved_2, rpi_o_t, param_o_t, rpi_t_o, param_t_o, trigger, path_size, path):
        self.service = service
        self.request_path_size = request_path_size
        self.request_path = request_path
        self.timeout = timeout
        self.id_o_t = id_o_t
        self.id_t_o = id_t_o
        self.conn_serial_num = conn_serial_num
        self.orig_vendor_id = orig_vendor_id
        self.orig_serial_num = orig_serial_num
        self.timeout_mult = timeout_mult
        self.reserved_1 = reserved_1
        self.reserved_2 = reserved_2
        self.rpi_o_t = rpi_o_t
        self.param_o_t = param_o_t
        self.rpi_t_o = rpi_t_o
        self.param_t_o = param_t_o
        self.trigger = trigger
        self.path_size = path_size
        self.path = path

    def hex(self):
        packet_hex = struct.pack('BBBB', 212, 0, 0, 0) # Reply service, reserved, status, reserved
        packet_hex += self.request_path
        packet_hex += struct.pack('IIHHIIIBB',
                                  self.id_o_t,
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
        raw_data = raw_data[request_path_size*2:]
        # Get next known data (36 bytes -> 72 hex)
        (timeout, id_o_t, id_t_o, conn_serial_num, orig_vendor_id, orig_serial_num, timeout_mult, reserved_1, reserved_2,
         rpi_o_t, param_o_t, rpi_t_o, param_t_o, trigger, path_size) = struct.unpack('HIIHHIBBHIHIHBB', raw_data[:36]+b'\x00'*4)
        # Remaining data
        path = raw_data[36:]
        return CMitemReqData00b2(service, request_path_size, request_path, timeout, id_o_t, id_t_o, conn_serial_num, orig_vendor_id,
                                 orig_serial_num, timeout_mult, reserved_1, reserved_2, rpi_o_t, param_o_t, rpi_t_o, param_t_o, trigger, path_size, path)

    
class CMitem():
    def __init__(self, type_id, length, data):
        self.type_id = type_id
        self.length = length
        if (type_id == 0x00b2):
            # Unconnected Data Item
            self.CM_item_data = CMitemReqData00b2.unpack(data)
        elif (type_id == 0x8001 or type_id == 0x8000):
            # Socket Adress Info T->0 or Socket Adress Info O->T
            self.CM_item_data = CMitemData800x.unpack(data)
        else:
            self.CM_item_data = CMitemData0000()

    def hex(self):
        data_hex = self.CM_item_data.hex()
        return struct.pack('HH', self.type_id, self.length) + data_hex


class EncapsulatedPacket():
    def __init__(self, items):
        self.items = items
        
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
    
'''
    for item in connection_manager_packet.specific_data.item_list:
        elif item.id == '0080':
            # TODO: Modify third item to match response (from O->T to T->O)
            #connection_manager_packet.specific_data.item_list[2].id = "0080"
            #connection_manager_packet.specific_data.item_list[2].CM_item_data.sin_addr = "00000000"
            pass
'''
class SendRRData():
    def __init__(self, interface_handle, timeout, encapsulated_packet):
        self.interface_handle = interface_handle
        self.timeout = timeout
        self.encapsulated_packet = encapsulated_packet

    def hex(self):
        return struct.pack('IH', self.interface_handle, self.timeout) + self.encapsulated_packet.hex() 

    @staticmethod
    def unpack(raw_data):
        (interface_handle, timeout) = struct.unpack('IH', raw_data[:6])
        encapsulated_packet = EncapsulatedPacket.unpack(raw_data[6:])
        return SendRRData(interface_handle, timeout, encapsulated_packet)


class EnipIOpacket():
    def __init__(self, data:bytes, seq:int, id:int, count:int):
        self.data = data
        self.seq = seq
        self.id = id
        self.seq_count = count

    def pack(self):
        data_io = struct.pack('>H', self.seq_count) + self.data
        res = struct.pack('HHH',
                           2,
                           0x8002,
                           8,
        )
        res += struct.pack('>I', self.id)
        res += struct.pack('IHH',
                           self.seq,
                           0x00b1,
                           len(data_io)
                           )
        return res+data_io

    
class EnipIOpacket_old():
    def __init__(self, data, seq, id, count):
        self.data = data
        self.seq = seq
        self.id = id
        self.seq_count = count

    def pack(self):
        item_count = 2
        adress_type = 0x8002
        adress_len = 8
        data_type = 0x00b1

        data_io = struct.pack('H', self.seq_count).hex() + self.data

        a = struct.pack('H', item_count).hex()
        b = struct.pack('H', adress_type).hex()
        c = struct.pack('H', adress_len).hex()
        d = struct.pack('>I', int(self.id, 16)).hex()
        e = struct.pack('I', self.seq).hex()
        f = struct.pack('H', data_type).hex()
        g = struct.pack('H', int(len(data_io)/2)).hex()

        result = a+b+c+d+e+f+g+data_io
        return result


