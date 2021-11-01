FANUC_API_FOUND = True
try:
    from fanuc_wrapper import *
except:
    FANUC_API_FOUND = False

assert FANUC_API_FOUND, "Fanuc is not installed"


import time

# Create API Instance
mobjRobot = FRCRobot()

# Connect
ip = '127.0.0.1'
try:
    mobjRobot.ConnectEx(HostName=ip, NoWait=False, NumRetries=1, Period=1)#, NoWait=False)
    print(mobjRobot.HostName)
    print(mobjRobot.IsOffline)
except:
    print("Connection failed! Client not found")
    exit(-1)
    
assert mobjRobot.IsConnected, f"Cannot coonect to {ip}" 
# TODO: Check if it is possible to connect to other computer using Neighboughood...

# Get/set registers (NOT ACTUALY USED)
write_value = 8
reg_value = 5
mobjRobot.RegNumerics(reg_value).Value.RegLong = write_value
#read_value = mobjRobot.RegNumerics(reg_value).Value.RegFloat
read_value = mobjRobot.RegNumerics(reg_value).Value.RegLong

# Read current Joint position
mobjCurPos = mobjRobot.CurPosition
assert mobjCurPos.NumGroups>0, "Joint positions not available"
print("Goups found:", mobjCurPos.NumGroups)
mobjCurGrpPos = mobjCurPos.Group(1, constants.frJointDisplayType)
mjointPos = mobjCurGrpPos.Formats(constants.frJoint)

# Periodically read position
axis_num = 2
while time.perf_counter()<3:
    mobjCurGrpPos.Refresh() # This seems necessary to update the values
    print(mjointPos.Item(axis_num)) # This returns the specific axis value

    time.sleep(0.1)

# Write input signals
mobjInSignals = mobjRobot.IOTypes(constants.frDInType).Signals
port_number = 1
mobjInSignals(port_number).Simulate = True # Necessary to allow setting values, Do it first time
mobjInSignals(port_number).Value = True

# Read output signals
mobjOutSignals = mobjRobot.IOTypes(constants.frDOutType).Signals
##mobjOutSignals.Refresh() # Check if necessary
port_number = 1
print(mobjOutSignals(port_number).Value)

# Write input group
"""
mobjInGroups = mobjRobot.IOTypes(constants.frGPInType)
print(mobjInGroups.__class__.__name__)
print(mobjInGroups.Signals.__class__.__name__)
print(mobjInGroups.Groups.__class__.__name__)
group_number = 1
mobjInGroups(group_number).Simulate = True # Necessary to allow setting values, Do it first time
mobjInGroups(group_number).Value = 5

# Read output group
mobjOutGroup = mobjRobot.IOTypes(constants.frGPOutType).Signals
##mobjOutSignals.Refresh() # Check if necessary
group_number = 1
print(mobjOutGroup(group_number).Value)
"""



