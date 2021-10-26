import pyads

# # create some constants for connection
# CLIENT_NETID = "192.168.1.160.1.1"
# CLIENT_IP = "192.168.1.160"
# TARGET_IP = "192.168.1.160"
# TARGET_USERNAME = "Administrator"
# TARGET_PASSWORD = "1"
# ROUTE_NAME = "route-to-my-plc"

# input("press any key..")

# # add a new route to the target plc
# pyads.add_route_to_plc(
#     CLIENT_NETID, CLIENT_IP, TARGET_IP, TARGET_USERNAME, TARGET_PASSWORD,
#     route_name=ROUTE_NAME
# )

print(pyads.PORT_TC3PLC1)

# connect to plc and open connection
# route is added automatically to client on Linux, on Windows use the TwinCAT router
plc = pyads.Connection('192.168.1.160.1.1', pyads.PORT_TC3PLC1)
plc.open()


# check the connection state
state = plc.read_state()
if state[0] == 5:
    print("5!!!!")
else:
    print("else....")


# read int value by name
i = plc.read_by_name("GVL.Digital_Out1")
print(i)

# write int value by name
plc.write_by_name("GVL.Digital_In1", False)

# # create a symbol that automatically updates to the plc value
# real_val = plc.get_symbol("GVL.real_val", auto_update=True)
# print(real_val.value)

# #42.0
# real_val.value = 5.0
# print(plc.read_by_name("GVL.real_val"))
# #5.0

# close connection
plc.close()