import clr
import os
import sys
import time
import win32service
import win32serviceutil
import socket

def GetServiceName(names):
    for name in names:
        try:
            win32serviceutil.QueryServiceStatus(name, None)
        except:
            continue
        else:    
            return name
    return None

def GetStatus(name):
    try:
        state = win32serviceutil.QueryServiceStatus(name, None)[1]
    except:
        return None
    else: 
        return state

print("Has to be ran as admin..")

p = os.path.dirname(os.path.abspath(__file__))
sys.path.append(p)

clr.FindAssembly("IsoToS7online")
clr.AddReference("IsoToS7online")
from IsoOnTcp import IsoToS7online

clr.AddReference('System.Net')
from System.Net import IPAddress



# Get service status
possible_service_names = ["s7oiehsx", "s7oiehsx64"]
service_name = GetServiceName(possible_service_names)
if service_name:
    print("service found")
    if GetStatus(service_name) == win32service.SERVICE_RUNNING:
        print("service is running")
    else:
        print("service is not running")
else:
    print("service not found")


# Stop service
print(f"Stopping server {service_name}")
win32serviceutil.StopService(service_name)

while GetStatus(service_name) != win32service.SERVICE_STOPPED:
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
print(f"Restarting server {service_name}")
win32serviceutil.RestartService(service_name)

while GetStatus(service_name) != win32service.SERVICE_RUNNING:
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