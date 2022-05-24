# import win32com.client
# prosim = win32com.client.Dispatch("S7wspsmx.S7ProSim.1")
# prosim.Connect() # Connect to Plcsim
# print ("PLCSIM status: " + prosim.GetState())
# print("MW0 = " + str(prosim.ReadFlagValue(0, 0, win32com.client.constants.S7_Word, None)))
# prosim.Disconnect()

# from wrappertest2 import *

# prosim = SimProjE()
# print(prosim.ConnectionExists())
# #print(prosim.GetNodeCount())
# #prosim.Continue()
# #prosim.SetScanMode(constants.ContinuousScan);     
# print ("PLCSIM status: " + prosim.GetState())
# prosim.Disconnect()

import clr
import os
import sys


p = os.path.dirname(os.path.abspath(__file__))
sys.path.append(p)

clr.FindAssembly("IsoToS7online")
clr.AddReference("IsoToS7online")

from IsoOnTcp import IsoToS7online

server = IsoToS7online(True)


print("reached here")