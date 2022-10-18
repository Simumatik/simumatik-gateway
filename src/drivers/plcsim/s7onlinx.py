import struct

class UserDataConnectionConfig:
    routing_enabled = 0x00
    b01 = 0x00
    b02 = 0x00
    b03 = 0x00
    b04 = 0x00
    b05 = 0x00
    b06 = 0x00
    b07 = 0x00
    b08 = 0x00
    destination_1 = 0x00
    destination_2 = 0x00
    destination_3 = 0x00
    destination_4 = 0x00
    b13 = 0x00
    b14 = 0x00
    b15 = 0x00
    b16 = 0x00
    b17 = 0x00
    connection_type = 0x00
    rack_slot = 0x00
    b20 = 0x00
    size_to_end = 0x00
    size_of_subnet = 0x00
    subnet_1 = 0x00
    subnet_2 = 0x00
    b25 = 0x00
    b26 = 0x00
    subnet_3 = 0x00
    subnet_4 = 0x00
    size_of_routing_destination = 0x00
    routing_destination_1 = 0x00
    routing_destination_2 = 0x00
    routing_destination_3 = 0x00
    routing_destination_4 = 0x00

    def __init__(self, ip:str, slot:int, rack:int):
        self.b01 = 0x02
        self.b02 = 0x01
        self.b04 = 0x0C
        self.b05 = 0x01
        self.b15 = 0x01
        self.b17 = 0x02
        self.rack_slot = (slot + rack * 32)
        self.connection_type = 1
        m_PlcIPAddress = ip.split('.')
        self.destination_1 = int(m_PlcIPAddress[0])
        self.destination_2 = int(m_PlcIPAddress[1])
        self.destination_3 = int(m_PlcIPAddress[2])
        self.destination_4 = int(m_PlcIPAddress[3])

    def to_buffer(self):
        buffer = struct.pack(
            '!BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB',
            self.routing_enabled,
            self.b01,
            self.b02,
            self.b03,
            self.b04,
            self.b05,
            self.b06,
            self.b07,
            self.b08,
            self.destination_1,
            self.destination_2,
            self.destination_3,
            self.destination_4,
            self.b13,
            self.b14,
            self.b15,
            self.b16,
            self.b17,
            self.connection_type,
            self.rack_slot,
            self.b20,
            self.size_to_end,
            self.size_of_subnet,
            self.subnet_1,
            self.subnet_2,
            self.b25,
            self.b26,
            self.subnet_3,
            self.subnet_4,
            self.size_of_routing_destination,
            self.routing_destination_1,
            self.routing_destination_2,
            self.routing_destination_3,
            self.routing_destination_4,
        )
        return (34, buffer)


class UserDataConnectionConfigTia:
    routing_enabled = 0x00
    b01 = 0x00
    b02 = 0x00
    b03 = 0x00
    b04 = 0x00
    b05 = 0x00
    b06 = 0x00
    b07 = 0x00
    b08 = 0x00
    destination_1 = 0x00
    destination_2 = 0x00
    destination_3 = 0x00
    destination_4 = 0x00
    b13 = 0x00
    b14 = 0x00
    b15 = 0x00
    b16 = 0x00
    accessname_length = 0x00
    accessname01 = 0x00
    accessname02 = 0x00
    accessname03 = 0x00
    accessname04 = 0x00
    accessname05 = 0x00
    accessname06 = 0x00
    accessname07 = 0x00
    accessname08 = 0x00
    accessname09 = 0x00
    accessname10 = 0x00
    accessname11 = 0x00
    accessname12 = 0x00
    accessname13 = 0x00
    accessname14 = 0x00
    accessname15 = 0x00
    accessname16 = 0x00

    def __init__(self, ip:str):
        self.b01 = 0x02
        self.b02 = 0x06
        self.b03 = 0x20
        self.b04 = 0x0C
        self.b05 = 0x01
        m_PlcIPAddress = ip.split('.')
        self.destination_1 = int(m_PlcIPAddress[0])
        self.destination_2 = int(m_PlcIPAddress[1])
        self.destination_3 = int(m_PlcIPAddress[2])
        self.destination_4 = int(m_PlcIPAddress[3])
        self.b15 = 0x01
        # theoretical this length is variable
        self.accessname_length = 16
        self.accessname01 = ord('S')
        self.accessname02 = ord('I')
        self.accessname03 = ord('M')
        self.accessname04 = ord('A')
        self.accessname05 = ord('T')
        self.accessname06 = ord('I')
        self.accessname07 = ord('C')
        self.accessname08 = ord('-')
        self.accessname09 = ord('R')
        self.accessname10 = ord('O')
        self.accessname11 = ord('O')
        self.accessname12 = ord('T')
        self.accessname13 = ord('-')
        self.accessname14 = ord('H')
        self.accessname15 = ord('M')
        self.accessname16 = ord('I')

    def to_buffer(self):
        buffer = struct.pack(
            '!BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB',
            self.routing_enabled,
            self.b01,
            self.b02,
            self.b03,
            self.b04,
            self.b05,
            self.b06,
            self.b07,
            self.b08,
            self.destination_1,
            self.destination_2,
            self.destination_3,
            self.destination_4,
            self.b13,
            self.b14,
            self.b15,
            self.b16,
            self.accessname_length,
            self.accessname01,
            self.accessname02,
            self.accessname03,
            self.accessname04,
            self.accessname05,
            self.accessname06,
            self.accessname07,
            self.accessname08,
            self.accessname09,
            self.accessname10,
            self.accessname11,
            self.accessname12,
            self.accessname13,
            self.accessname14,
            self.accessname15,
            self.accessname16
        )
        return (34, buffer)

class S7OexchangeBlock:
    # Header
    unknown = [0x0000]*2        # ushort[2],
    headerlength = 0x00         # byte, Length of the Request Block without Userdata_1 and 2 (80 Bytes!)
    user = 0x0000               # ushort, Application Specific
    rb_type = 0x02              # byte, Request Block type (always 2)
    priority = 0x00             # byte, Priority of the Task, identical like serv_class in the application block
    reserved_1 = 0x00           # byte, 
    reserved_2 = 0x0000         # ushort, 
    subsystem = 0x00            # byte, For FDL Communication this is 22h = 34
    opcode = 0x00               # byte, request, confirm, indication => same as opcode in application block
    response = 0x0000           # ushort, return-parameter => same as l_status in application block
    fill_length_1 = 0x0000      # ushort, 
    reserved_3 = 0x00           # byte, 
    seg_length_1 = 0x0000       # ushort, Length of Userdata_1
    offset_1 = 0x0050           # ushort, LEngth of header = 80 or 0x0050
    reserved_4 = 0x0000         # ushort,
    fill_length_2 = 0x0000      # ushort,
    reserved_5 = 0x00           # byte,
    seg_length_2 = 0x0000       # ushort,
    offset_2 = 0x0000           # ushort,
    reserved_6 = 0x0000         # ushort,
    # Application Block
    application_block_opcode = 0x00                 # byte, class of communication   (00 = request, 01=confirm, 02=indication)
    application_block_subsystem = 0x00              # byte, number of source-task (only necessary for MTK-user !!!!!)
    application_block_id = 0x0000                   # ushort, identification of FDL-USER
    application_block_service = 0x0000              # ushort, identification of service (00 -> SDA, send data with acknowlege)
    application_block_local_address_station = 0x00  # byte, only for network-connection !!!
    application_block_local_address_segment = 0x00  # byte, only for network-connection !!!
    application_block_ssap = 0x00                   # byte, source-service-access-point
    application_block_dsap = 0x00                   # byte, destination-service-access-point
    application_block_remote_address_station = 0x00 # byte, address of the remote-station
    application_block_remote_address_segment = 0x00 # byte, only for network-connection !!!
    application_block_service_class = 0x0000        # ushort, priority of service
    application_block_receive_l_sdu_buffer_ptr = 0  # int32, address and length of received netto-data, exception:
    application_block_receive_l_sdu_length = 0x00   # byte, address and length of received netto-data, exception:
    application_block_reserved_1 = 0x00             # byte, (reserved for FDL !!!!!!!!!!)
    application_block_reserved = 0x00               # byte, (reserved for FDL !!!!!!!!!!)
    application_block_send_l_sdu_buffer_ptr = 0     # int32, address and length of send-netto-data, exception:
    application_block_send_l_sdu_length = 0x00      # byte, address and length of send-netto-data, exception:
    application_block_l_status = 0x0000             # ushort, link-status of service or update_state for srd-indication
    application_block_reserved_2 = [0x0000]*2       # ushort[2], for concatenated lists       (reserved for FDL !!!!!!!!!!)
    # End Application block
    reserved = [0x00]*12                            # byte[12]
    reference = [0x00]*2                            # byte[2]
    # End of Header
    user_data_1 = None                              # byte[1024]

    def __init__(self, user=0, rb_type=2, subsystem=0x40, opcode=0, response=0xff, application_block_opcode=0xff, application_block_subsystem=0xff):
        self.headerlength = 80
        self.user = user
        self.rb_type = rb_type
        self.subsystem = subsystem
        self.opcode = opcode
        self.response = response
        self.application_block_opcode = application_block_opcode
        self.application_block_subsystem = application_block_subsystem    

    @classmethod
    def from_buffer(cls, buffer):
        ret = cls()
        assert len(buffer)>=80, "minimum length should be 80!"
        # header
        header = struct.unpack('=HHBHBBBHBBHHBHHHHBHHHBBHHBBBBBBHIBBBIBHHH',buffer[:66])
        ret.unknown[0] = header[0]
        ret.unknown[1] = header[1]
        ret.headerlength = header[2]
        ret.user = header[3]
        ret.rb_type = header[4]
        ret.priority = header[5]
        ret.reserved_1 = header[6] 
        ret.reserved_2 = header[7] 
        ret.subsystem = header[8]
        ret.opcode = header[9]
        ret.response = header[10]
        ret.fill_length_1 = header[11]
        ret.reserved_3 = header[12]
        ret.seg_length_1 = header[13]
        ret.offset_1 = header[14]
        ret.reserved_4 = header[15]
        ret.fill_length_2 = header[16]
        ret.reserved_5 = header[17]
        ret.seg_length_2 = header[18]
        ret.offset_2 = header[19]
        ret.reserved_6 = header[20]
        ret.application_block_opcode = header[21]
        ret.application_block_subsystem = header[22]
        ret.application_block_id = header[23]
        ret.application_block_service = header[24]
        ret.application_block_local_address_station = header[25]
        ret.application_block_local_address_segment = header[26]
        ret.application_block_ssap = header[27]
        ret.application_block_dsap = header[28]
        ret.application_block_remote_address_station = header[29]
        ret.application_block_remote_address_segment = header[30]
        ret.application_block_service_class = header[31]
        ret.application_block_receive_l_sdu_buffer_ptr = header[32]
        ret.application_block_receive_l_sdu_length = header[33]
        ret.application_block_reserved_1 = header[34]
        ret.application_block_reserved = header[35]
        ret.application_block_send_l_sdu_buffer_ptr = header[36]
        ret.application_block_send_l_sdu_length = header[37]
        ret.application_block_l_status = header[38]
        ret.application_block_reserved_2[0] = header[39]
        ret.application_block_reserved_2[1] = header[40]
        # Reserved
        ret.reserved = struct.unpack('!BBBBBBBBBBBB', buffer[66:78])
        # Reference
        ret.reference = struct.unpack('!BB', buffer[78:80])
        # User data
        if len(buffer)>80:
            ret.user_data_1 = buffer[80:len(buffer)]
        #print("received:", buffer.raw.hex())          
        return ret

    def to_buffer(self):
        buffer = struct.pack(
            '=HHBHBBBHBBHHBHHHHBHHHBBHHBBBBBBHIBBBIBHHH',
            self.unknown[0],
            self.unknown[1],
            self.headerlength,
            self.user,
            self.rb_type,
            self.priority,
            self.reserved_1, 
            self.reserved_2, 
            self.subsystem,
            self.opcode,
            self.response,
            self.fill_length_1,
            self.reserved_3,
            self.seg_length_1,
            self.offset_1,
            self.reserved_4,
            self.fill_length_2,
            self.reserved_5,
            self.seg_length_2,
            self.offset_2,
            self.reserved_6,
            self.application_block_opcode,
            self.application_block_subsystem,
            self.application_block_id,
            self.application_block_service,
            self.application_block_local_address_station,
            self.application_block_local_address_segment,
            self.application_block_ssap,
            self.application_block_dsap,
            self.application_block_remote_address_station,
            self.application_block_remote_address_segment,
            self.application_block_service_class,
            self.application_block_receive_l_sdu_buffer_ptr,
            self.application_block_receive_l_sdu_length,
            self.application_block_reserved_1,
            self.application_block_reserved,
            self.application_block_send_l_sdu_buffer_ptr,
            self.application_block_send_l_sdu_length,
            self.application_block_l_status,
            self.application_block_reserved_2[0],
            self.application_block_reserved_2[1],
        )
        # Reserved
        buffer += struct.pack('!BBBBBBBBBBBB', *self.reserved)
        # Reference
        buffer += struct.pack('!BB', self.reference[0], self.reference[1])
        # User data
        send_len = (self.headerlength + self.seg_length_1)
        if self.fill_length_1>0:
            buffer += self.user_data_1 # Should be a buffer
        buffer += b'\x00'*(1024-self.fill_length_1)
                
        #print("sent:", buffer.hex())          
        return (send_len, buffer)
    
    def set_user_data(self, length, buffer):
        self.user_data_1 = buffer
        self.fill_length_1 = length
        self.seg_length_1 = length