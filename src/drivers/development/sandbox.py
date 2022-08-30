import clr
import os
import sys
import time
import psutil

p = os.path.dirname(os.path.abspath(__file__))
sys.path.append(p)

clr.FindAssembly("IsoToS7online")
clr.AddReference("IsoToS7online")
from IsoOnTcp import IsoToS7online

clr.AddReference('System.Net')
from System.Net import IPAddress

# Stop S7 service
possible_service_names = ["s7oiehsx64", "s7oiehsx"]
service = None
for name in possible_service_names:
    try:
        service = psutil.win_service_get(name)
        service = service.as_dict()
    except Exception as ex:
        print(str(ex))

    if service:
        break

if service:
    print("service found")
else:
    print("service not found")


if service and service['status'] == 'running':
    print("service is running")
else:
    print("service is not running")


#print(service)

# Get port 102

# Restart service

NAME = "PLC#001"
NETWORKIPADRESS = IPAddress.Parse("192.168.1.192")
PLCSIMIPADRESS = IPAddress.Parse("192.168.0.1")
RACK = 0
SLOT = 1
ENABLETSAPCHECK = False

server = IsoToS7online(ENABLETSAPCHECK)
print("reached 1")



try:
    server.start(NAME, NETWORKIPADRESS, PLCSIMIPADRESS, RACK, SLOT)
except Exception as e:
    print(f"Except! {e}")
else:
    print("server started")

time.sleep(120)


server.Dispose()

print("reached 3")