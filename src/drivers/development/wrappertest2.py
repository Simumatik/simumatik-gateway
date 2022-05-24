# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 3.8.10 (tags/v3.8.10:3d8993a, May  3 2021, 11:34:34) [MSC v.1928 32 bit (Intel)]
# From type library 'S7WSAAPX.DLL'
# On Fri May 20 14:41:57 2022
'Siemens S7wsaapx 5.4 Type Library'
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

CLSID = IID('{492AF241-3430-4B27-8A51-78325B86B950}')
MajorVersion = 5
MinorVersion = 4
LibraryFlags = 8
LCID = 0x0

from win32com.client import DispatchBaseClass
class ICPUIF(DispatchBaseClass):
	'ICPUIF Interface'
	CLSID = IID('{492AF238-3430-4B27-8A51-78325B86B950}')
	coclass_clsid = IID('{492AF243-3430-4B27-8A51-78325B86B950}')

	def AreBlocksLoaded(self):
		'method AreBlocksLoaded'
		return self._oleobj_.InvokeTypes(47, LCID, 1, (11, 0), (),)

	def DisconnectAndDie(self):
		'method DisconnectAndDie'
		return self._oleobj_.InvokeTypes(44, LCID, 1, (24, 0), (),)

	def EnableWatchDog(self, enable=defaultNamedNotOptArg):
		'method EnableWatchDog'
		return self._oleobj_.InvokeTypes(19, LCID, 1, (24, 0), ((11, 1),),enable
			)

	def ExecNext(self):
		'method ExecNext'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (24, 0), (),)

	def ExecuteSingleScan(self):
		'method ExecuteSingleScan'
		return self._oleobj_.InvokeTypes(38, LCID, 1, (24, 0), (),)

	def GetData(self, pbDataType=defaultNamedNotOptArg, pData=pythoncom.Missing):
		'method GetData'
		return self._ApplyTypes_(5, 1, (24, 0), ((16392, 1), (16396, 2)), 'GetData', None,pbDataType
			, pData)

	def GetExecMode(self):
		'method GetExecMode'
		return self._oleobj_.InvokeTypes(7, LCID, 1, (2, 0), (),)

	def GetImageInputSize(self, size=pythoncom.Missing):
		'method GetImageInputSize'
		return self._ApplyTypes_(45, 1, (24, 0), ((16387, 2),), 'GetImageInputSize', None,size
			)

	def GetImageOuputSize(self, size=pythoncom.Missing):
		'method GetImageOuputSize'
		return self._ApplyTypes_(46, 1, (24, 0), ((16387, 2),), 'GetImageOuputSize', None,size
			)

	def GetPause(self):
		'method GetPause'
		return self._oleobj_.InvokeTypes(10, LCID, 1, (2, 0), (),)

	def GetProSimClientNum(self):
		'method GetProSimClientNum'
		return self._oleobj_.InvokeTypes(25, LCID, 1, (3, 0), (),)

	def GetRecorder(self, pUnkRecorder=pythoncom.Missing):
		'method GetRecorder'
		return self._ApplyTypes_(42, 1, (24, 0), ((16397, 2),), 'GetRecorder', None,pUnkRecorder
			)

	def GetSimAuthLevel(self, lvl=pythoncom.Missing):
		'method GetSimAuthLevel'
		return self._ApplyTypes_(28, 1, (24, 0), ((16387, 2),), 'GetSimAuthLevel', None,lvl
			)

	def GetStartupSwitchPosition(self):
		'method GetStartupSwitchPosition'
		return self._oleobj_.InvokeTypes(15, LCID, 1, (2, 0), (),)

	def GetSwitchPosition(self, position=pythoncom.Missing):
		'method GetSwitchPosition'
		return self._ApplyTypes_(41, 1, (24, 0), ((16387, 2),), 'GetSwitchPosition', None,position
			)

	def GetTimersMode(self):
		'method GetTimersMode'
		return self._oleobj_.InvokeTypes(14, LCID, 1, (3, 0), (),)

	def GetWatchDog(self):
		'method GetWatchDog'
		return self._oleobj_.InvokeTypes(17, LCID, 1, (2, 0), (),)

	def HasPower(self):
		'method HasPower'
		return self._oleobj_.InvokeTypes(24, LCID, 1, (2, 0), (),)

	def IsSafetyRelatedAddress(self, pbDataType=defaultNamedNotOptArg):
		'method IsSafetyRelatedAddress'
		return self._oleobj_.InvokeTypes(21, LCID, 1, (11, 0), ((16392, 1),),pbDataType
			)

	def IsWatchDogEnabled(self):
		'method IsWatchDogEnabled'
		return self._oleobj_.InvokeTypes(20, LCID, 1, (11, 0), (),)

	def LockedByS7DOS(self):
		'method LockedByS7DOS'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (11, 0), (),)

	def ReadDataBlockValue(self, BlockNumber=defaultNamedNotOptArg, ByteIndex=defaultNamedNotOptArg, BitIndex=defaultNamedNotOptArg, DataType=defaultNamedNotOptArg
			, pData=defaultNamedNotOptArg):
		'method ReadDataBlockValue'
		return self._ApplyTypes_(30, 1, (24, 0), ((3, 1), (3, 1), (3, 1), (3, 1), (16396, 3)), 'ReadDataBlockValue', None,BlockNumber
			, ByteIndex, BitIndex, DataType, pData)

	def ReadFlagValue(self, ByteIndex=defaultNamedNotOptArg, BitIndex=defaultNamedNotOptArg, DataType=defaultNamedNotOptArg, pData=defaultNamedNotOptArg):
		'method ReadFlagValue'
		return self._ApplyTypes_(32, 1, (24, 0), ((3, 1), (3, 1), (3, 1), (16396, 3)), 'ReadFlagValue', None,ByteIndex
			, BitIndex, DataType, pData)

	def ReadOutputImage(self, ByteIndex=defaultNamedNotOptArg, BytesToRead=defaultNamedNotOptArg, DataType=defaultNamedNotOptArg, pData=defaultNamedNotOptArg):
		'method ReadOutputImage'
		return self._ApplyTypes_(34, 1, (24, 0), ((3, 1), (3, 1), (3, 1), (16396, 3)), 'ReadOutputImage', None,ByteIndex
			, BytesToRead, DataType, pData)

	def ReadOutputPoint(self, ByteIndex=defaultNamedNotOptArg, BitIndex=defaultNamedNotOptArg, DataType=defaultNamedNotOptArg, pData=defaultNamedNotOptArg):
		'method ReadOutputPoint'
		return self._ApplyTypes_(36, 1, (24, 0), ((3, 1), (3, 1), (3, 1), (16396, 3)), 'ReadOutputPoint', None,ByteIndex
			, BitIndex, DataType, pData)

	def Register(self, InterfaceType=defaultNamedNotOptArg, pbDataType=defaultNamedNotOptArg, pNotifyDispatch=defaultNamedNotOptArg, pRegID=pythoncom.Missing):
		'method Register'
		return self._ApplyTypes_(4, 1, (3, 0), ((3, 1), (16392, 1), (9, 1), (16387, 2)), 'Register', None,InterfaceType
			, pbDataType, pNotifyDispatch, pRegID)

	def ReleaseLeftObjects(self):
		'method ReleaseLeftObjects'
		return self._oleobj_.InvokeTypes(26, LCID, 1, (24, 0), (),)

	def ResetTimers(self, timerNumber=defaultNamedNotOptArg):
		'method ResetTimers'
		return self._oleobj_.InvokeTypes(12, LCID, 1, (24, 0), ((3, 1),),timerNumber
			)

	def SetCPU(self, szCPUName=defaultNamedNotOptArg):
		'method SetCPU'
		return self._oleobj_.InvokeTypes(1, LCID, 1, (24, 0), ((8, 1),),szCPUName
			)

	def SetClrPIOFlagOnHotStart(self, bVal=defaultNamedNotOptArg):
		'method SetClrPIOFlagOnHotStart'
		return self._oleobj_.InvokeTypes(27, LCID, 1, (24, 0), ((3, 1),),bVal
			)

	def SetData(self, pbDataType=defaultNamedNotOptArg, pData=defaultNamedNotOptArg):
		'method SetData'
		return self._oleobj_.InvokeTypes(6, LCID, 1, (24, 0), ((16392, 1), (16396, 1)),pbDataType
			, pData)

	def SetExecMode(self, mode=defaultNamedNotOptArg):
		'method SetExecMode'
		return self._oleobj_.InvokeTypes(8, LCID, 1, (24, 0), ((2, 1),),mode
			)

	def SetPause(self, pauseMode=defaultNamedNotOptArg):
		'method SetPause'
		return self._oleobj_.InvokeTypes(11, LCID, 1, (24, 0), ((2, 1),),pauseMode
			)

	def SetPower(self, power=defaultNamedNotOptArg):
		'method SetPower'
		return self._oleobj_.InvokeTypes(23, LCID, 1, (24, 0), ((2, 1),),power
			)

	def SetScanMode(self, mode=defaultNamedNotOptArg):
		'method SetScanMode'
		return self._oleobj_.InvokeTypes(39, LCID, 1, (24, 0), ((3, 1),),mode
			)

	def SetSimAuthLevel(self, lvl=defaultNamedNotOptArg):
		'method SetSimAuthLevel'
		return self._oleobj_.InvokeTypes(29, LCID, 1, (24, 0), ((3, 1),),lvl
			)

	def SetStartupSwitchPosition(self, pos=defaultNamedNotOptArg):
		'method SetStartupSwitchPosition'
		return self._oleobj_.InvokeTypes(16, LCID, 1, (24, 0), ((2, 1),),pos
			)

	def SetSwitchPosition(self, position=defaultNamedNotOptArg):
		'method SetSwitchPosition'
		return self._oleobj_.InvokeTypes(40, LCID, 1, (24, 0), ((3, 1),),position
			)

	def SetTimersMode(self, mode=defaultNamedNotOptArg):
		'method SetTimersMode'
		return self._oleobj_.InvokeTypes(13, LCID, 1, (24, 0), ((3, 1),),mode
			)

	def SetUpdateMode(self, bVal=defaultNamedNotOptArg):
		'method SetUpdateMode'
		return self._oleobj_.InvokeTypes(43, LCID, 1, (24, 0), ((3, 1),),bVal
			)

	def SetWatchDog(self, WatchDog=defaultNamedNotOptArg):
		'method SetWatchDog'
		return self._oleobj_.InvokeTypes(18, LCID, 1, (24, 0), ((2, 1),),WatchDog
			)

	def Trace(self, tracetext=defaultNamedNotOptArg):
		'method Trace'
		return self._oleobj_.InvokeTypes(22, LCID, 1, (24, 0), ((8, 1),),tracetext
			)

	def Unregister(self, RegID=defaultNamedNotOptArg):
		'method Unregister'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (3, 0), ((3, 1),),RegID
			)

	def WriteDataBlockValue(self, BlockNumber=defaultNamedNotOptArg, ByteIndex=defaultNamedNotOptArg, BitIndex=defaultNamedNotOptArg, pData=defaultNamedNotOptArg):
		'method WriteDataBlockValue'
		return self._oleobj_.InvokeTypes(31, LCID, 1, (24, 0), ((3, 1), (3, 1), (3, 1), (16396, 1)),BlockNumber
			, ByteIndex, BitIndex, pData)

	def WriteFlagValue(self, ByteIndex=defaultNamedNotOptArg, BitIndex=defaultNamedNotOptArg, pData=defaultNamedNotOptArg):
		'method WriteFlagValue'
		return self._oleobj_.InvokeTypes(33, LCID, 1, (24, 0), ((3, 1), (3, 1), (16396, 1)),ByteIndex
			, BitIndex, pData)

	def WriteInputImage(self, ByteIndex=defaultNamedNotOptArg, pData=defaultNamedNotOptArg):
		'method WriteInputImage'
		return self._oleobj_.InvokeTypes(35, LCID, 1, (24, 0), ((3, 1), (16396, 1)),ByteIndex
			, pData)

	def WriteInputPoint(self, ByteIndex=defaultNamedNotOptArg, BitIndex=defaultNamedNotOptArg, pData=defaultNamedNotOptArg):
		'method WriteInputPoint'
		return self._oleobj_.InvokeTypes(37, LCID, 1, (24, 0), ((3, 1), (3, 1), (16396, 1)),ByteIndex
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

class ICPUIFEvents:
	'Event interface for CPUIF'
	CLSID = CLSID_Sink = IID('{492AF242-3430-4B27-8A51-78325B86B950}')
	coclass_clsid = IID('{492AF243-3430-4B27-8A51-78325B86B950}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        1 : "OnScanFinished",
		        2 : "OnStateChanged",
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except pythoncom.com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:
#	def OnScanFinished(self, ExecutionTime=defaultNamedNotOptArg, MinCycleTime=defaultNamedNotOptArg, LargestCycleTime=defaultNamedNotOptArg, AverageCycleTime=defaultNamedNotOptArg
#			, IsPLCRunning=defaultNamedNotOptArg):
#		'Fired when single scan is done.'
#	def OnStateChanged(self, State=defaultNamedNotOptArg):
#		'Fired when a new PLC switch state is detected.'


class IDiagnostic(DispatchBaseClass):
	'Diagnostic Interface'
	CLSID = IID('{492AF239-3430-4B27-8A51-78325B86B950}')
	coclass_clsid = IID('{492AF244-3430-4B27-8A51-78325B86B950}')

	def GetInterruptOBNumber(self, LogAddr=defaultNamedNotOptArg, pOBNumber=pythoncom.Missing):
		'method GetInterruptOBNumber'
		return self._ApplyTypes_(5, 1, (24, 0), ((18, 1), (16401, 2)), 'GetInterruptOBNumber', None,LogAddr
			, pOBNumber)

	def ReadDiagnosticBuffer(self, pDiagBuffer=pythoncom.Missing, pReturnCode=pythoncom.Missing):
		'method ReadDiagnosticBuffer'
		return self._ApplyTypes_(1, 1, (24, 0), ((16396, 2), (16387, 2)), 'ReadDiagnosticBuffer', None,pDiagBuffer
			, pReturnCode)

	def ReadSZLBuffer(self, SZL_id=defaultNamedNotOptArg, ListIndex=defaultNamedNotOptArg, pBuffer=pythoncom.Missing, pReturnCode=pythoncom.Missing):
		'method ReadSZLBuffer'
		return self._ApplyTypes_(2, 1, (24, 0), ((2, 1), (2, 1), (16396, 2), (16387, 2)), 'ReadSZLBuffer', None,SZL_id
			, ListIndex, pBuffer, pReturnCode)

	def SetCPU(self, szCPUName=defaultNamedNotOptArg, pReturnCode=pythoncom.Missing):
		'method SetCPU'
		return self._ApplyTypes_(4, 1, (24, 0), ((8, 1), (16387, 2)), 'SetCPU', None,szCPUName
			, pReturnCode)

	def TriggerOB(self, Buffer=defaultNamedNotOptArg, TriggerType=defaultNamedNotOptArg, pReturnCode=pythoncom.Missing):
		'method TriggerOB'
		return self._ApplyTypes_(3, 1, (24, 0), ((12, 1), (3, 1), (16387, 2)), 'TriggerOB', None,Buffer
			, TriggerType, pReturnCode)

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

class ISimProjE(DispatchBaseClass):
	'ISimProjE Interface'
	CLSID = IID('{492AF240-3430-4B27-8A51-78325B86B950}')
	coclass_clsid = IID('{492AF245-3430-4B27-8A51-78325B86B950}')

	def AddNode(self, szMachineName=defaultNamedNotOptArg, MachineType=defaultNamedNotOptArg, szSubnetName=defaultNamedNotOptArg, SubnetType=defaultNamedNotOptArg
			, szNodeAddress=defaultNamedNotOptArg, slotIndex=defaultNamedNotOptArg, rack=defaultNamedNotOptArg, deviceID=defaultNamedNotOptArg, submodAddr=defaultNamedNotOptArg
			, bKBusNode=defaultNamedNotOptArg, bSelected=defaultNamedNotOptArg):
		'method AddNode'
		return self._oleobj_.InvokeTypes(6, LCID, 1, (24, 0), ((8, 1), (3, 0), (8, 1), (3, 1), (8, 1), (3, 1), (3, 1), (3, 1), (3, 1), (11, 1), (11, 1)),szMachineName
			, MachineType, szSubnetName, SubnetType, szNodeAddress, slotIndex
			, rack, deviceID, submodAddr, bKBusNode, bSelected
			)

	def ConnectionExists(self):
		'method ConnectionExists'
		return self._oleobj_.InvokeTypes(16, LCID, 1, (24, 0), (),)

	def GetFirstSelectedCPUName(self, pCPUName=defaultNamedNotOptArg):
		'method GetFirstSelectedCPUName'
		return self._ApplyTypes_(9, 1, (24, 0), ((16392, 3),), 'GetFirstSelectedCPUName', None,pCPUName
			)

	def GetFirstSelectedNodeAddress(self, pNodeAddress=defaultNamedNotOptArg, pSubnetType=pythoncom.Missing):
		'method GetFirstSelectedNodeAddress'
		return self._ApplyTypes_(14, 1, (24, 0), ((16392, 3), (16387, 2)), 'GetFirstSelectedNodeAddress', None,pNodeAddress
			, pSubnetType)

	def GetNodeCount(self, count=pythoncom.Missing):
		'method GetNodeCount'
		return self._ApplyTypes_(1, 1, (24, 0), ((16387, 2),), 'GetNodeCount', None,count
			)

	def GetPGPC(self, logdev=defaultNamedNotOptArg):
		'method GetPGPC'
		return self._ApplyTypes_(19, 1, (24, 0), ((16392, 3),), 'GetPGPC', None,logdev
			)

	def GetProjectPath(self, pFilePath=defaultNamedNotOptArg):
		'method GetProjectPath'
		return self._ApplyTypes_(15, 1, (24, 0), ((16392, 3),), 'GetProjectPath', None,pFilePath
			)

	def GetSymbolInfo(self, pObjID=pythoncom.Missing, pEnvID=pythoncom.Missing, pRefDataLogPath=pythoncom.Missing):
		'method GetSymbolInfo'
		return self._ApplyTypes_(13, 1, (24, 0), ((16387, 2), (16387, 2), (16392, 2)), 'GetSymbolInfo', None,pObjID
			, pEnvID, pRefDataLogPath)

	def Reset(self):
		'method Reset'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (24, 0), (),)

	def RestoreProjectState(self, pFilePath=defaultNamedNotOptArg, pResult=pythoncom.Missing):
		'method RestoreProjectState'
		return self._ApplyTypes_(11, 1, (24, 0), ((16392, 1), (16403, 2)), 'RestoreProjectState', None,pFilePath
			, pResult)

	def SaveProjectState(self, pFilePath=defaultNamedNotOptArg, pResult=pythoncom.Missing):
		'method SaveProjectState'
		return self._ApplyTypes_(10, 1, (24, 0), ((16392, 1), (16403, 2)), 'SaveProjectState', None,pFilePath
			, pResult)

	def SelectNodeToSimulate(self, szSubnetName=defaultNamedNotOptArg, szMachineName=defaultNamedNotOptArg, lSubnetType=defaultNamedNotOptArg):
		'method SelectNodeToSimulate'
		return self._oleobj_.InvokeTypes(5, LCID, 1, (24, 0), ((8, 1), (8, 1), (3, 1)),szSubnetName
			, szMachineName, lSubnetType)

	def SetPGPC(self, logdev=defaultNamedNotOptArg):
		'method SetPGPC'
		return self._oleobj_.InvokeTypes(18, LCID, 1, (24, 0), ((8, 1),),logdev
			)

	def SetSymbolInfo(self, objID=defaultNamedNotOptArg, envID=defaultNamedNotOptArg, pRefDataLogPath=defaultNamedNotOptArg):
		'method SetSymbolInfo'
		return self._oleobj_.InvokeTypes(12, LCID, 1, (24, 0), ((3, 1), (3, 1), (16392, 1)),objID
			, envID, pRefDataLogPath)

	def SimulateMachine(self, szMachineName=defaultNamedNotOptArg):
		'method SimulateMachine'
		return self._oleobj_.InvokeTypes(17, LCID, 1, (24, 0), ((8, 1),),szMachineName
			)

	def StartSession(self):
		'method StartSession'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (24, 0), (),)

	def StopSession(self):
		'method StopSession'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (24, 0), (),)

	def UnitTestProject(self):
		'method UnitTestProject'
		return self._oleobj_.InvokeTypes(8, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"NodeCount": (7, 2, (3, 0), (), "NodeCount", None),
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
# This CoClass is known by the name 'S7wsaapx.CPUIF.1'
class CPUIF(CoClassBaseClass): # A CoClass
	# CPUIF Class
	CLSID = IID('{492AF243-3430-4B27-8A51-78325B86B950}')
	coclass_sources = [
		ICPUIFEvents,
	]
	default_source = ICPUIFEvents
	coclass_interfaces = [
		ICPUIF,
	]
	default_interface = ICPUIF

# This CoClass is known by the name 'S7wsaapx.Diagnostic.1'
class Diagnostic(CoClassBaseClass): # A CoClass
	# Diagnostic Class
	CLSID = IID('{492AF244-3430-4B27-8A51-78325B86B950}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IDiagnostic,
	]
	default_interface = IDiagnostic

# This CoClass is known by the name 'S7wsaapx.SimProjE.1'
class SimProjE(CoClassBaseClass): # A CoClass
	# SimProjE Class
	CLSID = IID('{492AF245-3430-4B27-8A51-78325B86B950}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ISimProjE,
	]
	default_interface = ISimProjE

ICPUIF_vtables_dispatch_ = 1
ICPUIF_vtables_ = [
	(( 'SetCPU' , 'szCPUName' , ), 1, (1, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'Unregister' , 'RegID' , 'ret' , ), 2, (2, (), [ (3, 1, None, None) , 
			 (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'LockedByS7DOS' , 'ret' , ), 3, (3, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'Register' , 'InterfaceType' , 'pbDataType' , 'pNotifyDispatch' , 'pRegID' , 
			 'ret' , ), 4, (4, (), [ (3, 1, None, None) , (16392, 1, None, None) , (9, 1, None, None) , 
			 (16387, 2, None, None) , (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'GetData' , 'pbDataType' , 'pData' , ), 5, (5, (), [ (16392, 1, None, None) , 
			 (16396, 2, None, None) , ], 1 , 1 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'SetData' , 'pbDataType' , 'pData' , ), 6, (6, (), [ (16392, 1, None, None) , 
			 (16396, 1, None, None) , ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'GetExecMode' , 'ret' , ), 7, (7, (), [ (16386, 10, None, None) , ], 1 , 1 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( 'SetExecMode' , 'mode' , ), 8, (8, (), [ (2, 1, None, None) , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'ExecNext' , ), 9, (9, (), [ ], 1 , 1 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( 'GetPause' , 'pauseMode' , ), 10, (10, (), [ (16386, 10, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'SetPause' , 'pauseMode' , ), 11, (11, (), [ (2, 1, None, None) , ], 1 , 1 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( 'ResetTimers' , 'timerNumber' , ), 12, (12, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'SetTimersMode' , 'mode' , ), 13, (13, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( 'GetTimersMode' , 'mode' , ), 14, (14, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'GetStartupSwitchPosition' , 'ret' , ), 15, (15, (), [ (16386, 10, None, None) , ], 1 , 1 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( 'SetStartupSwitchPosition' , 'pos' , ), 16, (16, (), [ (2, 1, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'GetWatchDog' , 'ret' , ), 17, (17, (), [ (16386, 10, None, None) , ], 1 , 1 , 4 , 0 , 92 , (3, 0, None, None) , 0 , )),
	(( 'SetWatchDog' , 'WatchDog' , ), 18, (18, (), [ (2, 1, None, None) , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'EnableWatchDog' , 'enable' , ), 19, (19, (), [ (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 100 , (3, 0, None, None) , 0 , )),
	(( 'IsWatchDogEnabled' , 'ret' , ), 20, (20, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'IsSafetyRelatedAddress' , 'pbDataType' , 'ret' , ), 21, (21, (), [ (16392, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 108 , (3, 0, None, None) , 0 , )),
	(( 'Trace' , 'tracetext' , ), 22, (22, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'SetPower' , 'power' , ), 23, (23, (), [ (2, 1, None, None) , ], 1 , 1 , 4 , 0 , 116 , (3, 0, None, None) , 0 , )),
	(( 'HasPower' , 'power' , ), 24, (24, (), [ (16386, 10, None, None) , ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'GetProSimClientNum' , 'num' , ), 25, (25, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 124 , (3, 0, None, None) , 0 , )),
	(( 'ReleaseLeftObjects' , ), 26, (26, (), [ ], 1 , 1 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'SetClrPIOFlagOnHotStart' , 'bVal' , ), 27, (27, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 132 , (3, 0, None, None) , 0 , )),
	(( 'GetSimAuthLevel' , 'lvl' , ), 28, (28, (), [ (16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'SetSimAuthLevel' , 'lvl' , ), 29, (29, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 140 , (3, 0, None, None) , 0 , )),
	(( 'DisconnectAndDie' , ), 44, (44, (), [ ], 1 , 1 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'ReadDataBlockValue' , 'BlockNumber' , 'ByteIndex' , 'BitIndex' , 'DataType' , 
			 'pData' , ), 30, (30, (), [ (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , 
			 (3, 1, None, None) , (16396, 3, None, None) , ], 1 , 1 , 4 , 0 , 148 , (3, 0, None, None) , 0 , )),
	(( 'WriteDataBlockValue' , 'BlockNumber' , 'ByteIndex' , 'BitIndex' , 'pData' , 
			 ), 31, (31, (), [ (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (16396, 1, None, None) , ], 1 , 1 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'ReadFlagValue' , 'ByteIndex' , 'BitIndex' , 'DataType' , 'pData' , 
			 ), 32, (32, (), [ (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (16396, 3, None, None) , ], 1 , 1 , 4 , 0 , 156 , (3, 0, None, None) , 0 , )),
	(( 'WriteFlagValue' , 'ByteIndex' , 'BitIndex' , 'pData' , ), 33, (33, (), [ 
			 (3, 1, None, None) , (3, 1, None, None) , (16396, 1, None, None) , ], 1 , 1 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'ReadOutputImage' , 'ByteIndex' , 'BytesToRead' , 'DataType' , 'pData' , 
			 ), 34, (34, (), [ (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (16396, 3, None, None) , ], 1 , 1 , 4 , 0 , 164 , (3, 0, None, None) , 0 , )),
	(( 'WriteInputImage' , 'ByteIndex' , 'pData' , ), 35, (35, (), [ (3, 1, None, None) , 
			 (16396, 1, None, None) , ], 1 , 1 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'ReadOutputPoint' , 'ByteIndex' , 'BitIndex' , 'DataType' , 'pData' , 
			 ), 36, (36, (), [ (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (16396, 3, None, None) , ], 1 , 1 , 4 , 0 , 172 , (3, 0, None, None) , 0 , )),
	(( 'WriteInputPoint' , 'ByteIndex' , 'BitIndex' , 'pData' , ), 37, (37, (), [ 
			 (3, 1, None, None) , (3, 1, None, None) , (16396, 1, None, None) , ], 1 , 1 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'ExecuteSingleScan' , ), 38, (38, (), [ ], 1 , 1 , 4 , 0 , 180 , (3, 0, None, None) , 0 , )),
	(( 'SetScanMode' , 'mode' , ), 39, (39, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'SetSwitchPosition' , 'position' , ), 40, (40, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 188 , (3, 0, None, None) , 0 , )),
	(( 'GetSwitchPosition' , 'position' , ), 41, (41, (), [ (16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'GetRecorder' , 'pUnkRecorder' , ), 42, (42, (), [ (16397, 2, None, None) , ], 1 , 1 , 4 , 0 , 196 , (3, 0, None, None) , 0 , )),
	(( 'SetUpdateMode' , 'bVal' , ), 43, (43, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'GetImageInputSize' , 'size' , ), 45, (45, (), [ (16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 204 , (3, 0, None, None) , 0 , )),
	(( 'GetImageOuputSize' , 'size' , ), 46, (46, (), [ (16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'AreBlocksLoaded' , 'ret' , ), 47, (47, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 212 , (3, 0, None, None) , 0 , )),
]

IDiagnostic_vtables_dispatch_ = 1
IDiagnostic_vtables_ = [
	(( 'ReadDiagnosticBuffer' , 'pDiagBuffer' , 'pReturnCode' , ), 1, (1, (), [ (16396, 2, None, None) , 
			 (16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'ReadSZLBuffer' , 'SZL_id' , 'ListIndex' , 'pBuffer' , 'pReturnCode' , 
			 ), 2, (2, (), [ (2, 1, None, None) , (2, 1, None, None) , (16396, 2, None, None) , (16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'TriggerOB' , 'Buffer' , 'TriggerType' , 'pReturnCode' , ), 3, (3, (), [ 
			 (12, 1, None, None) , (3, 1, None, None) , (16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'SetCPU' , 'szCPUName' , 'pReturnCode' , ), 4, (4, (), [ (8, 1, None, None) , 
			 (16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'GetInterruptOBNumber' , 'LogAddr' , 'pOBNumber' , ), 5, (5, (), [ (18, 1, None, None) , 
			 (16401, 2, None, None) , ], 1 , 1 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
]

ISimProjE_vtables_dispatch_ = 1
ISimProjE_vtables_ = [
	(( 'GetNodeCount' , 'count' , ), 1, (1, (), [ (16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'StartSession' , ), 2, (2, (), [ ], 1 , 1 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'StopSession' , ), 3, (3, (), [ ], 1 , 1 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'Reset' , ), 4, (4, (), [ ], 1 , 1 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'SelectNodeToSimulate' , 'szSubnetName' , 'szMachineName' , 'lSubnetType' , ), 5, (5, (), [ 
			 (8, 1, None, None) , (8, 1, None, None) , (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'AddNode' , 'szMachineName' , 'MachineType' , 'szSubnetName' , 'SubnetType' , 
			 'szNodeAddress' , 'slotIndex' , 'rack' , 'deviceID' , 'submodAddr' , 
			 'bKBusNode' , 'bSelected' , ), 6, (6, (), [ (8, 1, None, None) , (3, 0, None, None) , 
			 (8, 1, None, None) , (3, 1, None, None) , (8, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , 
			 (3, 1, None, None) , (3, 1, None, None) , (11, 1, None, None) , (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'NodeCount' , 'pVal' , ), 7, (7, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( 'UnitTestProject' , ), 8, (8, (), [ ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'GetFirstSelectedCPUName' , 'pCPUName' , ), 9, (9, (), [ (16392, 3, None, None) , ], 1 , 1 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( 'SaveProjectState' , 'pFilePath' , 'pResult' , ), 10, (10, (), [ (16392, 1, None, None) , 
			 (16403, 2, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'RestoreProjectState' , 'pFilePath' , 'pResult' , ), 11, (11, (), [ (16392, 1, None, None) , 
			 (16403, 2, None, None) , ], 1 , 1 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( 'SetSymbolInfo' , 'objID' , 'envID' , 'pRefDataLogPath' , ), 12, (12, (), [ 
			 (3, 1, None, None) , (3, 1, None, None) , (16392, 1, None, None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'GetSymbolInfo' , 'pObjID' , 'pEnvID' , 'pRefDataLogPath' , ), 13, (13, (), [ 
			 (16387, 2, None, None) , (16387, 2, None, None) , (16392, 2, None, None) , ], 1 , 1 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( 'GetFirstSelectedNodeAddress' , 'pNodeAddress' , 'pSubnetType' , ), 14, (14, (), [ (16392, 3, None, None) , 
			 (16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'GetProjectPath' , 'pFilePath' , ), 15, (15, (), [ (16392, 3, None, None) , ], 1 , 1 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( 'ConnectionExists' , ), 16, (16, (), [ ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'SimulateMachine' , 'szMachineName' , ), 17, (17, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 92 , (3, 0, None, None) , 0 , )),
	(( 'SetPGPC' , 'logdev' , ), 18, (18, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'GetPGPC' , 'logdev' , ), 19, (19, (), [ (16392, 3, None, None) , ], 1 , 1 , 4 , 0 , 100 , (3, 0, None, None) , 0 , )),
]

RecordMap = {
}

CLSIDToClassMap = {
	'{492AF242-3430-4B27-8A51-78325B86B950}' : ICPUIFEvents,
	'{492AF238-3430-4B27-8A51-78325B86B950}' : ICPUIF,
	'{492AF243-3430-4B27-8A51-78325B86B950}' : CPUIF,
	'{492AF239-3430-4B27-8A51-78325B86B950}' : IDiagnostic,
	'{492AF244-3430-4B27-8A51-78325B86B950}' : Diagnostic,
	'{492AF240-3430-4B27-8A51-78325B86B950}' : ISimProjE,
	'{492AF245-3430-4B27-8A51-78325B86B950}' : SimProjE,
}
CLSIDToPackageMap = {}
win32com.client.CLSIDToClass.RegisterCLSIDsFromDict( CLSIDToClassMap )
VTablesToPackageMap = {}
VTablesToClassMap = {
	'{492AF238-3430-4B27-8A51-78325B86B950}' : 'ICPUIF',
	'{492AF239-3430-4B27-8A51-78325B86B950}' : 'IDiagnostic',
	'{492AF240-3430-4B27-8A51-78325B86B950}' : 'ISimProjE',
}


NamesToIIDMap = {
	'ICPUIFEvents' : '{492AF242-3430-4B27-8A51-78325B86B950}',
	'ICPUIF' : '{492AF238-3430-4B27-8A51-78325B86B950}',
	'IDiagnostic' : '{492AF239-3430-4B27-8A51-78325B86B950}',
	'ISimProjE' : '{492AF240-3430-4B27-8A51-78325B86B950}',
}


