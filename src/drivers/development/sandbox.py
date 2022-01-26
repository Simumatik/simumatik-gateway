from multiprocessing import shared_memory
#import numpy as np
import struct
#import time

BIG_ENDIAN = False
def SetFormatString():
    format = ''
    if BIG_ENDIAN:
        format += '!'


shm_a = shared_memory.SharedMemory(name='SIMITShared Memory')
buffer = shm_a.buf
bytes = shm_a.buf.tobytes()
#area = np.ndarray(shm_a.size, dtype=np.uint8, buffer=shm_a.buf)


header = bytes[:8]
memory_size, header_size = struct.unpack('II', header)
# print(memory_size)
# print(header_size)
print(bytes[:memory_size])


# Word
start_adr = 12
len = 2
value = 255
new_bytes = struct.pack('H', value)

shm_a.buf[12:14] = new_bytes


#print(new_bytes)
#print(bytes[start_adr:start_adr+len])
test = b''.join([bytes[:12], new_bytes, bytes[14:]])
print(test[:memory_size])

# print(bytes.__len__())
# print(test.__len__())
quit()


if header_size != 8: #Header includes Signal information.
    m = bytes[16]
    start_signal1 = 17 + m
    s = bytes[start_signal1]
    packed = bytes[start_signal1:24+m+s+1]
    print(packed)
    #print(len(packed))
    values = struct.unpack('B10sIBB', packed)
    print(values)


# Word
start_adr = 8
len = 2
values = bytes[start_adr:start_adr+len] 
value = struct.unpack('!H',values)
print(value[0])

# Real
start_adr = 16
len = 4
values = bytes[start_adr:start_adr+len]
value = struct.unpack('!f',values)
print(value[0])

# Byte
start_adr = 24
len = 1
values = bytes[start_adr:start_adr+len]
value = struct.unpack('!B',values)
print(value[0])