# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 3.8.10 (tags/v3.8.10:3d8993a, May  3 2021, 11:34:34) [MSC v.1928 32 bit (Intel)]
# From type library 's7wspsmx.dll'
# On Fri May 20 13:39:00 2022
'Siemens S7ProSim COM Object'
makepy_version = '0.5.01'
python_version = 0x3080af0

import win32com.client.CLSIDToClass, pythoncom, pywintypes
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch

# The following 3 lines may need tweaking for the particular server
# Candidates are pythoncom.Missing, .Empty and .ArgNotFound
defaultNamedOptArg=pythoncom.Empty
defaultNamedNotOptArg=pythoncom.Empty
defaultUnnamedArg=pythoncom.Empty

CLSID = IID('{83CC0D80-FEDA-11D1-BE76-0060B06816CF}')
MajorVersion = 1
MinorVersion = 0
LibraryFlags = 8
LCID = 0x0

class constants:
	ContinuousScan                =1          # from enum __MIDL___MIDL_itf_S7wspsmx_0000_0000_0001
	SingleScan                    =0          # from enum __MIDL___MIDL_itf_S7wspsmx_0000_0000_0001
	S7Byte                        =2          # from enum __MIDL___MIDL_itf_S7wspsmx_0000_0000_0002
	S7DoubleWord                  =4          # from enum __MIDL___MIDL_itf_S7wspsmx_0000_0000_0002
	S7Word                        =3          # from enum __MIDL___MIDL_itf_S7wspsmx_0000_0000_0002
	S7_Bit                        =1          # from enum __MIDL___MIDL_itf_S7wspsmx_0000_0000_0003
	S7_Byte                       =2          # from enum __MIDL___MIDL_itf_S7wspsmx_0000_0000_0003
	S7_DoubleWord                 =4          # from enum __MIDL___MIDL_itf_S7wspsmx_0000_0000_0003
	S7_Word                       =3          # from enum __MIDL___MIDL_itf_S7wspsmx_0000_0000_0003
	Disabled                      =2          # from enum __MIDL___MIDL_itf_S7wspsmx_0000_0000_0004
	Paused                        =1          # from enum __MIDL___MIDL_itf_S7wspsmx_0000_0000_0004
	Running                       =0          # from enum __MIDL___MIDL_itf_S7wspsmx_0000_0000_0004
	ColdStart                     =2          # from enum __MIDL___MIDL_itf_S7wspsmx_0000_0000_0005
	HotStart                      =1          # from enum __MIDL___MIDL_itf_S7wspsmx_0000_0000_0005
	WarmStart                     =0          # from enum __MIDL___MIDL_itf_S7wspsmx_0000_0000_0005

from win32com.client import DispatchBaseClass
class IS7ProSim(DispatchBaseClass):
	'IS7ProSim Interface for S7ProSim COM Object'
	CLSID = IID('{83CC0D81-FEDA-11D1-BE76-0060B06816CF}')
	coclass_clsid = IID('{83CC0D83-FEDA-11D1-BE76-0060B06816CF}')

	def BeginScanNotify(self):
		'Register for scan notifications.'
		return self._oleobj_.InvokeTypes(8, LCID, 1, (24, 0), (),)

	def Connect(self):
		'Connect to Control Engine with instance number one.'
		return self._oleobj_.InvokeTypes(6, LCID, 1, (24, 0), (),)

	def ConnectExt(self, InstanceNumber=defaultNamedNotOptArg):
		'Connect to Control Engine with instance number.'
		return self._oleobj_.InvokeTypes(29, LCID, 1, (24, 0), ((3, 1),),InstanceNumber
			)

	def Continue(self):
		'UnPause the CPU'
		return self._oleobj_.InvokeTypes(15, LCID, 1, (24, 0), (),)

	def Disconnect(self):
		'Disconnect from Control Engine.'
		return self._oleobj_.InvokeTypes(7, LCID, 1, (24, 0), (),)

	def EndScanNotify(self):
		'Unregister for scan notifications.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (24, 0), (),)

	def ExecuteNScans(self, NScanNumber=defaultNamedNotOptArg):
		'Cause N single scan cycles to execute.'
		return self._oleobj_.InvokeTypes(11, LCID, 1, (24, 0), ((3, 1),),NScanNumber
			)

	def ExecuteNmsScan(self, MsNumber=defaultNamedNotOptArg):
		'Cause scan N milli-seconds then stop.'
		return self._oleobj_.InvokeTypes(10, LCID, 1, (24, 0), ((3, 1),),MsNumber
			)

	def ExecuteSingleScan(self):
		'Cause a single scan cycle to execute.'
		return self._oleobj_.InvokeTypes(5, LCID, 1, (24, 0), (),)

	def GetPauseState(self):
		'Returns the current state (Running or Paused) of Control Engine'
		return self._oleobj_.InvokeTypes(16, LCID, 1, (3, 0), (),)

	def GetScanMode(self):
		'Returns the current Control Engine scan mode.'
		return self._oleobj_.InvokeTypes(12, LCID, 1, (3, 0), (),)

	def GetStartUpSwitch(self):
		'Get Startup Switch Postion'
		return self._oleobj_.InvokeTypes(23, LCID, 1, (3, 0), (),)

	def GetState(self):
		'Returns the current CPU state.'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(19, LCID, 1, (8, 0), (),)

	def HotStartWithSavedValues(self, val=defaultNamedNotOptArg):
		'HotStart will maintain IO values'
		return self._oleobj_.InvokeTypes(18, LCID, 1, (24, 0), ((3, 1),),val
			)

	def Pause(self):
		'Pause the CPU'
		return self._oleobj_.InvokeTypes(14, LCID, 1, (24, 0), (),)

	def ReadDataBlockValue(self, BlockNum=defaultNamedNotOptArg, ByteIndex=defaultNamedNotOptArg, BitIndex=defaultNamedNotOptArg, DataType=defaultNamedNotOptArg
			, pData=defaultNamedNotOptArg):
		'Reads single bit, byte, word, or double word from a Control Engine Data Block.'
		return self._ApplyTypes_(24, 1, (24, 0), ((3, 1), (3, 1), (3, 1), (3, 1), (16396, 3)), 'ReadDataBlockValue', None,BlockNum
			, ByteIndex, BitIndex, DataType, pData)

	def ReadFlagValue(self, ByteIndex=defaultNamedNotOptArg, BitIndex=defaultNamedNotOptArg, DataType=defaultNamedNotOptArg, pData=defaultNamedNotOptArg):
		'Reads single bit, byte, word, or double word from the Control Engine Flag memory.'
		return self._ApplyTypes_(26, 1, (24, 0), ((3, 1), (3, 1), (3, 1), (16396, 3)), 'ReadFlagValue', None,ByteIndex
			, BitIndex, DataType, pData)

	def ReadOutputImage(self, StartIndex=defaultNamedNotOptArg, ElementsToRead=defaultNamedNotOptArg, DataType=defaultNamedNotOptArg, pData=defaultNamedNotOptArg):
		'Reads data from Control Engine Output memory image.'
		return self._ApplyTypes_(1, 1, (24, 0), ((3, 1), (3, 1), (3, 1), (16396, 3)), 'ReadOutputImage', None,StartIndex
			, ElementsToRead, DataType, pData)

	def ReadOutputPoint(self, ByteIndex=defaultNamedNotOptArg, BitIndex=defaultNamedNotOptArg, DataType=defaultNamedNotOptArg, pData=defaultNamedNotOptArg):
		'Reads single bit, byte, word, or double word from Control Engine Output memory image.'
		return self._ApplyTypes_(3, 1, (24, 0), ((3, 1), (3, 1), (3, 1), (16396, 3)), 'ReadOutputPoint', None,ByteIndex
			, BitIndex, DataType, pData)

	def SavePLC(self, FileName=defaultNamedNotOptArg):
		'method SavePLC'
		return self._oleobj_.InvokeTypes(17, LCID, 1, (24, 0), ((8, 1),),FileName
			)

	def SetScanMode(self, newVal=defaultNamedNotOptArg):
		'Sets the current Control Engine scan mode.'
		return self._oleobj_.InvokeTypes(13, LCID, 1, (24, 0), ((3, 1),),newVal
			)

	def SetStartUpSwitch(self, postion=defaultNamedNotOptArg):
		'Set Startup Switch Postion'
		return self._oleobj_.InvokeTypes(22, LCID, 1, (24, 0), ((3, 1),),postion
			)

	def SetState(self, newVal=defaultNamedNotOptArg):
		'Sets the current CPU state.'
		return self._oleobj_.InvokeTypes(20, LCID, 1, (24, 0), ((8, 1),),newVal
			)

	def StartPLCSim(self, plcFile=defaultNamedNotOptArg):
		'Start PLCSim'
		return self._oleobj_.InvokeTypes(21, LCID, 1, (24, 0), ((8, 1),),plcFile
			)

	def StartPLCSimExt(self, plcFile=defaultNamedNotOptArg):
		'Start PLCSim instances'
		return self._oleobj_.InvokeTypes(30, LCID, 1, (24, 0), ((8, 1),),plcFile
			)

	def WriteDataBlockValue(self, BlockNum=defaultNamedNotOptArg, ByteIndex=defaultNamedNotOptArg, BitIndex=defaultNamedNotOptArg, pData=defaultNamedNotOptArg):
		'Writes single bit, byte, word, or double word to a Control Engine Data Block.'
		return self._oleobj_.InvokeTypes(25, LCID, 1, (24, 0), ((3, 1), (3, 1), (3, 1), (16396, 1)),BlockNum
			, ByteIndex, BitIndex, pData)

	def WriteFlagValue(self, ByteIndex=defaultNamedNotOptArg, BitIndex=defaultNamedNotOptArg, pData=defaultNamedNotOptArg):
		'Writes single bit, byte, word, or double word to the Control Engine Flag memory.'
		return self._oleobj_.InvokeTypes(27, LCID, 1, (24, 0), ((3, 1), (3, 1), (16396, 1)),ByteIndex
			, BitIndex, pData)

	def WriteInputImage(self, StartIndex=defaultNamedNotOptArg, pData=defaultNamedNotOptArg):
		'Writes data to the Control Engine Input memory image.'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (24, 0), ((3, 1), (16396, 1)),StartIndex
			, pData)

	def WriteInputPoint(self, ByteIndex=defaultNamedNotOptArg, BitIndex=defaultNamedNotOptArg, pData=defaultNamedNotOptArg):
		'Writes single bit, byte, word, or double word to the Control Engine Input memory image.'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (24, 0), ((3, 1), (3, 1), (16396, 1)),ByteIndex
			, BitIndex, pData)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

from win32com.client import CoClassBaseClass
# This CoClass is known by the name 'S7wspsmx.S7ProSim.1'
class S7ProSim(CoClassBaseClass): # A CoClass
	# S7ProSim Class
	CLSID = IID('{83CC0D83-FEDA-11D1-BE76-0060B06816CF}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IS7ProSim,
	]
	default_interface = IS7ProSim

IS7ProSim_vtables_dispatch_ = 1
IS7ProSim_vtables_ = [
	(( 'ReadOutputImage' , 'StartIndex' , 'ElementsToRead' , 'DataType' , 'pData' , 
			 ), 1, (1, (), [ (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (16396, 3, None, None) , ], 1 , 1 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'WriteInputImage' , 'StartIndex' , 'pData' , ), 2, (2, (), [ (3, 1, None, None) , 
			 (16396, 1, None, None) , ], 1 , 1 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'ReadOutputPoint' , 'ByteIndex' , 'BitIndex' , 'DataType' , 'pData' , 
			 ), 3, (3, (), [ (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (16396, 3, None, None) , ], 1 , 1 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'WriteInputPoint' , 'ByteIndex' , 'BitIndex' , 'pData' , ), 4, (4, (), [ 
			 (3, 1, None, None) , (3, 1, None, None) , (16396, 1, None, None) , ], 1 , 1 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'ExecuteSingleScan' , ), 5, (5, (), [ ], 1 , 1 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'Connect' , ), 6, (6, (), [ ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'Disconnect' , ), 7, (7, (), [ ], 1 , 1 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( 'BeginScanNotify' , ), 8, (8, (), [ ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'EndScanNotify' , ), 9, (9, (), [ ], 1 , 1 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( 'ExecuteNmsScan' , 'MsNumber' , ), 10, (10, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'ExecuteNScans' , 'NScanNumber' , ), 11, (11, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( 'GetScanMode' , 'pVal' , ), 12, (12, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'SetScanMode' , 'newVal' , ), 13, (13, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( 'Pause' , ), 14, (14, (), [ ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Continue' , ), 15, (15, (), [ ], 1 , 1 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( 'GetPauseState' , 'pVal' , ), 16, (16, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'SavePLC' , 'FileName' , ), 17, (17, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 92 , (3, 0, None, None) , 0 , )),
	(( 'HotStartWithSavedValues' , 'val' , ), 18, (18, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'GetState' , 'pVal' , ), 19, (19, (), [ (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 100 , (3, 0, None, None) , 0 , )),
	(( 'SetState' , 'newVal' , ), 20, (20, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'StartPLCSim' , 'plcFile' , ), 21, (21, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 108 , (3, 0, None, None) , 0 , )),
	(( 'SetStartUpSwitch' , 'postion' , ), 22, (22, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'GetStartUpSwitch' , 'pPos' , ), 23, (23, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 116 , (3, 0, None, None) , 0 , )),
	(( 'ReadDataBlockValue' , 'BlockNum' , 'ByteIndex' , 'BitIndex' , 'DataType' , 
			 'pData' , ), 24, (24, (), [ (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , 
			 (3, 1, None, None) , (16396, 3, None, None) , ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'WriteDataBlockValue' , 'BlockNum' , 'ByteIndex' , 'BitIndex' , 'pData' , 
			 ), 25, (25, (), [ (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (16396, 1, None, None) , ], 1 , 1 , 4 , 0 , 124 , (3, 0, None, None) , 0 , )),
	(( 'ReadFlagValue' , 'ByteIndex' , 'BitIndex' , 'DataType' , 'pData' , 
			 ), 26, (26, (), [ (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (16396, 3, None, None) , ], 1 , 1 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'WriteFlagValue' , 'ByteIndex' , 'BitIndex' , 'pData' , ), 27, (27, (), [ 
			 (3, 1, None, None) , (3, 1, None, None) , (16396, 1, None, None) , ], 1 , 1 , 4 , 0 , 132 , (3, 0, None, None) , 0 , )),
	(( 'ConnectExt' , 'InstanceNumber' , ), 29, (29, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'StartPLCSimExt' , 'plcFile' , ), 30, (30, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 140 , (3, 0, None, None) , 0 , )),
]

IS7ProSimEvents_vtables_dispatch_ = 0
IS7ProSimEvents_vtables_ = [
	(( 'ScanFinished' , 'ScanInfo' , ), 1, (1, (), [ (12, 0, None, None) , ], 1 , 1 , 4 , 0 , 12 , (3, 0, None, None) , 0 , )),
	(( 'ConnectionError' , 'ControlEngine' , 'Error' , ), 2, (2, (), [ (8, 0, None, None) , 
			 (3, 0, None, None) , ], 1 , 1 , 4 , 0 , 16 , (3, 0, None, None) , 0 , )),
	(( 'PLCSimStateChanged' , 'NewState' , ), 3, (3, (), [ (8, 0, None, None) , ], 1 , 1 , 4 , 0 , 20 , (3, 0, None, None) , 0 , )),
	(( 'PauseStateChanged' , 'NewState' , ), 4, (4, (), [ (8, 0, None, None) , ], 1 , 1 , 4 , 0 , 24 , (3, 0, None, None) , 0 , )),
	(( 'ScanModeChanged' , 'NewState' , ), 5, (5, (), [ (8, 0, None, None) , ], 1 , 1 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
]

RecordMap = {
}

CLSIDToClassMap = {
	'{83CC0D81-FEDA-11D1-BE76-0060B06816CF}' : IS7ProSim,
	'{83CC0D83-FEDA-11D1-BE76-0060B06816CF}' : S7ProSim,
}
CLSIDToPackageMap = {}
win32com.client.CLSIDToClass.RegisterCLSIDsFromDict( CLSIDToClassMap )
VTablesToPackageMap = {}
VTablesToClassMap = {
	'{83CC0D82-FEDA-11D1-BE76-0060B06816CF}' : 'IS7ProSimEvents',
	'{83CC0D81-FEDA-11D1-BE76-0060B06816CF}' : 'IS7ProSim',
}


NamesToIIDMap = {
	'IS7ProSim' : '{83CC0D81-FEDA-11D1-BE76-0060B06816CF}',
	'IS7ProSimEvents' : '{83CC0D82-FEDA-11D1-BE76-0060B06816CF}',
}

win32com.client.constants.__dicts__.append(constants.__dict__)

