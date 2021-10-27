import pyads

plc = pyads.Connection('192.168.1.160.1.1', pyads.PORT_TC3PLC1)
plc.open()
print(plc.read_state())

#print(1863*8+1)
#plc.write(pyads.INDEXGROUP_DATA, 554749, True, pyads.PLCTYPE_BOOL)
plc.write_by_name("ConveyorControl.vulcanConveyor.conveyorIndexer.indexerPistonsControl[0].sensors[2].hardwareInput", True)

#symbols = plc.get_symbol("ConveyorControl.vulcanConveyor.conveyorIndexer.indexerPistonsControl[0].sensors[2].hardwareInput")
#print(symbols)

plc.close()

