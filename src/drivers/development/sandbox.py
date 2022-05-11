import OpenOPC
import pywintypes # To avoid timeout error
pywintypes.datetime=pywintypes.TimeType

# tagname = 'GP2.bool'
# opcserv = 'Matrikon.OPC.Simulation.1'
# opc = OpenOPC.client()
# print(opc.servers())

# while True:
#     opc.connect(opcserv)
#     print(opc.read(tagname))
#     opc.close()
#     # print(opc.list())
#     # print(opc.list('Configured Aliases'))
#     # print('hit')

# # try:
# #     (opcvalue,opcstat,opctime) = opc.read(tagname)
# # except:
# #     print('hej')

def readopc():
    opchost = 'localhost'
    taglist = ['Random.Int1']
    opc = OpenOPC.open_client(host = opchost)
    opc.connect()
    while True:
        v = opc.read(taglist)
        for i in range(len(v)):
            (name, val, qual, time) = v[i]
            print('% -15s % -15s % -15s % -15s'% (name, val, qual, time))
if __name__=='__main__':
    readopc()