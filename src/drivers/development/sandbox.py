import clr
import os
import sys
import time
import psutil
import win32serviceutil
import socket

print("Has to be ran as admin..")

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


print(service)

# Stop service
print(f"Stopping server {service['name']}")
win32serviceutil.StopService(service['name'])

while service['status'] != "stopped":
    service = psutil.win_service_get(service['name'])
    service = service.as_dict()
    print("service not stopped")
    time.sleep(0.5)
print("service is stopped")

# Get port 102
print("Starting socket on port 102") 
s = None
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("192.168.1.192", 102))
    s.listen()
    s.setblocking(False)
except Exception as e:
    print(f"Exception during get 102: {e}")

# Restart service
print(f"Restarting server {service['name']}")
win32serviceutil.RestartService(service['name'])

while service['status'] != "running":
    service = psutil.win_service_get(service['name'])
    service = service.as_dict()
    print("service not running")
    time.sleep(0.5)
print("service is running again")

# Close port
print(f"closing socket on port 102.")
s.close()


#Start IsToS7online server:
NAME = "PLC#001"
NETWORKIPADRESS = IPAddress.Parse("192.168.1.192")
PLCSIMIPADRESS = IPAddress.Parse("192.168.0.1")
RACK = 0
SLOT = 1
ENABLETSAPCHECK = False

print("create server")
server = IsoToS7online(ENABLETSAPCHECK)


try:
    print("start server")
    server.start(NAME, NETWORKIPADRESS, PLCSIMIPADRESS, RACK, SLOT)
except Exception as e:
    print(f"Except! {e}")
else:
    print("server started")


user_input = input("Press any key to stop server...")
server.Dispose()
print("Server stopped")