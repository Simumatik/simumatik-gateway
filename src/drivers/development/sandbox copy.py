import clr

clr.AddReference('System.Collections.Generic')
from System.Collections.Generic import *

RACK = 0
SLOT = 1

def CreateTSAP(rack, slot):
    return List[str](['a','list','of','strings'])

print(CreateTSAP(RACK, SLOT))