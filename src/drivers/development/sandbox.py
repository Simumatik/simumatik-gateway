import OpenOPC
import pywintypes # To avoid timeout error
pywintypes.datetime=pywintypes.TimeType

tags = ['GP2.bool', "GP2.int"]
opcserv = 'Matrikon.OPC.Simulation.1'

opc = OpenOPC.client()

num = 0
while True:
    opc.connect(opcserv)
    value = opc[tags[0]]
    value, quality, time = opc.read('GP2.bool1')
    success = opc.write(("GP2.wint", num))
    opc[tags[0]] = value
    num += 1
    opc.close()
