from multiprocessing import shared_memory
import numpy as np
import time
from drivers.s7protocol.iso_on_tcp import *
from drivers.driver import VariableDatatype

iolist ="""	IW0	InputWord	This is a comment
	I2.0	InputBool1	This is a comment
	I2.1	InputBool2	This is a comment
	QW4	OutputWord	This is a comment
	Q6.0	OutputBool	This is a comment"""

#variable_mapping = [x.strip().split('\t') for x in iolist.split('\n')]
variable_mapping = {x[1]:x[0] for x in [x.strip().split('\t') for x in iolist.split('\n')]}
# variable_mapping = {x[1]:x[0][1:] for x in [x.strip().split('\t') for x in iolist.split('\n')]}
print(variable_mapping)

def adress_to_byte_bit(adr:str):
  type = ""

  # Get the type (I, IB, IW, ID, Q, QB, QW, QD..)
  if adr[:2].isalpha():
    type = adr[:2]
    adr = adr[2:]
  elif adr[:1].isalpha():
    type = adr[:1]
    adr = adr[1:]

  if '.' in adr:
    adr = adr.split('.')
    return {"type" : type, "byte" : adr[0], "bit" : adr[1]}
  else:
    return {"type" : type, "byte" : adr[0]}

new_dict = {}
for key, value in variable_mapping.items():
  
  if 'Word' in key:
    vdtype = VariableDatatype.WORD
  else:
    vdtype = VariableDatatype.BOOL
  
  #new_dict[key] = adress_to_byte_bit(value)
  print(getAreaFromString(value, vdtype))
  quit()

print(new_dict)
quit()

existing_shm = shared_memory.SharedMemory(name='SIMITShared Memory')
c = np.ndarray((int(existing_shm.size/2),), dtype=np.int16, buffer=existing_shm.buf)
print(c[:8])



#c[5] = 1234

while True:
  testinput = c[4]
  #print(testinput, end="\r")
  print(c[:8], end="\r")
  testoutput = testinput + 1
  c[6] = testoutput
  testoutputBool = c[5]
  time.sleep(0.1)