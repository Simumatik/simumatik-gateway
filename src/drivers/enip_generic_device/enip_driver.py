from drivers.driver import driver, DriverStatus, DriverActions
from multiprocessing import Pipe
import socket
import time
import struct


def hex_unpack(format, raw_data):
    # Based on python struct, adapted for hexadecimal
    data = []
    raw_data_copy = raw_data
    for i in format:
        # Unsigned char: 1 byte -> 2 hex
        if (i == 'B'):
            i = 2
        # Unsigned short: 2 bytes -> 4 hex
        elif (i == 'H'):
            i = 4
        # Unsigned int: 4 bytes -> 8 hex
        elif (i == 'I'):
            i = 8
        # Unsigned
        elif (i == "Q"):
            i = 16
        # Extract hex values
        data.append(raw_data_copy[:i])
        # Remove extracted data
        raw_data_copy = raw_data_copy[i:]
    return tuple(data)


class CMitemData800x():
    def __init__(self, sin_family, sin_port, sin_addr, sin_zero):
        self.sin_family = sin_family
        self.sin_port = sin_port
        self.sin_addr = sin_addr
        self.sin_zero = sin_zero

    def hex(self):
        packet_hex = self.sin_family + self.sin_port + self.sin_addr + self.sin_zero
        return packet_hex

    @staticmethod
    def unpack(raw_data):
        (sin_family, sin_port, sin_addr, sin_zero) = hex_unpack('HHIQ', raw_data)
        return CMitemData800x(sin_family, sin_port, sin_addr, sin_zero)


class CMitemResData00b2():
    def __init__(self, id_o_t, id_t_o, conn_serial_num, orig_vendor_id, orig_serial_num, rpi_o_t, rpi_t_o):
        self.service = "d4"
        self.status = "000000"
        self.id_o_t = id_o_t
        self.id_t_o = id_t_o
        self.conn_serial_num = conn_serial_num
        self.orig_vendor_id = orig_vendor_id
        self.orig_serial_num = orig_serial_num
        self.rpi_o_t = rpi_o_t
        self.rpi_t_o = rpi_t_o
        self.reply_size = "00"
        self.reserved = "00"
        self.reply = ''

    def hex(self):
        packet_hex = self.service + self.status + self.id_o_t + self.id_t_o + self.conn_serial_num + self.orig_vendor_id + \
            self.orig_serial_num + self.rpi_o_t + self.rpi_t_o + \
            self.reply_size + self.reserved + self.reply
        return packet_hex


class CMitemReqData00b2():
    def __init__(self, service, request_path_size, request_path, timeout, id_o_t, id_t_o, conn_serial_num, orig_vendor_id,
                 orig_serial_num, timeout_mult, reserved, rpi_o_t, param_o_t, rpi_t_o, param_t_o, trigger, path_size, path):
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
        self.reserved = reserved
        self.rpi_o_t = rpi_o_t
        self.param_o_t = param_o_t
        self.rpi_t_o = rpi_t_o
        self.param_t_o = param_t_o
        self.trigger = trigger
        self.path_size = path_size
        self.path = path

    def hex(self):
        packet_hex = self.service + self.request_path_size + self.request_path + self.timeout + self.id_o_t + self.id_t_o + self.conn_serial_num + self.orig_vendor_id + \
            self.orig_serial_num + self.timeout_mult + self.reserved + self.rpi_o_t + \
            self.param_o_t + self.rpi_t_o + self.param_t_o + \
            self.trigger + self.path_size + self.path
        return packet_hex

    @staticmethod
    def unpack(raw_data):
        # Get initial known data
        (service, request_path_size) = hex_unpack('BB', raw_data[:4])
        # Remove data used from raw_data
        raw_data = raw_data[4:]
        # request_path_size tell us the number of words: 1 word -> 2 bytes -> 4 hex
        request_path_len = int(request_path_size, 16)*4
        request_path = raw_data[:request_path_len]
        # Remove data used from raw_data
        raw_data = raw_data[request_path_len:]
        # Get next known data (36 bytes -> 72 hex)
        (timeout, id_o_t, id_t_o, conn_serial_num, orig_vendor_id, orig_serial_num, timeout_mult, reserved_1, reserved_2,
         rpi_o_t, param_o_t, rpi_t_o, param_t_o, trigger, path_size) = hex_unpack('HIIHHIBBHIHIHBB', raw_data[:72])
        # Remove data used from raw_data
        raw_data = raw_data[72:]
        # Remaining data
        path = raw_data

        return CMitemReqData00b2(service, request_path_size, request_path, timeout, id_o_t, id_t_o, conn_serial_num, orig_vendor_id,
                                 orig_serial_num, timeout_mult, reserved_1+reserved_2, rpi_o_t, param_o_t, rpi_t_o, param_t_o, trigger, path_size, path)


class CMitemData0000:
    def __init__(self):
        pass

    def hex(self):
        return ""


class CMitem():
    def __init__(self, item_id, length, data):
        self.id = item_id
        self.length = length
        self.CM_item_data = data

    def update_length(self, new_data):
        self.length = struct.pack('H', int(len(new_data)/2)).hex()

    def hex(self):
        data_hex = self.CM_item_data.hex()
        self.update_length(data_hex)
        packet_hex = self.id + self.length + data_hex
        return packet_hex


class CMPacketData():
    def __init__(self, interface_handle, timeout, item_count, item_list):
        self.interface_handle = interface_handle
        self.timeout = timeout
        self.item_count = item_count,
        self.item_list = item_list

    def update_item_count(self):
        self.item_count = struct.pack('H', len(self.item_list)).hex()

    def hex(self):
        self.update_item_count()
        packet_hex = self.interface_handle + self.timeout + self.item_count
        for item in self.item_list:
            packet_hex += item.hex()
        return packet_hex

    @staticmethod
    def unpack(raw_data):
        # 8 bytes -> 16 hex
        (interface_handle, timeout, items_number) = hex_unpack(
            'IHH', raw_data[:16])
        # Remove already used data
        raw_data = raw_data[16:]
        # List of CMitems
        items_list = []
        # Item_count in dec (< for little endian)
        item_number_dec = struct.unpack('<H', bytes.fromhex(items_number))[0]
        for _item in range(item_number_dec):
            (item_id, item_length) = hex_unpack('HH', raw_data[:8])
            # Remove already used data
            raw_data = raw_data[8:]
            # Get item data length in decimal: 1 byte -> 2 hex (< for little endian)
            item_length_dec = struct.unpack(
                '<H', bytes.fromhex(item_length))[0]*2
            # Process item data
            item_data = raw_data[:item_length_dec]
            if (item_id == 'b200'):
                # Unconnected Data Item
                CM_item_data = CMitemReqData00b2.unpack(item_data)
            elif (item_id == '0180' or item_id == '0080'):
                # Socket Adress Info T->0 or Socket Adress Info O->T
                CM_item_data = CMitemData800x.unpack(item_data)
            elif (item_id == '0000'):
                CM_item_data = CMitemData0000()
            # Remove already used data
            raw_data = raw_data[item_length_dec:]
            # Add item to the list
            items_list.append(CMitem(item_id, item_length, CM_item_data))

        return CMPacketData(interface_handle, timeout, items_number, items_list)


class EnipPacket:
    def __init__(self, encapsulation_header, specific_data):
        self.encapsulation_header = encapsulation_header
        self.specific_data = specific_data

    def hex(self):
        packet_hex = ""
        data_hex = self.specific_data.hex()
        packet_hex += self.encapsulation_header.hex(data_hex)
        packet_hex += data_hex
        return packet_hex

    @staticmethod
    def unpack(raw_data):
        # Encapsulation_header is 24 bytes -> 48 hex
        encapsulation_header = EncapsulationHeader.unpack(raw_data[:48])
        if (encapsulation_header.command == "6f00"):
            specific_data = CMPacketData.unpack(raw_data[48:])
        else:
            specific_data = RegisterSessionData.unpack(raw_data[48:])
        return EnipPacket(encapsulation_header, specific_data)


class RegisterSessionData:
    def __init__(self, protocol_version, flags):
        self.protocol_version = protocol_version
        self.flags = flags

    def hex(self):
        packet_hex = self.protocol_version + self.flags
        return packet_hex

    @staticmethod
    def unpack(raw_data):
        (protocol_version, flags) = hex_unpack('HH', raw_data)
        return RegisterSessionData(protocol_version, flags)


class EncapsulationHeader:
    def __init__(self, command, session_handle, status, context, options, length=0):
        self.command = command  # 2 bytes (H)
        self.length = length  # 2 bytes (H)
        self.session_handle = session_handle  # 4 bytes (I)
        self.status = status  # 4 bytes (I)
        self.context = context  # 8 bytes (Q)
        self.options = options  # 4 bytes (I)

    def update_length(self, new_data):
        self.length = struct.pack('H', int(len(new_data)/2)).hex()

    def set_session_handle(self, new_data):
        self.session_handle = struct.pack('I', new_data).hex()

    def hex(self, data_hex):
        self.update_length(data_hex)
        packet_hex = self.command + self.length + self.session_handle + \
            self.status + self.context + self.options
        return packet_hex

    @staticmethod
    def unpack(raw_data):
        # See ODVA VOL2: 3-2.1
        (command, length, session, status, context,
         options) = hex_unpack('HHIIQI', raw_data)
        return EncapsulationHeader(command, session, status, context, options, length)


class EnipIOpacket():
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


class enip_driver(driver):

    def __init__(self, name, pipe, **kwargs):
        """ Constructor."""
        # Initial parameters
        self.driver_ip = '127.0.0.1'
        self.connection_path = ''
        self.read_size = 1
        self.write_size = 1

        # Object variables
        self.tcp_socket = None
        self.udp_socket = None
        self.plc_socket = None
        self.plc_address = ""

        # Enip IO packet variables
        self.io_seq = 0
        self.cip_counter = -1
        self.id_io = ""
        self.write_data = "0"
        self.read_data = "0"

        # Initialize variable
        self.input_data = ""
        for _b in range(0, self.write_size):
            self.input_data += '{:02x}'.format(0)

        # Inherit
        driver.__init__(self, name, pipe)

    def check_input_updates(self):
        if len(self.pending_updates.items)>0:
            address, value = self.pending_updates.popitem()
            # TODO: Add real check
            if (address == "input_data"):
                self.input_data = value.replace("0x", "")

    def sendEnipIOpacket(self, data):
        # TODO: Check write data size
        # Check if data has changed
        if (self.write_data != data):
            self.write_data = data
            self.cip_counter += 1
            self.print_hex_bin("Write", self.write_data)
        # Generate packet in hex
        packet_hex = EnipIOpacket(
            self.write_data, self.io_seq, self.id_io, self.cip_counter).pack()
        # Send packet
        self.udp_socket.sendto(bytes.fromhex(
            packet_hex), (self.plc_address, 2222))
        # Update variables
        self.io_seq += 1

    def listenEnipIOpacket(self):
        # TODO: Check read data size
        # Loop to listen until a valid enip packet is found
        packet_hex = ""
        while (packet_hex[4:8] != "0280"):
            packet_hex = self.udp_socket.recv(4096).hex()
        # Extract data: 1 byte -> 2 hex
        data = packet_hex[-(self.read_size*2):]
        if (self.read_data != data):
            self.read_data = data
            self.print_hex_bin("Read", self.read_data)
            # Send PLC data through the pipe. Add 0x before every byte
            send_data = "".join(["0x"+self.read_data[i:i+self.read_size*2] for i in range(0, len(self.read_data), self.read_size*2)])
            self.sendUpdate({"output_data":send_data})
        return self.read_data

    def print_hex_bin(self, text, raw_data):
        print(text, ': 0x' + str(raw_data) + " (" + bin(
            int(raw_data, 16))[2:].zfill(int(len(raw_data))*4) + ")")

    def generate_CM_res(self):
        req_connection_manager = self.plc_socket.recv(4096).hex()
        connection_manager_packet = EnipPacket.unpack(req_connection_manager)
        # Save variable for later use
        self.id_io = connection_manager_packet.specific_data.item_list[1].CM_item_data.id_t_o
        # Modify third item to match response (from O->T to T->O)
        connection_manager_packet.specific_data.item_list[2].id = "0080"
        connection_manager_packet.specific_data.item_list[2].CM_item_data.sin_addr = "00000000"
        # Create second item data from request and introduce it. TODO: Do not hardcode id_o_t
        item_data = connection_manager_packet.specific_data.item_list[1].CM_item_data
        item_data_new = CMitemResData00b2("41370000", item_data.id_t_o, item_data.conn_serial_num,
                                            item_data.orig_vendor_id, item_data.orig_serial_num, item_data.rpi_o_t, item_data.rpi_t_o)
        connection_manager_packet.specific_data.item_list[1].CM_item_data = item_data_new
        # Send response packet
        self.plc_socket.send(bytes.fromhex(connection_manager_packet.hex()))

    def generate_RS_res(self):
        req_register_session = self.plc_socket.recv(4096).hex()
        register_session_packet = EnipPacket.unpack(req_register_session)
        # Response is the same as request, but introducing the session handle ID (random)
        register_session_packet.encapsulation_header.set_session_handle(
            int(self.driver_ip.split('.')[3]))
        # Send response
        self.plc_socket.send(bytes.fromhex(register_session_packet.hex()))

    def doSetup(self, setup_data):
        # Inherit
        if not driver.doSetup(self, setup_data):
            return False
        try:
            print("DoSetup executed")
            # Create TCP socket
            self.tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.tcp_socket.bind((self.driver_ip, 44818))
            self.tcp_socket.listen(1)
            self.tcp_socket.settimeout(5)
            print("TCP socket created")

            # Wait for connection
            (self.plc_socket, self.plc_address) = self.tcp_socket.accept()
            # We just need the IP, not the port
            self.plc_address = self.plc_address[0]
            print("Connection established")

            # First packet is the Register Session. Listen to the request and then generate the response
            self.generate_RS_res()
            print("RegisterSession response sent")

            # Next packet is the CIP Connection Manager. Listen to the request and then generate the response
            self.generate_CM_res()
            print("CommunicationManager response sent")

            # Handshake done. Change to UDP
            self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.udp_socket.bind((self.driver_ip, 2222))
            self.udp_socket.settimeout(1.0)
            print("UDP socket created")

            # Send initial packet to start communication
            self.sendEnipIOpacket(self.input_data)
            print("ENIP I/O packet sent")

            # Wait until a ENIP IO packet is received from the PLC
            self.listenEnipIOpacket()
            print("ENIP I/O packet received")

            # Setup OK
            self.changeStatus(DriverStatus.RUNNING)

        except Exception as e:
            print("Exception in doSetup"+ str(e))
            self.sendDebugInfo('Exception while running: ' + str(e))
            self.changeStatus(DriverStatus.CLEANUP)

    def doRun(self):
        try:
            # Update input_data
            self.check_input_updates()

            # Send write data to PLC
            self.sendEnipIOpacket(self.input_data)

            # Wait until a ENIP IO packet is received from the PLC
            self.listenEnipIOpacket()

        except Exception as e:
            print("Exception in doRun"+ str(e))
            self.sendDebugInfo('Exception while running: ' + str(e))
            self.changeStatus(DriverStatus.CLEANUP)

    def doCleanup(self):
        print("doCleanup executed")
        try:
            # Close sockets
            if self.udp_socket:
                self.udp_socket.close()
            if self.plc_socket:
                self.plc_socket.close()
            if self.tcp_socket:
                self.tcp_socket.close()
            # Reset attirbutes
            self.plc_address = ""
            self.io_seq = 0
            self.cip_counter = -1
            self.id_io = ""
            self.write_data = "0"
            self.read_data = "0"
            self.input_data = ""
            for _b in range(0, self.write_size):
                self.input_data += '{:02x}'.format(0)

        except Exception as e:
            print("Exception in doCleanup")
            self.sendDebugInfo('Exception during cleanup: ' + str(e))
        finally:
            self.changeStatus(DriverStatus.SETUP)