import OpenOPC

opc = OpenOPC.client()
print(opc.servers())
opc.connect('Matrikon.OPC.Simulation.1')
print(opc.list())
print(opc.list('Configured Aliases'))

print(opc.info())

opc.close()