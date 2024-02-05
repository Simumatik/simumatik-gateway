import fins.udp
import time

fins_instance = fins.udp.UDPFinsConnection()
fins_instance.connect('192.168.0.1')
fins_instance.dest_node_add=1
fins_instance.srce_node_add=25

start = time.perf_counter()
counter = 0
WORD = 0
ADDRESS = WORD.to_bytes(2, 'big')+b'\x00'
VALUE = b'\x00\x1f'
AREA = fins.FinsPLCMemoryAreas().CIO_WORD #D: DATA_MEMORY_WORD, CIO:CIO_WORD, E:EM0_WORD, H:HOLDING_WORD, W:WORK_WORD
while time.perf_counter()-start<5:
    counter += 1
    VALUE = counter.to_bytes(2, 'big')
    fins_instance.memory_area_write(AREA,ADDRESS,VALUE,1)
    mem_area = fins_instance.memory_area_read(AREA,ADDRESS)
    
print(mem_area[-2:], int.from_bytes(mem_area[-2:], "big"))
print(time.perf_counter()-start, counter, round((time.perf_counter()-start)*1000/counter,2))