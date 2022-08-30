import win32service
import win32serviceutil

# print(win32service.SERVICE_RUNNING)       # - 4
# print(win32service.SERVICE_STOPPED)       # - 1
# print(win32service.SERVICE_START_PENDING) # - 2 
# print(win32service.SERVICE_STOP_PENDING)  # - 3

def GetServiceName(names):
    for name in names:
        try:
            win32serviceutil.QueryServiceStatus(name, None)
        except:
            continue
        else:    
            return name
    return None


possible_service_names = ["s7oiehsx", "s7oiehsx64"]
service_name = GetServiceName(possible_service_names)

if service_name:
   print("service_name")
