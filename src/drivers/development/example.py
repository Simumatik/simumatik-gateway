import OpenOPC

gateway='testbox'
opchost='testbox'
opcserv='Matrikon.OPC.Simulation.1'
taglist =['Random.Int4','Random.Real4']

print('Connecting to Gateway Server on: ' + gateway)

opc = OpenOPC.client()
opc.connect(opcserv)
v = opc.read(taglist)
print(v)

opc.close()
for i in range(len(v)):
    (name, val, qual, time) = v[i]
    print('%-15s %-15s %-15s %-15s'%(name,val,qual,time))