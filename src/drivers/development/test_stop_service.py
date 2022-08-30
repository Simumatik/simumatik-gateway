import win32serviceutil
import time

service_name = "s7oiehsx64"

win32serviceutil.StopService(service_name)

print("service stopped")

time.sleep(5)


print("Service started")
