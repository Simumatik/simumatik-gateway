from multiprocessing import shared_memory
import numpy as np
import struct
import time


shm_a = shared_memory.SharedMemory(name='SIMITShared Memory')
c = np.ndarray(shm_a.size, dtype=np.uint8, buffer=shm_a.buf)
print(c[:200])

header = b''.join(c[:8])
memory_size, header_size = struct.unpack('II', header)
print(memory_size)
print(header_size)


if header_size != 8: #Header includes Signal information.
    m = c[16]
    start_signal1 = 17 + m
    s = c[start_signal1]
    packed = b''.join(c[start_signal1:24+m+s+1])
    print(packed)
    #print(len(packed))
    values = struct.unpack('B10sIBB', packed)
    print(values)



else: #No signal information in header
    # Word
    start_adr = 8
    len = 2
    values = c[start_adr:start_adr+len] 
    packed = b''.join(values)
    value = struct.unpack('!H',packed)
    print(value[0])

    # Real
    start_adr = 16
    len = 4
    values = c[start_adr:start_adr+len]
    #print(values)
    packed = b''.join(values)
    #print(packed)
    value = struct.unpack('!f',packed)
    print(value[0])

    # Byte
    start_adr = 24
    len = 1
    values = c[start_adr:start_adr+len]
    #print(values)
    packed = b''.join(values)
    #print(packed)
    value = struct.unpack('!B',packed)
    print(value[0])