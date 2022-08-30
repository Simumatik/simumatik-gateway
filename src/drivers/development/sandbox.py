import clr
import os
import sys
import time

p = os.path.dirname(os.path.abspath(__file__))
sys.path.append(p)

clr.FindAssembly("IsoToS7online")
clr.AddReference("IsoToS7online")
from IsoOnTcp import IsoToS7online

clr.AddReference('System.Net')
from System.Net import IPAddress


NAME = "PLC#001"
NETWORKIPADRESS = IPAddress.Parse("192.168.1.192")
PLCSIMIPADRESS = IPAddress.Parse("192.168.0.1")
RACK = 0
SLOT = 1
ENABLETSAPCHECK = False

server = IsoToS7online(ENABLETSAPCHECK)
print("reached 1")

# Stop S7 service



try:
    server.start(NAME, NETWORKIPADRESS, PLCSIMIPADRESS, RACK, SLOT)
except Exception as e:
    print(f"Except! {e}")
else:
    print("server started")

time.sleep(120)


server.Dispose()

# Restart S7 service

print("reached 3")