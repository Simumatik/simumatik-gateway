import sys 
import os
import clr
import time

NAME = "safetytest" #"drivertest"

p = os.path.dirname(os.path.abspath(__file__))
sys.path.append(p)


if sys.maxsize > 2**32: # 64-Bit OS
    clr.FindAssembly("Siemens.Simatic.Simulation.Runtime.Api.x64")
    clr.AddReference("Siemens.Simatic.Simulation.Runtime.Api.x64")
else: # 32-Bit OS
    clr.FindAssembly("Siemens.Simatic.Simulation.Runtime.Api.x86")
    clr.AddReference("Siemens.Simatic.Simulation.Runtime.Api.x86")

from Siemens.Simatic.Simulation.Runtime import SimulationRuntimeManager

if SimulationRuntimeManager.RegisteredInstanceInfo.Length < 1:
    print("No PLC Sim advanced instance running")
else:
    for instance in SimulationRuntimeManager.RegisteredInstanceInfo:
        if instance.Name == NAME:
            print("PLCSimAdvanced Instance found")

            connection = SimulationRuntimeManager.CreateInterface(NAME)
            
            # # Get operating state
            # state = connection.OperatingState
            # print(state)

            # connection.UpdateTagList()

            # data = connection.TagInfos
            # print(data.Length)

            # for tag in connection.TagInfos:
            #     print(f"{tag.ToString()} {tag.PrimitiveDataType}")

            for i in range(10):
                connection.WriteBool('"ESTOP Ch1"', i%2==0)
                connection.WriteBool("TestHighSafe", i%2==0)
                connection.WriteBool("TestHigherSafe", i%2==0)
                connection.WriteBool("Reset_Safety", i%2==0)
                time.sleep(1)



    

