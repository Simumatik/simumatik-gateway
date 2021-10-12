# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 3.8.7 (tags/v3.8.7:6503f05, Dec 21 2020, 17:59:51) [MSC v.1928 64 bit (AMD64)]
# From type library '2'
# On Sun Sep 19 22:25:16 2021
'FANUC Robotics Controller Interface'
makepy_version = '0.5.01'
python_version = 0x30807f0

import win32com.client.CLSIDToClass, pythoncom, pywintypes
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch

# The following 3 lines may need tweaking for the particular server
# Candidates are pythoncom.Missing, .Empty and .ArgNotFound
defaultNamedOptArg=pythoncom.Empty
defaultNamedNotOptArg=pythoncom.Empty
defaultUnnamedArg=pythoncom.Empty

CLSID = IID('{6C779F21-4383-11D0-8901-0020AF68F0A3}')
MajorVersion = 1
MinorVersion = 5
LibraryFlags = 13
LCID = 0x0

class constants:
	frArcWeldingID                =1          # from enum FREAPCodeConstants
	frArcWeldingMask              =1          # from enum FREAPCodeConstants
	frBellToolID                  =18         # from enum FREAPCodeConstants
	frDispenseMask                =128        # from enum FREAPCodeConstants
	frHandlingToolID              =17         # from enum FREAPCodeConstants
	frHandlingToolMask            =8          # from enum FREAPCodeConstants
	frKARELProcess0ID             =20         # from enum FREAPCodeConstants
	frKARELProcess0Mask           =1          # from enum FREAPCodeConstants
	frKARELProcess1ID             =21         # from enum FREAPCodeConstants
	frKARELProcess1Mask           =2          # from enum FREAPCodeConstants
	frKARELProcess2ID             =22         # from enum FREAPCodeConstants
	frKARELProcess2Mask           =4          # from enum FREAPCodeConstants
	frKARELProcess3ID             =23         # from enum FREAPCodeConstants
	frKARELProcess3Mask           =8          # from enum FREAPCodeConstants
	frKARELProcess4ID             =24         # from enum FREAPCodeConstants
	frKARELProcess4Mask           =16         # from enum FREAPCodeConstants
	frKARELProcess5ID             =25         # from enum FREAPCodeConstants
	frKARELProcess5Mask           =32         # from enum FREAPCodeConstants
	frKARELProcess6ID             =26         # from enum FREAPCodeConstants
	frKARELProcess6Mask           =64         # from enum FREAPCodeConstants
	frKARELProcess7ID             =27         # from enum FREAPCodeConstants
	frKARELProcess7Mask           =128        # from enum FREAPCodeConstants
	frKARELProcess8ID             =28         # from enum FREAPCodeConstants
	frKARELProcess8Mask           =256        # from enum FREAPCodeConstants
	frKARELProcess9ID             =29         # from enum FREAPCodeConstants
	frKARELProcess9Mask           =512        # from enum FREAPCodeConstants
	frLDYagGeneratorID            =30         # from enum FREAPCodeConstants
	frLDYagRobotID                =31         # from enum FREAPCodeConstants
	frLaserApplicationID          =4          # from enum FREAPCodeConstants
	frLaserMask                   =16         # from enum FREAPCodeConstants
	frMaterialHandlingID          =3          # from enum FREAPCodeConstants
	frNoAppID                     =0          # from enum FREAPCodeConstants
	frNoAppMask                   =0          # from enum FREAPCodeConstants
	frPaintMask                   =64         # from enum FREAPCodeConstants
	frPaintingID                  =6          # from enum FREAPCodeConstants
	frPalletizingMask             =4          # from enum FREAPCodeConstants
	frSampleAppID                 =0          # from enum FREAPCodeConstants
	frSealingFluidKineticsID      =14         # from enum FREAPCodeConstants
	frSealingGracoID              =9          # from enum FREAPCodeConstants
	frSealingID                   =5          # from enum FREAPCodeConstants
	frSealingJESCOID              =13         # from enum FREAPCodeConstants
	frSealingMask                 =32         # from enum FREAPCodeConstants
	frSealingNordsonAnalogID      =7          # from enum FREAPCodeConstants
	frSealingNordsonDigitalID     =8          # from enum FREAPCodeConstants
	frSealingNordsonSelectCoatID  =10         # from enum FREAPCodeConstants
	frSealingNordsonUrethaneID    =11         # from enum FREAPCodeConstants
	frSealingReservedID           =12         # from enum FREAPCodeConstants
	frSealingRoboticsIncID        =15         # from enum FREAPCodeConstants
	frSealingSchuckerID           =16         # from enum FREAPCodeConstants
	frSpotWeldingID               =2          # from enum FREAPCodeConstants
	frSpotWeldingMask             =2          # from enum FREAPCodeConstants
	frUserAMRID                   =1          # from enum FREAPCodeConstants
	frAllAccess                   =7          # from enum FREAccessModeConstants
	frNoAccess                    =0          # from enum FREAccessModeConstants
	frOverwriteAccess             =4          # from enum FREAccessModeConstants
	frReadAccess                  =1          # from enum FREAccessModeConstants
	frReadOverwriteAccess         =5          # from enum FREAccessModeConstants
	frReadWriteAccess             =3          # from enum FREAccessModeConstants
	frWriteAccess                 =2          # from enum FREAccessModeConstants
	frWriteOverwriteAccess        =6          # from enum FREAccessModeConstants
	frErrorClear                  =2          # from enum FREAlarmSeverityConstants
	frErrorClearAll               =3          # from enum FREAlarmSeverityConstants
	frErrorNormal                 =0          # from enum FREAlarmSeverityConstants
	frErrorReset                  =1          # from enum FREAlarmSeverityConstants
	frSevAbort                    =43         # from enum FREAlarmSeverityConstants
	frSevAbortL                   =11         # from enum FREAlarmSeverityConstants
	frSevExAbort                  =3          # from enum FREAlarmSeverityConstants
	frSevExDebug                  =1          # from enum FREAlarmSeverityConstants
	frSevExMask                   =3          # from enum FREAlarmSeverityConstants
	frSevExNone                   =0          # from enum FREAlarmSeverityConstants
	frSevExPause                  =2          # from enum FREAlarmSeverityConstants
	frSevMoCancel                 =8          # from enum FREAlarmSeverityConstants
	frSevMoMask                   =12         # from enum FREAlarmSeverityConstants
	frSevMoNone                   =0          # from enum FREAlarmSeverityConstants
	frSevMoStop                   =4          # from enum FREAlarmSeverityConstants
	frSevNone                     =128        # from enum FREAlarmSeverityConstants
	frSevPause                    =34         # from enum FREAlarmSeverityConstants
	frSevPauseL                   =2          # from enum FREAlarmSeverityConstants
	frSevServo                    =54         # from enum FREAlarmSeverityConstants
	frSevServo2                   =59         # from enum FREAlarmSeverityConstants
	frSevStop                     =38         # from enum FREAlarmSeverityConstants
	frSevStopL                    =6          # from enum FREAlarmSeverityConstants
	frSevSystem                   =123        # from enum FREAlarmSeverityConstants
	frSevWarn                     =0          # from enum FREAlarmSeverityConstants
	frAllcSizeAttr                =4          # from enum FREAttributeConstants
	frBusyLampOffAttr             =15         # from enum FREAttributeConstants
	frCommentAttr                 =2          # from enum FREAttributeConstants
	frCreatedAttr                 =6          # from enum FREAttributeConstants
	frDefaultGroupAttr            =10         # from enum FREAttributeConstants
	frIgnoreAbortAttr             =16         # from enum FREAttributeConstants
	frIgnorePauseAttr             =17         # from enum FREAttributeConstants
	frInvisibleAttr               =18         # from enum FREAttributeConstants
	frLastModifiedAttr            =7          # from enum FREAttributeConstants
	frNameAttr                    =0          # from enum FREAttributeConstants
	frNumLinesAttr                =5          # from enum FREAttributeConstants
	frOriginalNameAttr            =8          # from enum FREAttributeConstants
	frOwnerAttr                   =1          # from enum FREAttributeConstants
	frPriorityAttr                =13         # from enum FREAttributeConstants
	frProtectionAttr              =11         # from enum FREAttributeConstants
	frSizeAttr                    =3          # from enum FREAttributeConstants
	frStackSizeAttr               =12         # from enum FREAttributeConstants
	frStorageTypeAttr             =19         # from enum FREAttributeConstants
	frTimeSliceAttr               =14         # from enum FREAttributeConstants
	frVersionAttr                 =9          # from enum FREAttributeConstants
	frJointDisplayType            =0          # from enum FRECurPositionConstants
	frUserDisplayType             =1          # from enum FRECurPositionConstants
	frWorldDisplayType            =2          # from enum FRECurPositionConstants
	frExecuteExtraBwd             =2          # from enum FREExecuteConstants
	frExecuteFwd                  =0          # from enum FREExecuteConstants
	frExecuteNormBwd              =1          # from enum FREExecuteConstants
	frGroup1BitMask               =1          # from enum FREGroupBitMaskConstants
	frGroup2BitMask               =2          # from enum FREGroupBitMaskConstants
	frGroup3BitMask               =4          # from enum FREGroupBitMaskConstants
	frGroup4BitMask               =8          # from enum FREGroupBitMaskConstants
	frGroup5BitMask               =16         # from enum FREGroupBitMaskConstants
	frGroup6BitMask               =32         # from enum FREGroupBitMaskConstants
	frGroup7BitMask               =64         # from enum FREGroupBitMaskConstants
	frGroup8BitMask               =128        # from enum FREGroupBitMaskConstants
	frHoldAMRDone                 =16384      # from enum FREHoldConditionConstants
	frHoldAMRPkt                  =32768      # from enum FREHoldConditionConstants
	frHoldAMRStrt                 =8192       # from enum FREHoldConditionConstants
	frHoldActDon                  =4096       # from enum FREHoldConditionConstants
	frHoldAny                     =-1         # from enum FREHoldConditionConstants
	frHoldCanDone                 =512        # from enum FREHoldConditionConstants
	frHoldChgExe                  =1          # from enum FREHoldConditionConstants
	frHoldCltDone                 =256        # from enum FREHoldConditionConstants
	frHoldFailLk                  =8          # from enum FREHoldConditionConstants
	frHoldIOPkt                   =128        # from enum FREHoldConditionConstants
	frHoldInrAbrt                 =4          # from enum FREHoldConditionConstants
	frHoldInrPaus                 =2          # from enum FREHoldConditionConstants
	frHoldMoDone                  =32         # from enum FREHoldConditionConstants
	frHoldMoStrt                  =16         # from enum FREHoldConditionConstants
	frHoldNoWtDone                =524288     # from enum FREHoldConditionConstants
	frHoldPktWt                   =1024       # from enum FREHoldConditionConstants
	frHoldPulsDone                =262144     # from enum FREHoldConditionConstants
	frHoldRlsDon                  =2048       # from enum FREHoldConditionConstants
	frHoldTimeDone                =2097152    # from enum FREHoldConditionConstants
	frHoldUAMRPkt                 =65536      # from enum FREHoldConditionConstants
	frHoldUnlock                  =1048576    # from enum FREHoldConditionConstants
	frHoldUnwait                  =64         # from enum FREHoldConditionConstants
	frHoldVBltin                  =131072     # from enum FREHoldConditionConstants
	frAInType                     =3          # from enum FREIOTypeConstants
	frAOutType                    =4          # from enum FREIOTypeConstants
	frDInType                     =1          # from enum FREIOTypeConstants
	frDOutType                    =2          # from enum FREIOTypeConstants
	frFlagType                    =35         # from enum FREIOTypeConstants
	frGPInType                    =18         # from enum FREIOTypeConstants
	frGPOutType                   =19         # from enum FREIOTypeConstants
	frLAInType                    =24         # from enum FREIOTypeConstants
	frLAOutType                   =25         # from enum FREIOTypeConstants
	frLDInType                    =22         # from enum FREIOTypeConstants
	frLDOutType                   =23         # from enum FREIOTypeConstants
	frMarkerType                  =36         # from enum FREIOTypeConstants
	frMaxIOType                   =38         # from enum FREIOTypeConstants
	frPLCInType                   =6          # from enum FREIOTypeConstants
	frPLCOutType                  =7          # from enum FREIOTypeConstants
	frRDInType                    =8          # from enum FREIOTypeConstants
	frRDOutType                   =9          # from enum FREIOTypeConstants
	frSOPInType                   =11         # from enum FREIOTypeConstants
	frSOPOutType                  =12         # from enum FREIOTypeConstants
	frTPInType                    =14         # from enum FREIOTypeConstants
	frTPOutType                   =15         # from enum FREIOTypeConstants
	frUOPInType                   =20         # from enum FREIOTypeConstants
	frUOPOutType                  =21         # from enum FREIOTypeConstants
	frWDInType                    =16         # from enum FREIOTypeConstants
	frWDOutType                   =17         # from enum FREIOTypeConstants
	frWSTKInType                  =26         # from enum FREIOTypeConstants
	frWSTKOutType                 =27         # from enum FREIOTypeConstants
	frInsertTextAfter             =2          # from enum FREInsertTextConstants
	frInsertTextBefore            =1          # from enum FREInsertTextConstants
	frInsertTextReplace           =0          # from enum FREInsertTextConstants
	frJoint1BitMask               =1          # from enum FREJointBitMaskConstants
	frJoint2BitMask               =2          # from enum FREJointBitMaskConstants
	frJoint3BitMask               =4          # from enum FREJointBitMaskConstants
	frJoint4BitMask               =8          # from enum FREJointBitMaskConstants
	frJoint5BitMask               =16         # from enum FREJointBitMaskConstants
	frJoint6BitMask               =32         # from enum FREJointBitMaskConstants
	frJoint7BitMask               =64         # from enum FREJointBitMaskConstants
	frJoint8BitMask               =128        # from enum FREJointBitMaskConstants
	frJoint9BitMask               =256        # from enum FREJointBitMaskConstants
	LM_ABORT_C                    =132        # from enum FRELMCodeConstants
	LM_ACC_C                      =211        # from enum FRELMCodeConstants
	LM_AIN_C                      =12         # from enum FRELMCodeConstants
	LM_AND_C                      =113        # from enum FRELMCodeConstants
	LM_AOUT_C                     =17         # from enum FRELMCodeConstants
	LM_APLY_C                     =8          # from enum FRELMCodeConstants
	LM_APPL1_C                    =151        # from enum FRELMCodeConstants
	LM_APPL2_C                    =152        # from enum FRELMCodeConstants
	LM_APPL_C                     =150        # from enum FRELMCodeConstants
	LM_ARGREG_C                   =62         # from enum FRELMCodeConstants
	LM_ARGSTR_C                   =63         # from enum FRELMCodeConstants
	LM_ARGTERM_C                  =64         # from enum FRELMCodeConstants
	LM_ARG_C                      =61         # from enum FRELMCodeConstants
	LM_ASGN_C                     =100        # from enum FRELMCodeConstants
	LM_AUXF_C                     =243        # from enum FRELMCodeConstants
	LM_AVEN_C                     =87         # from enum FRELMCodeConstants
	LM_CALB_C                     =252        # from enum FRELMCodeConstants
	LM_CALL_C                     =129        # from enum FRELMCodeConstants
	LM_CALM_C                     =142        # from enum FRELMCodeConstants
	LM_CALOFST2_C                 =14         # from enum FRELMCodeConstants
	LM_CALOFST_C                  =4          # from enum FRELMCodeConstants
	LM_CAMCALI_C                  =10         # from enum FRELMCodeConstants
	LM_CC_ARRY_C                  =0          # from enum FRELMCodeConstants
	LM_CC_BDA_C                   =2          # from enum FRELMCodeConstants
	LM_CC_BD_C                    =1          # from enum FRELMCodeConstants
	LM_CC_C                       =170        # from enum FRELMCodeConstants
	LM_CC_CAL_C                   =7          # from enum FRELMCodeConstants
	LM_CC_DEL_C                   =6          # from enum FRELMCodeConstants
	LM_CC_DM_C                    =11         # from enum FRELMCodeConstants
	LM_CC_EM_C                    =10         # from enum FRELMCodeConstants
	LM_CC_GET_C                   =5          # from enum FRELMCodeConstants
	LM_CC_GM_C                    =9          # from enum FRELMCodeConstants
	LM_CC_IDA_C                   =4          # from enum FRELMCodeConstants
	LM_CC_ID_C                    =3          # from enum FRELMCodeConstants
	LM_CC_SNS_C                   =8          # from enum FRELMCodeConstants
	LM_CELL_C                     =214        # from enum FRELMCodeConstants
	LM_CLRMON_C                   =6          # from enum FRELMCodeConstants
	LM_CLRSMPRG_C                 =54         # from enum FRELMCodeConstants
	LM_CNST_BYT_C                 =1          # from enum FRELMCodeConstants
	LM_CNST_FLT_C                 =3          # from enum FRELMCodeConstants
	LM_CNST_LNG_C                 =2          # from enum FRELMCodeConstants
	LM_CN_C                       =222        # from enum FRELMCodeConstants
	LM_CODEI_C                    =22         # from enum FRELMCodeConstants
	LM_CODEO_C                    =23         # from enum FRELMCodeConstants
	LM_CONCR_C                    =240        # from enum FRELMCodeConstants
	LM_CONST_C                    =1          # from enum FRELMCodeConstants
	LM_COORD_C                    =201        # from enum FRELMCodeConstants
	LM_CPBRK_C                    =238        # from enum FRELMCodeConstants
	LM_CPPSPD_C                   =237        # from enum FRELMCodeConstants
	LM_CT_C                       =213        # from enum FRELMCodeConstants
	LM_DELAY_C                    =123        # from enum FRELMCodeConstants
	LM_DISPLAY2_C                 =18         # from enum FRELMCodeConstants
	LM_DISPLAY_C                  =5          # from enum FRELMCodeConstants
	LM_DISPVIEW_C                 =15         # from enum FRELMCodeConstants
	LM_DIVI_C                     =105        # from enum FRELMCodeConstants
	LM_DIV_C                      =104        # from enum FRELMCodeConstants
	LM_DMON_C                     =59         # from enum FRELMCodeConstants
	LM_DOPROC2_C                  =16         # from enum FRELMCodeConstants
	LM_DOPROC_C                   =7          # from enum FRELMCodeConstants
	LM_DOPRONXT_C                 =17         # from enum FRELMCodeConstants
	LM_DSPQIMG_C                  =9          # from enum FRELMCodeConstants
	LM_ENDCN_C                    =241        # from enum FRELMCodeConstants
	LM_END_C                      =133        # from enum FRELMCodeConstants
	LM_EQ_C                       =107        # from enum FRELMCodeConstants
	LM_ERNUM_C                    =40         # from enum FRELMCodeConstants
	LM_ERPRG_C                    =27         # from enum FRELMCodeConstants
	LM_EST_C                      =6          # from enum FRELMCodeConstants
	LM_EST_M_C                    =7          # from enum FRELMCodeConstants
	LM_FC_C                       =137        # from enum FRELMCodeConstants
	LM_FIND2_C                    =12         # from enum FRELMCodeConstants
	LM_FIND_C                     =1          # from enum FRELMCodeConstants
	LM_FNDNXT2_C                  =13         # from enum FRELMCodeConstants
	LM_FNDNXT_C                   =2          # from enum FRELMCodeConstants
	LM_GE_C                       =112        # from enum FRELMCodeConstants
	LM_GRPNAME_C                  =178        # from enum FRELMCodeConstants
	LM_GT_C                       =111        # from enum FRELMCodeConstants
	LM_HIGHD_C                    =5          # from enum FRELMCodeConstants
	LM_HSCD_C                     =224        # from enum FRELMCodeConstants
	LM_HTSNS_C                    =138        # from enum FRELMCodeConstants
	LM_IAINST_C                   =231        # from enum FRELMCodeConstants
	LM_IA_IARATE_C                =2          # from enum FRELMCodeConstants
	LM_IA_IASTOP_C                =0          # from enum FRELMCodeConstants
	LM_IA_IAWAIT_C                =1          # from enum FRELMCodeConstants
	LM_IBGNEND_C                  =172        # from enum FRELMCodeConstants
	LM_IBGNRECE_C                 =174        # from enum FRELMCodeConstants
	LM_IBGNREC_C                  =173        # from enum FRELMCodeConstants
	LM_IBGNSTRT_C                 =171        # from enum FRELMCodeConstants
	LM_IBPX_ATCH_C                =0          # from enum FRELMCodeConstants
	LM_IBPX_C                     =179        # from enum FRELMCodeConstants
	LM_IBPX_DTCH_C                =1          # from enum FRELMCodeConstants
	LM_IBSC_ATCH_C                =0          # from enum FRELMCodeConstants
	LM_IBSC_C                     =177        # from enum FRELMCodeConstants
	LM_IBSC_DTCH_C                =1          # from enum FRELMCodeConstants
	LM_IF_C                       =120        # from enum FRELMCodeConstants
	LM_INC_C                      =210        # from enum FRELMCodeConstants
	LM_INDEX_C                    =2          # from enum FRELMCodeConstants
	LM_IV_C                       =190        # from enum FRELMCodeConstants
	LM_IV_PS_C                    =192        # from enum FRELMCodeConstants
	LM_IV_SC_C                    =191        # from enum FRELMCodeConstants
	LM_IWC_C                      =232        # from enum FRELMCodeConstants
	LM_IWC_ISOCON_C               =0          # from enum FRELMCodeConstants
	LM_IWC_RSTSTP_C               =1          # from enum FRELMCodeConstants
	LM_IWC_RSTWLD_C               =2          # from enum FRELMCodeConstants
	LM_JMPDS_C                    =127        # from enum FRELMCodeConstants
	LM_JMP_C                      =126        # from enum FRELMCodeConstants
	LM_LBL_C                      =128        # from enum FRELMCodeConstants
	LM_LDCL_C                     =225        # from enum FRELMCodeConstants
	LM_LDCL_END_C                 =1          # from enum FRELMCodeConstants
	LM_LDCL_STA_C                 =0          # from enum FRELMCodeConstants
	LM_LD_END_C                   =234        # from enum FRELMCodeConstants
	LM_LD_STRT_C                  =233        # from enum FRELMCodeConstants
	LM_LE_C                       =110        # from enum FRELMCodeConstants
	LM_LKPREG_C                   =52         # from enum FRELMCodeConstants
	LM_LNT_C                      =218        # from enum FRELMCodeConstants
	LM_LOWD_C                     =3          # from enum FRELMCodeConstants
	LM_LOWP_C                     =4          # from enum FRELMCodeConstants
	LM_LT_C                       =109        # from enum FRELMCodeConstants
	LM_L_PAREN_C                  =115        # from enum FRELMCodeConstants
	LM_MACRO_C                    =135        # from enum FRELMCodeConstants
	LM_MAXSPD_C                   =58         # from enum FRELMCodeConstants
	LM_MCT_C                      =217        # from enum FRELMCodeConstants
	LM_MEASURE_C                  =3          # from enum FRELMCodeConstants
	LM_MIG_C                      =160        # from enum FRELMCodeConstants
	LM_MINUS_C                    =102        # from enum FRELMCodeConstants
	LM_MLGP_C                     =253        # from enum FRELMCodeConstants
	LM_MLPLST_C                   =2          # from enum FRELMCodeConstants
	LM_MNTPRG_C                   =60         # from enum FRELMCodeConstants
	LM_MOD_C                      =106        # from enum FRELMCodeConstants
	LM_MOGRP_C                    =242        # from enum FRELMCodeConstants
	LM_MONITOR_C                  =147        # from enum FRELMCodeConstants
	LM_MOPTIME_C                  =246        # from enum FRELMCodeConstants
	LM_MOTN_EXT_C                 =249        # from enum FRELMCodeConstants
	LM_MOVE_C                     =254        # from enum FRELMCodeConstants
	LM_MROT_C                     =250        # from enum FRELMCodeConstants
	LM_MSG_C                      =31         # from enum FRELMCodeConstants
	LM_MSPD_JNT_C                 =1          # from enum FRELMCodeConstants
	LM_MSPD_LIN_C                 =2          # from enum FRELMCodeConstants
	LM_MSQZ_C                     =235        # from enum FRELMCodeConstants
	LM_MTN_APPLSPD_C              =192        # from enum FRELMCodeConstants
	LM_MTN_ARC_C                  =6          # from enum FRELMCodeConstants
	LM_MTN_CD_C                   =192        # from enum FRELMCodeConstants
	LM_MTN_CIR_C                  =3          # from enum FRELMCodeConstants
	LM_MTN_CMMIN_C                =2          # from enum FRELMCodeConstants
	LM_MTN_CNT_C                  =128        # from enum FRELMCodeConstants
	LM_MTN_DGSEC_C                =4          # from enum FRELMCodeConstants
	LM_MTN_FINE_C                 =0          # from enum FRELMCodeConstants
	LM_MTN_HOME_C                 =5          # from enum FRELMCodeConstants
	LM_MTN_INCL_C                 =4          # from enum FRELMCodeConstants
	LM_MTN_INCMN_C                =3          # from enum FRELMCodeConstants
	LM_MTN_JNT_C                  =1          # from enum FRELMCodeConstants
	LM_MTN_LIN_C                  =2          # from enum FRELMCodeConstants
	LM_MTN_MMSEC_C                =1          # from enum FRELMCodeConstants
	LM_MTN_MSEC_C                 =6          # from enum FRELMCodeConstants
	LM_MTN_MSPD_C                 =7          # from enum FRELMCodeConstants
	LM_MTN_NPOS_C                 =0          # from enum FRELMCodeConstants
	LM_MTN_NSPD_C                 =0          # from enum FRELMCodeConstants
	LM_MTN_PAL2_C                 =3          # from enum FRELMCodeConstants
	LM_MTN_PALLET_C               =2          # from enum FRELMCodeConstants
	LM_MTN_PER_C                  =0          # from enum FRELMCodeConstants
	LM_MTN_RCNT_C                 =64         # from enum FRELMCodeConstants
	LM_MTN_RPOS_C                 =1          # from enum FRELMCodeConstants
	LM_MTN_RRSPD_C                =128        # from enum FRELMCodeConstants
	LM_MTN_RSPD_C                 =64         # from enum FRELMCodeConstants
	LM_MTN_SEC_C                  =5          # from enum FRELMCodeConstants
	LM_MTN_UNSPD_C                =192        # from enum FRELMCodeConstants
	LM_MTN_UNT_C                  =0          # from enum FRELMCodeConstants
	LM_MULT_C                     =103        # from enum FRELMCodeConstants
	LM_NE_C                       =108        # from enum FRELMCodeConstants
	LM_NOAMR_APPL_C               =180        # from enum FRELMCodeConstants
	LM_NOITM_C                    =0          # from enum FRELMCodeConstants
	LM_NONE_AIR                   =2          # from enum FRELMCodeConstants
	LM_NONE_C                     =0          # from enum FRELMCodeConstants
	LM_NOT_C                      =117        # from enum FRELMCodeConstants
	LM_OCP_C                      =139        # from enum FRELMCodeConstants
	LM_OFIX_C                     =230        # from enum FRELMCodeConstants
	LM_OFSCND_C                   =207        # from enum FRELMCodeConstants
	LM_OFST_C                     =205        # from enum FRELMCodeConstants
	LM_OPTP_C                     =236        # from enum FRELMCodeConstants
	LM_ORGDSBL_C                  =55         # from enum FRELMCodeConstants
	LM_OR_C                       =114        # from enum FRELMCodeConstants
	LM_OTHWS_C                    =122        # from enum FRELMCodeConstants
	LM_OVRD_C                     =24         # from enum FRELMCodeConstants
	LM_PAL2_C                     =227        # from enum FRELMCodeConstants
	LM_PARAM_C                    =26         # from enum FRELMCodeConstants
	LM_PAUSE_C                    =131        # from enum FRELMCodeConstants
	LM_PCVIS_C                    =193        # from enum FRELMCodeConstants
	LM_PCVIS_DOPRO_C              =1          # from enum FRELMCodeConstants
	LM_PCVIS_OF_C                 =195        # from enum FRELMCodeConstants
	LM_PCVIS_ST_C                 =194        # from enum FRELMCodeConstants
	LM_PGNAM_C                    =130        # from enum FRELMCodeConstants
	LM_PLELM_C                    =7          # from enum FRELMCodeConstants
	LM_PLREG_C                    =6          # from enum FRELMCodeConstants
	LM_PLST_C                     =149        # from enum FRELMCodeConstants
	LM_PLUS_C                     =101        # from enum FRELMCodeConstants
	LM_POPQU_C                    =19         # from enum FRELMCodeConstants
	LM_POSITEM_C                  =5          # from enum FRELMCodeConstants
	LM_PREG_C                     =4          # from enum FRELMCodeConstants
	LM_PRESSURE_C                 =56         # from enum FRELMCodeConstants
	LM_PRES_GUN1_C                =3          # from enum FRELMCodeConstants
	LM_PRES_GUN2_C                =4          # from enum FRELMCodeConstants
	LM_PROCSYNC_C                 =248        # from enum FRELMCodeConstants
	LM_PSYN_END_C                 =1          # from enum FRELMCodeConstants
	LM_PSYN_INPOS_C               =3          # from enum FRELMCodeConstants
	LM_PSYN_START_C               =0          # from enum FRELMCodeConstants
	LM_PSYN_SYNC_C                =2          # from enum FRELMCodeConstants
	LM_PS_C                       =251        # from enum FRELMCodeConstants
	LM_PTH_C                      =244        # from enum FRELMCodeConstants
	LM_PULSE_C                    =51         # from enum FRELMCodeConstants
	LM_QSKP_C                     =204        # from enum FRELMCodeConstants
	LM_RCV_C                      =141        # from enum FRELMCodeConstants
	LM_RDI_C                      =11         # from enum FRELMCodeConstants
	LM_RDO_C                      =16         # from enum FRELMCodeConstants
	LM_REG_C                      =3          # from enum FRELMCodeConstants
	LM_REM_C                      =30         # from enum FRELMCodeConstants
	LM_RSMPRG_C                   =28         # from enum FRELMCodeConstants
	LM_RSR_C                      =20         # from enum FRELMCodeConstants
	LM_RTCP_C                     =245        # from enum FRELMCodeConstants
	LM_RUN_C                      =134        # from enum FRELMCodeConstants
	LM_R_PAREN_C                  =116        # from enum FRELMCodeConstants
	LM_SAMPLE_C                   =0          # from enum FRELMCodeConstants
	LM_SAVQIMG_C                  =8          # from enum FRELMCodeConstants
	LM_SCP_C                      =226        # from enum FRELMCodeConstants
	LM_SDI_C                      =10         # from enum FRELMCodeConstants
	LM_SDO_C                      =15         # from enum FRELMCodeConstants
	LM_SD_OFF_C                   =249        # from enum FRELMCodeConstants
	LM_SD_ON_C                    =248        # from enum FRELMCodeConstants
	LM_SEL_C                      =121        # from enum FRELMCodeConstants
	LM_SEMPH_C                    =29         # from enum FRELMCodeConstants
	LM_SEND_C                     =140        # from enum FRELMCodeConstants
	LM_SERVOGUN_C                 =228        # from enum FRELMCodeConstants
	LM_SFLTEND_C                  =3          # from enum FRELMCodeConstants
	LM_SFLTFLWUP_C                =2          # from enum FRELMCodeConstants
	LM_SFLTSCD_C                  =0          # from enum FRELMCodeConstants
	LM_SFLT_C                     =208        # from enum FRELMCodeConstants
	LM_SGPLST_C                   =1          # from enum FRELMCodeConstants
	LM_SGPM1_DST_C                =5          # from enum FRELMCodeConstants
	LM_SGPM2_DST_C                =6          # from enum FRELMCodeConstants
	LM_SG_ZERO_C                  =0          # from enum FRELMCodeConstants
	LM_SIVIS_DOPRO_C              =1          # from enum FRELMCodeConstants
	LM_SIVIS_OF_C                 =198        # from enum FRELMCodeConstants
	LM_SIVIS_ST_C                 =197        # from enum FRELMCodeConstants
	LM_SIVIS__C                   =196        # from enum FRELMCodeConstants
	LM_SI_C                       =36         # from enum FRELMCodeConstants
	LM_SKIP_C                     =202        # from enum FRELMCodeConstants
	LM_SKPCND_C                   =203        # from enum FRELMCodeConstants
	LM_SMIGE_C                    =145        # from enum FRELMCodeConstants
	LM_SNAP2_C                    =11         # from enum FRELMCodeConstants
	LM_SNAP_C                     =0          # from enum FRELMCodeConstants
	LM_SNSOF_C                    =144        # from enum FRELMCodeConstants
	LM_SNSON_C                    =143        # from enum FRELMCodeConstants
	LM_SO_C                       =38         # from enum FRELMCodeConstants
	LM_SP1_BA                     =74         # from enum FRELMCodeConstants
	LM_SP1_BB                     =71         # from enum FRELMCodeConstants
	LM_SP1_S                      =73         # from enum FRELMCodeConstants
	LM_SP1_V                      =72         # from enum FRELMCodeConstants
	LM_SP2_AV                     =84         # from enum FRELMCodeConstants
	LM_SP2_BA                     =78         # from enum FRELMCodeConstants
	LM_SP2_BB                     =75         # from enum FRELMCodeConstants
	LM_SP2_CT                     =81         # from enum FRELMCodeConstants
	LM_SP2_EP                     =88         # from enum FRELMCodeConstants
	LM_SP2_EQ                     =79         # from enum FRELMCodeConstants
	LM_SP2_S                      =77         # from enum FRELMCodeConstants
	LM_SP2_SN                     =82         # from enum FRELMCodeConstants
	LM_SP2_V                      =76         # from enum FRELMCodeConstants
	LM_SP2_VL                     =83         # from enum FRELMCodeConstants
	LM_SP2_WC                     =80         # from enum FRELMCodeConstants
	LM_SPCON_C                    =50         # from enum FRELMCodeConstants
	LM_SPC_CLOSE_C                =10         # from enum FRELMCodeConstants
	LM_SPC_COPEN_C                =13         # from enum FRELMCodeConstants
	LM_SPC_CREP_C                 =14         # from enum FRELMCodeConstants
	LM_SPC_DIS_C                  =3          # from enum FRELMCodeConstants
	LM_SPC_DIS_RELEASE_C          =24         # from enum FRELMCodeConstants
	LM_SPC_ENB_C                  =2          # from enum FRELMCodeConstants
	LM_SPC_ENTER_C                =11         # from enum FRELMCodeConstants
	LM_SPC_EXIT_C                 =12         # from enum FRELMCodeConstants
	LM_SPC_JPOS_C                 =8          # from enum FRELMCodeConstants
	LM_SPC_LPOS_C                 =7          # from enum FRELMCodeConstants
	LM_SPC_NOCHG2_C               =255        # from enum FRELMCodeConstants
	LM_SPC_NOCHG_C                =20         # from enum FRELMCodeConstants
	LM_SPC_OFFE_C                 =21         # from enum FRELMCodeConstants
	LM_SPC_OFF_C                  =0          # from enum FRELMCodeConstants
	LM_SPC_ONE_C                  =22         # from enum FRELMCodeConstants
	LM_SPC_ON_C                   =1          # from enum FRELMCodeConstants
	LM_SPC_OPEN_C                 =9          # from enum FRELMCodeConstants
	LM_SPC_RESET_C                =6          # from enum FRELMCodeConstants
	LM_SPC_START_C                =4          # from enum FRELMCodeConstants
	LM_SPC_STOP_C                 =5          # from enum FRELMCodeConstants
	LM_SPC_SVHIGH_C               =17         # from enum FRELMCodeConstants
	LM_SPC_SVLOW_C                =19         # from enum FRELMCodeConstants
	LM_SPC_SVMID_C                =18         # from enum FRELMCodeConstants
	LM_SPC_TMPDIS_C               =23         # from enum FRELMCodeConstants
	LM_STCH_END_C                 =1          # from enum FRELMCodeConstants
	LM_STCH_START_C               =0          # from enum FRELMCodeConstants
	LM_STCK_C                     =223        # from enum FRELMCodeConstants
	LM_STCK_OF_C                  =1          # from enum FRELMCodeConstants
	LM_STCK_ON_C                  =0          # from enum FRELMCodeConstants
	LM_STITCH_C                   =209        # from enum FRELMCodeConstants
	LM_STK_FCTR                   =85         # from enum FRELMCodeConstants
	LM_SVGC_ATCH_C                =0          # from enum FRELMCodeConstants
	LM_SVGC_C                     =175        # from enum FRELMCodeConstants
	LM_SVGC_DTCH_C                =1          # from enum FRELMCodeConstants
	LM_SVGC_XCHG_C                =2          # from enum FRELMCodeConstants
	LM_SVGGEN_C                   =65         # from enum FRELMCodeConstants
	LM_SVGPRES_C                  =229        # from enum FRELMCodeConstants
	LM_SVG_DOUBLE                 =2          # from enum FRELMCodeConstants
	LM_SVG_SINGLE                 =1          # from enum FRELMCodeConstants
	LM_SVHC_C                     =176        # from enum FRELMCodeConstants
	LM_SVTC_ATCH_C                =0          # from enum FRELMCodeConstants
	LM_SVTC_C                     =176        # from enum FRELMCodeConstants
	LM_SVTC_DTCH_C                =1          # from enum FRELMCodeConstants
	LM_SYS_AIR                    =0          # from enum FRELMCodeConstants
	LM_TCPSPD_C                   =66         # from enum FRELMCodeConstants
	LM_TERM_C                     =255        # from enum FRELMCodeConstants
	LM_TIMER_C                    =25         # from enum FRELMCodeConstants
	LM_TIMOVR_C                   =57         # from enum FRELMCodeConstants
	LM_TIP_STIK                   =86         # from enum FRELMCodeConstants
	LM_TMOUT_C                    =125        # from enum FRELMCodeConstants
	LM_TOFSCND_C                  =221        # from enum FRELMCodeConstants
	LM_TOFST_C                    =219        # from enum FRELMCodeConstants
	LM_TORQ_C                     =146        # from enum FRELMCodeConstants
	LM_TOUCH_C                    =212        # from enum FRELMCodeConstants
	LM_TRACK_C                    =216        # from enum FRELMCodeConstants
	LM_TVIAOFS_C                  =220        # from enum FRELMCodeConstants
	LM_UALM_C                     =21         # from enum FRELMCodeConstants
	LM_UFRAME_C                   =33         # from enum FRELMCodeConstants
	LM_UFRNUM_C                   =32         # from enum FRELMCodeConstants
	LM_UI_C                       =37         # from enum FRELMCodeConstants
	LM_ULPREG_C                   =53         # from enum FRELMCodeConstants
	LM_UO_C                       =39         # from enum FRELMCodeConstants
	LM_USER_AIR                   =1          # from enum FRELMCodeConstants
	LM_UTLNUM_C                   =34         # from enum FRELMCodeConstants
	LM_UTOOL_C                    =35         # from enum FRELMCodeConstants
	LM_VC_C                       =247        # from enum FRELMCodeConstants
	LM_VEIN_C                     =136        # from enum FRELMCodeConstants
	LM_VIAOFS_C                   =206        # from enum FRELMCodeConstants
	LM_VISION_C                   =161        # from enum FRELMCodeConstants
	LM_VIS_FL_C                   =165        # from enum FRELMCodeConstants
	LM_VIS_ID_C                   =164        # from enum FRELMCodeConstants
	LM_VIS_IM_C                   =162        # from enum FRELMCodeConstants
	LM_VIS_OF_C                   =167        # from enum FRELMCodeConstants
	LM_VIS_QN_C                   =168        # from enum FRELMCodeConstants
	LM_VIS_RS_C                   =166        # from enum FRELMCodeConstants
	LM_VIS_ST_C                   =163        # from enum FRELMCodeConstants
	LM_VIS_VW_C                   =169        # from enum FRELMCodeConstants
	LM_WAIPT_C                    =20         # from enum FRELMCodeConstants
	LM_WAIT_C                     =124        # from enum FRELMCodeConstants
	LM_WE_C                       =216        # from enum FRELMCodeConstants
	LM_WHEN_C                     =148        # from enum FRELMCodeConstants
	LM_WI_C                       =13         # from enum FRELMCodeConstants
	LM_WJNT_C                     =200        # from enum FRELMCodeConstants
	LM_WO_C                       =18         # from enum FRELMCodeConstants
	LM_WS_C                       =215        # from enum FRELMCodeConstants
	frChineseLanguage             =6          # from enum FRELanguageConstants
	frCzechLanguage               =9          # from enum FRELanguageConstants
	frDefaultLanguage             =0          # from enum FRELanguageConstants
	frEnglishLanguage             =1          # from enum FRELanguageConstants
	frFrenchLanguage              =3          # from enum FRELanguageConstants
	frGermanLanguage              =4          # from enum FRELanguageConstants
	frJapaneseLanguage            =2          # from enum FRELanguageConstants
	frKoreanLanguage              =11         # from enum FRELanguageConstants
	frOtherLanguage               =12         # from enum FRELanguageConstants
	frPortugueseLanguage          =8          # from enum FRELanguageConstants
	frRussianLanguage             =10         # from enum FRELanguageConstants
	frSpanishLanguage             =5          # from enum FRELanguageConstants
	frTaiwaneseLanguage           =7          # from enum FRELanguageConstants
	frColdConvertSysLoad          =18         # from enum FRELoadOptionConstants
	frColdSysLoad                 =17         # from enum FRELoadOptionConstants
	frConvertVarLoad              =16         # from enum FRELoadOptionConstants
	frDramOnlyVarLoad             =19         # from enum FRELoadOptionConstants
	frOverrideVarLoad             =256        # from enum FRELoadOptionConstants
	frOverwriteTPLoad             =1          # from enum FRELoadOptionConstants
	frStandardLoad                =0          # from enum FRELoadOptionConstants
	frStandardVarLoad             =0          # from enum FRELoadOptionConstants
	frTempPCLoad                  =10         # from enum FRELoadOptionConstants
	frCircularMotionType          =8          # from enum FREMotionTypeConstants
	frJointMotionType             =6          # from enum FREMotionTypeConstants
	frLinearMotionType            =7          # from enum FREMotionTypeConstants
	frSnapToMotionType            =-1         # from enum FREMotionTypeConstants
	frAESWorldOrientType          =2          # from enum FREOrientTypeConstants
	frMinRotationOrientType       =256        # from enum FREOrientTypeConstants
	frRSWorldOrientType           =1          # from enum FREOrientTypeConstants
	frWristJointOrientType        =3          # from enum FREOrientTypeConstants
	frPID_Wild                    =-1         # from enum FREPacketEventConstants
	frReqC_Wild                   =255        # from enum FREPacketEventConstants
	frSSC_KAREL                   =115        # from enum FREPacketEventConstants
	frSSC_Wild                    =255        # from enum FREPacketEventConstants
	frPipeAxTaskID                =16         # from enum FREPipeIDConstants
	frPipeDataMonitorID           =6          # from enum FREPipeIDConstants
	frPipeErrorLoggerID           =13         # from enum FREPipeIDConstants
	frPipeFilterID                =12         # from enum FREPipeIDConstants
	frPipeIOScanAnalogID          =3          # from enum FREPipeIDConstants
	frPipeIOScanDigitalID         =2          # from enum FREPipeIDConstants
	frPipeIntrOtherID             =15         # from enum FREPipeIDConstants
	frPipeJointAngleID            =1          # from enum FREPipeIDConstants
	frPipeKAREL1ID                =7          # from enum FREPipeIDConstants
	frPipeKAREL2ID                =8          # from enum FREPipeIDConstants
	frPipeKAREL3ID                =9          # from enum FREPipeIDConstants
	frPipeKAREL4ID                =10         # from enum FREPipeIDConstants
	frPipeKAREL5ID                =11         # from enum FREPipeIDConstants
	frPipeMFDataID                =27         # from enum FREPipeIDConstants
	frPipeMISegID                 =26         # from enum FREPipeIDConstants
	frPipeMOTNSimID               =28         # from enum FREPipeIDConstants
	frPipeMoDaqID                 =18         # from enum FREPipeIDConstants
	frPipePgDaqID                 =17         # from enum FREPipeIDConstants
	frPipePgMotionID              =5          # from enum FREPipeIDConstants
	frPipePlannerTaskID           =4          # from enum FREPipeIDConstants
	frPipePxTaskID                =14         # from enum FREPipeIDConstants
	frPipeActiveState             =2          # from enum FREPipeStateConstants
	frPipeFlushedState            =64         # from enum FREPipeStateConstants
	frPipeOverflowedState         =32         # from enum FREPipeStateConstants
	frPipeTempOverflowedState     =256        # from enum FREPipeStateConstants
	frKarelProgramType            =2          # from enum FREProgramTypeConstants
	frTPProgramType               =1          # from enum FREProgramTypeConstants
	frVRProgramType               =0          # from enum FREProgramTypeConstants
	frReadOnlyProtection          =2          # from enum FREProtectionConstants
	frReadWriteProtection         =1          # from enum FREProtectionConstants
	frAllReject                   =7          # from enum FRERejectModeConstants
	frNoReject                    =0          # from enum FRERejectModeConstants
	frOverwriteReject             =4          # from enum FRERejectModeConstants
	frReadOverwriteReject         =5          # from enum FRERejectModeConstants
	frReadReject                  =1          # from enum FRERejectModeConstants
	frReadWriteReject             =3          # from enum FRERejectModeConstants
	frWriteOverwriteReject        =6          # from enum FRERejectModeConstants
	frWriteReject                 =2          # from enum FRERejectModeConstants
	frHostMaster                  =2          # from enum FRERemoteMotionMasterConstants
	frKCLMaster                   =1          # from enum FRERemoteMotionMasterConstants
	frNoMaster                    =3          # from enum FRERemoteMotionMasterConstants
	frUOPMaster                   =0          # from enum FRERemoteMotionMasterConstants
	frAlmIndexBounds              =-2147220004 # from enum FRERobotErrors
	frAlmMaxSiz                   =-2147220003 # from enum FRERobotErrors
	frAlmOutMem                   =-2147220002 # from enum FRERobotErrors
	frAxesRange                   =-2147220702 # from enum FRERobotErrors
	frCantChangeToSyncDir         =-2147220502 # from enum FRERobotErrors
	frCantConnect                 =-2147221497 # from enum FRERobotErrors
	frCantConnectOfflineRunning   =-2147221496 # from enum FRERobotErrors
	frCantCopyClipboard           =-2147219203 # from enum FRERobotErrors
	frCantCreateSyncDir           =-2147220503 # from enum FRERobotErrors
	frCantOpenClipboard           =-2147219204 # from enum FRERobotErrors
	frCantPostLocalAlarms         =-2147220001 # from enum FRERobotErrors
	frCantStartOfflineServer      =-2147221495 # from enum FRERobotErrors
	frCantStartPMON               =-2147221500 # from enum FRERobotErrors
	frClipboardNoLines            =-2147219202 # from enum FRERobotErrors
	frConnectionRefused           =-2147221498 # from enum FRERobotErrors
	frExtAxesNotSupported         =-2147220701 # from enum FRERobotErrors
	frExtAxesRange                =-2147220699 # from enum FRERobotErrors
	frExternalObject              =-2147221479 # from enum FRERobotErrors
	frFailedStartupOfOfflineServer=-2147221494 # from enum FRERobotErrors
	frFeatureBadIndex             =-2147219504 # from enum FRERobotErrors
	frFeatureBadOrderNum          =-2147219503 # from enum FRERobotErrors
	frFeatureNotSupported         =-2147219497 # from enum FRERobotErrors
	frFloatRange                  =-2147220200 # from enum FRERobotErrors
	frFrameRange                  =-2147220801 # from enum FRERobotErrors
	frGroupIndexRange             =-2147220704 # from enum FRERobotErrors
	frGroupNotSupported           =-2147220703 # from enum FRERobotErrors
	frIOSaveBadFileExtension      =-2147219896 # from enum FRERobotErrors
	frIOStatBadConfigIndex        =-2147219901 # from enum FRERobotErrors
	frIOStatBadSignalIndex        =-2147219903 # from enum FRERobotErrors
	frIOStatBadTypeIndex          =-2147219904 # from enum FRERobotErrors
	frIOStatBadUserIndex          =-2147219902 # from enum FRERobotErrors
	frIOStatDupUserSignal         =-2147219899 # from enum FRERobotErrors
	frIOStatDupUserType           =-2147219900 # from enum FRERobotErrors
	frIOStatNotUserType           =-2147219897 # from enum FRERobotErrors
	frIOStatUserTypeLocked        =-2147219898 # from enum FRERobotErrors
	frIOTPOutIsAlwaysFresh        =-2147219895 # from enum FRERobotErrors
	frInvArrayIndex               =-2147220198 # from enum FRERobotErrors
	frInvConfigString             =-2147220797 # from enum FRERobotErrors
	frInvCurPosDisplayType        =-2147220803 # from enum FRERobotErrors
	frInvForSysvars               =-2147220199 # from enum FRERobotErrors
	frInvIndex                    =-2147221399 # from enum FRERobotErrors
	frInvLanguage                 =-2147221491 # from enum FRERobotErrors
	frInvParamRange               =-2147220197 # from enum FRERobotErrors
	frInvPosId                    =-2147220800 # from enum FRERobotErrors
	frInvPositionType             =-2147220804 # from enum FRERobotErrors
	frInvProgIndex                =-2147221402 # from enum FRERobotErrors
	frInvStartMode                =-2147219054 # from enum FRERobotErrors
	frInvTPBinayPosData           =-2147220696 # from enum FRERobotErrors
	frInvTPLblId                  =-2147220604 # from enum FRERobotErrors
	frInvTPPosId                  =-2147220697 # from enum FRERobotErrors
	frInvTurnIndex                =-2147220798 # from enum FRERobotErrors
	frInvTurnNumber               =-2147220799 # from enum FRERobotErrors
	frInvVarClass                 =-2147220203 # from enum FRERobotErrors
	frInvVarIndex                 =-2147221003 # from enum FRERobotErrors
	frInvVarName                  =-2147221004 # from enum FRERobotErrors
	frInvVarType                  =-2147220204 # from enum FRERobotErrors
	frInvVectIndex                =-2147220700 # from enum FRERobotErrors
	frInvalidApplData             =-2147219304 # from enum FRERobotErrors
	frInvalidApplSynch            =-2147219302 # from enum FRERobotErrors
	frInvalidDateTime             =-2147221104 # from enum FRERobotErrors
	frInvalidErrorFacility        =-2147219999 # from enum FRERobotErrors
	frInvalidErrorNumber          =-2147219998 # from enum FRERobotErrors
	frInvalidErrorSeverity        =-2147220000 # from enum FRERobotErrors
	frInvalidLineNum              =-2147221304 # from enum FRERobotErrors
	frInvalidLineObj              =-2147221302 # from enum FRERobotErrors
	frInvalidMnCode               =-2147221303 # from enum FRERobotErrors
	frKeyNotFound                 =-2147221397 # from enum FRERobotErrors
	frLicenseNotValid             =-2147221478 # from enum FRERobotErrors
	frLineCantCreate              =-2147221201 # from enum FRERobotErrors
	frLineDeletedFromProg         =-2147221200 # from enum FRERobotErrors
	frLineErrFromBinary           =-2147221203 # from enum FRERobotErrors
	frLineNoSupportBinary         =-2147221204 # from enum FRERobotErrors
	frLineNoSupportTPLineHelper   =-2147221202 # from enum FRERobotErrors
	frMoTypeNotSupported          =-2147220795 # from enum FRERobotErrors
	frNoAccessError               =-2147220999 # from enum FRERobotErrors
	frNoWriteAccessError          =-2147220998 # from enum FRERobotErrors
	frNotAPosition                =-2147220796 # from enum FRERobotErrors
	frNotAStringVar               =-2147221002 # from enum FRERobotErrors
	frNotAvailableAsEventLogger   =-2147221492 # from enum FRERobotErrors
	frNotChangePosType            =-2147220802 # from enum FRERobotErrors
	frNotNewRef                   =-2147221396 # from enum FRERobotErrors
	frNotNoUpdate                 =-2147220997 # from enum FRERobotErrors
	frNumRetriesOOR               =-2147221483 # from enum FRERobotErrors
	frObjAlreadyExists            =-2147221398 # from enum FRERobotErrors
	frObjectNotSet                =-2147221489 # from enum FRERobotErrors
	frObjectNotValid              =-2147221490 # from enum FRERobotErrors
	frPCIFNotLoaded               =-2147221489 # from enum FRERobotErrors
	frPacketEventBodyCorrupt      =-2147219600 # from enum FRERobotErrors
	frPacketEventInvReqC          =-2147219603 # from enum FRERobotErrors
	frPacketEventInvSSC           =-2147219604 # from enum FRERobotErrors
	frPacketEventNoSuchItem       =-2147219601 # from enum FRERobotErrors
	frPeriodOOR                   =-2147221482 # from enum FRERobotErrors
	frPipeBadPipeID               =-2147219029 # from enum FRERobotErrors
	frPipeBadPipeIndex            =-2147219028 # from enum FRERobotErrors
	frPipeCantCreateMonitor       =-2147219024 # from enum FRERobotErrors
	frPipeDAQNotLoaded            =-2147219023 # from enum FRERobotErrors
	frPipeInvalidDataType         =-2147219027 # from enum FRERobotErrors
	frPipeInvalidFieldIndex       =-2147219025 # from enum FRERobotErrors
	frPipeInvalidFieldName        =-2147219026 # from enum FRERobotErrors
	frPipeNotRegisteredForEvents  =-2147219022 # from enum FRERobotErrors
	frProgInvalidParam            =-2147221103 # from enum FRERobotErrors
	frProgParamRange              =-2147221102 # from enum FRERobotErrors
	frProgTypeNotSupported        =-2147221403 # from enum FRERobotErrors
	frProgramNotLoaded            =-2147221404 # from enum FRERobotErrors
	frProgramReOpenFailed         =-2147221400 # from enum FRERobotErrors
	frProgramReOpenNotAllowed     =-2147221401 # from enum FRERobotErrors
	frRegCantOpenValue            =-2147220402 # from enum FRERobotErrors
	frRegNotInteger               =-2147220904 # from enum FRERobotErrors
	frRegNotReal                  =-2147220903 # from enum FRERobotErrors
	frRobotAlreadyConnected       =-2147221499 # from enum FRERobotErrors
	frRobotConnecting             =-2147221481 # from enum FRERobotErrors
	frRobotConnectionFailed       =-2147221480 # from enum FRERobotErrors
	frRobotError                  =-2147221484 # from enum FRERobotErrors
	frRobotNotConnected           =-2147221504 # from enum FRERobotErrors
	frScattAccInvType             =-2147219103 # from enum FRERobotErrors
	frScattAccNoItems             =-2147219104 # from enum FRERobotErrors
	frStrValueTooLong             =-2147221001 # from enum FRERobotErrors
	frSynchApplDataItemBadID      =-2147219498 # from enum FRERobotErrors
	frSynchApplDataItemBadIndex   =-2147219499 # from enum FRERobotErrors
	frSynchLoadErr                =1000       # from enum FRERobotErrors
	frTPApplAlreadyExists         =-2147219303 # from enum FRERobotErrors
	frTPInstructionBadIndex       =-2147219501 # from enum FRERobotErrors
	frTPInstructionBadLMCode      =-2147219502 # from enum FRERobotErrors
	frTPInstructionBadOptCode     =-2147219500 # from enum FRERobotErrors
	frTPPosAlreadyExists          =-2147220698 # from enum FRERobotErrors
	frTPScrnUnknownKeys           =-2147219804 # from enum FRERobotErrors
	frTaskInvalidParam            =-2147219704 # from enum FRERobotErrors
	frTaskNoName                  =-2147219702 # from enum FRERobotErrors
	frTaskParamRange              =-2147219703 # from enum FRERobotErrors
	frTimeoutStartupOfOfflineServer=-2147221493 # from enum FRERobotErrors
	frUnimpVarType                =-2147220202 # from enum FRERobotErrors
	frUninit                      =-2147221000 # from enum FRERobotErrors
	frUseRobotRegPositions        =-2147220201 # from enum FRERobotErrors
	frAllSaveClass                =0          # from enum FRESaveClassConstants
	frFTPAccessSaveClass          =11         # from enum FRESaveClassConstants
	frHostSaveClass               =10         # from enum FRESaveClassConstants
	frMacroSaveClass              =5          # from enum FRESaveClassConstants
	frMajoritySaveClass           =1          # from enum FRESaveClassConstants
	frMasterSaveClass             =2          # from enum FRESaveClassConstants
	frNoSaveClass                 =4          # from enum FRESaveClassConstants
	frPMCSaveClass                =12         # from enum FRESaveClassConstants
	frPasswordSaveClass           =9          # from enum FRESaveClassConstants
	frProfibusFMSSaveClass        =8          # from enum FRESaveClassConstants
	frProfibusSaveClass           =7          # from enum FRESaveClassConstants
	frServroSaveClass             =3          # from enum FRESaveClassConstants
	frSpotSaveClass               =6          # from enum FRESaveClassConstants
	frOverwriteSave               =1          # from enum FRESaveOptionConstants
	frStandardSave                =0          # from enum FRESaveOptionConstants
	frCentimetersPerMinuteSpeedUnit=2          # from enum FRESpeedUnitConstants
	frDegreesPerSecondSpeedUnit   =4          # from enum FRESpeedUnitConstants
	frInchesPerMinuteSpeedUnit    =3          # from enum FRESpeedUnitConstants
	frMillimetersPerSecondSpeedUnit=1          # from enum FRESpeedUnitConstants
	frMillisecondsSpeedUnit       =6          # from enum FRESpeedUnitConstants
	frPercentSpeedUnit            =0          # from enum FRESpeedUnitConstants
	frSecondsSpeedUnit            =5          # from enum FRESpeedUnitConstants
	frClockStopped                =128        # from enum FREStartModeConstants
	frColdStart                   =2          # from enum FREStartModeConstants
	frConfigStart                 =16         # from enum FREStartModeConstants
	frControlStart                =1          # from enum FREStartModeConstants
	frHotStart                    =3          # from enum FREStartModeConstants
	frInitStart                   =0          # from enum FREStartModeConstants
	frNotStarted                  =255        # from enum FREStartModeConstants
	frStatusTypeAll               =0          # from enum FREStatusTypeConstants
	frStatusTypeStepType          =2          # from enum FREStatusTypeConstants
	frStatusTypeTask              =1          # from enum FREStatusTypeConstants
	frStepMotion                  =1          # from enum FREStepTypeConstants
	frStepNone                    =-1         # from enum FREStepTypeConstants
	frStepRoutine                 =2          # from enum FREStepTypeConstants
	frStepStatement               =0          # from enum FREStepTypeConstants
	frStepTPMotion                =3          # from enum FREStepTypeConstants
	frBaseFrameSysPosition        =4          # from enum FRESysPositionConstants
	frJogFrameSysPosition         =2          # from enum FRESysPositionConstants
	frRegSysPosition              =0          # from enum FRESysPositionConstants
	frToolFrameSysPosition        =1          # from enum FRESysPositionConstants
	frUserFrameSysPosition        =3          # from enum FRESysPositionConstants
	frTPKeyBackspace              =8          # from enum FRETPKeyConstants
	frTPKeyDnArw                  =213        # from enum FRETPKeyConstants
	frTPKeyEnter                  =13         # from enum FRETPKeyConstants
	frTPKeyF1                     =129        # from enum FRETPKeyConstants
	frTPKeyF2                     =131        # from enum FRETPKeyConstants
	frTPKeyF3                     =132        # from enum FRETPKeyConstants
	frTPKeyF4                     =133        # from enum FRETPKeyConstants
	frTPKeyF5                     =134        # from enum FRETPKeyConstants
	frTPKeyItem                   =148        # from enum FRETPKeyConstants
	frTPKeyLfArw                  =209        # from enum FRETPKeyConstants
	frTPKeyNext                   =135        # from enum FRETPKeyConstants
	frTPKeyPrev                   =128        # from enum FRETPKeyConstants
	frTPKeyRtArw                  =208        # from enum FRETPKeyConstants
	frTPKeyShfDnArw               =205        # from enum FRETPKeyConstants
	frTPKeyShfF1                  =137        # from enum FRETPKeyConstants
	frTPKeyShfF2                  =138        # from enum FRETPKeyConstants
	frTPKeyShfF3                  =139        # from enum FRETPKeyConstants
	frTPKeyShfF4                  =140        # from enum FRETPKeyConstants
	frTPKeyShfF5                  =141        # from enum FRETPKeyConstants
	frTPKeyShfItem                =154        # from enum FRETPKeyConstants
	frTPKeyShfLfArw               =207        # from enum FRETPKeyConstants
	frTPKeyShfNext                =142        # from enum FRETPKeyConstants
	frTPKeyShfPrev                =136        # from enum FRETPKeyConstants
	frTPKeyShfRtArw               =206        # from enum FRETPKeyConstants
	frTPKeyShfStep                =157        # from enum FRETPKeyConstants
	frTPKeyShfUpArw               =204        # from enum FRETPKeyConstants
	frTPKeyShfUsr1                =179        # from enum FRETPKeyConstants
	frTPKeyShfUsr2                =180        # from enum FRETPKeyConstants
	frTPKeyShfUsr3                =181        # from enum FRETPKeyConstants
	frTPKeyShfUsr4                =182        # from enum FRETPKeyConstants
	frTPKeyShfUsr5                =183        # from enum FRETPKeyConstants
	frTPKeyShfUsr6                =184        # from enum FRETPKeyConstants
	frTPKeyShfUsr7                =211        # from enum FRETPKeyConstants
	frTPKeyStep                   =152        # from enum FRETPKeyConstants
	frTPKeyUpArw                  =212        # from enum FRETPKeyConstants
	frTPKeyUsr1                   =173        # from enum FRETPKeyConstants
	frTPKeyUsr2                   =174        # from enum FRETPKeyConstants
	frTPKeyUsr3                   =175        # from enum FRETPKeyConstants
	frTPKeyUsr4                   =176        # from enum FRETPKeyConstants
	frTPKeyUsr5                   =177        # from enum FRETPKeyConstants
	frTPKeyUsr6                   =178        # from enum FRETPKeyConstants
	frTPKeyUsr7                   =210        # from enum FRETPKeyConstants
	frTPOutApp1                   =6          # from enum FRETPOutSignalConstants
	frTPOutApp2                   =7          # from enum FRETPOutSignalConstants
	frTPOutApp3                   =8          # from enum FRETPOutSignalConstants
	frTPOutBusy                   =4          # from enum FRETPOutSignalConstants
	frTPOutFault                  =1          # from enum FRETPOutSignalConstants
	frTPOutHold                   =2          # from enum FRETPOutSignalConstants
	frTPOutRunning                =5          # from enum FRETPOutSignalConstants
	frTPOutStep                   =3          # from enum FRETPOutSignalConstants
	frTPScrnASCII                 =147        # from enum FRETPScreenConstants
	frTPScrnBackspace             =8          # from enum FRETPScreenConstants
	frTPScrnBlink                 =138        # from enum FRETPScreenConstants
	frTPScrnBold                  =140        # from enum FRETPScreenConstants
	frTPScrnCR                    =13         # from enum FRETPScreenConstants
	frTPScrnCUP                   =131        # from enum FRETPScreenConstants
	frTPScrnClear                 =128        # from enum FRETPScreenConstants
	frTPScrnClearEOL              =129        # from enum FRETPScreenConstants
	frTPScrnClearEOW              =130        # from enum FRETPScreenConstants
	frTPScrnCursorBack            =136        # from enum FRETPScreenConstants
	frTPScrnCursorDown            =133        # from enum FRETPScreenConstants
	frTPScrnCursorForward         =156        # from enum FRETPScreenConstants
	frTPScrnCursorHome            =137        # from enum FRETPScreenConstants
	frTPScrnCursorUp              =134        # from enum FRETPScreenConstants
	frTPScrnEuropean              =158        # from enum FRETPScreenConstants
	frTPScrnFormfeed              =12         # from enum FRETPScreenConstants
	frTPScrnGraphics              =146        # from enum FRETPScreenConstants
	frTPScrnHighSize              =148        # from enum FRETPScreenConstants
	frTPScrnKatakana              =159        # from enum FRETPScreenConstants
	frTPScrnLinefeed              =10         # from enum FRETPScreenConstants
	frTPScrnNewLine               =135        # from enum FRETPScreenConstants
	frTPScrnNoBlink               =144        # from enum FRETPScreenConstants
	frTPScrnNoReverseVid          =145        # from enum FRETPScreenConstants
	frTPScrnNormal                =143        # from enum FRETPScreenConstants
	frTPScrnNormalSize            =153        # from enum FRETPScreenConstants
	frTPScrnReturn                =132        # from enum FRETPScreenConstants
	frTPScrnReverseVid            =139        # from enum FRETPScreenConstants
	frTPScrnScroll                =157        # from enum FRETPScreenConstants
	frTPScrnTab                   =9          # from enum FRETPScreenConstants
	frTPScrnUnderscore            =141        # from enum FRETPScreenConstants
	frTPScrnVertTab               =11         # from enum FRETPScreenConstants
	frTPScrnWideSize              =142        # from enum FRETPScreenConstants
	frCMOSStorageType             =1          # from enum FRETPStorageTypeConstants
	frFileCMOSStorageType         =7          # from enum FRETPStorageTypeConstants
	frFileDRAMStorageType         =6          # from enum FRETPStorageTypeConstants
	frFileStorageType             =3          # from enum FRETPStorageTypeConstants
	frShadowCMOSStorageType       =5          # from enum FRETPStorageTypeConstants
	frShadowOnDemandCMOSStorageType=8          # from enum FRETPStorageTypeConstants
	frShadowOnDemandDRAMStorageType=9          # from enum FRETPStorageTypeConstants
	frShadowOnDemandStorageType   =4          # from enum FRETPStorageTypeConstants
	frShadowStorageType           =2          # from enum FRETPStorageTypeConstants
	frCollectionTPSubType         =7          # from enum FRETPSubTypeConstants
	frConditionTPSubType          =4          # from enum FRETPSubTypeConstants
	frJobTPSubType                =1          # from enum FRETPSubTypeConstants
	frMacroTPSubType              =3          # from enum FRETPSubTypeConstants
	frNoneTPSubType               =0          # from enum FRETPSubTypeConstants
	frPalletTPSubType             =5          # from enum FRETPSubTypeConstants
	frPanelTPSubType              =6          # from enum FRETPSubTypeConstants
	frProcessTPSubType            =2          # from enum FRETPSubTypeConstants
	frTaskAttrAllAtr              =100        # from enum FRETaskAttributeConstants
	frTaskAttrBusyLampOff         =112        # from enum FRETaskAttributeConstants
	frTaskAttrCircMotion          =125        # from enum FRETaskAttributeConstants
	frTaskAttrCurLine             =106        # from enum FRETaskAttributeConstants
	frTaskAttrDuration            =103        # from enum FRETaskAttributeConstants
	frTaskAttrEPTIndex            =104        # from enum FRETaskAttributeConstants
	frTaskAttrERPrgName           =129        # from enum FRETaskAttributeConstants
	frTaskAttrIgnoreAbort         =110        # from enum FRETaskAttributeConstants
	frTaskAttrIgnorePause         =111        # from enum FRETaskAttributeConstants
	frTaskAttrInvisibleTask       =120        # from enum FRETaskAttributeConstants
	frTaskAttrLockedArm           =126        # from enum FRETaskAttributeConstants
	frTaskAttrMotionCtl           =127        # from enum FRETaskAttributeConstants
	frTaskAttrNumChild            =117        # from enum FRETaskAttributeConstants
	frTaskAttrNumOutMMR           =128        # from enum FRETaskAttributeConstants
	frTaskAttrParenNum            =119        # from enum FRETaskAttributeConstants
	frTaskAttrPauseOnShift        =123        # from enum FRETaskAttributeConstants
	frTaskAttrProgName            =131        # from enum FRETaskAttributeConstants
	frTaskAttrProgType            =105        # from enum FRETaskAttributeConstants
	frTaskAttrRoutName            =132        # from enum FRETaskAttributeConstants
	frTaskAttrStepTask            =113        # from enum FRETaskAttributeConstants
	frTaskAttrStkSize             =109        # from enum FRETaskAttributeConstants
	frTaskAttrSuperMotion         =116        # from enum FRETaskAttributeConstants
	frTaskAttrSystemTask          =121        # from enum FRETaskAttributeConstants
	frTaskAttrTCDStatus           =124        # from enum FRETaskAttributeConstants
	frTaskAttrTPMotion            =115        # from enum FRETaskAttributeConstants
	frTaskAttrTaskName            =101        # from enum FRETaskAttributeConstants
	frTaskAttrTaskPri             =102        # from enum FRETaskAttributeConstants
	frTaskAttrTaskSt              =107        # from enum FRETaskAttributeConstants
	frTaskAttrTraceEnb            =114        # from enum FRETaskAttributeConstants
	frTaskAttrTraceLength         =118        # from enum FRETaskAttributeConstants
	frTaskAttrTskHld              =108        # from enum FRETaskAttributeConstants
	frTaskAttrUserTaskID          =130        # from enum FRETaskAttributeConstants
	frTaskAttrVarWriteEnable      =122        # from enum FRETaskAttributeConstants
	frIgnoreCommand               =2          # from enum FRETaskIgnoreConstants
	frIgnoreError                 =1          # from enum FRETaskIgnoreConstants
	frIgnoreErrorAbort            =16         # from enum FRETaskIgnoreConstants
	frIgnorePauseAbort            =8          # from enum FRETaskIgnoreConstants
	frIgnoreTP                    =4          # from enum FRETaskIgnoreConstants
	frStatusAborted               =2          # from enum FRETaskStatusConstants
	frStatusAborting              =-1         # from enum FRETaskStatusConstants
	frStatusIdle                  =-32768     # from enum FRETaskStatusConstants
	frStatusPaused                =1          # from enum FRETaskStatusConstants
	frStatusRun                   =0          # from enum FRETaskStatusConstants
	frStatusRunAccept             =-2         # from enum FRETaskStatusConstants
	frCoarseTermType              =2          # from enum FRETermTypeConstants
	frFineTermType                =1          # from enum FRETermTypeConstants
	frNoDecelTermType             =4          # from enum FRETermTypeConstants
	frNoSettleTermType            =3          # from enum FRETermTypeConstants
	frVarDecelTermType            =5          # from enum FRETermTypeConstants
	frArrayType                   =215        # from enum FRETypeCodeConstants
	frBooleanType                 =18         # from enum FRETypeCodeConstants
	frByteType                    =24         # from enum FRETypeCodeConstants
	frCommonAssocType             =20         # from enum FRETypeCodeConstants
	frConfigType                  =28         # from enum FRETypeCodeConstants
	frExtTransform                =5          # from enum FRETypeCodeConstants
	frExtXyz456                   =8          # from enum FRETypeCodeConstants
	frExtXyzAes                   =7          # from enum FRETypeCodeConstants
	frExtXyzWpr                   =6          # from enum FRETypeCodeConstants
	frFileType                    =29         # from enum FRETypeCodeConstants
	frGroupAssocType              =30         # from enum FRETypeCodeConstants
	frIntegerType                 =16         # from enum FRETypeCodeConstants
	frJoint                       =9          # from enum FRETypeCodeConstants
	frPathType                    =31         # from enum FRETypeCodeConstants
	frRealType                    =17         # from enum FRETypeCodeConstants
	frRegNumericType              =38         # from enum FRETypeCodeConstants
	frRegPositionType             =37         # from enum FRETypeCodeConstants
	frRegStringType               =39         # from enum FRETypeCodeConstants
	frShortType                   =23         # from enum FRETypeCodeConstants
	frStringType                  =209        # from enum FRETypeCodeConstants
	frStructureType               =210        # from enum FRETypeCodeConstants
	frTransform                   =1          # from enum FRETypeCodeConstants
	frVectorType                  =19         # from enum FRETypeCodeConstants
	frXyz456                      =4          # from enum FRETypeCodeConstants
	frXyzAes                      =3          # from enum FRETypeCodeConstants
	frXyzWpr                      =2          # from enum FRETypeCodeConstants
	frVarApplicationControlAccess =16         # from enum FREVarAccessCodeConstants
	frVarFieldProtectionAccess    =5          # from enum FREVarAccessCodeConstants
	frVarMotionControlAccess      =8          # from enum FREVarAccessCodeConstants
	frVarNoAccess                 =0          # from enum FREVarAccessCodeConstants
	frVarReadAccess               =1          # from enum FREVarAccessCodeConstants
	frVarReadWriteAccess          =3          # from enum FREVarAccessCodeConstants
	frRefreshSysvarsOverride      =4          # from enum FREVarOverrideConstants
	frVarAccessOverride           =1          # from enum FREVarOverrideConstants
	frVarAllOverride              =-1         # from enum FREVarOverrideConstants
	frVarLimitOverride            =2          # from enum FREVarOverrideConstants
	frVarNoOverride               =0          # from enum FREVarOverrideConstants
	frVarCMOS                     =253        # from enum FREVarStorageClassConstants
	frVarDRAM                     =0          # from enum FREVarStorageClassConstants
	frVarFastCMOS                 =252        # from enum FREVarStorageClassConstants

from win32com.client import DispatchBaseClass
class IAlarm(DispatchBaseClass):
	'\x0bThis object contains error and cause data for the item selected from the FRCAlarms collection.'
	CLSID = IID('{7C37F236-A494-11D0-A37F-0020AF39BE5A}')
	coclass_clsid = IID('{7C37F237-A494-11D0-A37F-0020AF39BE5A}')

	_prop_map_get_ = {
		"CauseFacility": (207, 2, (3, 0), (), "CauseFacility", None),
		"CauseMessage": (209, 2, (8, 0), (), "CauseMessage", None),
		"CauseMnemonic": (214, 2, (8, 0), (), "CauseMnemonic", None),
		"CauseNumber": (208, 2, (3, 0), (), "CauseNumber", None),
		"ErrorClass": (215, 2, (3, 0), (), "ErrorClass", None),
		"ErrorExecution": (203, 2, (3, 0), (), "ErrorExecution", None),
		"ErrorFacility": (201, 2, (3, 0), (), "ErrorFacility", None),
		"ErrorMessage": (206, 2, (8, 0), (), "ErrorMessage", None),
		"ErrorMnemonic": (213, 2, (8, 0), (), "ErrorMnemonic", None),
		"ErrorMotion": (204, 2, (3, 0), (), "ErrorMotion", None),
		"ErrorNumber": (205, 2, (3, 0), (), "ErrorNumber", None),
		"ErrorSeverity": (202, 2, (3, 0), (), "ErrorSeverity", None),
		"HostName": (216, 2, (8, 0), (), "HostName", None),
		"IPAddress": (217, 2, (8, 0), (), "IPAddress", None),
		"Index": (212, 2, (3, 0), (), "Index", None),
		# Method 'Robot' returns object of type 'FRCRobot'
		"Robot": (1, 2, (13, 0), (), "Robot", '{6D7E3A01-9ECC-11D0-94D5-0020AF68F0A3}'),
		"SeverityMessage": (211, 2, (8, 0), (), "SeverityMessage", None),
		"TimeStamp": (210, 2, (7, 0), (), "TimeStamp", None),
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

class IAlarmNotify:
	CLSID = CLSID_Sink = IID('{7DD25A00-AC49-11D0-8B7F-0020AF39BE5A}')
	coclass_clsid = IID('{7C37F235-A494-11D0-A37F-0020AF39BE5A}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        1 : "OnAlarmNotify",
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
#	def OnAlarmNotify(self, Alarm=defaultNamedNotOptArg):
#		'\x0bOccurs when an alarm is created by the controller, including RESET, CLEAR, and CLEAR ALL.'


class IAlarms(DispatchBaseClass):
	'\x0bThe FRCAlarms object is a collection of FRCAlarm objects.  This collection contains all the alarms that have occurred since the last time that the log was cleared, up to a predefined number.'
	CLSID = IID('{7C37F232-A494-11D0-A37F-0020AF39BE5A}')
	coclass_clsid = IID('{7C37F235-A494-11D0-A37F-0020AF39BE5A}')

	# Result is of type FRCAlarm
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Index=defaultNamedNotOptArg):
		'\x0bReturns a particular FRCAlarm object from the alarm log. '
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (13, 0), ((3, 1),),Index
			)
		if ret is not None:
			# See if this IUnknown is really an IDispatch
			try:
				ret = ret.QueryInterface(pythoncom.IID_IDispatch)
			except pythoncom.error:
				return ret
			ret = Dispatch(ret, 'Item', '{7C37F237-A494-11D0-A37F-0020AF39BE5A}')
		return ret

	def Reset(self):
		'\x0bIssues a RESET command to the controller.'
		return self._oleobj_.InvokeTypes(205, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"ActiveAlarms": (204, 2, (11, 0), (), "ActiveAlarms", None),
		"Count": (201, 2, (3, 0), (), "Count", None),
		"Max": (203, 2, (3, 0), (), "Max", None),
		# Method 'Robot' returns object of type 'FRCRobot'
		"Robot": (1, 2, (13, 0), (), "Robot", '{6D7E3A01-9ECC-11D0-94D5-0020AF68F0A3}'),
	}
	_prop_map_put_ = {
		"Max": ((203, LCID, 4, 0),()),
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		'\x0bReturns a particular FRCAlarm object from the alarm log. '
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (13, 0), ((3, 1),),Index
			)
		if ret is not None:
			# See if this IUnknown is really an IDispatch
			try:
				ret = ret.QueryInterface(pythoncom.IID_IDispatch)
			except pythoncom.error:
				return ret
			ret = Dispatch(ret, '__call__', '{7C37F237-A494-11D0-A37F-0020AF39BE5A}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{7C37F237-A494-11D0-A37F-0020AF39BE5A}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(201, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IAnalogIOSignal(DispatchBaseClass):
	'\x0bRepresents an analog I/O signal.  '
	CLSID = IID('{714CC921-B4E5-11D0-A073-00A02436CF7E}')
	coclass_clsid = IID('{714CC92E-B4E5-11D0-A073-00A02436CF7E}')

	def Refresh(self):
		'\x0bReads new information of the signal from the robot.'
		return self._oleobj_.InvokeTypes(252, LCID, 1, (24, 0), (),)

	def StartMonitor(self, Latency=defaultNamedNotOptArg):
		'\x0bStarts the monitoring of the I/O signal for changes.'
		return self._oleobj_.InvokeTypes(150, LCID, 1, (24, 0), ((3, 0),),Latency
			)

	def StopMonitor(self):
		'\x0bStops the monitoring of the I/O signal for changes.'
		return self._oleobj_.InvokeTypes(151, LCID, 1, (24, 0), (),)

	def Update(self):
		"\x0bSends the local copy of this signal's information to the robot."
		return self._oleobj_.InvokeTypes(253, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"IsAssigned": (103, 2, (11, 0), (), "IsAssigned", None),
		"IsMonitoring": (105, 2, (11, 0), (), "IsMonitoring", None),
		"IsOffline": (104, 2, (11, 0), (), "IsOffline", None),
		"LogicalNum": (101, 2, (3, 0), (), "LogicalNum", None),
		"NoRefresh": (250, 2, (11, 0), (), "NoRefresh", None),
		"NoUpdate": (251, 2, (11, 0), (), "NoUpdate", None),
		# Method 'Parent' returns object of type 'FRCIOSignals'
		"Parent": (203, 2, (13, 0), (), "Parent", '{59DC16F8-AF91-11D0-A072-00A02436CF7E}'),
		# Method 'Robot' returns object of type 'FRCRobot'
		"Robot": (1, 2, (13, 0), (), "Robot", '{6D7E3A01-9ECC-11D0-94D5-0020AF68F0A3}'),
		"Simulate": (202, 2, (11, 0), (), "Simulate", None),
		"Value": (201, 2, (3, 0), (), "Value", None),
	}
	_prop_map_put_ = {
		"Comment": ((102, LCID, 4, 0),()),
		"NoRefresh": ((250, LCID, 4, 0),()),
		"NoUpdate": ((251, LCID, 4, 0),()),
		"Simulate": ((202, LCID, 4, 0),()),
		"Value": ((201, LCID, 4, 0),()),
	}
	# Default property for this class is 'Value'
	def __call__(self):
		return self._ApplyTypes_(*(201, 2, (3, 0), (), "Value", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IApplications(DispatchBaseClass):
	'\x0bThis object is a general-purpose collection of application specific objects.'
	CLSID = IID('{78063945-E50A-11D1-B778-00C04FB99C75}')
	coclass_clsid = IID('{679622C3-E50A-11D1-B778-00C04FB99C75}')

	def Add(self, AppObject=defaultNamedNotOptArg, Key=defaultNamedNotOptArg):
		'\x0bAdds an application specific object to the Applications collection.  '
		return self._oleobj_.InvokeTypes(151, LCID, 1, (24, 0), ((9, 1), (8, 1)),AppObject
			, Key)

	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Key=defaultNamedNotOptArg):
		'\x0bReturns an object from the Applications collection object.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((8, 1),),Key
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', None)
		return ret

	def Remove(self, Key=defaultNamedNotOptArg):
		'\x0bRemoves an application specific object from the Applications collection.  '
		return self._oleobj_.InvokeTypes(152, LCID, 1, (24, 0), ((8, 1),),Key
			)

	_prop_map_get_ = {
		"Count": (101, 2, (3, 0), (), "Count", None),
		# Method 'Robot' returns object of type 'FRCRobot'
		"Robot": (1, 2, (13, 0), (), "Robot", '{6D7E3A01-9ECC-11D0-94D5-0020AF68F0A3}'),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Key=defaultNamedNotOptArg):
		'\x0bReturns an object from the Applications collection object.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((8, 1),),Key
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', None)
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(101, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IAxesCollection(DispatchBaseClass):
	'\x0bRepresents the extended axes for a position. '
	CLSID = IID('{035505A0-1C41-11D0-8901-0020AF68F0A3}')
	coclass_clsid = IID('{035505A1-1C41-11D0-8901-0020AF68F0A3}')

	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, JointNum=defaultNamedNotOptArg):
		'\x0bReturns/sets the values for each extended axis in the position.'
		return self._oleobj_.InvokeTypes(0, LCID, 2, (5, 0), ((2, 1),),JointNum
			)

	# The method SetItem is actually a property, but must be used as a method to correctly pass the arguments
	def SetItem(self, JointNum=defaultNamedNotOptArg, arg1=defaultUnnamedArg):
		'\x0bReturns/sets the values for each extended axis in the position.'
		return self._oleobj_.InvokeTypes(0, LCID, 4, (24, 0), ((2, 1), (5, 1)),JointNum
			, arg1)

	_prop_map_get_ = {
		"Count": (101, 2, (2, 0), (), "Count", None),
		# Method 'Robot' returns object of type 'FRCRobot'
		"Robot": (1, 2, (13, 0), (), "Robot", '{6D7E3A01-9ECC-11D0-94D5-0020AF68F0A3}'),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, JointNum=defaultNamedNotOptArg):
		'\x0bReturns/sets the values for each extended axis in the position.'
		return self._oleobj_.InvokeTypes(0, LCID, 2, (5, 0), ((2, 1),),JointNum
			)

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(101, 2, (2, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ICartesianFormat(DispatchBaseClass):
	'\x0bRepresents the position of a single group of axes as a transformation matrix consisting of normal, orient, approach, and location vectors and a component specifying a configuration.'
	CLSID = IID('{D42AB5DC-8FFB-11D0-94CC-0020AF68F0A3}')
	coclass_clsid = None

	_prop_map_get_ = {
		# Method 'Config' returns object of type 'FRCConfig'
		"Config": (201, 2, (13, 0), (), "Config", '{C58B0E61-ECD4-11D0-9FA5-00A024329125}'),
		# Method 'Ext' returns object of type 'FRCAxesCollection'
		"Ext": (202, 2, (13, 0), (), "Ext", '{035505A1-1C41-11D0-8901-0020AF68F0A3}'),
		# Method 'Parent' returns object of type 'FRCPosition'
		"Parent": (203, 2, (13, 0), (), "Parent", '{D42AB5DB-8FFB-11D0-94CC-0020AF68F0A3}'),
		# Method 'Program' returns object of type 'FRCProgram'
		"Program": (101, 2, (13, 0), (), "Program", '{D42AB5D5-8FFB-11D0-94CC-0020AF68F0A3}'),
		# Method 'Robot' returns object of type 'FRCRobot'
		"Robot": (1, 2, (13, 0), (), "Robot", '{6D7E3A01-9ECC-11D0-94D5-0020AF68F0A3}'),
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

class ICommonAssoc(DispatchBaseClass):
	'\x0bThis object is used to access standard associated data common for all KAREL path motion groups.'
	CLSID = IID('{34E3E250-1107-11D2-86F4-00C04F9184DB}')
	coclass_clsid = IID('{15AAA600-1108-11D2-86F4-00C04F9184DB}')

	_prop_map_get_ = {
		# Method 'Parent' returns object of type 'FRCVar'
		"Parent": (205, 2, (13, 0), (), "Parent", '{8C8ACC81-4F57-11D0-BC32-444553540000}'),
		# Method 'Program' returns object of type 'FRCProgram'
		"Program": (101, 2, (13, 0), (), "Program", '{D42AB5D5-8FFB-11D0-94CC-0020AF68F0A3}'),
		# Method 'Robot' returns object of type 'FRCRobot'
		"Robot": (1, 2, (13, 0), (), "Robot", '{6D7E3A01-9ECC-11D0-94D5-0020AF68F0A3}'),
		"SegDecelTol": (202, 2, (2, 0), (), "SegDecelTol", None),
		"SegRelAccel": (203, 2, (2, 0), (), "SegRelAccel", None),
		"SegTermType": (201, 2, (3, 0), (), "SegTermType", None),
		"SegTimeShift": (204, 2, (2, 0), (), "SegTimeShift", None),
	}
	_prop_map_put_ = {
		"SegDecelTol": ((202, LCID, 4, 0),()),
		"SegRelAccel": ((203, LCID, 4, 0),()),
		"SegTermType": ((201, LCID, 4, 0),()),
		"SegTimeShift": ((204, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IConfig(DispatchBaseClass):
	'\x0bRepresents a Cartesian position’s configuration.'
	CLSID = IID('{C58B0E60-ECD4-11D0-9FA5-00A024329125}')
	coclass_clsid = IID('{C58B0E61-ECD4-11D0-9FA5-00A024329125}')

	# The method SetTurnNum is actually a property, but must be used as a method to correctly pass the arguments
	def SetTurnNum(self, Index=defaultNamedNotOptArg, arg1=defaultUnnamedArg):
		'\x0bReturns/sets each turn number of the configuration.'
		return self._oleobj_.InvokeTypes(201, LCID, 4, (24, 0), ((2, 1), (2, 1)),Index
			, arg1)

	# The method TurnNum is actually a property, but must be used as a method to correctly pass the arguments
	def TurnNum(self, Index=defaultNamedNotOptArg):
		'\x0bReturns/sets each turn number of the configuration.'
		return self._oleobj_.InvokeTypes(201, LCID, 2, (2, 0), ((2, 1),),Index
			)

	_prop_map_get_ = {
		"Flip": (202, 2, (11, 0), (), "Flip", None),
		"Front": (205, 2, (11, 0), (), "Front", None),
		"Left": (203, 2, (11, 0), (), "Left", None),
		"Parent": (206, 2, (9, 0), (), "Parent", None),
		# Method 'Program' returns object of type 'FRCProgram'
		"Program": (101, 2, (13, 0), (), "Program", '{D42AB5D5-8FFB-11D0-94CC-0020AF68F0A3}'),
		# Method 'Robot' returns object of type 'FRCRobot'
		"Robot": (1, 2, (13, 0), (), "Robot", '{6D7E3A01-9ECC-11D0-94D5-0020AF68F0A3}'),
		"Text": (0, 2, (8, 0), (), "Text", None),
		"Up": (204, 2, (11, 0), (), "Up", None),
	}
	_prop_map_put_ = {
		"Flip": ((202, LCID, 4, 0),()),
		"Front": ((205, LCID, 4, 0),()),
		"Left": ((203, LCID, 4, 0),()),
		"Text": ((0, LCID, 4, 0),()),
		"Up": ((204, LCID, 4, 0),()),
	}
	# Default property for this class is 'Text'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (8, 0), (), "Text", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IConfigurableIOType(DispatchBaseClass):
	'\x0bThis object is used to access both I/O signal and I/O configuration collections.'
	CLSID = IID('{59DC16F3-AF91-11D0-A072-00A02436CF7E}')
	coclass_clsid = IID('{714CC920-B4E5-11D0-A073-00A02436CF7E}')

	_prop_map_get_ = {
		"CanComplement": (208, 2, (11, 0), (), "CanComplement", None),
		"CanConfigure": (205, 2, (11, 0), (), "CanConfigure", None),
		"CanInvert": (207, 2, (11, 0), (), "CanInvert", None),
		"CanSimulate": (206, 2, (11, 0), (), "CanSimulate", None),
		# Method 'Configs' returns object of type 'FRCIOConfigs'
		"Configs": (301, 2, (13, 0), (), "Configs", '{59DC1701-AF91-11D0-A072-00A02436CF7E}'),
		"IsBoolean": (204, 2, (11, 0), (), "IsBoolean", None),
		"IsInput": (203, 2, (11, 0), (), "IsInput", None),
		"Name": (201, 2, (8, 0), (), "Name", None),
		# Method 'Parent' returns object of type 'FRCIOTypes'
		"Parent": (102, 2, (13, 0), (), "Parent", '{59DC16ED-AF91-11D0-A072-00A02436CF7E}'),
		# Method 'Robot' returns object of type 'FRCRobot'
		"Robot": (1, 2, (13, 0), (), "Robot", '{6D7E3A01-9ECC-11D0-94D5-0020AF68F0A3}'),
		# Method 'Signals' returns object of type 'FRCIOSignals'
		"Signals": (202, 2, (13, 0), (), "Signals", '{59DC16F8-AF91-11D0-A072-00A02436CF7E}'),
		"Type": (101, 2, (2, 0), (), "Type", None),
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

class ICurGroupPosition(DispatchBaseClass):
	'\x0bProvides access to the current position of the robot for a specific motion group.'
	CLSID = IID('{75CEF1D6-1E43-11D1-B6FF-00C04FB9C401}')
	coclass_clsid = IID('{75CEF1D7-1E43-11D1-B6FF-00C04FB9C401}')

	def CheckReach(self, From=defaultNamedNotOptArg, MoType=6, OrientType=2, Destination=defaultNamedNotOptArg
			, MotionErrorInfo=0):
		'\x0bReturns a Boolean indicating if the robot can reach the position or not.'
		return self._ApplyTypes_(305, 1, (11, 0), ((12, 17), (3, 49), (3, 49), (12, 17), (16397, 50)), 'CheckReach', None,From
			, MoType, OrientType, Destination, MotionErrorInfo)

	def Copy(self, Position=defaultNamedNotOptArg):
		'\x0bCopies the positional data from another object into this one.'
		return self._oleobj_.InvokeTypes(304, LCID, 1, (24, 0), ((9, 1),),Position
			)

	# The method Formats is actually a property, but must be used as a method to correctly pass the arguments
	def Formats(self, Type=defaultNamedNotOptArg):
		'\x0bReturns positional data in the specified format.'
		ret = self._oleobj_.InvokeTypes(203, LCID, 2, (9, 0), ((3, 1),),Type
			)
		if ret is not None:
			ret = Dispatch(ret, 'Formats', None)
		return ret

	# The method IsEqualTo is actually a property, but must be used as a method to correctly pass the arguments
	def IsEqualTo(self, TargetPos=defaultNamedNotOptArg):
		"Returns a boolean value that indicates if the positional data contained in the current object is 'almost equal to' the positional data of another object."
		return self._oleobj_.InvokeTypes(302, LCID, 2, (11, 0), ((9, 1),),TargetPos
			)

	# The method IsReachable is actually a property, but must be used as a method to correctly pass the arguments
	def IsReachable(self, From=defaultNamedNotOptArg, MoType=6, OrientType=2, Destination=defaultNamedNotOptArg
			, MotionErrorInfo=0):
		'\x0bReturns a Boolean indicating if the robot can reach the position or not.'
		return self._ApplyTypes_(303, 2, (11, 0), ((12, 17), (3, 49), (3, 49), (12, 17), (16397, 50)), 'IsReachable', None,From
			, MoType, OrientType, Destination, MotionErrorInfo)

	def MatInv(self, InputPos=defaultNamedNotOptArg):
		'\x0bInvert the input position transformation matrix and set the results to this position.'
		return self._oleobj_.InvokeTypes(259, LCID, 1, (24, 0), ((9, 1),),InputPos
			)

	def MatMul(self, LeftPos=defaultNamedNotOptArg, RightPos=defaultNamedNotOptArg):
		'\x0bMultiply two input positions’ transformation matrices and set the results to this position.'
		return self._oleobj_.InvokeTypes(258, LCID, 1, (24, 0), ((9, 1), (9, 1)),LeftPos
			, RightPos)

	def Moveto(self):
		'\x0bMoves the robot to this position.'
		return self._oleobj_.InvokeTypes(253, LCID, 1, (24, 0), (),)

	def Record(self):
		'\x0bRecords the current position of the robot to this position.'
		return self._oleobj_.InvokeTypes(254, LCID, 1, (24, 0), (),)

	def Refresh(self):
		'\x0bClears all changes to the position since the last update of the position.'
		return self._oleobj_.InvokeTypes(252, LCID, 1, (24, 0), (),)

	def StartMonitor(self, Latency=defaultNamedNotOptArg):
		'\x0bEnables the Change event, with specified latency.'
		return self._oleobj_.InvokeTypes(255, LCID, 1, (24, 0), ((3, 1),),Latency
			)

	def StopMonitor(self):
		'\x0bStops the Change event from occurring.'
		return self._oleobj_.InvokeTypes(256, LCID, 1, (24, 0), (),)

	def Uninitialize(self):
		'\x0bUninitializes the position. '
		return self._oleobj_.InvokeTypes(257, LCID, 1, (24, 0), (),)

	def Update(self):
		'\x0bUpdates any changes to the position back to the controller.'
		return self._oleobj_.InvokeTypes(251, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"AutomaticUpdate": (201, 2, (11, 0), (), "AutomaticUpdate", None),
		"GroupNum": (204, 2, (2, 0), (), "GroupNum", None),
		"Id": (205, 2, (3, 0), (), "Id", None),
		"IsAtCurPosition": (206, 2, (11, 0), (), "IsAtCurPosition", None),
		"IsInitialized": (207, 2, (11, 0), (), "IsInitialized", None),
		"IsMonitoring": (210, 2, (11, 0), (), "IsMonitoring", None),
		# Method 'Parent' returns object of type 'FRCCurPosition'
		"Parent": (301, 2, (13, 0), (), "Parent", '{E2686FA9-1E42-11D1-B6FF-00C04FB9C401}'),
		# Method 'Program' returns object of type 'FRCProgram'
		"Program": (101, 2, (13, 0), (), "Program", '{D42AB5D5-8FFB-11D0-94CC-0020AF68F0A3}'),
		# Method 'Robot' returns object of type 'FRCRobot'
		"Robot": (1, 2, (13, 0), (), "Robot", '{6D7E3A01-9ECC-11D0-94D5-0020AF68F0A3}'),
		"Type": (202, 2, (3, 0), (), "Type", None),
		"UserFrame": (208, 2, (3, 0), (), "UserFrame", None),
		"UserTool": (209, 2, (3, 0), (), "UserTool", None),
	}
	_prop_map_put_ = {
		"AutomaticUpdate": ((201, LCID, 4, 0),()),
		"Type": ((202, LCID, 4, 0),()),
		"UserFrame": ((208, LCID, 4, 0),()),
		"UserTool": ((209, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ICurGroupPositionEvents:
	CLSID = CLSID_Sink = IID('{2BF7E386-87A9-11D1-B765-00C04FBBE42A}')
	coclass_clsid = IID('{75CEF1D7-1E43-11D1-B6FF-00C04FB9C401}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        1 : "OnChange",
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
#	def OnChange(self):
#		'\x0bOccurs when the current position on the controller is changed.'


class ICurPosition(DispatchBaseClass):
	'\x0bProvides access to the current position of the robot for all motion groups.'
	CLSID = IID('{E2686FA8-1E42-11D1-B6FF-00C04FB9C401}')
	coclass_clsid = IID('{E2686FA9-1E42-11D1-B6FF-00C04FB9C401}')

	# Result is of type FRCCurGroupPosition
	# The method Group is actually a property, but must be used as a method to correctly pass the arguments
	def Group(self, GroupNum=defaultNamedNotOptArg, DisplayType=defaultNamedNotOptArg):
		'\x0bReturns FRCCurGroupPosition object representing the current position of the robot for the specified group and DisplayType.'
		ret = self._oleobj_.InvokeTypes(202, LCID, 2, (13, 0), ((2, 1), (3, 1)),GroupNum
			, DisplayType)
		if ret is not None:
			# See if this IUnknown is really an IDispatch
			try:
				ret = ret.QueryInterface(pythoncom.IID_IDispatch)
			except pythoncom.error:
				return ret
			ret = Dispatch(ret, 'Group', '{75CEF1D7-1E43-11D1-B6FF-00C04FB9C401}')
		return ret

	# The method GroupMask is actually a property, but must be used as a method to correctly pass the arguments
	def GroupMask(self, GroupNum=defaultNamedNotOptArg):
		'\x0bReturns whether the specified group is supported on the controller.'
		return self._oleobj_.InvokeTypes(201, LCID, 2, (11, 0), ((2, 1),),GroupNum
			)

	def StartMonitor(self, Latency=defaultNamedNotOptArg):
		'\x0bEnables the Change event, with specified latency.'
		return self._oleobj_.InvokeTypes(250, LCID, 1, (24, 0), ((3, 0),),Latency
			)

	def StopMonitor(self):
		'\x0bStops the Change event from occurring.'
		return self._oleobj_.InvokeTypes(251, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"GroupBitMask": (252, 2, (3, 0), (), "GroupBitMask", None),
		"IsMonitoring": (204, 2, (11, 0), (), "IsMonitoring", None),
		"NumGroups": (203, 2, (2, 0), (), "NumGroups", None),
		# Method 'Robot' returns object of type 'FRCRobot'
		"Robot": (1, 2, (13, 0), (), "Robot", '{6D7E3A01-9ECC-11D0-94D5-0020AF68F0A3}'),
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

class ICurPositionEvents:
	CLSID = CLSID_Sink = IID('{EF22631E-87A8-11D1-B765-00C04FBBE42A}')
	coclass_clsid = IID('{E2686FA9-1E42-11D1-B6FF-00C04FB9C401}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        1 : "OnChange",
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
#	def OnChange(self, GroupList=defaultNamedNotOptArg):
#		'\x0bOccurs when the robot position changes.  Returns an array of which motion group positions have changed. '


class IDigitalIOSignal(DispatchBaseClass):
	'\x0bRepresents a digital I/O signal object.  '
	CLSID = IID('{59DC16FC-AF91-11D0-A072-00A02436CF7E}')
	coclass_clsid = IID('{714CC92F-B4E5-11D0-A073-00A02436CF7E}')

	def Refresh(self):
		'\x0bReads new information of the signal from the robot.'
		return self._oleobj_.InvokeTypes(252, LCID, 1, (24, 0), (),)

	def StartMonitor(self, Latency=defaultNamedNotOptArg):
		'\x0bStarts the monitoring of the I/O signal for changes.'
		return self._oleobj_.InvokeTypes(150, LCID, 1, (24, 0), ((3, 0),),Latency
			)

	def StopMonitor(self):
		'\x0bStops the monitoring of the I/O signal for changes.'
		return self._oleobj_.InvokeTypes(151, LCID, 1, (24, 0), (),)

	def Update(self):
		"\x0bSends the local copy of this signal's information to the robot."
		return self._oleobj_.InvokeTypes(253, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"Complementary": (204, 2, (11, 0), (), "Complementary", None),
		"IsAssigned": (103, 2, (11, 0), (), "IsAssigned", None),
		"IsMonitoring": (105, 2, (11, 0), (), "IsMonitoring", None),
		"IsOffline": (104, 2, (11, 0), (), "IsOffline", None),
		"LogicalNum": (101, 2, (3, 0), (), "LogicalNum", None),
		"NoRefresh": (250, 2, (11, 0), (), "NoRefresh", None),
		"NoUpdate": (251, 2, (11, 0), (), "NoUpdate", None),
		# Method 'Parent' returns object of type 'FRCIOSignals'
		"Parent": (205, 2, (13, 0), (), "Parent", '{59DC16F8-AF91-11D0-A072-00A02436CF7E}'),
		"Polarity": (203, 2, (11, 0), (), "Polarity", None),
		# Method 'Robot' returns object of type 'FRCRobot'
		"Robot": (1, 2, (13, 0), (), "Robot", '{6D7E3A01-9ECC-11D0-94D5-0020AF68F0A3}'),
		"Simulate": (202, 2, (11, 0), (), "Simulate", None),
		"Value": (201, 2, (11, 0), (), "Value", None),
	}
	_prop_map_put_ = {
		"Comment": ((102, LCID, 4, 0),()),
		"Complementary": ((204, LCID, 4, 0),()),
		"NoRefresh": ((250, LCID, 4, 0),()),
		"NoUpdate": ((251, LCID, 4, 0),()),
		"Polarity": ((203, LCID, 4, 0),()),
		"Simulate": ((202, LCID, 4, 0),()),
		"Value": ((201, LCID, 4, 0),()),
	}
	# Default property for this class is 'Value'
	def __call__(self):
		return self._ApplyTypes_(*(201, 2, (11, 0), (), "Value", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IFeature(DispatchBaseClass):
	'\x0bThis object represents a single feature loaded on the controller.  '
	CLSID = IID('{2AF44185-9273-11D1-B6F9-00C04FA3BD85}')
	coclass_clsid = IID('{2AF44186-9273-11D1-B6F9-00C04FA3BD85}')

	_prop_map_get_ = {
		"Name": (102, 2, (8, 0), (), "Name", None),
		"OrderNumber": (101, 2, (8, 0), (), "OrderNumber", None),
		# Method 'Robot' returns object of type 'FRCRobot'
		"Robot": (1, 2, (13, 0), (), "Robot", '{6D7E3A01-9ECC-11D0-94D5-0020AF68F0A3}'),
		"Version": (103, 2, (8, 0), (), "Version", None),
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

class IFeatures(DispatchBaseClass):
	'\x0bThe features collection is a representation of all currently loaded controller features.  This collection will contain one object for each feature.  '
	CLSID = IID('{2AF44183-9273-11D1-B6F9-00C04FA3BD85}')
	coclass_clsid = IID('{2AF44184-9273-11D1-B6F9-00C04FA3BD85}')

	# Result is of type FRCFeature
	# The method GetItem is actually a property, but must be used as a method to correctly pass the arguments
	def GetItem(self, OrderNumber=defaultNamedOptArg, Index=defaultNamedOptArg):
		' \x0bItem returns a feature object, specified by collection index or by order number, from the collection to the caller. '
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (13, 0), ((12, 17), (12, 17)),OrderNumber
			, Index)
		if ret is not None:
			# See if this IUnknown is really an IDispatch
			try:
				ret = ret.QueryInterface(pythoncom.IID_IDispatch)
			except pythoncom.error:
				return ret
			ret = Dispatch(ret, 'GetItem', '{2AF44186-9273-11D1-B6F9-00C04FA3BD85}')
		return ret

	# The method IsValid is actually a property, but must be used as a method to correctly pass the arguments
	def IsValid(self, OrderNumber=defaultNamedNotOptArg):
		'\x0bIsValid returns TRUE if a feature is loaded, and FALSE if it is not loaded. '
		return self._oleobj_.InvokeTypes(102, LCID, 2, (11, 0), ((8, 1),),OrderNumber
			)

	def Refresh(self):
		'\x0bRefresh rebuilds the features collection from the $FEATURE system variables.  '
		return self._oleobj_.InvokeTypes(150, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"Count": (101, 2, (3, 0), (), "Count", None),
		# Method 'Item' returns object of type 'FRCFeature'
		"Item": (0, 2, (13, 0), ((12, 17), (12, 17)), "Item", '{2AF44186-9273-11D1-B6F9-00C04FA3BD85}'),
		# Method 'Robot' returns object of type 'FRCRobot'
		"Robot": (1, 2, (13, 0), (), "Robot", '{6D7E3A01-9ECC-11D0-94D5-0020AF68F0A3}'),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, OrderNumber=defaultNamedOptArg, Index=defaultNamedOptArg):
		' \x0bItem returns a feature object, specified by collection index or by order number, from the collection to the caller. '
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (13, 0), ((12, 17), (12, 17)),OrderNumber
			, Index)
		if ret is not None:
			# See if this IUnknown is really an IDispatch
			try:
				ret = ret.QueryInterface(pythoncom.IID_IDispatch)
			except pythoncom.error:
				return ret
			ret = Dispatch(ret, '__call__', '{2AF44186-9273-11D1-B6F9-00C04FA3BD85}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(101, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IGroupAssoc(DispatchBaseClass):
	'\x0bThis object is used to access standard associated data for all KAREL path motion groups.'
	CLSID = IID('{424160A0-1108-11D2-86F4-00C04F9184DB}')
	coclass_clsid = IID('{4DE6A770-1108-11D2-86F4-00C04F9184DB}')

	_prop_map_get_ = {
		# Method 'Parent' returns object of type 'FRCVar'
		"Parent": (205, 2, (13, 0), (), "Parent", '{8C8ACC81-4F57-11D0-BC32-444553540000}'),
		# Method 'Program' returns object of type 'FRCProgram'
		"Program": (101, 2, (13, 0), (), "Program", '{D42AB5D5-8FFB-11D0-94CC-0020AF68F0A3}'),
		# Method 'Robot' returns object of type 'FRCRobot'
		"Robot": (1, 2, (13, 0), (), "Robot", '{6D7E3A01-9ECC-11D0-94D5-0020AF68F0A3}'),
		"SegBreak": (204, 2, (11, 0), (), "SegBreak", None),
		"SegMoType": (202, 2, (3, 0), (), "SegMoType", None),
		"SegOrientType": (203, 2, (3, 0), (), "SegOrientType", None),
		"SegRelSpeed": (201, 2, (2, 0), (), "SegRelSpeed", None),
	}
	_prop_map_put_ = {
		"SegBreak": ((204, LCID, 4, 0),()),
		"SegMoType": ((202, LCID, 4, 0),()),
		"SegOrientType": ((203, LCID, 4, 0),()),
		"SegRelSpeed": ((201, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IGroupPosition(DispatchBaseClass):
	'\x0bProvides access to the positional data of a TP position for a specific motion group.'
	CLSID = IID('{A47A5880-056D-11D0-8901-0020AF68F0A3}')
	coclass_clsid = IID('{A47A5881-056D-11D0-8901-0020AF68F0A3}')

	def CheckReach(self, From=defaultNamedNotOptArg, MoType=6, OrientType=2, Destination=defaultNamedNotOptArg
			, MotionErrorInfo=0):
		'\x0bReturns a Boolean indicating if the robot can reach the position or not.'
		return self._ApplyTypes_(305, 1, (11, 0), ((12, 17), (3, 49), (3, 49), (12, 17), (16397, 50)), 'CheckReach', None,From
			, MoType, OrientType, Destination, MotionErrorInfo)

	def Copy(self, Position=defaultNamedNotOptArg):
		'\x0bCopies the positional data from another object into this one.'
		return self._oleobj_.InvokeTypes(304, LCID, 1, (24, 0), ((9, 1),),Position
			)

	# The method Formats is actually a property, but must be used as a method to correctly pass the arguments
	def Formats(self, Type=defaultNamedNotOptArg):
		'\x0bReturns positional data in the specified format.'
		ret = self._oleobj_.InvokeTypes(203, LCID, 2, (9, 0), ((3, 1),),Type
			)
		if ret is not None:
			ret = Dispatch(ret, 'Formats', None)
		return ret

	# The method IsEqualTo is actually a property, but must be used as a method to correctly pass the arguments
	def IsEqualTo(self, TargetPos=defaultNamedNotOptArg):
		"Returns a boolean value that indicates if the positional data contained in the current object is 'almost equal to' the positional data of another object."
		return self._oleobj_.InvokeTypes(302, LCID, 2, (11, 0), ((9, 1),),TargetPos
			)

	# The method IsReachable is actually a property, but must be used as a method to correctly pass the arguments
	def IsReachable(self, From=defaultNamedNotOptArg, MoType=6, OrientType=2, Destination=defaultNamedNotOptArg
			, MotionErrorInfo=0):
		'\x0bReturns a Boolean indicating if the robot can reach the position or not.'
		return self._ApplyTypes_(303, 2, (11, 0), ((12, 17), (3, 49), (3, 49), (12, 17), (16397, 50)), 'IsReachable', None,From
			, MoType, OrientType, Destination, MotionErrorInfo)

	def MatInv(self, InputPos=defaultNamedNotOptArg):
		'\x0bInvert the input position transformation matrix and set the results to this position.'
		return self._oleobj_.InvokeTypes(259, LCID, 1, (24, 0), ((9, 1),),InputPos
			)

	def MatMul(self, LeftPos=defaultNamedNotOptArg, RightPos=defaultNamedNotOptArg):
		'\x0bMultiply two input positions’ transformation matrices and set the results to this position.'
		return self._oleobj_.InvokeTypes(258, LCID, 1, (24, 0), ((9, 1), (9, 1)),LeftPos
			, RightPos)

	def Moveto(self):
		'\x0bMoves the robot to this position.'
		return self._oleobj_.InvokeTypes(253, LCID, 1, (24, 0), (),)

	def Record(self):
		'\x0bRecords the current position of the robot to this position.'
		return self._oleobj_.InvokeTypes(254, LCID, 1, (24, 0), (),)

	def Refresh(self):
		'\x0bClears all changes to the position since the last update of the position.'
		return self._oleobj_.InvokeTypes(252, LCID, 1, (24, 0), (),)

	def StartMonitor(self, Latency=defaultNamedNotOptArg):
		'\x0bEnables the Change event, with specified latency.'
		return self._oleobj_.InvokeTypes(255, LCID, 1, (24, 0), ((3, 1),),Latency
			)

	def StopMonitor(self):
		'\x0bStops the Change event from occurring.'
		return self._oleobj_.InvokeTypes(256, LCID, 1, (24, 0), (),)

	def Uninitialize(self):
		'\x0bUninitializes the position. '
		return self._oleobj_.InvokeTypes(257, LCID, 1, (24, 0), (),)

	def Update(self):
		'\x0bUpdates any changes to the position back to the controller.'
		return self._oleobj_.InvokeTypes(251, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"AutomaticUpdate": (201, 2, (11, 0), (), "AutomaticUpdate", None),
		"GroupNum": (204, 2, (2, 0), (), "GroupNum", None),
		"Id": (205, 2, (3, 0), (), "Id", None),
		"IsAtCurPosition": (206, 2, (11, 0), (), "IsAtCurPosition", None),
		"IsInitialized": (207, 2, (11, 0), (), "IsInitialized", None),
		"IsMonitoring": (210, 2, (11, 0), (), "IsMonitoring", None),
		# Method 'Parent' returns object of type 'FRCTPPosition'
		"Parent": (301, 2, (13, 0), (), "Parent", '{3A49BE61-F5B9-11CF-8901-0020AF68F0A3}'),
		# Method 'Program' returns object of type 'FRCProgram'
		"Program": (101, 2, (13, 0), (), "Program", '{D42AB5D5-8FFB-11D0-94CC-0020AF68F0A3}'),
		# Method 'Robot' returns object of type 'FRCRobot'
		"Robot": (1, 2, (13, 0), (), "Robot", '{6D7E3A01-9ECC-11D0-94D5-0020AF68F0A3}'),
		"Type": (202, 2, (3, 0), (), "Type", None),
		"UserFrame": (208, 2, (3, 0), (), "UserFrame", None),
		"UserTool": (209, 2, (3, 0), (), "UserTool", None),
	}
	_prop_map_put_ = {
		"AutomaticUpdate": ((201, LCID, 4, 0),()),
		"Type": ((202, LCID, 4, 0),()),
		"UserFrame": ((208, LCID, 4, 0),()),
		"UserTool": ((209, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IGroupPositionEvents:
	CLSID = CLSID_Sink = IID('{18B02B4D-9DA9-11D1-B73B-00C04FB9E76B}')
	coclass_clsid = IID('{A47A5881-056D-11D0-8901-0020AF68F0A3}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        1 : "OnChange",
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
#	def OnChange(self):
#		'\x0bOccurs after the position is changed.'


class IIOConfig(DispatchBaseClass):
	'\x0bThis object represents an input or output configuration.'
	CLSID = IID('{59DC1702-AF91-11D0-A072-00A02436CF7E}')
	coclass_clsid = IID('{59DC1703-AF91-11D0-A072-00A02436CF7E}')

	_prop_map_get_ = {
		"FirstLogicalNum": (101, 2, (3, 0), (), "FirstLogicalNum", None),
		"FirstPhysicalNum": (106, 2, (3, 0), (), "FirstPhysicalNum", None),
		"IsValid": (107, 2, (11, 0), (), "IsValid", None),
		"NumSignals": (102, 2, (3, 0), (), "NumSignals", None),
		# Method 'Parent' returns object of type 'FRCIOConfigs'
		"Parent": (108, 2, (13, 0), (), "Parent", '{59DC1701-AF91-11D0-A072-00A02436CF7E}'),
		"PhysicalType": (105, 2, (3, 0), (), "PhysicalType", None),
		"Rack": (103, 2, (2, 0), (), "Rack", None),
		# Method 'Robot' returns object of type 'FRCRobot'
		"Robot": (1, 2, (13, 0), (), "Robot", '{6D7E3A01-9ECC-11D0-94D5-0020AF68F0A3}'),
		"Slot": (104, 2, (2, 0), (), "Slot", None),
	}
	_prop_map_put_ = {
		"FirstPhysicalNum": ((106, LCID, 4, 0),()),
		"NumSignals": ((102, LCID, 4, 0),()),
		"PhysicalType": ((105, LCID, 4, 0),()),
		"Rack": ((103, LCID, 4, 0),()),
		"Slot": ((104, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IIOConfigEvents:
	CLSID = CLSID_Sink = IID('{051D0EE2-F930-11D0-B6EE-00C04FB9E76B}')
	coclass_clsid = IID('{59DC1703-AF91-11D0-A072-00A02436CF7E}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        1 : "OnDelete",
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
#	def OnDelete(self):
#		'\x0bOccurs before the configuration is deleted.'


class IIOConfigs(DispatchBaseClass):
	'\x0bThis object is used to access all I/O configurations for a particular I/O type.\x0b'
	CLSID = IID('{59DC1700-AF91-11D0-A072-00A02436CF7E}')
	coclass_clsid = IID('{59DC1701-AF91-11D0-A072-00A02436CF7E}')

	# Result is of type FRCIOConfig
	def Add(self, FirstLogicalNum=defaultNamedOptArg):
		'\x0bAdds a new configuration to the collection.  '
		ret = self._oleobj_.InvokeTypes(151, LCID, 1, (13, 0), ((12, 17),),FirstLogicalNum
			)
		if ret is not None:
			# See if this IUnknown is really an IDispatch
			try:
				ret = ret.QueryInterface(pythoncom.IID_IDispatch)
			except pythoncom.error:
				return ret
			ret = Dispatch(ret, 'Add', '{59DC1703-AF91-11D0-A072-00A02436CF7E}')
		return ret

	# Result is of type FRCIOConfig
	# The method GetItem is actually a property, but must be used as a method to correctly pass the arguments
	def GetItem(self, FirstLogicalNum=defaultNamedOptArg, Index=defaultNamedOptArg):
		'\x0bReturns a configuration from the collection.  '
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (13, 0), ((12, 17), (12, 17)),FirstLogicalNum
			, Index)
		if ret is not None:
			# See if this IUnknown is really an IDispatch
			try:
				ret = ret.QueryInterface(pythoncom.IID_IDispatch)
			except pythoncom.error:
				return ret
			ret = Dispatch(ret, 'GetItem', '{59DC1703-AF91-11D0-A072-00A02436CF7E}')
		return ret

	def Remove(self, FirstLogicalNum=defaultNamedOptArg, Index=defaultNamedOptArg):
		'\x0bRemoves a configuration from the collection.'
		return self._oleobj_.InvokeTypes(152, LCID, 1, (24, 0), ((12, 17), (12, 17)),FirstLogicalNum
			, Index)

	_prop_map_get_ = {
		"Count": (101, 2, (3, 0), (), "Count", None),
		# Method 'Item' returns object of type 'FRCIOConfig'
		"Item": (0, 2, (13, 0), ((12, 17), (12, 17)), "Item", '{59DC1703-AF91-11D0-A072-00A02436CF7E}'),
		# Method 'Parent' returns object of type 'FRCIOType'
		"Parent": (102, 2, (13, 0), (), "Parent", '{59DC16F1-AF91-11D0-A072-00A02436CF7E}'),
		# Method 'Robot' returns object of type 'FRCRobot'
		"Robot": (1, 2, (13, 0), (), "Robot", '{6D7E3A01-9ECC-11D0-94D5-0020AF68F0A3}'),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, FirstLogicalNum=defaultNamedOptArg, Index=defaultNamedOptArg):
		'\x0bReturns a configuration from the collection.  '
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (13, 0), ((12, 17), (12, 17)),FirstLogicalNum
			, Index)
		if ret is not None:
			# See if this IUnknown is really an IDispatch
			try:
				ret = ret.QueryInterface(pythoncom.IID_IDispatch)
			except pythoncom.error:
				return ret
			ret = Dispatch(ret, '__call__', '{59DC1703-AF91-11D0-A072-00A02436CF7E}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(101, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IIOConfigsEvents:
	CLSID = CLSID_Sink = IID('{021408E1-F879-11D0-A093-00A02436CF7E}')
	coclass_clsid = IID('{59DC1701-AF91-11D0-A072-00A02436CF7E}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        1 : "OnCreate",
		        2 : "OnDelete",
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
#	def OnCreate(self, IOConfig=defaultNamedNotOptArg):
#		'\x0bOccurs after a configuration is created.'
#	def OnDelete(self, IOConfig=defaultNamedNotOptArg):
#		'\x0bOccurs after a configuration is deleted.'


class IIOSignal(DispatchBaseClass):
	'\x0bRepresents an I/O signal.  '
	CLSID = IID('{59DC16FB-AF91-11D0-A072-00A02436CF7E}')
	coclass_clsid = None

	def StartMonitor(self, Latency=defaultNamedNotOptArg):
		'\x0bStarts the monitoring of the I/O signal for changes.'
		return self._oleobj_.InvokeTypes(150, LCID, 1, (24, 0), ((3, 0),),Latency
			)

	def StopMonitor(self):
		'\x0bStops the monitoring of the I/O signal for changes.'
		return self._oleobj_.InvokeTypes(151, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"IsAssigned": (103, 2, (11, 0), (), "IsAssigned", None),
		"IsMonitoring": (105, 2, (11, 0), (), "IsMonitoring", None),
		"IsOffline": (104, 2, (11, 0), (), "IsOffline", None),
		"LogicalNum": (101, 2, (3, 0), (), "LogicalNum", None),
		# Method 'Robot' returns object of type 'FRCRobot'
		"Robot": (1, 2, (13, 0), (), "Robot", '{6D7E3A01-9ECC-11D0-94D5-0020AF68F0A3}'),
	}
	_prop_map_put_ = {
		"Comment": ((102, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IIOSignal2(DispatchBaseClass):
	'\x0bRepresents an I/O signal.  '
	CLSID = IID('{D3EE1B91-8BB6-11D3-877C-00C04F81118D}')
	coclass_clsid = IID('{59DC170B-AF91-11D0-A072-00A02436CF7E}')

	def Refresh(self):
		'\x0bReads new information of the signal from the robot.'
		return self._oleobj_.InvokeTypes(252, LCID, 1, (24, 0), (),)

	def StartMonitor(self, Latency=defaultNamedNotOptArg):
		'\x0bStarts the monitoring of the I/O signal for changes.'
		return self._oleobj_.InvokeTypes(150, LCID, 1, (24, 0), ((3, 0),),Latency
			)

	def StopMonitor(self):
		'\x0bStops the monitoring of the I/O signal for changes.'
		return self._oleobj_.InvokeTypes(151, LCID, 1, (24, 0), (),)

	def Update(self):
		"\x0bSends the local copy of this signal's information to the robot."
		return self._oleobj_.InvokeTypes(253, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"IsAssigned": (103, 2, (11, 0), (), "IsAssigned", None),
		"IsMonitoring": (105, 2, (11, 0), (), "IsMonitoring", None),
		"IsOffline": (104, 2, (11, 0), (), "IsOffline", None),
		"LogicalNum": (101, 2, (3, 0), (), "LogicalNum", None),
		"NoRefresh": (250, 2, (11, 0), (), "NoRefresh", None),
		"NoUpdate": (251, 2, (11, 0), (), "NoUpdate", None),
		# Method 'Robot' returns object of type 'FRCRobot'
		"Robot": (1, 2, (13, 0), (), "Robot", '{6D7E3A01-9ECC-11D0-94D5-0020AF68F0A3}'),
		"Simulate": (202, 2, (11, 0), (), "Simulate", None),
		"Value": (201, 2, (11, 0), (), "Value", None),
	}
	_prop_map_put_ = {
		"Comment": ((102, LCID, 4, 0),()),
		"NoRefresh": ((250, LCID, 4, 0),()),
		"NoUpdate": ((251, LCID, 4, 0),()),
                "Simulate": ((202, LCID, 4, 0),()),
                "Value": ((201, LCID, 4, 0),()),
	}
	# Default property for this class is 'Value'
	def __call__(self):
		return self._ApplyTypes_(*(201, 2, (11, 0), (), "Value", None))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IIOSignalEvents:
	CLSID = CLSID_Sink = IID('{0DBE3EF1-F870-11D0-A093-00A02436CF7E}')
	coclass_clsid = IID('{714CC92F-B4E5-11D0-A073-00A02436CF7E}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        1 : "OnDelete",
		        2 : "OnChange",
		        3 : "OnSimulate",
		        4 : "OnUnsimulate",
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
#	def OnDelete(self):
#		'\x0bOccurs before the I/O signal is deleted.'
#	def OnChange(self):
#		'\x0bOccurs after the I/O signal has changed.'
#	def OnSimulate(self):
#		'\x0bOccurs after the I/O signal is simulated.'
#	def OnUnsimulate(self):
#		'\x0bOccurs after the I/O signal is unsimulated.'


class IIOSignals(DispatchBaseClass):
	'\x0bThis object is used to access all I/O signals for a particular I/O type.'
	CLSID = IID('{59DC16F7-AF91-11D0-A072-00A02436CF7E}')
	coclass_clsid = IID('{59DC16F8-AF91-11D0-A072-00A02436CF7E}')

	# Result is of type FRCIOSignal
	# The method GetItem is actually a property, but must be used as a method to correctly pass the arguments
	def GetItem(self, LogicalNum=defaultNamedOptArg, Index=defaultNamedOptArg):
		'\x0bReturns a specific signal from the collection. '
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (13, 0), ((12, 17), (12, 17)),LogicalNum
			, Index)
		if ret is not None:
			# See if this IUnknown is really an IDispatch
			try:
				ret = ret.QueryInterface(pythoncom.IID_IDispatch)
			except pythoncom.error:
				return ret
			ret = Dispatch(ret, 'GetItem', '{59DC170B-AF91-11D0-A072-00A02436CF7E}')
		return ret

	def Refresh(self):
		'\x0bRefreshes the I/O Signal data when the NoRefresh property is true.'
		return self._oleobj_.InvokeTypes(152, LCID, 1, (24, 0), (),)

	def StartMonitor(self, Latency=defaultNamedNotOptArg):
		'\x0bStarts the monitoring of the I/O signals collection for changes.'
		return self._oleobj_.InvokeTypes(150, LCID, 1, (24, 0), ((3, 0),),Latency
			)

	def StopMonitor(self):
		'\x0bStops the monitoring of the I/O signals collection for changes.'
		return self._oleobj_.InvokeTypes(151, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"Count": (101, 2, (3, 0), (), "Count", None),
		"IsMonitoring": (103, 2, (11, 0), (), "IsMonitoring", None),
		# Method 'Item' returns object of type 'FRCIOSignal'
		"Item": (0, 2, (13, 0), ((12, 17), (12, 17)), "Item", '{59DC170B-AF91-11D0-A072-00A02436CF7E}'),
		"NoRefresh": (104, 2, (11, 0), (), "NoRefresh", None),
		# Method 'Parent' returns object of type 'FRCIOType'
		"Parent": (102, 2, (13, 0), (), "Parent", '{59DC16F1-AF91-11D0-A072-00A02436CF7E}'),
		# Method 'Robot' returns object of type 'FRCRobot'
		"Robot": (1, 2, (13, 0), (), "Robot", '{6D7E3A01-9ECC-11D0-94D5-0020AF68F0A3}'),
	}
	_prop_map_put_ = {
		"NoRefresh": ((104, LCID, 4, 0),()),
	}
	# Default method for this class is 'Item'
	def __call__(self, LogicalNum=defaultNamedOptArg, Index=defaultNamedOptArg):
		'\x0bReturns a specific signal from the collection. '
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (13, 0), ((12, 17), (12, 17)),LogicalNum
			, Index)
		if ret is not None:
			# See if this IUnknown is really an IDispatch
			try:
				ret = ret.QueryInterface(pythoncom.IID_IDispatch)
			except pythoncom.error:
				return ret
			ret = Dispatch(ret, '__call__', '{59DC170B-AF91-11D0-A072-00A02436CF7E}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(101, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IIOSignalsEvents:
	CLSID = CLSID_Sink = IID('{39A374D1-F86E-11D0-A093-00A02436CF7E}')
	coclass_clsid = IID('{59DC16F8-AF91-11D0-A072-00A02436CF7E}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        1 : "OnCreate",
		        2 : "OnDelete",
		        3 : "OnChange",
		        4 : "OnSimulate",
		        5 : "OnUnsimulate",
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
#	def OnCreate(self, IOSignal=defaultNamedNotOptArg):
#		'\x0bOccurs after an I/O signal is created.'
#	def OnDelete(self, IOSignal=defaultNamedNotOptArg):
#		'\x0bOccurs after an I/O signal is deleted.'
#	def OnChange(self, IOSignal=defaultNamedNotOptArg):
#		'\x0bOccurs after one or more I/O signals are changed.'
#	def OnSimulate(self, IOSignal=defaultNamedNotOptArg):
#		'\x0bOccurs after one or more I/O signals are simulated.'
#	def OnUnsimulate(self, IOSignal=defaultNamedNotOptArg):
#		'\x0bOccurs after one or more I/O signals are unsimulated.'


class IIOType(DispatchBaseClass):
	'\x0bThis object is used to access both I/O signal and I/O configuration collections.'
	CLSID = IID('{59DC16EF-AF91-11D0-A072-00A02436CF7E}')
	coclass_clsid = IID('{59DC16F1-AF91-11D0-A072-00A02436CF7E}')

	_prop_map_get_ = {
		# Method 'Parent' returns object of type 'FRCIOTypes'
		"Parent": (102, 2, (13, 0), (), "Parent", '{59DC16ED-AF91-11D0-A072-00A02436CF7E}'),
		# Method 'Robot' returns object of type 'FRCRobot'
		"Robot": (1, 2, (13, 0), (), "Robot", '{6D7E3A01-9ECC-11D0-94D5-0020AF68F0A3}'),
		# Method 'Signals' returns object of type 'FRCIOSignals'
		"Signals": (202, 2, (13, 0), (), "Signals", '{59DC16F8-AF91-11D0-A072-00A02436CF7E}'),
		"Type": (101, 2, (2, 0), (), "Type", None),
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

class IIOTypes(DispatchBaseClass):
	'\x0bRepresents the collection of all the I/O types currently set up on the controller.'
	CLSID = IID('{59DC16EB-AF91-11D0-A072-00A02436CF7E}')
	coclass_clsid = IID('{59DC16ED-AF91-11D0-A072-00A02436CF7E}')

	# Result is of type FRCUserIOType
	def Add(self, Type=defaultNamedOptArg):
		'\x0bAdds a new User I/O type object to the collection.  '
		ret = self._oleobj_.InvokeTypes(151, LCID, 1, (13, 0), ((12, 17),),Type
			)
		if ret is not None:
			# See if this IUnknown is really an IDispatch
			try:
				ret = ret.QueryInterface(pythoncom.IID_IDispatch)
			except pythoncom.error:
				return ret
			ret = Dispatch(ret, 'Add', '{59DC16F6-AF91-11D0-A072-00A02436CF7E}')
		return ret

	# Result is of type FRCIOType
	# The method GetItem is actually a property, but must be used as a method to correctly pass the arguments
	def GetItem(self, Type=defaultNamedOptArg, Index=defaultNamedOptArg):
		'\x0bReturns a specific I/O type object from the collection.  '
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (13, 0), ((12, 17), (12, 17)),Type
			, Index)
		if ret is not None:
			# See if this IUnknown is really an IDispatch
			try:
				ret = ret.QueryInterface(pythoncom.IID_IDispatch)
			except pythoncom.error:
				return ret
			ret = Dispatch(ret, 'GetItem', '{59DC16F1-AF91-11D0-A072-00A02436CF7E}')
		return ret

	def Remove(self, Type=defaultNamedOptArg, Index=defaultNamedOptArg):
		'\x0bRemoves a specified User I/O type object from the collection.  '
		return self._oleobj_.InvokeTypes(152, LCID, 1, (24, 0), ((12, 17), (12, 17)),Type
			, Index)

	def Save(self, FileName=defaultNamedNotOptArg):
		'\x0bSaves all configuration data from memory to the specified file device.'
		return self._oleobj_.InvokeTypes(153, LCID, 1, (24, 0), ((8, 1),),FileName
			)

	def Unsimulate(self):
		'\x0bUnsimulates all I/O.'
		return self._oleobj_.InvokeTypes(154, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"Count": (101, 2, (2, 0), (), "Count", None),
		"DryRun": (103, 2, (11, 0), (), "DryRun", None),
		# Method 'Item' returns object of type 'FRCIOType'
		"Item": (0, 2, (13, 0), ((12, 17), (12, 17)), "Item", '{59DC16F1-AF91-11D0-A072-00A02436CF7E}'),
		# Method 'Parent' returns object of type 'FRCRobot'
		"Parent": (102, 2, (13, 0), (), "Parent", '{6D7E3A01-9ECC-11D0-94D5-0020AF68F0A3}'),
		# Method 'Robot' returns object of type 'FRCRobot'
		"Robot": (1, 2, (13, 0), (), "Robot", '{6D7E3A01-9ECC-11D0-94D5-0020AF68F0A3}'),
	}
	_prop_map_put_ = {
		"DryRun": ((103, LCID, 4, 0),()),
	}
	# Default method for this class is 'Item'
	def __call__(self, Type=defaultNamedOptArg, Index=defaultNamedOptArg):
		'\x0bReturns a specific I/O type object from the collection.  '
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (13, 0), ((12, 17), (12, 17)),Type
			, Index)
		if ret is not None:
			# See if this IUnknown is really an IDispatch
			try:
				ret = ret.QueryInterface(pythoncom.IID_IDispatch)
			except pythoncom.error:
				return ret
			ret = Dispatch(ret, '__call__', '{59DC16F1-AF91-11D0-A072-00A02436CF7E}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(101, 2, (2, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IIOTypesEvents:
	CLSID = CLSID_Sink = IID('{B23F3D71-F86A-11D0-A093-00A02436CF7E}')
	coclass_clsid = IID('{59DC16ED-AF91-11D0-A072-00A02436CF7E}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        1 : "OnCreate",
		        2 : "OnDelete",
		        3 : "OnRefresh",
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
#	def OnCreate(self, UserIOType=defaultNamedNotOptArg):
#		'\x0bOccurs after a User I/O is created.'
#	def OnDelete(self, UserIOType=defaultNamedNotOptArg):
#		'\x0bOccurs before a User I/O is deleted.'
#	def OnRefresh(self):
#		'\x0bOccurs after all the I/O types have been updated.'


class IIndGroupPosition(DispatchBaseClass):
	'\x0bProvides access to the positional data of an Independant position for a specific motion group.'
	CLSID = IID('{1F6F314A-F81F-4B6D-AEDE-5AFD558256E8}')
	coclass_clsid = IID('{DBE7F3B9-01E5-4935-A211-B5CC9D3A1048}')

	def CheckReach(self, From=defaultNamedNotOptArg, MoType=6, OrientType=2, Destination=defaultNamedNotOptArg
			, MotionErrorInfo=0):
		'\x0bReturns a Boolean indicating if the robot can reach the position or not.'
		return self._ApplyTypes_(305, 1, (11, 0), ((12, 17), (3, 49), (3, 49), (12, 17), (16397, 50)), 'CheckReach', None,From
			, MoType, OrientType, Destination, MotionErrorInfo)

	def Copy(self, Position=defaultNamedNotOptArg):
		'\x0bCopies the positional data from another object into this one.'
		return self._oleobj_.InvokeTypes(304, LCID, 1, (24, 0), ((9, 1),),Position
			)

	# The method Formats is actually a property, but must be used as a method to correctly pass the arguments
	def Formats(self, Type=defaultNamedNotOptArg):
		'\x0bReturns positional data in the specified format.'
		ret = self._oleobj_.InvokeTypes(203, LCID, 2, (9, 0), ((3, 1),),Type
			)
		if ret is not None:
			ret = Dispatch(ret, 'Formats', None)
		return ret

	# The method IsEqualTo is actually a property, but must be used as a method to correctly pass the arguments
	def IsEqualTo(self, TargetPos=defaultNamedNotOptArg):
		"Returns a boolean value that indicates if the positional data contained in the current object is 'almost equal to' the positional data of another object."
		return self._oleobj_.InvokeTypes(302, LCID, 2, (11, 0), ((9, 1),),TargetPos
			)

	# The method IsReachable is actually a property, but must be used as a method to correctly pass the arguments
	def IsReachable(self, From=defaultNamedNotOptArg, MoType=6, OrientType=2, Destination=defaultNamedNotOptArg
			, MotionErrorInfo=0):
		'\x0bReturns a Boolean indicating if the robot can reach the position or not.'
		return self._ApplyTypes_(303, 2, (11, 0), ((12, 17), (3, 49), (3, 49), (12, 17), (16397, 50)), 'IsReachable', None,From
			, MoType, OrientType, Destination, MotionErrorInfo)

	def MatInv(self, InputPos=defaultNamedNotOptArg):
		'\x0bInvert the input position transformation matrix and set the results to this position.'
		return self._oleobj_.InvokeTypes(259, LCID, 1, (24, 0), ((9, 1),),InputPos
			)

	def MatMul(self, LeftPos=defaultNamedNotOptArg, RightPos=defaultNamedNotOptArg):
		'\x0bMultiply two input positions’ transformation matrices and set the results to this position.'
		return self._oleobj_.InvokeTypes(258, LCID, 1, (24, 0), ((9, 1), (9, 1)),LeftPos
			, RightPos)

	def Moveto(self):
		'\x0bMoves the robot to this position.'
		return self._oleobj_.InvokeTypes(253, LCID, 1, (24, 0), (),)

	def Record(self):
		'\x0bRecords the current position of the robot to this position.'
		return self._oleobj_.InvokeTypes(254, LCID, 1, (24, 0), (),)

	def Refresh(self):
		'\x0bClears all changes to the position since the last update of the position.'
		return self._oleobj_.InvokeTypes(252, LCID, 1, (24, 0), (),)

	def StartMonitor(self, Latency=defaultNamedNotOptArg):
		'\x0bEnables the Change event, with specified latency.'
		return self._oleobj_.InvokeTypes(255, LCID, 1, (24, 0), ((3, 1),),Latency
			)

	def StopMonitor(self):
		'\x0bStops the Change event from occurring.'
		return self._oleobj_.InvokeTypes(256, LCID, 1, (24, 0), (),)

	def Uninitialize(self):
		'\x0bUninitializes the position. '
		return self._oleobj_.InvokeTypes(257, LCID, 1, (24, 0), (),)

	def Update(self):
		'\x0bUpdates any changes to the position back to the controller.'
		return self._oleobj_.InvokeTypes(251, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"AutomaticUpdate": (201, 2, (11, 0), (), "AutomaticUpdate", None),
		"GroupNum": (204, 2, (2, 0), (), "GroupNum", None),
		"Id": (205, 2, (3, 0), (), "Id", None),
		"IsAtCurPosition": (206, 2, (11, 0), (), "IsAtCurPosition", None),
		"IsInitialized": (207, 2, (11, 0), (), "IsInitialized", None),
		"IsMonitoring": (210, 2, (11, 0), (), "IsMonitoring", None),
		# Method 'Parent' returns object of type 'FRCIndPosition'
		"Parent": (301, 2, (13, 0), (), "Parent", '{B4819F73-FC65-4475-97D3-974ACF6EE03E}'),
		# Method 'Program' returns object of type 'FRCProgram'
		"Program": (101, 2, (13, 0), (), "Program", '{D42AB5D5-8FFB-11D0-94CC-0020AF68F0A3}'),
		# Method 'Robot' returns object of type 'FRCRobot'
		"Robot": (1, 2, (13, 0), (), "Robot", '{6D7E3A01-9ECC-11D0-94D5-0020AF68F0A3}'),
		"Type": (202, 2, (3, 0), (), "Type", None),
		"UserFrame": (208, 2, (3, 0), (), "UserFrame", None),
		"UserTool": (209, 2, (3, 0), (), "UserTool", None),
	}
	_prop_map_put_ = {
		"AutomaticUpdate": ((201, LCID, 4, 0),()),
		"Type": ((202, LCID, 4, 0),()),
		"UserFrame": ((208, LCID, 4, 0),()),
		"UserTool": ((209, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IIndGroupPositionEvents:
	CLSID = CLSID_Sink = IID('{82DDCEA2-3608-404D-90B2-E636F7E7DDD8}')
	coclass_clsid = IID('{DBE7F3B9-01E5-4935-A211-B5CC9D3A1048}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        1 : "OnChange",
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
#	def OnChange(self):
#		'\x0bOccurs after the position is changed.'


class IIndPosition(DispatchBaseClass):
	'\x0bEnables you to work with position data without requiring you to create the position on the controller or find an existing one to use.'
	CLSID = IID('{D21DF523-8D4A-4A7C-B367-5725E53A21A1}')
	coclass_clsid = IID('{B4819F73-FC65-4475-97D3-974ACF6EE03E}')

	def CheckReach(self, From=defaultNamedNotOptArg, MoType=6, OrientType=2, Destination=defaultNamedNotOptArg
			, MotionErrorInfo=0):
		'\x0bReturns a Boolean indicating if the robot can reach the position or not.'
		return self._ApplyTypes_(256, 1, (11, 0), ((12, 17), (3, 49), (3, 49), (12, 17), (16397, 50)), 'CheckReach', None,From
			, MoType, OrientType, Destination, MotionErrorInfo)

	def Copy(self, Position=defaultNamedNotOptArg):
		'\x0bCopies the positional data from another object into this one.'
		return self._oleobj_.InvokeTypes(250, LCID, 1, (24, 0), ((9, 1),),Position
			)

	# Result is of type FRCIndGroupPosition
	# The method Group is actually a property, but must be used as a method to correctly pass the arguments
	def Group(self, GroupNum=defaultNamedNotOptArg):
		'\x0bReturns a FRCIndGroupPosition object representing the position in the specified motion group.'
		ret = self._oleobj_.InvokeTypes(202, LCID, 2, (13, 0), ((2, 1),),GroupNum
			)
		if ret is not None:
			# See if this IUnknown is really an IDispatch
			try:
				ret = ret.QueryInterface(pythoncom.IID_IDispatch)
			except pythoncom.error:
				return ret
			ret = Dispatch(ret, 'Group', '{DBE7F3B9-01E5-4935-A211-B5CC9D3A1048}')
		return ret

	# The method GroupMask is actually a property, but must be used as a method to correctly pass the arguments
	def GroupMask(self, GroupNum=defaultNamedNotOptArg):
		'\x0bReturns whether the specified group is supported on the controller.'
		return self._oleobj_.InvokeTypes(203, LCID, 2, (11, 0), ((2, 1),),GroupNum
			)

	# The method IsReachable is actually a property, but must be used as a method to correctly pass the arguments
	def IsReachable(self, From=defaultNamedNotOptArg, MoType=6, OrientType=2, Destination=defaultNamedNotOptArg
			, MotionErrorInfo=0):
		'\x0bReturns a Boolean indicating if the robot can reach the position or not.'
		return self._ApplyTypes_(207, 2, (11, 0), ((12, 17), (3, 49), (3, 49), (12, 17), (16397, 50)), 'IsReachable', None,From
			, MoType, OrientType, Destination, MotionErrorInfo)

	def Moveto(self):
		'\x0bMoves the robot to this position.'
		return self._oleobj_.InvokeTypes(251, LCID, 1, (24, 0), (),)

	def Record(self):
		'\x0bRecords the current position of the robot to this position.'
		return self._oleobj_.InvokeTypes(253, LCID, 1, (24, 0), (),)

	def Uninitialize(self):
		'\x0bUninitializes the position.'
		return self._oleobj_.InvokeTypes(254, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"Comment": (201, 2, (8, 0), (), "Comment", None),
		"GroupBitMask": (255, 2, (3, 0), (), "GroupBitMask", None),
		"Id": (204, 2, (3, 0), (), "Id", None),
		"IsAtCurPosition": (205, 2, (11, 0), (), "IsAtCurPosition", None),
		"IsInitialized": (206, 2, (11, 0), (), "IsInitialized", None),
		# Method 'Robot' returns object of type 'FRCRobot'
		"Robot": (1, 2, (13, 0), (), "Robot", '{6D7E3A01-9ECC-11D0-94D5-0020AF68F0A3}'),
	}
	_prop_map_put_ = {
		"Comment": ((201, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IIndPositionEvents:
	CLSID = CLSID_Sink = IID('{0872A5E4-398C-46A3-989D-1E9B1BCA72DC}')
	coclass_clsid = IID('{B4819F73-FC65-4475-97D3-974ACF6EE03E}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        1 : "OnChange",
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
#	def OnChange(self, GroupNum=defaultNamedNotOptArg):
#		'\x0bOccurs after the position is changed.'


class IJoint(DispatchBaseClass):
	'\x0bRepresents the position data for a single group as simple joint axes. '
	CLSID = IID('{A47A5886-056D-11D0-8901-0020AF68F0A3}')
	coclass_clsid = IID('{A47A5887-056D-11D0-8901-0020AF68F0A3}')

	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, JointNum=defaultNamedNotOptArg):
		'\x0bReturns/sets the value for each axis in the position.'
		return self._oleobj_.InvokeTypes(0, LCID, 2, (5, 0), ((2, 1),),JointNum
			)

	# The method SetItem is actually a property, but must be used as a method to correctly pass the arguments
	def SetItem(self, JointNum=defaultNamedNotOptArg, arg1=defaultUnnamedArg):
		'\x0bReturns/sets the value for each axis in the position.'
		return self._oleobj_.InvokeTypes(0, LCID, 4, (24, 0), ((2, 1), (5, 1)),JointNum
			, arg1)

	_prop_map_get_ = {
		"Count": (202, 2, (2, 0), (), "Count", None),
		# Method 'Parent' returns object of type 'FRCPosition'
		"Parent": (201, 2, (13, 0), (), "Parent", '{D42AB5DB-8FFB-11D0-94CC-0020AF68F0A3}'),
		# Method 'Program' returns object of type 'FRCProgram'
		"Program": (101, 2, (13, 0), (), "Program", '{D42AB5D5-8FFB-11D0-94CC-0020AF68F0A3}'),
		# Method 'Robot' returns object of type 'FRCRobot'
		"Robot": (1, 2, (13, 0), (), "Robot", '{6D7E3A01-9ECC-11D0-94D5-0020AF68F0A3}'),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, JointNum=defaultNamedNotOptArg):
		'\x0bReturns/sets the value for each axis in the position.'
		return self._oleobj_.InvokeTypes(0, LCID, 2, (5, 0), ((2, 1),),JointNum
			)

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(202, 2, (2, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IKARELProgram(DispatchBaseClass):
	'\x0bRepresents a KAREL program on the robot controller.  '
	CLSID = IID('{73FF06C4-7178-11D1-B762-00C04FBBE42A}')
	coclass_clsid = IID('{DA462B71-DD0D-11D0-A083-00A02436CF7E}')

	# The method DefaultGroup is actually a property, but must be used as a method to correctly pass the arguments
	def DefaultGroup(self, GroupNumber=defaultNamedNotOptArg):
		'\x0bReturns/sets the group numbers for the program.  True if the motion group is used.'
		return self._oleobj_.InvokeTypes(116, LCID, 2, (11, 0), ((2, 1),),GroupNumber
			)

	# The method IgnoreAbort is actually a property, but must be used as a method to correctly pass the arguments
	def IgnoreAbort(self, IgnoreConstant=defaultNamedNotOptArg):
		'\x0bReturns/sets the state of the IgnoreAbort attribute.'
		return self._oleobj_.InvokeTypes(117, LCID, 2, (11, 0), ((3, 1),),IgnoreConstant
			)

	# The method IgnorePause is actually a property, but must be used as a method to correctly pass the arguments
	def IgnorePause(self, IgnoreConstant=defaultNamedNotOptArg):
		'\x0bReturns/sets the state of the IgnorePause attribute. '
		return self._oleobj_.InvokeTypes(118, LCID, 2, (11, 0), ((3, 1),),IgnoreConstant
			)

	def ReOpen(self, AccessMode=defaultNamedNotOptArg, RejectMode=defaultNamedNotOptArg):
		'\x0bReopens the program with different access or reject mode attributes.'
		return self._oleobj_.InvokeTypes(150, LCID, 1, (24, 0), ((3, 1), (3, 1)),AccessMode
			, RejectMode)

	def Run(self, StepType=defaultNamedOptArg, LineNum=defaultNamedOptArg, Direction=defaultNamedOptArg):
		'\x0bRuns the KAREL program by creating a task for the program.'
		return self._oleobj_.InvokeTypes(250, LCID, 1, (24, 0), ((12, 17), (12, 17), (12, 17)),StepType
			, LineNum, Direction)

	def Save(self, FileName=defaultNamedNotOptArg, Option=defaultNamedOptArg, SaveClass=defaultNamedOptArg):
		'\x0bSaves the TP program and/or the variables associated with the program from memory to the specified file device.  KAREL program executable statements can not be saved using this mechanism.'
		return self._oleobj_.InvokeTypes(151, LCID, 1, (24, 0), ((8, 1), (12, 17), (12, 17)),FileName
			, Option, SaveClass)

	# The method SetDefaultGroup is actually a property, but must be used as a method to correctly pass the arguments
	def SetDefaultGroup(self, GroupNumber=defaultNamedNotOptArg, arg1=defaultUnnamedArg):
		'\x0bReturns/sets the group numbers for the program.  True if the motion group is used.'
		return self._oleobj_.InvokeTypes(116, LCID, 4, (24, 0), ((2, 1), (11, 1)),GroupNumber
			, arg1)

	# The method SetIgnoreAbort is actually a property, but must be used as a method to correctly pass the arguments
	def SetIgnoreAbort(self, IgnoreConstant=defaultNamedNotOptArg, arg1=defaultUnnamedArg):
		'\x0bReturns/sets the state of the IgnoreAbort attribute.'
		return self._oleobj_.InvokeTypes(117, LCID, 4, (24, 0), ((3, 1), (11, 1)),IgnoreConstant
			, arg1)

	# The method SetIgnorePause is actually a property, but must be used as a method to correctly pass the arguments
	def SetIgnorePause(self, IgnoreConstant=defaultNamedNotOptArg, arg1=defaultUnnamedArg):
		'\x0bReturns/sets the state of the IgnorePause attribute. '
		return self._oleobj_.InvokeTypes(118, LCID, 4, (24, 0), ((3, 1), (11, 1)),IgnoreConstant
			, arg1)

	_prop_map_get_ = {
		"AccessMode": (102, 2, (3, 0), (), "AccessMode", None),
		"BusyLampOff": (115, 2, (11, 0), (), "BusyLampOff", None),
		"Comment": (105, 2, (8, 0), (), "Comment", None),
		"Created": (106, 2, (12, 0), (), "Created", None),
		"Invisible": (119, 2, (11, 0), (), "Invisible", None),
		"LastModified": (107, 2, (12, 0), (), "LastModified", None),
		"Name": (0, 2, (8, 0), (), "Name", None),
		"OriginalName": (108, 2, (8, 0), (), "OriginalName", None),
		"Owner": (120, 2, (8, 0), (), "Owner", None),
		# Method 'Parent' returns object of type 'FRCPrograms'
		"Parent": (104, 2, (13, 0), (), "Parent", '{1FBD567D-8F13-11D0-94CB-0020AF68F0A3}'),
		"Priority": (113, 2, (3, 0), (), "Priority", None),
		"Protection": (111, 2, (3, 0), (), "Protection", None),
		"RejectMode": (103, 2, (3, 0), (), "RejectMode", None),
		# Method 'Robot' returns object of type 'FRCRobot'
		"Robot": (1, 2, (13, 0), (), "Robot", '{6D7E3A01-9ECC-11D0-94D5-0020AF68F0A3}'),
		"Size": (110, 2, (3, 0), (), "Size", None),
		"StackSize": (112, 2, (3, 0), (), "StackSize", None),
		"SubType": (203, 2, (3, 0), (), "SubType", None),
		"TimeSlice": (114, 2, (3, 0), (), "TimeSlice", None),
		# Method 'Variables' returns object of type 'FRCVars'
		"Variables": (101, 2, (13, 0), (), "Variables", '{88B57BCB-D0CA-11CF-959F-00A024329125}'),
		"Version": (109, 2, (2, 0), (), "Version", None),
	}
	_prop_map_put_ = {
		"BusyLampOff": ((115, LCID, 4, 0),()),
		"Comment": ((105, LCID, 4, 0),()),
		"Invisible": ((119, LCID, 4, 0),()),
		"Owner": ((120, LCID, 4, 0),()),
		"Priority": ((113, LCID, 4, 0),()),
		"Protection": ((111, LCID, 4, 0),()),
		"StackSize": ((112, LCID, 4, 0),()),
		"TimeSlice": ((114, LCID, 4, 0),()),
	}
	# Default property for this class is 'Name'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (8, 0), (), "Name", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IKARELProgramEvents:
	CLSID = CLSID_Sink = IID('{44E3D090-7178-11D1-B762-00C04FBBE42A}')
	coclass_clsid = IID('{DA462B71-DD0D-11D0-A083-00A02436CF7E}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        1 : "OnDelete",
		        2 : "OnAttrChange",
		        3 : "OnRefresh",
		        4 : "OnRefreshVars",
		        5 : "OnSubTypeChange",
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
#	def OnDelete(self):
#		'\x0bOccurs after a program is deleted.'
#	def OnAttrChange(self, Attr=defaultNamedNotOptArg):
#		'\x0bOccurs after an attribute is changed.'
#	def OnRefresh(self):
#		'\x0bOccurs after a KAREL program is reloaded.'
#	def OnRefreshVars(self):
#		'\x0bOccurs after a program’s variables are reloaded.'
#	def OnSubTypeChange(self):
#		'\x0bOccurs after a KAREL program’s subtype is changed.'


class IMotionErrorInfo(DispatchBaseClass):
	'\x0bProvides access to the status of a motion operation.'
	CLSID = IID('{50F24196-4CB8-4375-96C3-A05885F4189D}')
	coclass_clsid = IID('{EE912848-BB81-427A-951F-5D9DC0FE74A7}')

	_prop_map_get_ = {
		"GroupNum": (101, 2, (3, 0), (), "GroupNum", None),
		"JointBitMask": (102, 2, (3, 0), (), "JointBitMask", None),
		"MoTaskId": (103, 2, (3, 0), (), "MoTaskId", None),
		"MoTaskParam": (104, 2, (3, 0), (), "MoTaskParam", None),
		"RlibId": (105, 2, (3, 0), (), "RlibId", None),
		"RlibParam": (106, 2, (3, 0), (), "RlibParam", None),
		# Method 'Robot' returns object of type 'FRCRobot'
		"Robot": (1, 2, (13, 0), (), "Robot", '{6D7E3A01-9ECC-11D0-94D5-0020AF68F0A3}'),
		# Method 'RobotErrorInfo' returns object of type 'FRCRobotErrorInfo'
		"RobotErrorInfo": (107, 2, (13, 0), (), "RobotErrorInfo", '{5BBFA760-09C6-11D2-871C-00C04F98D092}'),
		"UpperLimMask": (108, 2, (3, 0), (), "UpperLimMask", None),
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

class IPacket(DispatchBaseClass):
	'\x0bProvides access to the information received in a ROS packet.'
	CLSID = IID('{7B125AAE-9330-11D1-B751-00C04FB99C75}')
	coclass_clsid = IID('{64AF4546-9331-11D1-B751-00C04FB99C75}')

	def DecodeBody(self, Item=defaultNamedNotOptArg):
		'\x0bExtracts data from the Body of the packet if the data was inserted using the companion KAREL Add_xxxPC built-ins.  '
		return self._ApplyTypes_(151, 1, (12, 0), ((3, 1),), 'DecodeBody', None,Item
			)

	_prop_map_get_ = {
		"Body": (101, 2, (8209, 0), (), "Body", None),
		"ItrDepth": (102, 2, (17, 0), (), "ItrDepth", None),
		"PacketID": (103, 2, (3, 0), (), "PacketID", None),
		"PacketType": (104, 2, (17, 0), (), "PacketType", None),
		"RequestCode": (105, 2, (17, 0), (), "RequestCode", None),
		"RequestorID": (106, 2, (3, 0), (), "RequestorID", None),
		# Method 'Robot' returns object of type 'FRCRobot'
		"Robot": (1, 2, (13, 0), (), "Robot", '{6D7E3A01-9ECC-11D0-94D5-0020AF68F0A3}'),
		"Status": (107, 2, (3, 0), (), "Status", None),
		"SubSystemCode": (108, 2, (17, 0), (), "SubSystemCode", None),
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

class IPacketEvent(DispatchBaseClass):
	'\x0bRaises an event when the desired ROS Packet is received from the controller. '
	CLSID = IID('{FCCE9E60-9420-11D1-B751-00C04FB99C75}')
	coclass_clsid = IID('{FCCE9E5F-9420-11D1-B751-00C04FB99C75}')

	_prop_map_get_ = {
		"PacketID": (101, 2, (3, 0), (), "PacketID", None),
		"RequestCode": (102, 2, (17, 0), (), "RequestCode", None),
		# Method 'Robot' returns object of type 'FRCRobot'
		"Robot": (1, 2, (13, 0), (), "Robot", '{6D7E3A01-9ECC-11D0-94D5-0020AF68F0A3}'),
		"SubSystemCode": (103, 2, (17, 0), (), "SubSystemCode", None),
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

class IPacketEventEvents:
	CLSID = CLSID_Sink = IID('{298DEBD5-9976-11D1-B753-00C04FB99C75}')
	coclass_clsid = IID('{FCCE9E5F-9420-11D1-B751-00C04FB99C75}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        1 : "OnReceive",
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
#	def OnReceive(self, Packet=defaultNamedNotOptArg):
#		'\x0bOccurs when a ROS is received that matches the trigger criteria specified by the RequestCode and SybSystemCode properties..'


class IPipe(DispatchBaseClass):
	'Provides access to a pipe defined on the controller.'
	CLSID = IID('{B475BC94-3AF1-11D4-9F66-00105AE428C3}')
	coclass_clsid = IID('{B475BC95-3AF1-11D4-9F66-00105AE428C3}')

	def Flush(self):
		'Tells the controller to flush the pipe.'
		return self._oleobj_.InvokeTypes(201, LCID, 1, (24, 0), (),)

	def StartMonitor(self, FlushTime=defaultNamedNotOptArg):
		'Starts monitoring data put into the pipe.'
		return self._oleobj_.InvokeTypes(206, LCID, 1, (24, 0), ((3, 1),),FlushTime
			)

	def StopMonitor(self):
		'Stops monitoring data put into the pipe.'
		return self._oleobj_.InvokeTypes(207, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"Id": (202, 2, (3, 0), (), "Id", None),
		"IsMonitoring": (203, 2, (11, 0), (), "IsMonitoring", None),
		"IsOverflowed": (204, 2, (11, 0), (), "IsOverflowed", None),
		# Method 'Parent' returns object of type 'FRCPipes'
		"Parent": (205, 2, (13, 0), (), "Parent", '{B475BC91-3AF1-11D4-9F66-00105AE428C3}'),
		# Method 'Robot' returns object of type 'FRCRobot'
		"Robot": (1, 2, (13, 0), (), "Robot", '{6D7E3A01-9ECC-11D0-94D5-0020AF68F0A3}'),
		"TypeName": (208, 2, (8, 0), (), "TypeName", None),
		"TypeProgName": (209, 2, (8, 0), (), "TypeProgName", None),
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

class IPipeEvents:
	CLSID = CLSID_Sink = IID('{B475BC93-3AF1-11D4-9F66-00105AE428C3}')
	coclass_clsid = IID('{B475BC95-3AF1-11D4-9F66-00105AE428C3}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        1 : "OnReceive",
		        2 : "OnUnregister",
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
#	def OnReceive(self, State=defaultNamedNotOptArg, Data=defaultNamedNotOptArg):
#		'Occurs when new information is received from the pipe.'
#	def OnUnregister(self):
#		'Occurs when this pipe is unregistered on the controller.'


class IPipeField(DispatchBaseClass):
	'Provides access to data values received from a pipe.'
	CLSID = IID('{B475BC98-3AF1-11D4-9F66-00105AE428C3}')
	coclass_clsid = IID('{B475BC99-3AF1-11D4-9F66-00105AE428C3}')

	_prop_map_get_ = {
		"FieldName": (201, 2, (8, 0), (), "FieldName", None),
		"FullName": (202, 2, (8, 0), (), "FullName", None),
		"IsInitialized": (203, 2, (11, 0), (), "IsInitialized", None),
		"Parent": (204, 2, (9, 0), (), "Parent", None),
		# Method 'Pipe' returns object of type 'FRCPipe'
		"Pipe": (205, 2, (13, 0), (), "Pipe", '{B475BC95-3AF1-11D4-9F66-00105AE428C3}'),
		# Method 'Robot' returns object of type 'FRCRobot'
		"Robot": (1, 2, (13, 0), (), "Robot", '{6D7E3A01-9ECC-11D0-94D5-0020AF68F0A3}'),
		"TypeCode": (206, 2, (3, 0), (), "TypeCode", None),
		"TypeName": (207, 2, (8, 0), (), "TypeName", None),
		"Value": (0, 2, (12, 0), (), "Value", None),
	}
	_prop_map_put_ = {
	}
	# Default property for this class is 'Value'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (12, 0), (), "Value", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IPipeFields(DispatchBaseClass):
	'Provides access to data blocks from a pipe as a set of named fields.'
	CLSID = IID('{B475BC96-3AF1-11D4-9F66-00105AE428C3}')
	coclass_clsid = IID('{B475BC97-3AF1-11D4-9F66-00105AE428C3}')

	# The method GetItem is actually a property, but must be used as a method to correctly pass the arguments
	def GetItem(self, Name=defaultNamedOptArg, Index=defaultNamedOptArg):
		'Returns a field object from the collection.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 17), (12, 17)),Name
			, Index)
		if ret is not None:
			ret = Dispatch(ret, 'GetItem', None)
		return ret

	_prop_map_get_ = {
		"Count": (201, 2, (3, 0), (), "Count", None),
		"FieldName": (202, 2, (8, 0), (), "FieldName", None),
		"FullName": (203, 2, (8, 0), (), "FullName", None),
		"Item": (0, 2, (9, 0), ((12, 17), (12, 17)), "Item", None),
		"Parent": (204, 2, (9, 0), (), "Parent", None),
		# Method 'Pipe' returns object of type 'FRCPipe'
		"Pipe": (205, 2, (13, 0), (), "Pipe", '{B475BC95-3AF1-11D4-9F66-00105AE428C3}'),
		# Method 'Robot' returns object of type 'FRCRobot'
		"Robot": (1, 2, (13, 0), (), "Robot", '{6D7E3A01-9ECC-11D0-94D5-0020AF68F0A3}'),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Name=defaultNamedOptArg, Index=defaultNamedOptArg):
		'Returns a field object from the collection.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 17), (12, 17)),Name
			, Index)
		if ret is not None:
			ret = Dispatch(ret, '__call__', None)
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(201, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IPipePosition(DispatchBaseClass):
	CLSID = IID('{B475BC9A-3AF1-11D4-9F66-00105AE428C3}')
	coclass_clsid = IID('{B475BC9B-3AF1-11D4-9F66-00105AE428C3}')

	# The method Formats is actually a property, but must be used as a method to correctly pass the arguments
	def Formats(self, Type=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(201, LCID, 2, (9, 0), ((3, 1),),Type
			)
		if ret is not None:
			ret = Dispatch(ret, 'Formats', None)
		return ret

	# The method IsEqualTo is actually a property, but must be used as a method to correctly pass the arguments
	def IsEqualTo(self, TargetPos=defaultNamedNotOptArg):
		"Returns a boolean value that indicates if the positional data contained in the current object is 'almost equal to' the positional data of another object."
		return self._oleobj_.InvokeTypes(204, LCID, 2, (11, 0), ((9, 1),),TargetPos
			)

	_prop_map_get_ = {
		"GroupNum": (202, 2, (2, 0), (), "GroupNum", None),
		"IsAtCurPosition": (203, 2, (11, 0), (), "IsAtCurPosition", None),
		"IsInitialized": (205, 2, (11, 0), (), "IsInitialized", None),
		# Method 'Parent' returns object of type 'FRCPipeField'
		"Parent": (206, 2, (13, 0), (), "Parent", '{B475BC99-3AF1-11D4-9F66-00105AE428C3}'),
		# Method 'Pipe' returns object of type 'FRCPipe'
		"Pipe": (207, 2, (13, 0), (), "Pipe", '{B475BC95-3AF1-11D4-9F66-00105AE428C3}'),
		# Method 'Robot' returns object of type 'FRCRobot'
		"Robot": (1, 2, (13, 0), (), "Robot", '{6D7E3A01-9ECC-11D0-94D5-0020AF68F0A3}'),
		"Type": (208, 2, (3, 0), (), "Type", None),
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

class IPipes(DispatchBaseClass):
	'Provides access to pipes defined on the controller.'
	CLSID = IID('{B475BC90-3AF1-11D4-9F66-00105AE428C3}')
	coclass_clsid = IID('{B475BC91-3AF1-11D4-9F66-00105AE428C3}')

	# Result is of type FRCPipe
	# The method GetItem is actually a property, but must be used as a method to correctly pass the arguments
	def GetItem(self, Id=defaultNamedOptArg, Index=defaultNamedOptArg):
		'Returns a pipe object from the collection.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (13, 0), ((12, 17), (12, 17)),Id
			, Index)
		if ret is not None:
			# See if this IUnknown is really an IDispatch
			try:
				ret = ret.QueryInterface(pythoncom.IID_IDispatch)
			except pythoncom.error:
				return ret
			ret = Dispatch(ret, 'GetItem', '{B475BC95-3AF1-11D4-9F66-00105AE428C3}')
		return ret

	_prop_map_get_ = {
		"Count": (201, 2, (3, 0), (), "Count", None),
		# Method 'Item' returns object of type 'FRCPipe'
		"Item": (0, 2, (13, 0), ((12, 17), (12, 17)), "Item", '{B475BC95-3AF1-11D4-9F66-00105AE428C3}'),
		# Method 'Robot' returns object of type 'FRCRobot'
		"Robot": (1, 2, (13, 0), (), "Robot", '{6D7E3A01-9ECC-11D0-94D5-0020AF68F0A3}'),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Id=defaultNamedOptArg, Index=defaultNamedOptArg):
		'Returns a pipe object from the collection.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (13, 0), ((12, 17), (12, 17)),Id
			, Index)
		if ret is not None:
			# See if this IUnknown is really an IDispatch
			try:
				ret = ret.QueryInterface(pythoncom.IID_IDispatch)
			except pythoncom.error:
				return ret
			ret = Dispatch(ret, '__call__', '{B475BC95-3AF1-11D4-9F66-00105AE428C3}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(201, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IPipesEvents:
	CLSID = CLSID_Sink = IID('{B475BC92-3AF1-11D4-9F66-00105AE428C3}')
	coclass_clsid = IID('{B475BC91-3AF1-11D4-9F66-00105AE428C3}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        1 : "OnRegister",
		        2 : "OnUnregister",
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
#	def OnRegister(self, Pipe=defaultNamedNotOptArg):
#		'Occurs when a new pipe is registered on the controller.'
#	def OnUnregister(self, Pipe=defaultNamedNotOptArg):
#		'Occurs when a  pipe is unregistered on the controller.'


class IPosition(DispatchBaseClass):
	'\x0bProvides access to the positional data.'
	CLSID = IID('{D42AB5DA-8FFB-11D0-94CC-0020AF68F0A3}')
	coclass_clsid = None

	# The method Formats is actually a property, but must be used as a method to correctly pass the arguments
	def Formats(self, Type=defaultNamedNotOptArg):
		'\x0bReturns positional data in the specified format.'
		ret = self._oleobj_.InvokeTypes(203, LCID, 2, (9, 0), ((3, 1),),Type
			)
		if ret is not None:
			ret = Dispatch(ret, 'Formats', None)
		return ret

	def MatInv(self, InputPos=defaultNamedNotOptArg):
		'\x0bInvert the input position transformation matrix and set the results to this position.'
		return self._oleobj_.InvokeTypes(259, LCID, 1, (24, 0), ((9, 1),),InputPos
			)

	def MatMul(self, LeftPos=defaultNamedNotOptArg, RightPos=defaultNamedNotOptArg):
		'\x0bMultiply two input positions’ transformation matrices and set the results to this position.'
		return self._oleobj_.InvokeTypes(258, LCID, 1, (24, 0), ((9, 1), (9, 1)),LeftPos
			, RightPos)

	def Moveto(self):
		'\x0bMoves the robot to this position.'
		return self._oleobj_.InvokeTypes(253, LCID, 1, (24, 0), (),)

	def Record(self):
		'\x0bRecords the current position of the robot to this position.'
		return self._oleobj_.InvokeTypes(254, LCID, 1, (24, 0), (),)

	def Refresh(self):
		'\x0bClears all changes to the position since the last update of the position.'
		return self._oleobj_.InvokeTypes(252, LCID, 1, (24, 0), (),)

	def StartMonitor(self, Latency=defaultNamedNotOptArg):
		'\x0bEnables the Change event, with specified latency.'
		return self._oleobj_.InvokeTypes(255, LCID, 1, (24, 0), ((3, 1),),Latency
			)

	def StopMonitor(self):
		'\x0bStops the Change event from occurring.'
		return self._oleobj_.InvokeTypes(256, LCID, 1, (24, 0), (),)

	def Uninitialize(self):
		'\x0bUninitializes the position. '
		return self._oleobj_.InvokeTypes(257, LCID, 1, (24, 0), (),)

	def Update(self):
		'\x0bUpdates any changes to the position back to the controller.'
		return self._oleobj_.InvokeTypes(251, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"AutomaticUpdate": (201, 2, (11, 0), (), "AutomaticUpdate", None),
		"GroupNum": (204, 2, (2, 0), (), "GroupNum", None),
		"Id": (205, 2, (3, 0), (), "Id", None),
		"IsAtCurPosition": (206, 2, (11, 0), (), "IsAtCurPosition", None),
		"IsInitialized": (207, 2, (11, 0), (), "IsInitialized", None),
		"IsMonitoring": (210, 2, (11, 0), (), "IsMonitoring", None),
		# Method 'Program' returns object of type 'FRCProgram'
		"Program": (101, 2, (13, 0), (), "Program", '{D42AB5D5-8FFB-11D0-94CC-0020AF68F0A3}'),
		# Method 'Robot' returns object of type 'FRCRobot'
		"Robot": (1, 2, (13, 0), (), "Robot", '{6D7E3A01-9ECC-11D0-94D5-0020AF68F0A3}'),
		"Type": (202, 2, (3, 0), (), "Type", None),
		"UserFrame": (208, 2, (3, 0), (), "UserFrame", None),
		"UserTool": (209, 2, (3, 0), (), "UserTool", None),
	}
	_prop_map_put_ = {
		"AutomaticUpdate": ((201, LCID, 4, 0),()),
		"Type": ((202, LCID, 4, 0),()),
		"UserFrame": ((208, LCID, 4, 0),()),
		"UserTool": ((209, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IPosition2(DispatchBaseClass):
	'\x0bProvides access to the positional data.'
	CLSID = IID('{E494B8E1-A59A-11D2-8724-00C04F918427}')
	coclass_clsid = IID('{D42AB5DB-8FFB-11D0-94CC-0020AF68F0A3}')

	def CheckReach(self, From=defaultNamedNotOptArg, MoType=6, OrientType=2, Destination=defaultNamedNotOptArg
			, MotionErrorInfo=0):
		'\x0bReturns a Boolean indicating if the robot can reach the position or not.'
		return self._ApplyTypes_(263, 1, (11, 0), ((12, 17), (3, 49), (3, 49), (12, 17), (16397, 50)), 'CheckReach', None,From
			, MoType, OrientType, Destination, MotionErrorInfo)

	def Copy(self, Position=defaultNamedNotOptArg):
		'\x0bCopies the positional data from another object into this one.'
		return self._oleobj_.InvokeTypes(262, LCID, 1, (24, 0), ((9, 1),),Position
			)

	# The method Formats is actually a property, but must be used as a method to correctly pass the arguments
	def Formats(self, Type=defaultNamedNotOptArg):
		'\x0bReturns positional data in the specified format.'
		ret = self._oleobj_.InvokeTypes(203, LCID, 2, (9, 0), ((3, 1),),Type
			)
		if ret is not None:
			ret = Dispatch(ret, 'Formats', None)
		return ret

	# The method IsEqualTo is actually a property, but must be used as a method to correctly pass the arguments
	def IsEqualTo(self, TargetPos=defaultNamedNotOptArg):
		"Returns a boolean value that indicates if the positional data contained in the current object is 'almost equal to' the positional data of another object."
		return self._oleobj_.InvokeTypes(260, LCID, 2, (11, 0), ((9, 1),),TargetPos
			)

	# The method IsReachable is actually a property, but must be used as a method to correctly pass the arguments
	def IsReachable(self, From=defaultNamedNotOptArg, MoType=6, OrientType=2, Destination=defaultNamedNotOptArg
			, MotionErrorInfo=0):
		'\x0bReturns a Boolean indicating if the robot can reach the position or not.'
		return self._ApplyTypes_(261, 2, (11, 0), ((12, 17), (3, 49), (3, 49), (12, 17), (16397, 50)), 'IsReachable', None,From
			, MoType, OrientType, Destination, MotionErrorInfo)

	def MatInv(self, InputPos=defaultNamedNotOptArg):
		'\x0bInvert the input position transformation matrix and set the results to this position.'
		return self._oleobj_.InvokeTypes(259, LCID, 1, (24, 0), ((9, 1),),InputPos
			)

	def MatMul(self, LeftPos=defaultNamedNotOptArg, RightPos=defaultNamedNotOptArg):
		'\x0bMultiply two input positions’ transformation matrices and set the results to this position.'
		return self._oleobj_.InvokeTypes(258, LCID, 1, (24, 0), ((9, 1), (9, 1)),LeftPos
			, RightPos)

	def Moveto(self):
		'\x0bMoves the robot to this position.'
		return self._oleobj_.InvokeTypes(253, LCID, 1, (24, 0), (),)

	def Record(self):
		'\x0bRecords the current position of the robot to this position.'
		return self._oleobj_.InvokeTypes(254, LCID, 1, (24, 0), (),)

	def Refresh(self):
		'\x0bClears all changes to the position since the last update of the position.'
		return self._oleobj_.InvokeTypes(252, LCID, 1, (24, 0), (),)

	def StartMonitor(self, Latency=defaultNamedNotOptArg):
		'\x0bEnables the Change event, with specified latency.'
		return self._oleobj_.InvokeTypes(255, LCID, 1, (24, 0), ((3, 1),),Latency
			)

	def StopMonitor(self):
		'\x0bStops the Change event from occurring.'
		return self._oleobj_.InvokeTypes(256, LCID, 1, (24, 0), (),)

	def Uninitialize(self):
		'\x0bUninitializes the position. '
		return self._oleobj_.InvokeTypes(257, LCID, 1, (24, 0), (),)

	def Update(self):
		'\x0bUpdates any changes to the position back to the controller.'
		return self._oleobj_.InvokeTypes(251, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"AutomaticUpdate": (201, 2, (11, 0), (), "AutomaticUpdate", None),
		"GroupNum": (204, 2, (2, 0), (), "GroupNum", None),
		"Id": (205, 2, (3, 0), (), "Id", None),
		"IsAtCurPosition": (206, 2, (11, 0), (), "IsAtCurPosition", None),
		"IsInitialized": (207, 2, (11, 0), (), "IsInitialized", None),
		"IsMonitoring": (210, 2, (11, 0), (), "IsMonitoring", None),
		# Method 'Program' returns object of type 'FRCProgram'
		"Program": (101, 2, (13, 0), (), "Program", '{D42AB5D5-8FFB-11D0-94CC-0020AF68F0A3}'),
		# Method 'Robot' returns object of type 'FRCRobot'
		"Robot": (1, 2, (13, 0), (), "Robot", '{6D7E3A01-9ECC-11D0-94D5-0020AF68F0A3}'),
		"Type": (202, 2, (3, 0), (), "Type", None),
		"UserFrame": (208, 2, (3, 0), (), "UserFrame", None),
		"UserTool": (209, 2, (3, 0), (), "UserTool", None),
	}
	_prop_map_put_ = {
		"AutomaticUpdate": ((201, LCID, 4, 0),()),
		"Type": ((202, LCID, 4, 0),()),
		"UserFrame": ((208, LCID, 4, 0),()),
		"UserTool": ((209, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IPositionEvents:
	CLSID = CLSID_Sink = IID('{D6219FE0-87A0-11D1-B765-00C04FBBE42A}')
	coclass_clsid = IID('{E3FFB439-2613-11D1-B702-00C04FB9C401}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        1 : "OnChange",
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
#	def OnChange(self):
#		'\x0bOccurs after the position is changed.'


class IProgram(DispatchBaseClass):
	'\x0bRepresents a program on the robot controller. '
	CLSID = IID('{8C8ACC99-4F57-11D0-BC32-444553540000}')
	coclass_clsid = IID('{8C8ACC9A-4F57-11D0-BC32-444553540000}')

	# The method DefaultGroup is actually a property, but must be used as a method to correctly pass the arguments
	def DefaultGroup(self, GroupNumber=defaultNamedNotOptArg):
		'\x0bReturns/sets the group numbers for the program.  True if the motion group is used.'
		return self._oleobj_.InvokeTypes(116, LCID, 2, (11, 0), ((2, 1),),GroupNumber
			)

	# The method IgnoreAbort is actually a property, but must be used as a method to correctly pass the arguments
	def IgnoreAbort(self, IgnoreConstant=defaultNamedNotOptArg):
		'\x0bReturns/sets the state of the IgnoreAbort attribute.'
		return self._oleobj_.InvokeTypes(117, LCID, 2, (11, 0), ((3, 1),),IgnoreConstant
			)

	# The method IgnorePause is actually a property, but must be used as a method to correctly pass the arguments
	def IgnorePause(self, IgnoreConstant=defaultNamedNotOptArg):
		'\x0bReturns/sets the state of the IgnorePause attribute. '
		return self._oleobj_.InvokeTypes(118, LCID, 2, (11, 0), ((3, 1),),IgnoreConstant
			)

	def ReOpen(self, AccessMode=defaultNamedNotOptArg, RejectMode=defaultNamedNotOptArg):
		'\x0bReopens the program with different access or reject mode attributes.'
		return self._oleobj_.InvokeTypes(150, LCID, 1, (24, 0), ((3, 1), (3, 1)),AccessMode
			, RejectMode)

	def Save(self, FileName=defaultNamedNotOptArg, Option=defaultNamedOptArg, SaveClass=defaultNamedOptArg):
		'\x0bSaves the TP program and/or the variables associated with the program from memory to the specified file device.  KAREL program executable statements can not be saved using this mechanism.'
		return self._oleobj_.InvokeTypes(151, LCID, 1, (24, 0), ((8, 1), (12, 17), (12, 17)),FileName
			, Option, SaveClass)

	# The method SetDefaultGroup is actually a property, but must be used as a method to correctly pass the arguments
	def SetDefaultGroup(self, GroupNumber=defaultNamedNotOptArg, arg1=defaultUnnamedArg):
		'\x0bReturns/sets the group numbers for the program.  True if the motion group is used.'
		return self._oleobj_.InvokeTypes(116, LCID, 4, (24, 0), ((2, 1), (11, 1)),GroupNumber
			, arg1)

	# The method SetIgnoreAbort is actually a property, but must be used as a method to correctly pass the arguments
	def SetIgnoreAbort(self, IgnoreConstant=defaultNamedNotOptArg, arg1=defaultUnnamedArg):
		'\x0bReturns/sets the state of the IgnoreAbort attribute.'
		return self._oleobj_.InvokeTypes(117, LCID, 4, (24, 0), ((3, 1), (11, 1)),IgnoreConstant
			, arg1)

	# The method SetIgnorePause is actually a property, but must be used as a method to correctly pass the arguments
	def SetIgnorePause(self, IgnoreConstant=defaultNamedNotOptArg, arg1=defaultUnnamedArg):
		'\x0bReturns/sets the state of the IgnorePause attribute. '
		return self._oleobj_.InvokeTypes(118, LCID, 4, (24, 0), ((3, 1), (11, 1)),IgnoreConstant
			, arg1)

	_prop_map_get_ = {
		"AccessMode": (102, 2, (3, 0), (), "AccessMode", None),
		"BusyLampOff": (115, 2, (11, 0), (), "BusyLampOff", None),
		"Comment": (105, 2, (8, 0), (), "Comment", None),
		"Created": (106, 2, (12, 0), (), "Created", None),
		"Invisible": (119, 2, (11, 0), (), "Invisible", None),
		"LastModified": (107, 2, (12, 0), (), "LastModified", None),
		"Name": (0, 2, (8, 0), (), "Name", None),
		"OriginalName": (108, 2, (8, 0), (), "OriginalName", None),
		"Owner": (120, 2, (8, 0), (), "Owner", None),
		# Method 'Parent' returns object of type 'FRCPrograms'
		"Parent": (104, 2, (13, 0), (), "Parent", '{1FBD567D-8F13-11D0-94CB-0020AF68F0A3}'),
		"Priority": (113, 2, (3, 0), (), "Priority", None),
		"Protection": (111, 2, (3, 0), (), "Protection", None),
		"RejectMode": (103, 2, (3, 0), (), "RejectMode", None),
		# Method 'Robot' returns object of type 'FRCRobot'
		"Robot": (1, 2, (13, 0), (), "Robot", '{6D7E3A01-9ECC-11D0-94D5-0020AF68F0A3}'),
		"Size": (110, 2, (3, 0), (), "Size", None),
		"StackSize": (112, 2, (3, 0), (), "StackSize", None),
		"TimeSlice": (114, 2, (3, 0), (), "TimeSlice", None),
		# Method 'Variables' returns object of type 'FRCVars'
		"Variables": (101, 2, (13, 0), (), "Variables", '{88B57BCB-D0CA-11CF-959F-00A024329125}'),
		"Version": (109, 2, (2, 0), (), "Version", None),
	}
	_prop_map_put_ = {
		"BusyLampOff": ((115, LCID, 4, 0),()),
		"Comment": ((105, LCID, 4, 0),()),
		"Invisible": ((119, LCID, 4, 0),()),
		"Owner": ((120, LCID, 4, 0),()),
		"Priority": ((113, LCID, 4, 0),()),
		"Protection": ((111, LCID, 4, 0),()),
		"StackSize": ((112, LCID, 4, 0),()),
		"TimeSlice": ((114, LCID, 4, 0),()),
	}
	# Default property for this class is 'Name'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (8, 0), (), "Name", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IProgramEvents:
	CLSID = CLSID_Sink = IID('{18254511-DC4C-11D0-A083-00A02436CF7E}')
	coclass_clsid = IID('{8C8ACC9A-4F57-11D0-BC32-444553540000}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        1 : "OnDelete",
		        2 : "OnAttrChange",
		        3 : "OnRefresh",
		        4 : "OnRefreshVars",
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
#	def OnDelete(self):
#		'\x0bOccurs after a program is deleted.'
#	def OnAttrChange(self, Attr=defaultNamedNotOptArg):
#		'\x0bOccurs after an attribute is changed.'
#	def OnRefresh(self):
#		'\x0bOccurs after a TP program is reloaded.'
#	def OnRefreshVars(self):
#		'\x0bOccurs after a program’s variables are reloaded.'


class IProgramObject(DispatchBaseClass):
	CLSID = IID('{D42AB5D9-8FFB-11D0-94CC-0020AF68F0A3}')
	coclass_clsid = None

	_prop_map_get_ = {
		# Method 'Program' returns object of type 'FRCProgram'
		"Program": (101, 2, (13, 0), (), "Program", '{D42AB5D5-8FFB-11D0-94CC-0020AF68F0A3}'),
		# Method 'Robot' returns object of type 'FRCRobot'
		"Robot": (1, 2, (13, 0), (), "Robot", '{6D7E3A01-9ECC-11D0-94D5-0020AF68F0A3}'),
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

class IPrograms(DispatchBaseClass):
	'\x0bRepresents the collection of all programs currently loaded on the robot controller, i.e. Teach Pendant, KAREL, and VR programs.'
	CLSID = IID('{18F67740-46A8-11D0-8901-0020AF68F0A3}')
	coclass_clsid = IID('{1FBD567D-8F13-11D0-94CB-0020AF68F0A3}')

	# Result is of type FRCProgram
	def Add(self, Name=defaultNamedNotOptArg, Type=defaultNamedNotOptArg):
		'\x0bAdds a new program to the collection.'
		ret = self._oleobj_.InvokeTypes(150, LCID, 1, (13, 0), ((8, 1), (3, 1)),Name
			, Type)
		if ret is not None:
			# See if this IUnknown is really an IDispatch
			try:
				ret = ret.QueryInterface(pythoncom.IID_IDispatch)
			except pythoncom.error:
				return ret
			ret = Dispatch(ret, 'Add', '{D42AB5D5-8FFB-11D0-94CC-0020AF68F0A3}')
		return ret

	# Result is of type FRCProgram
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Name=defaultNamedNotOptArg, NewReference=defaultNamedOptArg, AccessMode=defaultNamedOptArg, RejectMode=defaultNamedOptArg):
		'\x0bReturns the specified program from the programs collection.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (13, 0), ((12, 1), (12, 17), (12, 17), (12, 17)),Name
			, NewReference, AccessMode, RejectMode)
		if ret is not None:
			# See if this IUnknown is really an IDispatch
			try:
				ret = ret.QueryInterface(pythoncom.IID_IDispatch)
			except pythoncom.error:
				return ret
			ret = Dispatch(ret, 'Item', '{D42AB5D5-8FFB-11D0-94CC-0020AF68F0A3}')
		return ret

	def Remove(self, Name=defaultNamedNotOptArg):
		'\x0bRemoves a program from the programs collection and the memory of the controller.'
		return self._oleobj_.InvokeTypes(151, LCID, 1, (24, 0), ((8, 1),),Name
			)

	def TryItem(self, Name=defaultNamedNotOptArg, NewReference=defaultNamedNotOptArg, AccessMode=defaultNamedNotOptArg, RejectMode=defaultNamedNotOptArg
			, Program=pythoncom.Missing):
		'\x0bTests if the specified program exists and if it does, the FRCProgam object to access it is returned.'
		return self._ApplyTypes_(152, 1, (11, 0), ((8, 1), (12, 17), (12, 17), (12, 17), (16397, 2)), 'TryItem', None,Name
			, NewReference, AccessMode, RejectMode, Program)

	_prop_map_get_ = {
		"Count": (101, 2, (3, 0), (), "Count", None),
		# Method 'Parent' returns object of type 'FRCRobot'
		"Parent": (103, 2, (13, 0), (), "Parent", '{6D7E3A01-9ECC-11D0-94D5-0020AF68F0A3}'),
		# Method 'Robot' returns object of type 'FRCRobot'
		"Robot": (1, 2, (13, 0), (), "Robot", '{6D7E3A01-9ECC-11D0-94D5-0020AF68F0A3}'),
		"Selected": (102, 2, (8, 0), (), "Selected", None),
	}
	_prop_map_put_ = {
		"Selected": ((102, LCID, 4, 0),()),
	}
	# Default method for this class is 'Item'
	def __call__(self, Name=defaultNamedNotOptArg, NewReference=defaultNamedOptArg, AccessMode=defaultNamedOptArg, RejectMode=defaultNamedOptArg):
		'\x0bReturns the specified program from the programs collection.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (13, 0), ((12, 1), (12, 17), (12, 17), (12, 17)),Name
			, NewReference, AccessMode, RejectMode)
		if ret is not None:
			# See if this IUnknown is really an IDispatch
			try:
				ret = ret.QueryInterface(pythoncom.IID_IDispatch)
			except pythoncom.error:
				return ret
			ret = Dispatch(ret, '__call__', '{D42AB5D5-8FFB-11D0-94CC-0020AF68F0A3}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{D42AB5D5-8FFB-11D0-94CC-0020AF68F0A3}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(101, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IProgramsEvents:
	CLSID = CLSID_Sink = IID('{BB944831-DB7C-11D0-A083-00A02436CF7E}')
	coclass_clsid = IID('{1FBD567D-8F13-11D0-94CB-0020AF68F0A3}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        1 : "OnCreate",
		        2 : "OnDelete",
		        3 : "OnAttrChange",
		        4 : "OnSelect",
		        5 : "OnRename",
		        6 : "OnSubTypeChange",
		        7 : "OnRefresh",
		        8 : "OnRefreshVars",
		        9 : "OnSubTypeChange2",
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
#	def OnCreate(self, Program=defaultNamedNotOptArg):
#		'\x0bOccurs after a program is created or loaded on the controller.'
#	def OnDelete(self, Program=defaultNamedNotOptArg):
#		'\x0bOccurs after a program is deleted.'
#	def OnAttrChange(self, Program=defaultNamedNotOptArg, Attr=defaultNamedNotOptArg):
#		'\x0bOccurs after an attribute is changed.'
#	def OnSelect(self):
#		'\x0bOccurs after a program is selected.'
#	def OnRename(self, Program=defaultNamedNotOptArg):
#		'\x0bOccurs after a program is renamed.'
#	def OnSubTypeChange(self, Program=defaultNamedNotOptArg):
#		'\x0bOccurs after a TP or KAREL program’s subtype is changed.'
#	def OnRefresh(self, Program=defaultNamedNotOptArg):
#		'\x0bOccurs after a TP program is reloaded.'
#	def OnRefreshVars(self, Program=defaultNamedNotOptArg):
#		'\x0bOccurs after a program’s variables are reloaded.'
#	def OnSubTypeChange2(self, Program=defaultNamedNotOptArg):
#		'\x0bOccurs after a TP or KAREL program’s subtype is changed.'


class IRegNumeric(DispatchBaseClass):
	'\x0bThis object allows access to numeric registers on the robot controller.'
	CLSID = IID('{6B51A440-212A-11D0-959F-00A024329125}')
	coclass_clsid = IID('{6B51A441-212A-11D0-959F-00A024329125}')

	_prop_map_get_ = {
		"Comment": (201, 2, (8, 0), (), "Comment", None),
		# Method 'Parent' returns object of type 'FRCVar'
		"Parent": (205, 2, (13, 0), (), "Parent", '{8C8ACC81-4F57-11D0-BC32-444553540000}'),
		# Method 'Program' returns object of type 'FRCProgram'
		"Program": (101, 2, (13, 0), (), "Program", '{D42AB5D5-8FFB-11D0-94CC-0020AF68F0A3}'),
		"RegFloat": (203, 2, (4, 0), (), "RegFloat", None),
		"RegLong": (202, 2, (3, 0), (), "RegLong", None),
		# Method 'Robot' returns object of type 'FRCRobot'
		"Robot": (1, 2, (13, 0), (), "Robot", '{6D7E3A01-9ECC-11D0-94D5-0020AF68F0A3}'),
		"Type": (204, 2, (3, 0), (), "Type", None),
	}
	_prop_map_put_ = {
		"Comment": ((201, LCID, 4, 0),()),
		"RegFloat": ((203, LCID, 4, 0),()),
		"RegLong": ((202, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IRegString(DispatchBaseClass):
	'\x0bThis object allows access to string registers on the robot controller.'
	CLSID = IID('{CADEF7CB-650F-45B7-BC95-9080FA32640B}')
	coclass_clsid = IID('{B5BD1EBA-FEC8-49CC-965B-7DD03974CDB8}')

	_prop_map_get_ = {
		"Comment": (201, 2, (8, 0), (), "Comment", None),
		# Method 'Parent' returns object of type 'FRCVar'
		"Parent": (205, 2, (13, 0), (), "Parent", '{8C8ACC81-4F57-11D0-BC32-444553540000}'),
		# Method 'Program' returns object of type 'FRCProgram'
		"Program": (101, 2, (13, 0), (), "Program", '{D42AB5D5-8FFB-11D0-94CC-0020AF68F0A3}'),
		# Method 'Robot' returns object of type 'FRCRobot'
		"Robot": (1, 2, (13, 0), (), "Robot", '{6D7E3A01-9ECC-11D0-94D5-0020AF68F0A3}'),
		"Value": (202, 2, (8, 0), (), "Value", None),
	}
	_prop_map_put_ = {
		"Comment": ((201, LCID, 4, 0),()),
		"Value": ((202, LCID, 4, 0),()),
	}
	# Default property for this class is 'Value'
	def __call__(self):
		return self._ApplyTypes_(*(202, 2, (8, 0), (), "Value", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IRobManProxy(DispatchBaseClass):
	CLSID = IID('{53D6E5D1-F5E2-11D3-9F35-00500409FF06}')
	coclass_clsid = IID('{53D6E5D2-F5E2-11D3-9F35-00500409FF06}')

	def ReleaseRobot(self):
		return self._oleobj_.InvokeTypes(102, LCID, 1, (3, 0), (),)

	_prop_map_get_ = {
		# Method 'GetRobot' returns object of type 'IRobot'
		"GetRobot": (101, 2, (9, 0), (), "GetRobot", '{6C779F22-4383-11D0-8901-0020AF68F0A3}'),
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

class IRobManProxyEvents:
	CLSID = CLSID_Sink = IID('{53D6E5D3-F5E2-11D3-9F35-00500409FF06}')
	coclass_clsid = IID('{53D6E5D2-F5E2-11D3-9F35-00500409FF06}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        4 : "OnTerminateRobot",
		        1 : "OnConnect",
		        2 : "OnDisconnect",
		        3 : "OnError",
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
#	def OnTerminateRobot(self, Answer=defaultNamedNotOptArg):
#	def OnConnect(self):
#	def OnDisconnect(self):
#	def OnError(self, Error=defaultNamedNotOptArg):


class IRobot(DispatchBaseClass):
	'\x0bTop level Robot Object interface used to establish connections and get references objects representing other system areas.'
	CLSID = IID('{6C779F22-4383-11D0-8901-0020AF68F0A3}')
	coclass_clsid = None

	def Connect(self, HostName=defaultNamedNotOptArg):
		'Obsolete. Use ConnectEx method'
		return self._oleobj_.InvokeTypes(151, LCID, 1, (24, 0), ((8, 1),),HostName
			)

	def ConnectEx(self, HostName=defaultNamedNotOptArg, NoWait=defaultNamedNotOptArg, NumRetries=defaultNamedNotOptArg, Period=defaultNamedNotOptArg):
		'Attempts connection to the robot controller specified by HostName the number of times specified by NumRetries at a the Period specified.  NoWait = TRUE will return immediately.'
		return self._oleobj_.InvokeTypes(161, LCID, 1, (24, 0), ((8, 1), (11, 1), (3, 1), (3, 1)),HostName
			, NoWait, NumRetries, Period)

	# Result is of type FRCIndPosition
	def CreateIndependentPosition(self, GroupBitMask=0):
		'\x0bCreates a new FRCIndPosition class object for your use.'
		ret = self._oleobj_.InvokeTypes(166, LCID, 1, (13, 0), ((3, 49),),GroupBitMask
			)
		if ret is not None:
			# See if this IUnknown is really an IDispatch
			try:
				ret = ret.QueryInterface(pythoncom.IID_IDispatch)
			except pythoncom.error:
				return ret
			ret = Dispatch(ret, 'CreateIndependentPosition', '{B4819F73-FC65-4475-97D3-974ACF6EE03E}')
		return ret

	# Result is of type FRCPacketEvent
	def CreatePacketEvent(self, SubSystemCode=defaultNamedOptArg, RequestCode=defaultNamedOptArg, PacketID=defaultNamedOptArg):
		'\x0bCreates a ROS packet event object for receiving events from the robot.'
		ret = self._oleobj_.InvokeTypes(154, LCID, 1, (13, 0), ((12, 17), (12, 17), (12, 17)),SubSystemCode
			, RequestCode, PacketID)
		if ret is not None:
			# See if this IUnknown is really an IDispatch
			try:
				ret = ret.QueryInterface(pythoncom.IID_IDispatch)
			except pythoncom.error:
				return ret
			ret = Dispatch(ret, 'CreatePacketEvent', '{FCCE9E5F-9420-11D1-B751-00C04FB99C75}')
		return ret

	# Result is of type FRCScatteredAccess
	def CreateScatteredAccess(self, *args):
		'\x0bCreates a new FRCScatteredAccess class object for your use.'
		return self._get_good_object_(self._oleobj_.Invoke(*((163,0,1,1)+args)),'CreateScatteredAccess')

	def EventLoggerConnect(self):
		'\x0bConnects the Robot object as an event logger service.'
		return self._oleobj_.InvokeTypes(157, LCID, 1, (24, 0), (),)

	# Result is of type FRCRobotErrorInfo
	def GetErrorInfo(self):
		'\x0bReturns extended error information for the last error thrown.'
		ret = self._oleobj_.InvokeTypes(156, LCID, 1, (13, 0), (),)
		if ret is not None:
			# See if this IUnknown is really an IDispatch
			try:
				ret = ret.QueryInterface(pythoncom.IID_IDispatch)
			except pythoncom.error:
				return ret
			ret = Dispatch(ret, 'GetErrorInfo', '{5BBFA760-09C6-11D2-871C-00C04F98D092}')
		return ret

	def KCL(self, Command=defaultNamedNotOptArg, Wait=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(158, LCID, 1, (24, 0), ((8, 1), (11, 1)),Command
			, Wait)

	def Load(self, FileName=defaultNamedNotOptArg, Option=defaultNamedNotOptArg):
		'\x0bLoads a file from a controller device into memory.'
		return self._oleobj_.InvokeTypes(153, LCID, 1, (24, 0), ((8, 1), (3, 1)),FileName
			, Option)

	def OfflineConnect(self, HostName=defaultNamedOptArg, MDPath=defaultNamedOptArg, FRSPath=defaultNamedOptArg, IgnoreVersion=defaultNamedOptArg):
		'\x0bConnects to an off-line simulated robot controller, specified by a virtual hostname.'
		return self._oleobj_.InvokeTypes(155, LCID, 1, (24, 0), ((12, 17), (12, 17), (12, 17), (12, 17)),HostName
			, MDPath, FRSPath, IgnoreVersion)

	def OutputDebugMessage(self, Message=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(160, LCID, 1, (24, 0), ((8, 1),),Message
			)

	def PostAlarm(self, *args):
		"\x0bPosts an alarm to the controller's alarm log."
		return self._get_good_object_(self._oleobj_.Invoke(*((152,0,1,1)+args)),'PostAlarm')

	def SPRUNCMD(self, FileName=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(159, LCID, 1, (24, 0), ((8, 1),),FileName
			)

	_prop_map_get_ = {
		# Method 'Alarms' returns object of type 'FRCAlarms'
		"Alarms": (109, 2, (13, 0), (), "Alarms", '{7C37F235-A494-11D0-A37F-0020AF39BE5A}'),
		# Method 'Applications' returns object of type 'FRCApplications'
		"Applications": (118, 2, (13, 0), (), "Applications", '{679622C3-E50A-11D1-B778-00C04FB99C75}'),
		# Method 'CurPosition' returns object of type 'FRCCurPosition'
		"CurPosition": (102, 2, (13, 0), (), "CurPosition", '{E2686FA9-1E42-11D1-B6FF-00C04FB9C401}'),
		"Devices": (103, 2, (9, 0), (), "Devices", None),
		"HostName": (101, 2, (8, 0), (), "HostName", None),
		# Method 'IOTypes' returns object of type 'FRCIOTypes'
		"IOTypes": (110, 2, (13, 0), (), "IOTypes", '{59DC16ED-AF91-11D0-A072-00A02436CF7E}'),
		"IsConnected": (162, 2, (11, 0), (), "IsConnected", None),
		"IsEventLogger": (121, 2, (11, 0), (), "IsEventLogger", None),
		"IsOffline": (120, 2, (11, 0), (), "IsOffline", None),
		# Method 'JogFrames' returns object of type 'FRCSysPositions'
		"JogFrames": (115, 2, (13, 0), (), "JogFrames", '{6055D69B-FFAE-11D0-B6F4-00C04FB9C401}'),
		"Language": (112, 2, (3, 0), (), "Language", None),
		# Method 'Pipes' returns object of type 'FRCPipes'
		"Pipes": (165, 2, (13, 0), (), "Pipes", '{B475BC91-3AF1-11D4-9F66-00105AE428C3}'),
		"ProcessID": (167, 2, (3, 0), (), "ProcessID", None),
		# Method 'Programs' returns object of type 'FRCPrograms'
		"Programs": (104, 2, (13, 0), (), "Programs", '{1FBD567D-8F13-11D0-94CB-0020AF68F0A3}'),
		# Method 'RegNumerics' returns object of type 'FRCVars'
		"RegNumerics": (106, 2, (13, 0), (), "RegNumerics", '{88B57BCB-D0CA-11CF-959F-00A024329125}'),
		# Method 'RegPositions' returns object of type 'FRCSysPositions'
		"RegPositions": (105, 2, (13, 0), (), "RegPositions", '{6055D69B-FFAE-11D0-B6F4-00C04FB9C401}'),
		# Method 'RegStrings' returns object of type 'FRCVars'
		"RegStrings": (168, 2, (13, 0), (), "RegStrings", '{88B57BCB-D0CA-11CF-959F-00A024329125}'),
		"RemoteMotionMaster": (108, 2, (3, 0), (), "RemoteMotionMaster", None),
		# Method 'SynchData' returns object of type 'FRCSynchData'
		"SynchData": (117, 2, (13, 0), (), "SynchData", '{2AF44182-9273-11D1-B6F9-00C04FA3BD85}'),
		# Method 'SysInfo' returns object of type 'FRCSysInfo'
		"SysInfo": (164, 2, (13, 0), (), "SysInfo", '{4553DA63-ACA1-11D3-8783-00C04F81118D}'),
		# Method 'SysVariables' returns object of type 'FRCVars'
		"SysVariables": (107, 2, (13, 0), (), "SysVariables", '{88B57BCB-D0CA-11CF-959F-00A024329125}'),
		"TPMotionSource": (119, 2, (11, 0), (), "TPMotionSource", None),
		# Method 'TPScreen' returns object of type 'FRCTPScreen'
		"TPScreen": (111, 2, (13, 0), (), "TPScreen", '{660E6870-E286-11D0-8BB6-0020AF39BE5A}'),
		# Method 'Tasks' returns object of type 'FRCTasks'
		"Tasks": (116, 2, (13, 0), (), "Tasks", '{6B01CFFC-4626-11D1-B745-00C04FBBE42A}'),
		# Method 'ToolFrames' returns object of type 'FRCSysPositions'
		"ToolFrames": (113, 2, (13, 0), (), "ToolFrames", '{6055D69B-FFAE-11D0-B6F4-00C04FB9C401}'),
		# Method 'UserFrames' returns object of type 'FRCSysPositions'
		"UserFrames": (114, 2, (13, 0), (), "UserFrames", '{6055D69B-FFAE-11D0-B6F4-00C04FB9C401}'),
	}
	_prop_map_put_ = {
		"Language": ((112, LCID, 4, 0),()),
		"RemoteMotionMaster": ((108, LCID, 4, 0),()),
		"TPMotionSource": ((119, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IRobot2(DispatchBaseClass):
	'\x0bTop level Robot Object interface used to establish connections and get references objects representing other system areas.'
	CLSID = IID('{A6861F10-5F34-4053-ABE4-55C55F595814}')
	coclass_clsid = IID('{6D7E3A01-9ECC-11D0-94D5-0020AF68F0A3}')

	def Connect(self, HostName=defaultNamedNotOptArg):
		'Obsolete. Use ConnectEx method'
		return self._oleobj_.InvokeTypes(151, LCID, 1, (24, 0), ((8, 1),),HostName
			)

	def ConnectEx(self, HostName=defaultNamedNotOptArg, NoWait=defaultNamedNotOptArg, NumRetries=defaultNamedNotOptArg, Period=defaultNamedNotOptArg):
		'Attempts connection to the robot controller specified by HostName the number of times specified by NumRetries at a the Period specified.  NoWait = TRUE will return immediately.'
		return self._oleobj_.InvokeTypes(161, LCID, 1, (24, 0), ((8, 1), (11, 1), (3, 1), (3, 1)),HostName
			, NoWait, NumRetries, Period)

	# Result is of type FRCIndPosition
	def CreateIndependentPosition(self, GroupBitMask=0):
		'\x0bCreates a new FRCIndPosition class object for your use.'
		ret = self._oleobj_.InvokeTypes(166, LCID, 1, (13, 0), ((3, 49),),GroupBitMask
			)
		if ret is not None:
			# See if this IUnknown is really an IDispatch
			try:
				ret = ret.QueryInterface(pythoncom.IID_IDispatch)
			except pythoncom.error:
				return ret
			ret = Dispatch(ret, 'CreateIndependentPosition', '{B4819F73-FC65-4475-97D3-974ACF6EE03E}')
		return ret

	# Result is of type FRCPacketEvent
	def CreatePacketEvent(self, SubSystemCode=defaultNamedOptArg, RequestCode=defaultNamedOptArg, PacketID=defaultNamedOptArg):
		'\x0bCreates a ROS packet event object for receiving events from the robot.'
		ret = self._oleobj_.InvokeTypes(154, LCID, 1, (13, 0), ((12, 17), (12, 17), (12, 17)),SubSystemCode
			, RequestCode, PacketID)
		if ret is not None:
			# See if this IUnknown is really an IDispatch
			try:
				ret = ret.QueryInterface(pythoncom.IID_IDispatch)
			except pythoncom.error:
				return ret
			ret = Dispatch(ret, 'CreatePacketEvent', '{FCCE9E5F-9420-11D1-B751-00C04FB99C75}')
		return ret

	# Result is of type FRCScatteredAccess
	def CreateScatteredAccess(self, *args):
		'\x0bCreates a new FRCScatteredAccess class object for your use.'
		return self._get_good_object_(self._oleobj_.Invoke(*((163,0,1,1)+args)),'CreateScatteredAccess')

	def EventLoggerConnect(self):
		'\x0bConnects the Robot object as an event logger service.'
		return self._oleobj_.InvokeTypes(157, LCID, 1, (24, 0), (),)

	# Result is of type FRCRobotErrorInfo
	def GetErrorInfo(self):
		'\x0bReturns extended error information for the last error thrown.'
		ret = self._oleobj_.InvokeTypes(156, LCID, 1, (13, 0), (),)
		if ret is not None:
			# See if this IUnknown is really an IDispatch
			try:
				ret = ret.QueryInterface(pythoncom.IID_IDispatch)
			except pythoncom.error:
				return ret
			ret = Dispatch(ret, 'GetErrorInfo', '{5BBFA760-09C6-11D2-871C-00C04F98D092}')
		return ret

	def KCL(self, Command=defaultNamedNotOptArg, Wait=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(158, LCID, 1, (24, 0), ((8, 1), (11, 1)),Command
			, Wait)

	def Load(self, FileName=defaultNamedNotOptArg, Option=defaultNamedNotOptArg):
		'\x0bLoads a file from a controller device into memory.'
		return self._oleobj_.InvokeTypes(153, LCID, 1, (24, 0), ((8, 1), (3, 1)),FileName
			, Option)

	def OfflineConnect(self, HostName=defaultNamedOptArg, MDPath=defaultNamedOptArg, FRSPath=defaultNamedOptArg, IgnoreVersion=defaultNamedOptArg):
		'\x0bConnects to an off-line simulated robot controller, specified by a virtual hostname.'
		return self._oleobj_.InvokeTypes(155, LCID, 1, (24, 0), ((12, 17), (12, 17), (12, 17), (12, 17)),HostName
			, MDPath, FRSPath, IgnoreVersion)

	def OutputDebugMessage(self, Message=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(160, LCID, 1, (24, 0), ((8, 1),),Message
			)

	def PostAlarm(self, *args):
		"\x0bPosts an alarm to the controller's alarm log."
		return self._get_good_object_(self._oleobj_.Invoke(*((152,0,1,1)+args)),'PostAlarm')

	def SPRUNCMD(self, FileName=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(159, LCID, 1, (24, 0), ((8, 1),),FileName
			)

	_prop_map_get_ = {
		# Method 'Alarms' returns object of type 'FRCAlarms'
		"Alarms": (109, 2, (13, 0), (), "Alarms", '{7C37F235-A494-11D0-A37F-0020AF39BE5A}'),
		# Method 'Applications' returns object of type 'FRCApplications'
		"Applications": (118, 2, (13, 0), (), "Applications", '{679622C3-E50A-11D1-B778-00C04FB99C75}'),
		# Method 'CurPosition' returns object of type 'FRCCurPosition'
		"CurPosition": (102, 2, (13, 0), (), "CurPosition", '{E2686FA9-1E42-11D1-B6FF-00C04FB9C401}'),
		"Devices": (103, 2, (9, 0), (), "Devices", None),
		"HostName": (101, 2, (8, 0), (), "HostName", None),
		# Method 'IOTypes' returns object of type 'FRCIOTypes'
		"IOTypes": (110, 2, (13, 0), (), "IOTypes", '{59DC16ED-AF91-11D0-A072-00A02436CF7E}'),
		"IsConnected": (162, 2, (11, 0), (), "IsConnected", None),
		"IsEventLogger": (121, 2, (11, 0), (), "IsEventLogger", None),
		"IsOffline": (120, 2, (11, 0), (), "IsOffline", None),
		# Method 'JogFrames' returns object of type 'FRCSysPositions'
		"JogFrames": (115, 2, (13, 0), (), "JogFrames", '{6055D69B-FFAE-11D0-B6F4-00C04FB9C401}'),
		"Language": (112, 2, (3, 0), (), "Language", None),
		# Method 'Pipes' returns object of type 'FRCPipes'
		"Pipes": (165, 2, (13, 0), (), "Pipes", '{B475BC91-3AF1-11D4-9F66-00105AE428C3}'),
		"ProcessID": (167, 2, (3, 0), (), "ProcessID", None),
		# Method 'Programs' returns object of type 'FRCPrograms'
		"Programs": (104, 2, (13, 0), (), "Programs", '{1FBD567D-8F13-11D0-94CB-0020AF68F0A3}'),
		# Method 'RegNumerics' returns object of type 'FRCVars'
		"RegNumerics": (106, 2, (13, 0), (), "RegNumerics", '{88B57BCB-D0CA-11CF-959F-00A024329125}'),
		# Method 'RegPositions' returns object of type 'FRCSysPositions'
		"RegPositions": (105, 2, (13, 0), (), "RegPositions", '{6055D69B-FFAE-11D0-B6F4-00C04FB9C401}'),
		# Method 'RegStrings' returns object of type 'FRCVars'
		"RegStrings": (168, 2, (13, 0), (), "RegStrings", '{88B57BCB-D0CA-11CF-959F-00A024329125}'),
		"RemoteMotionMaster": (108, 2, (3, 0), (), "RemoteMotionMaster", None),
		# Method 'SynchData' returns object of type 'FRCSynchData'
		"SynchData": (117, 2, (13, 0), (), "SynchData", '{2AF44182-9273-11D1-B6F9-00C04FA3BD85}'),
		# Method 'SysInfo' returns object of type 'FRCSysInfo'
		"SysInfo": (164, 2, (13, 0), (), "SysInfo", '{4553DA63-ACA1-11D3-8783-00C04F81118D}'),
		# Method 'SysVariables' returns object of type 'FRCVars'
		"SysVariables": (107, 2, (13, 0), (), "SysVariables", '{88B57BCB-D0CA-11CF-959F-00A024329125}'),
		"TPMotionSource": (119, 2, (11, 0), (), "TPMotionSource", None),
		# Method 'TPScreen' returns object of type 'FRCTPScreen'
		"TPScreen": (111, 2, (13, 0), (), "TPScreen", '{660E6870-E286-11D0-8BB6-0020AF39BE5A}'),
		# Method 'Tasks' returns object of type 'FRCTasks'
		"Tasks": (116, 2, (13, 0), (), "Tasks", '{6B01CFFC-4626-11D1-B745-00C04FBBE42A}'),
		# Method 'ToolFrames' returns object of type 'FRCSysPositions'
		"ToolFrames": (113, 2, (13, 0), (), "ToolFrames", '{6055D69B-FFAE-11D0-B6F4-00C04FB9C401}'),
		# Method 'UserFrames' returns object of type 'FRCSysPositions'
		"UserFrames": (114, 2, (13, 0), (), "UserFrames", '{6055D69B-FFAE-11D0-B6F4-00C04FB9C401}'),
	}
	_prop_map_put_ = {
		"Language": ((112, LCID, 4, 0),()),
		"RemoteMotionMaster": ((108, LCID, 4, 0),()),
		"TPMotionSource": ((119, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IRobotErrorInfo(DispatchBaseClass):
	'\x0bObject used to access extended error information after an error has been thrown (raised) and caught.'
	CLSID = IID('{115069C0-09C5-11D2-871C-00C04F98D092}')
	coclass_clsid = IID('{5BBFA760-09C6-11D2-871C-00C04F98D092}')

	_prop_map_get_ = {
		"Description": (4, 2, (8, 0), (), "Description", None),
		"Facility": (1, 2, (3, 0), (), "Facility", None),
		"GUID": (5, 2, (8, 0), (), "GUID", None),
		"HelpContext": (6, 2, (19, 0), (), "HelpContext", None),
		"HelpFile": (7, 2, (8, 0), (), "HelpFile", None),
		"Number": (3, 2, (3, 0), (), "Number", None),
		"Severity": (2, 2, (3, 0), (), "Severity", None),
		"Source": (8, 2, (8, 0), (), "Source", None),
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

class IRobotEvents:
	CLSID = CLSID_Sink = IID('{52A6CF60-4732-11D2-8738-00C04F98D092}')
	coclass_clsid = IID('{6D7E3A01-9ECC-11D0-94D5-0020AF68F0A3}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        1 : "OnConnect",
		        2 : "OnDisconnect",
		        3 : "OnError",
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
#	def OnConnect(self):
#		'\x0bThis event is fired after the connection has been established to the controller.'
#	def OnDisconnect(self):
#		'\x0bThis event is fired after a connection to a controller has been terminated abnormally.'
#	def OnError(self, Error=defaultNamedNotOptArg):
#		'Occurs when an error is detected that is not handled by normal excpetion handling.'


class IRobotIOSignal(DispatchBaseClass):
	'\x0bRepresents a robot I/O signal.  '
	CLSID = IID('{714CC926-B4E5-11D0-A073-00A02436CF7E}')
	coclass_clsid = IID('{A5F1E1FE-F2B7-40AB-9D33-6932112978BD}')

	def Refresh(self):
		'\x0bReads new information of the signal from the robot.'
		return self._oleobj_.InvokeTypes(252, LCID, 1, (24, 0), (),)

	def StartMonitor(self, Latency=defaultNamedNotOptArg):
		'\x0bStarts the monitoring of the I/O signal for changes.'
		return self._oleobj_.InvokeTypes(150, LCID, 1, (24, 0), ((3, 0),),Latency
			)

	def StopMonitor(self):
		'\x0bStops the monitoring of the I/O signal for changes.'
		return self._oleobj_.InvokeTypes(151, LCID, 1, (24, 0), (),)

	def Update(self):
		"\x0bSends the local copy of this signal's information to the robot."
		return self._oleobj_.InvokeTypes(253, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"Complementary": (204, 2, (11, 0), (), "Complementary", None),
		"IsAssigned": (103, 2, (11, 0), (), "IsAssigned", None),
		"IsMonitoring": (105, 2, (11, 0), (), "IsMonitoring", None),
		"IsOffline": (104, 2, (11, 0), (), "IsOffline", None),
		"LogicalNum": (101, 2, (3, 0), (), "LogicalNum", None),
		"NoRefresh": (250, 2, (11, 0), (), "NoRefresh", None),
		"NoUpdate": (251, 2, (11, 0), (), "NoUpdate", None),
		# Method 'Parent' returns object of type 'FRCIOSignals'
		"Parent": (205, 2, (13, 0), (), "Parent", '{59DC16F8-AF91-11D0-A072-00A02436CF7E}'),
		"Polarity": (203, 2, (11, 0), (), "Polarity", None),
		# Method 'Robot' returns object of type 'FRCRobot'
		"Robot": (1, 2, (13, 0), (), "Robot", '{6D7E3A01-9ECC-11D0-94D5-0020AF68F0A3}'),
		"Simulate": (202, 2, (11, 0), (), "Simulate", None),
		"Value": (201, 2, (11, 0), (), "Value", None),
	}
	_prop_map_put_ = {
		"Comment": ((102, LCID, 4, 0),()),
		"Complementary": ((204, LCID, 4, 0),()),
		"NoRefresh": ((250, LCID, 4, 0),()),
		"NoUpdate": ((251, LCID, 4, 0),()),
		"Polarity": ((203, LCID, 4, 0),()),
		"Simulate": ((202, LCID, 4, 0),()),
		"Value": ((201, LCID, 4, 0),()),
	}
	# Default property for this class is 'Value'
	def __call__(self):
		return self._ApplyTypes_(*(201, 2, (11, 0), (), "Value", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IRobotObject(DispatchBaseClass):
	CLSID = IID('{D42AB5D4-8FFB-11D0-94CC-0020AF68F0A3}')
	coclass_clsid = None

	_prop_map_get_ = {
		# Method 'Robot' returns object of type 'FRCRobot'
		"Robot": (1, 2, (13, 0), (), "Robot", '{6D7E3A01-9ECC-11D0-94D5-0020AF68F0A3}'),
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

class IScatteredAccess(DispatchBaseClass):
	'\x0bEnables you to access a group of independent variables and I/O signals with minimum network overhead.'
	CLSID = IID('{6F33A4D2-91F3-11D3-877C-00C04F81118D}')
	coclass_clsid = IID('{6F33A4D1-91F3-11D3-877C-00C04F81118D}')

	def Refresh(self):
		'\x0bReads the values of all items controlled by this object from the robot into local Robot Server memory on the PC.'
		return self._oleobj_.InvokeTypes(101, LCID, 1, (24, 0), (),)

	def Update(self):
		'\x0bWrites the values of all items controlled by this object from local Robot Server memory on the PC to the robot.'
		return self._oleobj_.InvokeTypes(102, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		# Method 'Robot' returns object of type 'FRCRobot'
		"Robot": (1, 2, (13, 0), (), "Robot", '{6D7E3A01-9ECC-11D0-94D5-0020AF68F0A3}'),
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

class ISelectedLines(DispatchBaseClass):
	CLSID = IID('{12585150-9394-11D2-877C-00C04FB9C401}')
	coclass_clsid = IID('{58ADC520-9395-11D2-877C-00C04FB9C401}')

	def Add(self, StartLine=defaultNamedNotOptArg, EndLine=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(251, LCID, 1, (24, 0), ((3, 1), (3, 17)),StartLine
			, EndLine)

	def Copy(self):
		return self._oleobj_.InvokeTypes(252, LCID, 1, (24, 0), (),)

	def Cut(self):
		return self._oleobj_.InvokeTypes(253, LCID, 1, (24, 0), (),)

	# The method IsSelected is actually a property, but must be used as a method to correctly pass the arguments
	def IsSelected(self, LineNum=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(202, LCID, 2, (11, 0), ((3, 1),),LineNum
			)

	def Paste(self, LineNum=defaultNamedNotOptArg, PasteType=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(254, LCID, 1, (24, 0), ((3, 1), (3, 1)),LineNum
			, PasteType)

	def Remove(self, LineNum=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(255, LCID, 1, (24, 0), ((3, 1),),LineNum
			)

	def RemoveAll(self):
		return self._oleobj_.InvokeTypes(256, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"Count": (201, 2, (3, 0), (), "Count", None),
		# Method 'Robot' returns object of type 'FRCRobot'
		"Robot": (1, 2, (13, 0), (), "Robot", '{6D7E3A01-9ECC-11D0-94D5-0020AF68F0A3}'),
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
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(201, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ISelectedLinesEvents:
	CLSID = CLSID_Sink = IID('{26466EE1-9393-11D2-877C-00C04FB9C401}')
	coclass_clsid = IID('{58ADC520-9395-11D2-877C-00C04FB9C401}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        1 : "OnCopy",
		        2 : "OnBeginCut",
		        3 : "OnEndCut",
		        4 : "OnBeginPaste",
		        5 : "OnEndPaste",
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
#	def OnCopy(self):
#	def OnBeginCut(self):
#	def OnEndCut(self):
#	def OnBeginPaste(self):
#	def OnEndPaste(self):


class ISynchApplData(DispatchBaseClass):
	CLSID = IID('{8FAFC8E7-B2B8-11D1-B705-00C04FA3BD85}')
	coclass_clsid = IID('{8FAFC8E8-B2B8-11D1-B705-00C04FA3BD85}')

	# Result is of type FRCSynchApplDataItem
	def Add(self, Name=defaultNamedNotOptArg, ApplicationID=defaultNamedNotOptArg, ApplProgID=defaultNamedNotOptArg, EditProgID=defaultNamedNotOptArg):
		'\x0bAdd places a new TPP application data object in the TPP application data collection.'
		ret = self._oleobj_.InvokeTypes(150, LCID, 1, (13, 0), ((8, 1), (12, 17), (8, 1), (8, 1)),Name
			, ApplicationID, ApplProgID, EditProgID)
		if ret is not None:
			# See if this IUnknown is really an IDispatch
			try:
				ret = ret.QueryInterface(pythoncom.IID_IDispatch)
			except pythoncom.error:
				return ret
			ret = Dispatch(ret, 'Add', '{8FAFC8EA-B2B8-11D1-B705-00C04FA3BD85}')
		return ret

	# Result is of type FRCSynchApplDataItem
	# The method GetItem is actually a property, but must be used as a method to correctly pass the arguments
	def GetItem(self, Name=defaultNamedOptArg, CollectionIndex=defaultNamedOptArg, ApplicationID=defaultNamedOptArg):
		'\x0bItem returns an application data item object from the collection to the caller.  '
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (13, 0), ((12, 17), (12, 17), (12, 17)),Name
			, CollectionIndex, ApplicationID)
		if ret is not None:
			# See if this IUnknown is really an IDispatch
			try:
				ret = ret.QueryInterface(pythoncom.IID_IDispatch)
			except pythoncom.error:
				return ret
			ret = Dispatch(ret, 'GetItem', '{8FAFC8EA-B2B8-11D1-B705-00C04FA3BD85}')
		return ret

	def Remove(self, Name=defaultNamedNotOptArg, ApplicationID=defaultNamedOptArg):
		' \x0bRemove deletes a TPP application data object from the application data collection.  '
		return self._oleobj_.InvokeTypes(151, LCID, 1, (24, 0), ((8, 1), (12, 17)),Name
			, ApplicationID)

	_prop_map_get_ = {
		"Count": (101, 2, (3, 0), (), "Count", None),
		# Method 'Item' returns object of type 'FRCSynchApplDataItem'
		"Item": (0, 2, (13, 0), ((12, 17), (12, 17), (12, 17)), "Item", '{8FAFC8EA-B2B8-11D1-B705-00C04FA3BD85}'),
		# Method 'Robot' returns object of type 'FRCRobot'
		"Robot": (1, 2, (13, 0), (), "Robot", '{6D7E3A01-9ECC-11D0-94D5-0020AF68F0A3}'),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Name=defaultNamedOptArg, CollectionIndex=defaultNamedOptArg, ApplicationID=defaultNamedOptArg):
		'\x0bItem returns an application data item object from the collection to the caller.  '
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (13, 0), ((12, 17), (12, 17), (12, 17)),Name
			, CollectionIndex, ApplicationID)
		if ret is not None:
			# See if this IUnknown is really an IDispatch
			try:
				ret = ret.QueryInterface(pythoncom.IID_IDispatch)
			except pythoncom.error:
				return ret
			ret = Dispatch(ret, '__call__', '{8FAFC8EA-B2B8-11D1-B705-00C04FA3BD85}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(101, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ISynchApplDataItem(DispatchBaseClass):
	CLSID = IID('{8FAFC8E9-B2B8-11D1-B705-00C04FA3BD85}')
	coclass_clsid = IID('{8FAFC8EA-B2B8-11D1-B705-00C04FA3BD85}')

	_prop_map_get_ = {
		"ApplProgID": (103, 2, (8, 0), (), "ApplProgID", None),
		"ApplicationID": (102, 2, (2, 0), (), "ApplicationID", None),
		"EditProgID": (104, 2, (8, 0), (), "EditProgID", None),
		"Name": (101, 2, (8, 0), (), "Name", None),
		# Method 'Robot' returns object of type 'FRCRobot'
		"Robot": (1, 2, (13, 0), (), "Robot", '{6D7E3A01-9ECC-11D0-94D5-0020AF68F0A3}'),
	}
	_prop_map_put_ = {
		"ApplProgID": ((103, LCID, 4, 0),()),
		"EditProgID": ((104, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISynchData(DispatchBaseClass):
	' \x0bThis object is used to access all other controller feature/option synchronization objects.'
	CLSID = IID('{3C3988CD-9275-11D1-B6F9-00C04FA3BD85}')
	coclass_clsid = IID('{2AF44182-9273-11D1-B6F9-00C04FA3BD85}')

	_prop_map_get_ = {
		# Method 'Features' returns object of type 'FRCFeatures'
		"Features": (101, 2, (13, 0), (), "Features", '{2AF44184-9273-11D1-B6F9-00C04FA3BD85}'),
		# Method 'Robot' returns object of type 'FRCRobot'
		"Robot": (1, 2, (13, 0), (), "Robot", '{6D7E3A01-9ECC-11D0-94D5-0020AF68F0A3}'),
		# Method 'TPApplData' returns object of type 'FRCSynchApplData'
		"TPApplData": (103, 2, (13, 0), (), "TPApplData", '{8FAFC8E8-B2B8-11D1-B705-00C04FA3BD85}'),
		# Method 'TPInstructions' returns object of type 'FRCTPInstructions'
		"TPInstructions": (102, 2, (13, 0), (), "TPInstructions", '{3C05D26E-9BE8-11D1-B6FC-00C04FA3BD85}'),
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

class ISysGroupPosition(DispatchBaseClass):
	'\x0bProvides access to the positional data of a controller system position for a specific motion group.'
	CLSID = IID('{DC2FA0C7-FFAB-11D0-B6F4-00C04FB9C401}')
	coclass_clsid = IID('{DC2FA0C8-FFAB-11D0-B6F4-00C04FB9C401}')

	def CheckReach(self, From=defaultNamedNotOptArg, MoType=6, OrientType=2, Destination=defaultNamedNotOptArg
			, MotionErrorInfo=0):
		'\x0bReturns a Boolean indicating if the robot can reach the position or not.'
		return self._ApplyTypes_(306, 1, (11, 0), ((12, 17), (3, 49), (3, 49), (12, 17), (16397, 50)), 'CheckReach', None,From
			, MoType, OrientType, Destination, MotionErrorInfo)

	def Copy(self, Position=defaultNamedNotOptArg):
		'\x0bCopies the positional data from another object into this one.'
		return self._oleobj_.InvokeTypes(305, LCID, 1, (24, 0), ((9, 1),),Position
			)

	# The method Formats is actually a property, but must be used as a method to correctly pass the arguments
	def Formats(self, Type=defaultNamedNotOptArg):
		'\x0bReturns positional data in the specified format.'
		ret = self._oleobj_.InvokeTypes(203, LCID, 2, (9, 0), ((3, 1),),Type
			)
		if ret is not None:
			ret = Dispatch(ret, 'Formats', None)
		return ret

	# The method IsEqualTo is actually a property, but must be used as a method to correctly pass the arguments
	def IsEqualTo(self, TargetPos=defaultNamedNotOptArg):
		"Returns a boolean value that indicates if the positional data contained in the current object is 'almost equal to' the positional data of another object."
		return self._oleobj_.InvokeTypes(303, LCID, 2, (11, 0), ((9, 1),),TargetPos
			)

	# The method IsReachable is actually a property, but must be used as a method to correctly pass the arguments
	def IsReachable(self, From=defaultNamedNotOptArg, MoType=6, OrientType=2, Destination=defaultNamedNotOptArg
			, MotionErrorInfo=0):
		'\x0bReturns a Boolean indicating if the robot can reach the position or not.'
		return self._ApplyTypes_(304, 2, (11, 0), ((12, 17), (3, 49), (3, 49), (12, 17), (16397, 50)), 'IsReachable', None,From
			, MoType, OrientType, Destination, MotionErrorInfo)

	def MatInv(self, InputPos=defaultNamedNotOptArg):
		'\x0bInvert the input position transformation matrix and set the results to this position.'
		return self._oleobj_.InvokeTypes(259, LCID, 1, (24, 0), ((9, 1),),InputPos
			)

	def MatMul(self, LeftPos=defaultNamedNotOptArg, RightPos=defaultNamedNotOptArg):
		'\x0bMultiply two input positions’ transformation matrices and set the results to this position.'
		return self._oleobj_.InvokeTypes(258, LCID, 1, (24, 0), ((9, 1), (9, 1)),LeftPos
			, RightPos)

	def Moveto(self):
		'\x0bMoves the robot to this position.'
		return self._oleobj_.InvokeTypes(253, LCID, 1, (24, 0), (),)

	def Record(self):
		'\x0bRecords the current position of the robot to this position.'
		return self._oleobj_.InvokeTypes(254, LCID, 1, (24, 0), (),)

	def Refresh(self):
		'\x0bClears all changes to the position since the last update of the position.'
		return self._oleobj_.InvokeTypes(252, LCID, 1, (24, 0), (),)

	def StartMonitor(self, Latency=defaultNamedNotOptArg):
		'\x0bEnables the Change event, with specified latency.'
		return self._oleobj_.InvokeTypes(255, LCID, 1, (24, 0), ((3, 1),),Latency
			)

	def StopMonitor(self):
		'\x0bStops the Change event from occurring.'
		return self._oleobj_.InvokeTypes(256, LCID, 1, (24, 0), (),)

	def Uninitialize(self):
		'\x0bUninitializes the position. '
		return self._oleobj_.InvokeTypes(257, LCID, 1, (24, 0), (),)

	def Update(self):
		'\x0bUpdates any changes to the position back to the controller.'
		return self._oleobj_.InvokeTypes(251, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"AutomaticUpdate": (201, 2, (11, 0), (), "AutomaticUpdate", None),
		"Comment": (302, 2, (8, 0), (), "Comment", None),
		"GroupNum": (204, 2, (2, 0), (), "GroupNum", None),
		"Id": (205, 2, (3, 0), (), "Id", None),
		"IsAtCurPosition": (206, 2, (11, 0), (), "IsAtCurPosition", None),
		"IsInitialized": (207, 2, (11, 0), (), "IsInitialized", None),
		"IsMonitoring": (210, 2, (11, 0), (), "IsMonitoring", None),
		# Method 'Parent' returns object of type 'FRCSysPosition'
		"Parent": (301, 2, (13, 0), (), "Parent", '{6055D699-FFAE-11D0-B6F4-00C04FB9C401}'),
		# Method 'Program' returns object of type 'FRCProgram'
		"Program": (101, 2, (13, 0), (), "Program", '{D42AB5D5-8FFB-11D0-94CC-0020AF68F0A3}'),
		# Method 'Robot' returns object of type 'FRCRobot'
		"Robot": (1, 2, (13, 0), (), "Robot", '{6D7E3A01-9ECC-11D0-94D5-0020AF68F0A3}'),
		"Type": (202, 2, (3, 0), (), "Type", None),
		"UserFrame": (208, 2, (3, 0), (), "UserFrame", None),
		"UserTool": (209, 2, (3, 0), (), "UserTool", None),
	}
	_prop_map_put_ = {
		"AutomaticUpdate": ((201, LCID, 4, 0),()),
		"Comment": ((302, LCID, 4, 0),()),
		"Type": ((202, LCID, 4, 0),()),
		"UserFrame": ((208, LCID, 4, 0),()),
		"UserTool": ((209, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISysGroupPositionEvents:
	CLSID = CLSID_Sink = IID('{6EA7D4AD-381C-11D1-B6FE-00C04FB9E76B}')
	coclass_clsid = IID('{DC2FA0C8-FFAB-11D0-B6F4-00C04FB9C401}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        1 : "OnChange",
		        2 : "OnCommentChange",
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
#	def OnChange(self):
#		'\x0bOccurs after the position is changed.'
#	def OnCommentChange(self):
#		'\x0bOccurs when the position’s comment is changed.'


class ISysInfo(DispatchBaseClass):
	'\x0bProvides access to robot controller system information.'
	CLSID = IID('{4553DA61-ACA1-11D3-8783-00C04F81118D}')
	coclass_clsid = IID('{4553DA63-ACA1-11D3-8783-00C04F81118D}')

	_prop_map_get_ = {
		"CMOS": (102, 2, (3, 0), (), "CMOS", None),
		"Clock": (101, 2, (7, 0), (), "Clock", None),
		"DRAM": (103, 2, (3, 0), (), "DRAM", None),
		"FROMType": (121, 2, (3, 0), (), "FROMType", None),
		"From": (104, 2, (3, 0), (), "From", None),
		"PermMemFree": (106, 2, (3, 0), (), "PermMemFree", None),
		"PermMemLargestFreeBlock": (107, 2, (3, 0), (), "PermMemLargestFreeBlock", None),
		"PermMemTotal": (105, 2, (3, 0), (), "PermMemTotal", None),
		"PermMemUsed": (108, 2, (3, 0), (), "PermMemUsed", None),
		# Method 'Robot' returns object of type 'FRCRobot'
		"Robot": (1, 2, (13, 0), (), "Robot", '{6D7E3A01-9ECC-11D0-94D5-0020AF68F0A3}'),
		"StartMode": (122, 2, (3, 0), (), "StartMode", None),
		"SystemMemFree": (118, 2, (3, 0), (), "SystemMemFree", None),
		"SystemMemLargestFreeBlock": (119, 2, (3, 0), (), "SystemMemLargestFreeBlock", None),
		"SystemMemTotal": (117, 2, (3, 0), (), "SystemMemTotal", None),
		"SystemMemUsed": (120, 2, (3, 0), (), "SystemMemUsed", None),
		"TPPMemFree": (114, 2, (3, 0), (), "TPPMemFree", None),
		"TPPMemLargestFreeBlock": (115, 2, (3, 0), (), "TPPMemLargestFreeBlock", None),
		"TPPMemTotal": (113, 2, (3, 0), (), "TPPMemTotal", None),
		"TPPMemUsed": (116, 2, (3, 0), (), "TPPMemUsed", None),
		"TempMemFree": (110, 2, (3, 0), (), "TempMemFree", None),
		"TempMemLargestFreeBlock": (111, 2, (3, 0), (), "TempMemLargestFreeBlock", None),
		"TempMemTotal": (109, 2, (3, 0), (), "TempMemTotal", None),
		"TempMemUsed": (112, 2, (3, 0), (), "TempMemUsed", None),
	}
	_prop_map_put_ = {
		"Clock": ((101, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISysPosition(DispatchBaseClass):
	'\x0bProvides access to a single controller system position.'
	CLSID = IID('{6055D698-FFAE-11D0-B6F4-00C04FB9C401}')
	coclass_clsid = IID('{6055D699-FFAE-11D0-B6F4-00C04FB9C401}')

	def CheckReach(self, From=defaultNamedNotOptArg, MoType=6, OrientType=2, Destination=defaultNamedNotOptArg
			, MotionErrorInfo=0):
		'\x0bReturns a Boolean indicating if the robot can reach the position or not.'
		return self._ApplyTypes_(259, 1, (11, 0), ((12, 17), (3, 49), (3, 49), (12, 17), (16397, 50)), 'CheckReach', None,From
			, MoType, OrientType, Destination, MotionErrorInfo)

	def Copy(self, Position=defaultNamedNotOptArg):
		'\x0bCopies the positional data from another object into this one.'
		return self._oleobj_.InvokeTypes(257, LCID, 1, (24, 0), ((9, 1),),Position
			)

	# Result is of type FRCSysGroupPosition
	# The method Group is actually a property, but must be used as a method to correctly pass the arguments
	def Group(self, GroupNum=defaultNamedNotOptArg):
		'\x0bReturns a FRCSysGroupPosition object representing the system position in the specified motion group.'
		ret = self._oleobj_.InvokeTypes(203, LCID, 2, (13, 0), ((2, 1),),GroupNum
			)
		if ret is not None:
			# See if this IUnknown is really an IDispatch
			try:
				ret = ret.QueryInterface(pythoncom.IID_IDispatch)
			except pythoncom.error:
				return ret
			ret = Dispatch(ret, 'Group', '{DC2FA0C8-FFAB-11D0-B6F4-00C04FB9C401}')
		return ret

	# The method GroupMask is actually a property, but must be used as a method to correctly pass the arguments
	def GroupMask(self, GroupNum=defaultNamedNotOptArg):
		'\x0bReturns whether the specified group is supported on the controller.'
		return self._oleobj_.InvokeTypes(202, LCID, 2, (11, 0), ((2, 1),),GroupNum
			)

	# The method IsReachable is actually a property, but must be used as a method to correctly pass the arguments
	def IsReachable(self, From=defaultNamedNotOptArg, MoType=6, OrientType=2, Destination=defaultNamedNotOptArg
			, MotionErrorInfo=0):
		'\x0bReturns a Boolean indicating if the robot can reach the position or not.'
		return self._ApplyTypes_(256, 2, (11, 0), ((12, 17), (3, 49), (3, 49), (12, 17), (16397, 50)), 'IsReachable', None,From
			, MoType, OrientType, Destination, MotionErrorInfo)

	def Moveto(self):
		'\x0bMoves the robot to this position for all groups defined on the controller.'
		return self._oleobj_.InvokeTypes(251, LCID, 1, (24, 0), (),)

	def Record(self):
		'\x0bRecords the current position of the robot to this position for all groups defined on the controller.'
		return self._oleobj_.InvokeTypes(252, LCID, 1, (24, 0), (),)

	def Refresh(self):
		'\x0bReads fresh values for a position register, tool frame, user frame, or jog frame from the robot.'
		return self._oleobj_.InvokeTypes(254, LCID, 1, (24, 0), (),)

	def Uninitialize(self):
		'\x0bUninitializes the position for all groups defined on the controller. '
		return self._oleobj_.InvokeTypes(253, LCID, 1, (24, 0), (),)

	def Update(self):
		'\x0bSends the local copy of a position register, tool frame, user frame, or jog frame to the robot.'
		return self._oleobj_.InvokeTypes(255, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"GroupBitMask": (258, 2, (3, 0), (), "GroupBitMask", None),
		"Id": (201, 2, (3, 0), (), "Id", None),
		"IsAtCurPosition": (204, 2, (11, 0), (), "IsAtCurPosition", None),
		"IsInitialized": (205, 2, (11, 0), (), "IsInitialized", None),
		# Method 'Robot' returns object of type 'FRCRobot'
		"Robot": (1, 2, (13, 0), (), "Robot", '{6D7E3A01-9ECC-11D0-94D5-0020AF68F0A3}'),
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

class ISysPositionEvents:
	CLSID = CLSID_Sink = IID('{3AC7EA79-381C-11D1-B6FE-00C04FB9E76B}')
	coclass_clsid = IID('{6055D699-FFAE-11D0-B6F4-00C04FB9C401}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        1 : "OnChange",
		        2 : "OnCommentChange",
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
#	def OnChange(self, GroupNum=defaultNamedNotOptArg):
#		'\x0bOccurs when the position is changed, GroupNum specifies which group was changed.'
#	def OnCommentChange(self, GroupNum=defaultNamedNotOptArg):
#		'\x0bOccurs when a position’s comment is changed, GroupNum specifies which group was changed.'


class ISysPositions(DispatchBaseClass):
	'\x0bProvides access to a collection of controller system positions.'
	CLSID = IID('{6055D69A-FFAE-11D0-B6F4-00C04FB9C401}')
	coclass_clsid = IID('{6055D69B-FFAE-11D0-B6F4-00C04FB9C401}')

	# Result is of type FRCSysPosition
	# The method GetItem is actually a property, but must be used as a method to correctly pass the arguments
	def GetItem(self, Id=defaultNamedOptArg, Index=defaultNamedOptArg):
		'\x0bReturns a position from the collection. '
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (13, 0), ((12, 17), (12, 17)),Id
			, Index)
		if ret is not None:
			# See if this IUnknown is really an IDispatch
			try:
				ret = ret.QueryInterface(pythoncom.IID_IDispatch)
			except pythoncom.error:
				return ret
			ret = Dispatch(ret, 'GetItem', '{6055D699-FFAE-11D0-B6F4-00C04FB9C401}')
		return ret

	def Refresh(self):
		'\x0bReads fresh values for all position registers, tool frames, user frames, or jog frames from the robot.'
		return self._oleobj_.InvokeTypes(203, LCID, 1, (24, 0), (),)

	# The method Selected is actually a property, but must be used as a method to correctly pass the arguments
	def Selected(self, GroupNum=defaultNamedNotOptArg):
		'\x0bReturns/sets the selected “active” frame.'
		return self._oleobj_.InvokeTypes(202, LCID, 2, (3, 0), ((2, 1),),GroupNum
			)

	# The method SetSelected is actually a property, but must be used as a method to correctly pass the arguments
	def SetSelected(self, GroupNum=defaultNamedNotOptArg, arg1=defaultUnnamedArg):
		'\x0bReturns/sets the selected “active” frame.'
		return self._oleobj_.InvokeTypes(202, LCID, 4, (24, 0), ((2, 1), (3, 1)),GroupNum
			, arg1)

	def Update(self):
		'\x0bSends the local copy of the position registers, tool frames, user frames, or jog frames to the robot.'
		return self._oleobj_.InvokeTypes(204, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"Count": (201, 2, (3, 0), (), "Count", None),
		# Method 'Item' returns object of type 'FRCSysPosition'
		"Item": (0, 2, (13, 0), ((12, 17), (12, 17)), "Item", '{6055D699-FFAE-11D0-B6F4-00C04FB9C401}'),
		# Method 'Robot' returns object of type 'FRCRobot'
		"Robot": (1, 2, (13, 0), (), "Robot", '{6D7E3A01-9ECC-11D0-94D5-0020AF68F0A3}'),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Id=defaultNamedOptArg, Index=defaultNamedOptArg):
		'\x0bReturns a position from the collection. '
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (13, 0), ((12, 17), (12, 17)),Id
			, Index)
		if ret is not None:
			# See if this IUnknown is really an IDispatch
			try:
				ret = ret.QueryInterface(pythoncom.IID_IDispatch)
			except pythoncom.error:
				return ret
			ret = Dispatch(ret, '__call__', '{6055D699-FFAE-11D0-B6F4-00C04FB9C401}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(201, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ISysPositionsEvents:
	CLSID = CLSID_Sink = IID('{94F57CE7-381B-11D1-B6FE-00C04FB9E76B}')
	coclass_clsid = IID('{6055D69B-FFAE-11D0-B6F4-00C04FB9C401}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        1 : "OnChange",
		        2 : "OnCommentChange",
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
#	def OnChange(self, Id=defaultNamedNotOptArg, GroupNum=defaultNamedNotOptArg):
#		'\x0bOccurs when a position is changed, Id and GroupNum specifies which position was changed.'
#	def OnCommentChange(self, Id=defaultNamedNotOptArg, GroupNum=defaultNamedNotOptArg):
#		'\x0bOccurs when a position’s comment is changed, Id and GroupNum specifies which position was changed.'


class ISystemIOType(DispatchBaseClass):
	'\x0bThis object is used to access both I/O signal and I/O configuration collections.'
	CLSID = IID('{59DC16F2-AF91-11D0-A072-00A02436CF7E}')
	coclass_clsid = IID('{1C9FC454-C455-4A41-80EF-0894FEB07BF8}')

	_prop_map_get_ = {
		"CanComplement": (208, 2, (11, 0), (), "CanComplement", None),
		"CanConfigure": (205, 2, (11, 0), (), "CanConfigure", None),
		"CanInvert": (207, 2, (11, 0), (), "CanInvert", None),
		"CanSimulate": (206, 2, (11, 0), (), "CanSimulate", None),
		"IsBoolean": (204, 2, (11, 0), (), "IsBoolean", None),
		"IsInput": (203, 2, (11, 0), (), "IsInput", None),
		"Name": (201, 2, (8, 0), (), "Name", None),
		# Method 'Parent' returns object of type 'FRCIOTypes'
		"Parent": (102, 2, (13, 0), (), "Parent", '{59DC16ED-AF91-11D0-A072-00A02436CF7E}'),
		# Method 'Robot' returns object of type 'FRCRobot'
		"Robot": (1, 2, (13, 0), (), "Robot", '{6D7E3A01-9ECC-11D0-94D5-0020AF68F0A3}'),
		# Method 'Signals' returns object of type 'FRCIOSignals'
		"Signals": (202, 2, (13, 0), (), "Signals", '{59DC16F8-AF91-11D0-A072-00A02436CF7E}'),
		"Type": (101, 2, (2, 0), (), "Type", None),
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

class ITPApplDataCollection(DispatchBaseClass):
	CLSID = IID('{A7E095A2-DCDE-11D0-A083-00A02436CF7E}')
	coclass_clsid = IID('{70F06EE1-DCE0-11D0-A083-00A02436CF7E}')

	def Add(self, Name=defaultNamedNotOptArg, Index1=defaultNamedOptArg, Index2=defaultNamedOptArg):
		ret = self._oleobj_.InvokeTypes(251, LCID, 1, (9, 0), ((8, 1), (12, 17), (12, 17)),Name
			, Index1, Index2)
		if ret is not None:
			ret = Dispatch(ret, 'Add', None)
		return ret

	# The method GetItem is actually a property, but must be used as a method to correctly pass the arguments
	def GetItem(self, Name=defaultNamedOptArg, Index1=defaultNamedOptArg, Index2=defaultNamedOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 17), (12, 17), (12, 17)),Name
			, Index1, Index2)
		if ret is not None:
			ret = Dispatch(ret, 'GetItem', None)
		return ret

	def Remove(self, Name=defaultNamedOptArg, Index1=defaultNamedOptArg, Index2=defaultNamedOptArg):
		return self._oleobj_.InvokeTypes(252, LCID, 1, (24, 0), ((12, 17), (12, 17), (12, 17)),Name
			, Index1, Index2)

	_prop_map_get_ = {
		"Count": (201, 2, (3, 0), (), "Count", None),
		"Item": (0, 2, (9, 0), ((12, 17), (12, 17), (12, 17)), "Item", None),
		# Method 'Program' returns object of type 'FRCProgram'
		"Program": (101, 2, (13, 0), (), "Program", '{D42AB5D5-8FFB-11D0-94CC-0020AF68F0A3}'),
		# Method 'Robot' returns object of type 'FRCRobot'
		"Robot": (1, 2, (13, 0), (), "Robot", '{6D7E3A01-9ECC-11D0-94D5-0020AF68F0A3}'),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Name=defaultNamedOptArg, Index1=defaultNamedOptArg, Index2=defaultNamedOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 17), (12, 17), (12, 17)),Name
			, Index1, Index2)
		if ret is not None:
			ret = Dispatch(ret, '__call__', None)
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(201, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ITPApplDataCollectionEvents:
	CLSID = CLSID_Sink = IID('{A7E095A1-DCDE-11D0-A083-00A02436CF7E}')
	coclass_clsid = IID('{70F06EE1-DCE0-11D0-A083-00A02436CF7E}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        1 : "OnCreate",
		        2 : "OnChange",
		        3 : "OnDelete",
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
#	def OnCreate(self, ApplData=defaultNamedNotOptArg):
#	def OnChange(self, ApplData=defaultNamedNotOptArg):
#	def OnDelete(self, ApplData=defaultNamedNotOptArg):


class ITPApplDataEvents:
	CLSID = CLSID_Sink = IID('{9728B471-DCE0-11D0-A083-00A02436CF7E}')
	coclass_clsid = IID('{51FF0460-DCE1-11D0-A083-00A02436CF7E}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        1 : "OnChange",
		        2 : "OnDelete",
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
#	def OnChange(self):
#	def OnDelete(self):


class ITPApplDataHelper(DispatchBaseClass):
	CLSID = IID('{343D8EB1-DCE1-11D0-A083-00A02436CF7E}')
	coclass_clsid = IID('{51FF0460-DCE1-11D0-A083-00A02436CF7E}')

	def ApplDataChanged(self):
		return self._oleobj_.InvokeTypes(251, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"Index1": (202, 2, (3, 0), (), "Index1", None),
		"Index2": (203, 2, (3, 0), (), "Index2", None),
		"Name": (201, 2, (8, 0), (), "Name", None),
		# Method 'Program' returns object of type 'FRCProgram'
		"Program": (101, 2, (13, 0), (), "Program", '{D42AB5D5-8FFB-11D0-94CC-0020AF68F0A3}'),
		# Method 'Robot' returns object of type 'FRCRobot'
		"Robot": (1, 2, (13, 0), (), "Robot", '{6D7E3A01-9ECC-11D0-94D5-0020AF68F0A3}'),
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

class ITPInstruction(DispatchBaseClass):
	CLSID = IID('{3C05D26F-9BE8-11D1-B6FC-00C04FA3BD85}')
	coclass_clsid = IID('{3C05D270-9BE8-11D1-B6FC-00C04FA3BD85}')

	_prop_map_get_ = {
		"Caption": (105, 2, (8, 0), (), "Caption", None),
		"EditProgID": (107, 2, (8, 0), (), "EditProgID", None),
		"IsMotionAppend": (109, 2, (11, 0), (), "IsMotionAppend", None),
		"LMCode": (101, 2, (2, 0), (), "LMCode", None),
		"LinesProgID": (106, 2, (8, 0), (), "LinesProgID", None),
		"OptionID1": (102, 2, (2, 0), (), "OptionID1", None),
		"OptionID2": (103, 2, (2, 0), (), "OptionID2", None),
		"OptionID3": (104, 2, (2, 0), (), "OptionID3", None),
		"PictureName": (108, 2, (8, 0), (), "PictureName", None),
		# Method 'Robot' returns object of type 'FRCRobot'
		"Robot": (1, 2, (13, 0), (), "Robot", '{6D7E3A01-9ECC-11D0-94D5-0020AF68F0A3}'),
	}
	_prop_map_put_ = {
		"Caption": ((105, LCID, 4, 0),()),
		"EditProgID": ((107, LCID, 4, 0),()),
		"IsMotionAppend": ((109, LCID, 4, 0),()),
		"LinesProgID": ((106, LCID, 4, 0),()),
		"PictureName": ((108, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ITPInstructions(DispatchBaseClass):
	CLSID = IID('{3C05D26D-9BE8-11D1-B6FC-00C04FA3BD85}')
	coclass_clsid = IID('{3C05D26E-9BE8-11D1-B6FC-00C04FA3BD85}')

	# Result is of type FRCTPInstruction
	def Add(self, LMCode=defaultNamedNotOptArg, OptParam1=defaultNamedNotOptArg, OptParam2=defaultNamedNotOptArg, OptParam3=defaultNamedNotOptArg
			, Caption=defaultNamedNotOptArg, LinesProgID=defaultNamedNotOptArg, EditProgID=defaultNamedNotOptArg, PictureName=defaultNamedNotOptArg, IsMotionAppend=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(150, LCID, 1, (13, 0), ((2, 1), (12, 17), (12, 17), (12, 17), (8, 1), (8, 1), (8, 1), (8, 1), (11, 1)),LMCode
			, OptParam1, OptParam2, OptParam3, Caption, LinesProgID
			, EditProgID, PictureName, IsMotionAppend)
		if ret is not None:
			# See if this IUnknown is really an IDispatch
			try:
				ret = ret.QueryInterface(pythoncom.IID_IDispatch)
			except pythoncom.error:
				return ret
			ret = Dispatch(ret, 'Add', '{3C05D270-9BE8-11D1-B6FC-00C04FA3BD85}')
		return ret

	# Result is of type FRCTPInstruction
	# The method GetItem is actually a property, but must be used as a method to correctly pass the arguments
	def GetItem(self, LMCode=defaultNamedOptArg, Index=defaultNamedOptArg, OptParam1=defaultNamedOptArg, OptParam2=defaultNamedOptArg
			, OptParam3=defaultNamedOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (13, 0), ((12, 17), (12, 17), (12, 17), (12, 17), (12, 17)),LMCode
			, Index, OptParam1, OptParam2, OptParam3)
		if ret is not None:
			# See if this IUnknown is really an IDispatch
			try:
				ret = ret.QueryInterface(pythoncom.IID_IDispatch)
			except pythoncom.error:
				return ret
			ret = Dispatch(ret, 'GetItem', '{3C05D270-9BE8-11D1-B6FC-00C04FA3BD85}')
		return ret

	# The method IsValid is actually a property, but must be used as a method to correctly pass the arguments
	def IsValid(self, LMCode=defaultNamedNotOptArg, OptParam1=defaultNamedOptArg, OptParam2=defaultNamedOptArg, OptParam3=defaultNamedOptArg):
		return self._oleobj_.InvokeTypes(102, LCID, 2, (11, 0), ((2, 1), (12, 17), (12, 17), (12, 17)),LMCode
			, OptParam1, OptParam2, OptParam3)

	def Remove(self, LMCode=defaultNamedNotOptArg, OptParam1=defaultNamedOptArg, OptParam2=defaultNamedOptArg, OptParam3=defaultNamedOptArg):
		return self._oleobj_.InvokeTypes(151, LCID, 1, (24, 0), ((2, 1), (12, 17), (12, 17), (12, 17)),LMCode
			, OptParam1, OptParam2, OptParam3)

	_prop_map_get_ = {
		"Count": (101, 2, (3, 0), (), "Count", None),
		# Method 'Item' returns object of type 'FRCTPInstruction'
		"Item": (0, 2, (13, 0), ((12, 17), (12, 17), (12, 17), (12, 17), (12, 17)), "Item", '{3C05D270-9BE8-11D1-B6FC-00C04FA3BD85}'),
		# Method 'Robot' returns object of type 'FRCRobot'
		"Robot": (1, 2, (13, 0), (), "Robot", '{6D7E3A01-9ECC-11D0-94D5-0020AF68F0A3}'),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, LMCode=defaultNamedOptArg, Index=defaultNamedOptArg, OptParam1=defaultNamedOptArg, OptParam2=defaultNamedOptArg
			, OptParam3=defaultNamedOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (13, 0), ((12, 17), (12, 17), (12, 17), (12, 17), (12, 17)),LMCode
			, Index, OptParam1, OptParam2, OptParam3)
		if ret is not None:
			# See if this IUnknown is really an IDispatch
			try:
				ret = ret.QueryInterface(pythoncom.IID_IDispatch)
			except pythoncom.error:
				return ret
			ret = Dispatch(ret, '__call__', '{3C05D270-9BE8-11D1-B6FC-00C04FA3BD85}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(101, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ITPLabel(DispatchBaseClass):
	CLSID = IID('{C3FB0D02-58D6-11D0-8901-0020AF68F0A3}')
	coclass_clsid = IID('{C3FB0D03-58D6-11D0-8901-0020AF68F0A3}')

	_prop_map_get_ = {
		"Id": (201, 2, (3, 0), (), "Id", None),
		"Line": (202, 2, (9, 0), (), "Line", None),
		# Method 'Program' returns object of type 'FRCProgram'
		"Program": (101, 2, (13, 0), (), "Program", '{D42AB5D5-8FFB-11D0-94CC-0020AF68F0A3}'),
		# Method 'Robot' returns object of type 'FRCRobot'
		"Robot": (1, 2, (13, 0), (), "Robot", '{6D7E3A01-9ECC-11D0-94D5-0020AF68F0A3}'),
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

class ITPLabelEvents:
	CLSID = CLSID_Sink = IID('{D81C9351-DCDB-11D0-A083-00A02436CF7E}')
	coclass_clsid = IID('{C3FB0D03-58D6-11D0-8901-0020AF68F0A3}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        1 : "OnChange",
		        2 : "OnDelete",
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
#	def OnChange(self):
#	def OnDelete(self):


class ITPLabels(DispatchBaseClass):
	CLSID = IID('{C3FB0D00-58D6-11D0-8901-0020AF68F0A3}')
	coclass_clsid = IID('{C3FB0D01-58D6-11D0-8901-0020AF68F0A3}')

	# Result is of type FRCTPLabel
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, LabelID=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (13, 0), ((3, 1),),LabelID
			)
		if ret is not None:
			# See if this IUnknown is really an IDispatch
			try:
				ret = ret.QueryInterface(pythoncom.IID_IDispatch)
			except pythoncom.error:
				return ret
			ret = Dispatch(ret, 'Item', '{C3FB0D03-58D6-11D0-8901-0020AF68F0A3}')
		return ret

	_prop_map_get_ = {
		"Count": (201, 2, (3, 0), (), "Count", None),
		# Method 'Program' returns object of type 'FRCProgram'
		"Program": (101, 2, (13, 0), (), "Program", '{D42AB5D5-8FFB-11D0-94CC-0020AF68F0A3}'),
		# Method 'Robot' returns object of type 'FRCRobot'
		"Robot": (1, 2, (13, 0), (), "Robot", '{6D7E3A01-9ECC-11D0-94D5-0020AF68F0A3}'),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, LabelID=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (13, 0), ((3, 1),),LabelID
			)
		if ret is not None:
			# See if this IUnknown is really an IDispatch
			try:
				ret = ret.QueryInterface(pythoncom.IID_IDispatch)
			except pythoncom.error:
				return ret
			ret = Dispatch(ret, '__call__', '{C3FB0D03-58D6-11D0-8901-0020AF68F0A3}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{C3FB0D03-58D6-11D0-8901-0020AF68F0A3}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(201, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ITPLabelsEvents:
	CLSID = CLSID_Sink = IID('{90E827A1-DCDB-11D0-A083-00A02436CF7E}')
	coclass_clsid = IID('{C3FB0D01-58D6-11D0-8901-0020AF68F0A3}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        1 : "OnCreate",
		        2 : "OnChange",
		        3 : "OnDelete",
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
#	def OnCreate(self, Label=defaultNamedNotOptArg):
#	def OnChange(self, Label=defaultNamedNotOptArg):
#	def OnDelete(self, Label=defaultNamedNotOptArg):


class ITPLineEvents:
	CLSID = CLSID_Sink = IID('{0277AC51-DCDB-11D0-A083-00A02436CF7E}')
	coclass_clsid = IID('{FC761641-4CEA-11D0-8901-0020AF68F0A3}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        1 : "OnChange",
		        2 : "OnDelete",
		        3 : "OnReplace",
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
#	def OnChange(self):
#	def OnDelete(self):
#	def OnReplace(self):


class ITPLineHelper(DispatchBaseClass):
	CLSID = IID('{FC761640-4CEA-11D0-8901-0020AF68F0A3}')
	coclass_clsid = IID('{FC761641-4CEA-11D0-8901-0020AF68F0A3}')

	def LineChanged(self):
		return self._oleobj_.InvokeTypes(251, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"Number": (201, 2, (3, 0), (), "Number", None),
		# Method 'Program' returns object of type 'FRCProgram'
		"Program": (101, 2, (13, 0), (), "Program", '{D42AB5D5-8FFB-11D0-94CC-0020AF68F0A3}'),
		# Method 'Robot' returns object of type 'FRCRobot'
		"Robot": (1, 2, (13, 0), (), "Robot", '{6D7E3A01-9ECC-11D0-94D5-0020AF68F0A3}'),
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

class ITPLines(DispatchBaseClass):
	CLSID = IID('{F5C31106-46AE-11D0-8901-0020AF68F0A3}')
	coclass_clsid = IID('{F5C31107-46AE-11D0-8901-0020AF68F0A3}')

	def Add(self, MnCode=defaultNamedNotOptArg, InsertLine=defaultNamedNotOptArg, OptParam1=defaultNamedOptArg, OptParam2=defaultNamedOptArg
			, OptParam3=defaultNamedOptArg):
		ret = self._oleobj_.InvokeTypes(252, LCID, 1, (9, 0), ((2, 1), (3, 1), (12, 17), (12, 17), (12, 17)),MnCode
			, InsertLine, OptParam1, OptParam2, OptParam3)
		if ret is not None:
			ret = Dispatch(ret, 'Add', None)
		return ret

	def InsertText(self, TextLines=defaultNamedNotOptArg, LineNum=defaultNamedNotOptArg, InsertMode=defaultNamedOptArg):
		return self._oleobj_.InvokeTypes(253, LCID, 1, (24, 0), ((24584, 1), (3, 1), (12, 17)),TextLines
			, LineNum, InsertMode)

	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, LineNum=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),LineNum
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', None)
		return ret

	def Remove(self, LineNum=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(251, LCID, 1, (24, 0), ((3, 1),),LineNum
			)

	_prop_map_get_ = {
		"Count": (201, 2, (3, 0), (), "Count", None),
		"CurLineNum": (202, 2, (3, 0), (), "CurLineNum", None),
		"FullText": (204, 2, (8, 0), (), "FullText", None),
		# Method 'Program' returns object of type 'FRCProgram'
		"Program": (101, 2, (13, 0), (), "Program", '{D42AB5D5-8FFB-11D0-94CC-0020AF68F0A3}'),
		# Method 'Robot' returns object of type 'FRCRobot'
		"Robot": (1, 2, (13, 0), (), "Robot", '{6D7E3A01-9ECC-11D0-94D5-0020AF68F0A3}'),
		# Method 'SelectedLines' returns object of type 'FRCSelectedLines'
		"SelectedLines": (203, 2, (13, 0), (), "SelectedLines", '{58ADC520-9395-11D2-877C-00C04FB9C401}'),
	}
	_prop_map_put_ = {
		"CurLineNum": ((202, LCID, 4, 0),()),
	}
	# Default method for this class is 'Item'
	def __call__(self, LineNum=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),LineNum
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', None)
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(201, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ITPLinesEvents:
	CLSID = CLSID_Sink = IID('{2D9F8871-DCDA-11D0-A083-00A02436CF7E}')
	coclass_clsid = IID('{F5C31107-46AE-11D0-8901-0020AF68F0A3}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        1 : "OnCurChange",
		        2 : "OnCreate",
		        3 : "OnChange",
		        4 : "OnDelete",
		        5 : "OnReplace",
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
#	def OnCurChange(self):
#	def OnCreate(self, LineNum=defaultNamedNotOptArg):
#	def OnChange(self, LineNum=defaultNamedNotOptArg):
#	def OnDelete(self, LineNum=defaultNamedNotOptArg):
#	def OnReplace(self, LineNum=defaultNamedNotOptArg):


class ITPPosition(DispatchBaseClass):
	'\x0bProvides access to a single position in a TP program.'
	CLSID = IID('{3A49BE60-F5B9-11CF-8901-0020AF68F0A3}')
	coclass_clsid = IID('{3A49BE61-F5B9-11CF-8901-0020AF68F0A3}')

	def CheckReach(self, From=defaultNamedNotOptArg, MoType=6, OrientType=2, Destination=defaultNamedNotOptArg
			, MotionErrorInfo=0):
		'\x0bReturns a Boolean indicating if the robot can reach the position or not.'
		return self._ApplyTypes_(260, 1, (11, 0), ((12, 17), (3, 49), (3, 49), (12, 17), (16397, 50)), 'CheckReach', None,From
			, MoType, OrientType, Destination, MotionErrorInfo)

	def Copy(self, Position=defaultNamedNotOptArg):
		'\x0bCopies the positional data from another object into this one.'
		return self._oleobj_.InvokeTypes(257, LCID, 1, (24, 0), ((9, 1),),Position
			)

	# Result is of type FRCGroupPosition
	# The method Group is actually a property, but must be used as a method to correctly pass the arguments
	def Group(self, GroupNum=defaultNamedNotOptArg):
		'\x0bReturns a FRCGroupPosition object representing the TP position in the specified motion group.'
		ret = self._oleobj_.InvokeTypes(204, LCID, 2, (13, 0), ((2, 1),),GroupNum
			)
		if ret is not None:
			# See if this IUnknown is really an IDispatch
			try:
				ret = ret.QueryInterface(pythoncom.IID_IDispatch)
			except pythoncom.error:
				return ret
			ret = Dispatch(ret, 'Group', '{A47A5881-056D-11D0-8901-0020AF68F0A3}')
		return ret

	# The method GroupMask is actually a property, but must be used as a method to correctly pass the arguments
	def GroupMask(self, GroupNum=defaultNamedNotOptArg):
		'\x0bReturns whether the particular motion group is defined for the TP position.'
		return self._oleobj_.InvokeTypes(203, LCID, 2, (11, 0), ((2, 1),),GroupNum
			)

	# The method IsReachable is actually a property, but must be used as a method to correctly pass the arguments
	def IsReachable(self, From=defaultNamedNotOptArg, MoType=6, OrientType=2, Destination=defaultNamedNotOptArg
			, MotionErrorInfo=0):
		'\x0bReturns a Boolean indicating if the robot can reach the position or not.'
		return self._ApplyTypes_(256, 2, (11, 0), ((12, 17), (3, 49), (3, 49), (12, 17), (16397, 50)), 'IsReachable', None,From
			, MoType, OrientType, Destination, MotionErrorInfo)

	def Moveto(self):
		'\x0bMoves the robot to this position for all groups defined for the TP position.'
		return self._oleobj_.InvokeTypes(251, LCID, 1, (24, 0), (),)

	def Record(self):
		'\x0bRecords the current position of the robot to this position for all groups defined for the TP position.'
		return self._oleobj_.InvokeTypes(252, LCID, 1, (24, 0), (),)

	def Refresh(self):
		'\x0bReads fresh values for a TP position from the robot.'
		return self._oleobj_.InvokeTypes(254, LCID, 1, (24, 0), (),)

	def Uninitialize(self):
		'\x0bUninitializes the position for all groups defined for the TP position. '
		return self._oleobj_.InvokeTypes(253, LCID, 1, (24, 0), (),)

	def Update(self):
		'\x0bSends the local copy of a TP position to the robot.'
		return self._oleobj_.InvokeTypes(255, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"Binary": (207, 2, (12, 0), (), "Binary", None),
		"Comment": (201, 2, (8, 0), (), "Comment", None),
		# Method 'FirstExistGroup' returns object of type 'FRCXyzWpr'
		"FirstExistGroup": (259, 2, (13, 0), (), "FirstExistGroup", '{A47A5885-056D-11D0-8901-0020AF68F0A3}'),
		"GroupBitMask": (258, 2, (3, 0), (), "GroupBitMask", None),
		"Id": (202, 2, (3, 0), (), "Id", None),
		"IsAtCurPosition": (205, 2, (11, 0), (), "IsAtCurPosition", None),
		"IsInitialized": (208, 2, (11, 0), (), "IsInitialized", None),
		# Method 'Program' returns object of type 'FRCProgram'
		"Program": (101, 2, (13, 0), (), "Program", '{D42AB5D5-8FFB-11D0-94CC-0020AF68F0A3}'),
		"ReferenceCount": (206, 2, (3, 0), (), "ReferenceCount", None),
		# Method 'Robot' returns object of type 'FRCRobot'
		"Robot": (1, 2, (13, 0), (), "Robot", '{6D7E3A01-9ECC-11D0-94D5-0020AF68F0A3}'),
	}
	_prop_map_put_ = {
		"Binary": ((207, LCID, 4, 0),()),
		"Comment": ((201, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ITPPositionEvents:
	CLSID = CLSID_Sink = IID('{21CB68D1-DCDE-11D0-A083-00A02436CF7E}')
	coclass_clsid = IID('{3A49BE61-F5B9-11CF-8901-0020AF68F0A3}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        1 : "OnChange",
		        2 : "OnDelete",
		        3 : "OnRenumber",
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
#	def OnChange(self, GroupNum=defaultNamedNotOptArg):
#		'\x0bOccurs after a TP position is changed.'
#	def OnDelete(self):
#		'\x0bOccurs before a TP position is deleted.'
#	def OnRenumber(self):
#		'\x0bOccurs after a TP position is renumbered.'


class ITPPositions(DispatchBaseClass):
	'\x0bProvides access to the collection of positions in a TP program. '
	CLSID = IID('{A16AD1C6-F45A-11CF-8901-0020AF68F0A3}')
	coclass_clsid = IID('{A16AD1C7-F45A-11CF-8901-0020AF68F0A3}')

	def GetGroupXyzWprByIndex(self, GroupNum=defaultNamedNotOptArg, Index=defaultNamedNotOptArg, X=pythoncom.Missing, Y=pythoncom.Missing
			, Z=pythoncom.Missing, W=pythoncom.Missing, P=pythoncom.Missing, R=pythoncom.Missing):
		'\x0bReturns a TP position from the collection. '
		return self._ApplyTypes_(203, 1, (11, 0), ((2, 1), (3, 1), (16389, 2), (16389, 2), (16389, 2), (16389, 2), (16389, 2), (16389, 2)), 'GetGroupXyzWprByIndex', None,GroupNum
			, Index, X, Y, Z, W
			, P, R)

	# Result is of type FRCTPPosition
	# The method GetItem is actually a property, but must be used as a method to correctly pass the arguments
	def GetItem(self, Id=defaultNamedOptArg, Index=defaultNamedOptArg):
		'\x0bReturns a TP position from the collection. '
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (13, 0), ((12, 17), (12, 17)),Id
			, Index)
		if ret is not None:
			# See if this IUnknown is really an IDispatch
			try:
				ret = ret.QueryInterface(pythoncom.IID_IDispatch)
			except pythoncom.error:
				return ret
			ret = Dispatch(ret, 'GetItem', '{3A49BE61-F5B9-11CF-8901-0020AF68F0A3}')
		return ret

	def RenumberAll(self):
		return self._oleobj_.InvokeTypes(251, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"Count": (201, 2, (3, 0), (), "Count", None),
		# Method 'Item' returns object of type 'FRCTPPosition'
		"Item": (0, 2, (13, 0), ((12, 17), (12, 17)), "Item", '{3A49BE61-F5B9-11CF-8901-0020AF68F0A3}'),
		"NewPosID": (202, 2, (3, 0), (), "NewPosID", None),
		# Method 'Program' returns object of type 'FRCProgram'
		"Program": (101, 2, (13, 0), (), "Program", '{D42AB5D5-8FFB-11D0-94CC-0020AF68F0A3}'),
		# Method 'Robot' returns object of type 'FRCRobot'
		"Robot": (1, 2, (13, 0), (), "Robot", '{6D7E3A01-9ECC-11D0-94D5-0020AF68F0A3}'),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Id=defaultNamedOptArg, Index=defaultNamedOptArg):
		'\x0bReturns a TP position from the collection. '
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (13, 0), ((12, 17), (12, 17)),Id
			, Index)
		if ret is not None:
			# See if this IUnknown is really an IDispatch
			try:
				ret = ret.QueryInterface(pythoncom.IID_IDispatch)
			except pythoncom.error:
				return ret
			ret = Dispatch(ret, '__call__', '{3A49BE61-F5B9-11CF-8901-0020AF68F0A3}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(201, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ITPPositionsEvents:
	CLSID = CLSID_Sink = IID('{10CB2FD0-DCDC-11D0-A083-00A02436CF7E}')
	coclass_clsid = IID('{A16AD1C7-F45A-11CF-8901-0020AF68F0A3}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        1 : "OnCreate",
		        2 : "OnChange",
		        3 : "OnDelete",
		        4 : "OnRenumber",
		        5 : "OnBeginRenumberAll",
		        6 : "OnEndRenumberAll",
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
#	def OnCreate(self, Position=defaultNamedNotOptArg):
#		'\x0bOccurs after a TP position is created.'
#	def OnChange(self, Position=defaultNamedNotOptArg, GroupNum=defaultNamedNotOptArg):
#		'\x0bOccurs after a TP position is changed, Position specifies which position was changed.'
#	def OnDelete(self, Position=defaultNamedNotOptArg):
#		'\x0bOccurs before a TP position is deleted.'
#	def OnRenumber(self, Position=defaultNamedNotOptArg):
#		'\x0bOccurs after a TP position is renumbered.'
#	def OnBeginRenumberAll(self):
#		'\x0bOccurs before RenumberAll is started.'
#	def OnEndRenumberAll(self):
#		'\x0bOccurs after RenumberAll is done.'


class ITPProgram(DispatchBaseClass):
	'\x0bRepresents a TP program on the robot controller.'
	CLSID = IID('{D42AB5D3-8FFB-11D0-94CC-0020AF68F0A3}')
	coclass_clsid = IID('{F5C31101-46AE-11D0-8901-0020AF68F0A3}')

	def Close(self):
		'\x0bClose program.'
		return self._oleobj_.InvokeTypes(253, LCID, 1, (24, 0), (),)

	# The method DefaultGroup is actually a property, but must be used as a method to correctly pass the arguments
	def DefaultGroup(self, GroupNumber=defaultNamedNotOptArg):
		'\x0bReturns/sets the group numbers for the program.  True if the motion group is used.'
		return self._oleobj_.InvokeTypes(116, LCID, 2, (11, 0), ((2, 1),),GroupNumber
			)

	def EditLine(self, LineNum=defaultNamedNotOptArg, ColNum=defaultNamedOptArg):
		'\x0bSelects a line for editing by internal editor.'
		return self._oleobj_.InvokeTypes(254, LCID, 1, (24, 0), ((3, 1), (12, 17)),LineNum
			, ColNum)

	# The method IgnoreAbort is actually a property, but must be used as a method to correctly pass the arguments
	def IgnoreAbort(self, IgnoreConstant=defaultNamedNotOptArg):
		'\x0bReturns/sets the state of the IgnoreAbort attribute.'
		return self._oleobj_.InvokeTypes(117, LCID, 2, (11, 0), ((3, 1),),IgnoreConstant
			)

	# The method IgnorePause is actually a property, but must be used as a method to correctly pass the arguments
	def IgnorePause(self, IgnoreConstant=defaultNamedNotOptArg):
		'\x0bReturns/sets the state of the IgnorePause attribute. '
		return self._oleobj_.InvokeTypes(118, LCID, 2, (11, 0), ((3, 1),),IgnoreConstant
			)

	def ReOpen(self, AccessMode=defaultNamedNotOptArg, RejectMode=defaultNamedNotOptArg):
		'\x0bReopens the program with different access or reject mode attributes.'
		return self._oleobj_.InvokeTypes(150, LCID, 1, (24, 0), ((3, 1), (3, 1)),AccessMode
			, RejectMode)

	def Rename(self, NewProgName=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(251, LCID, 1, (24, 0), ((8, 1),),NewProgName
			)

	def Run(self, StepType=defaultNamedOptArg, LineNum=defaultNamedOptArg, Direction=defaultNamedOptArg):
		'\x0bRuns the TP program by creating a task for the program.'
		return self._oleobj_.InvokeTypes(250, LCID, 1, (24, 0), ((12, 17), (12, 17), (12, 17)),StepType
			, LineNum, Direction)

	def Save(self, FileName=defaultNamedNotOptArg, Option=defaultNamedOptArg, SaveClass=defaultNamedOptArg):
		'\x0bSaves the TP program and/or the variables associated with the program from memory to the specified file device.  KAREL program executable statements can not be saved using this mechanism.'
		return self._oleobj_.InvokeTypes(151, LCID, 1, (24, 0), ((8, 1), (12, 17), (12, 17)),FileName
			, Option, SaveClass)

	# The method SetDefaultGroup is actually a property, but must be used as a method to correctly pass the arguments
	def SetDefaultGroup(self, GroupNumber=defaultNamedNotOptArg, arg1=defaultUnnamedArg):
		'\x0bReturns/sets the group numbers for the program.  True if the motion group is used.'
		return self._oleobj_.InvokeTypes(116, LCID, 4, (24, 0), ((2, 1), (11, 1)),GroupNumber
			, arg1)

	# The method SetIgnoreAbort is actually a property, but must be used as a method to correctly pass the arguments
	def SetIgnoreAbort(self, IgnoreConstant=defaultNamedNotOptArg, arg1=defaultUnnamedArg):
		'\x0bReturns/sets the state of the IgnoreAbort attribute.'
		return self._oleobj_.InvokeTypes(117, LCID, 4, (24, 0), ((3, 1), (11, 1)),IgnoreConstant
			, arg1)

	# The method SetIgnorePause is actually a property, but must be used as a method to correctly pass the arguments
	def SetIgnorePause(self, IgnoreConstant=defaultNamedNotOptArg, arg1=defaultUnnamedArg):
		'\x0bReturns/sets the state of the IgnorePause attribute. '
		return self._oleobj_.InvokeTypes(118, LCID, 4, (24, 0), ((3, 1), (11, 1)),IgnoreConstant
			, arg1)

	_prop_map_get_ = {
		"AccessMode": (102, 2, (3, 0), (), "AccessMode", None),
		# Method 'ApplData' returns object of type 'FRCTPApplDataCollection'
		"ApplData": (204, 2, (13, 0), (), "ApplData", '{70F06EE1-DCE0-11D0-A083-00A02436CF7E}'),
		"BusyLampOff": (115, 2, (11, 0), (), "BusyLampOff", None),
		"Comment": (105, 2, (8, 0), (), "Comment", None),
		"Created": (106, 2, (12, 0), (), "Created", None),
		"DefaultGroupBitMask": (252, 2, (3, 0), (), "DefaultGroupBitMask", None),
		"Invisible": (119, 2, (11, 0), (), "Invisible", None),
		# Method 'Labels' returns object of type 'FRCTPLabels'
		"Labels": (205, 2, (13, 0), (), "Labels", '{C3FB0D01-58D6-11D0-8901-0020AF68F0A3}'),
		"LastModified": (107, 2, (12, 0), (), "LastModified", None),
		# Method 'Lines' returns object of type 'FRCTPLines'
		"Lines": (202, 2, (13, 0), (), "Lines", '{F5C31107-46AE-11D0-8901-0020AF68F0A3}'),
		"Name": (0, 2, (8, 0), (), "Name", None),
		"OriginalName": (108, 2, (8, 0), (), "OriginalName", None),
		"Owner": (120, 2, (8, 0), (), "Owner", None),
		# Method 'Parent' returns object of type 'FRCPrograms'
		"Parent": (104, 2, (13, 0), (), "Parent", '{1FBD567D-8F13-11D0-94CB-0020AF68F0A3}'),
		# Method 'Positions' returns object of type 'FRCTPPositions'
		"Positions": (201, 2, (13, 0), (), "Positions", '{A16AD1C7-F45A-11CF-8901-0020AF68F0A3}'),
		"Priority": (113, 2, (3, 0), (), "Priority", None),
		"Protection": (111, 2, (3, 0), (), "Protection", None),
		"RejectMode": (103, 2, (3, 0), (), "RejectMode", None),
		# Method 'Robot' returns object of type 'FRCRobot'
		"Robot": (1, 2, (13, 0), (), "Robot", '{6D7E3A01-9ECC-11D0-94D5-0020AF68F0A3}'),
		"Size": (110, 2, (3, 0), (), "Size", None),
		"StackSize": (112, 2, (3, 0), (), "StackSize", None),
		"StorageType": (255, 2, (3, 0), (), "StorageType", None),
		"SubType": (203, 2, (3, 0), (), "SubType", None),
		"TimeSlice": (114, 2, (3, 0), (), "TimeSlice", None),
		# Method 'Variables' returns object of type 'FRCVars'
		"Variables": (101, 2, (13, 0), (), "Variables", '{88B57BCB-D0CA-11CF-959F-00A024329125}'),
		"Version": (109, 2, (2, 0), (), "Version", None),
	}
	_prop_map_put_ = {
		"BusyLampOff": ((115, LCID, 4, 0),()),
		"Comment": ((105, LCID, 4, 0),()),
		"Invisible": ((119, LCID, 4, 0),()),
		"Owner": ((120, LCID, 4, 0),()),
		"Priority": ((113, LCID, 4, 0),()),
		"Protection": ((111, LCID, 4, 0),()),
		"StackSize": ((112, LCID, 4, 0),()),
		"StorageType": ((255, LCID, 4, 0),()),
		"SubType": ((203, LCID, 4, 0),()),
		"TimeSlice": ((114, LCID, 4, 0),()),
	}
	# Default property for this class is 'Name'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (8, 0), (), "Name", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ITPProgramEvents:
	CLSID = CLSID_Sink = IID('{F96C81C1-DCD9-11D0-A083-00A02436CF7E}')
	coclass_clsid = IID('{F5C31101-46AE-11D0-8901-0020AF68F0A3}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        1 : "OnDelete",
		        2 : "OnAttrChange",
		        3 : "OnRefresh",
		        4 : "OnRefreshVars",
		        5 : "OnRename",
		        6 : "OnSubTypeChange",
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
#	def OnDelete(self):
#		'\x0bOccurs after a program is deleted.'
#	def OnAttrChange(self, Attr=defaultNamedNotOptArg):
#		'\x0bOccurs after an attribute is changed.'
#	def OnRefresh(self):
#		'\x0bOccurs after a TP program is reloaded.'
#	def OnRefreshVars(self):
#		'\x0bOccurs after a program’s variables are reloaded.'
#	def OnRename(self):
#		'\x0bOccurs after a program is renamed.'
#	def OnSubTypeChange(self):
#		'\x0bOccurs after a TP program’s subtype is changed.'


class ITPScreen(DispatchBaseClass):
	CLSID = IID('{DEE5EAE0-E283-11D0-8BB6-0020AF39BE5A}')
	coclass_clsid = IID('{660E6870-E286-11D0-8BB6-0020AF39BE5A}')

	def ForceMenu(self, Softpart=defaultNamedNotOptArg, ScreenID=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(103, LCID, 1, (24, 0), ((3, 1), (3, 1)),Softpart
			, ScreenID)

	def GetCurScreen(self, SoftpartID=pythoncom.Missing, ScreenID=pythoncom.Missing, Title=pythoncom.Missing):
		return self._ApplyTypes_(101, 1, (24, 0), ((16387, 2), (16387, 2), (16392, 2)), 'GetCurScreen', None,SoftpartID
			, ScreenID, Title)

	def SimKeys(self, Keys=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(102, LCID, 1, (24, 0), ((12, 1),),Keys
			)

	def TPLinkExecUrl(self, TPConnID=defaultNamedNotOptArg, Url=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(104, LCID, 1, (24, 0), ((3, 1), (8, 1)),TPConnID
			, Url)

	_prop_map_get_ = {
		# Method 'Robot' returns object of type 'FRCRobot'
		"Robot": (1, 2, (13, 0), (), "Robot", '{6D7E3A01-9ECC-11D0-94D5-0020AF68F0A3}'),
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

class ITPScreenEvents:
	CLSID = CLSID_Sink = IID('{797CEA11-DD7B-11D2-8A28-00105AE42A59}')
	coclass_clsid = IID('{660E6870-E286-11D0-8BB6-0020AF39BE5A}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        1 : "OnKeyDown",
		        2 : "OnKeyUp",
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
#	def OnKeyDown(self, KeyCode=defaultNamedNotOptArg):
#	def OnKeyUp(self, KeyCode=defaultNamedNotOptArg):


class ITPSimpleLine(DispatchBaseClass):
	CLSID = IID('{6C473F21-B5F0-11D2-8781-00C04F98D092}')
	coclass_clsid = IID('{6C473F20-B5F0-11D2-8781-00C04F98D092}')

	def BinGetFloat(self, IndexOfByte=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(207, LCID, 1, (4, 0), ((3, 1),),IndexOfByte
			)

	def BinSetFloat(self, IndexOfByte=defaultNamedNotOptArg, fNewValue=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(208, LCID, 1, (24, 0), ((3, 1), (4, 1)),IndexOfByte
			, fNewValue)

	def BinUpdate(self):
		return self._oleobj_.InvokeTypes(206, LCID, 1, (24, 0), (),)

	def ChangeLine(self, Text=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(209, LCID, 1, (24, 0), ((8, 1),),Text
			)

	_prop_map_get_ = {
		"BinNoUpdate": (205, 2, (11, 0), (), "BinNoUpdate", None),
		"Binary": (201, 2, (12, 0), (), "Binary", None),
		"MnCode": (203, 2, (17, 0), (), "MnCode", None),
		"Number": (202, 2, (3, 0), (), "Number", None),
		# Method 'Program' returns object of type 'FRCProgram'
		"Program": (101, 2, (13, 0), (), "Program", '{D42AB5D5-8FFB-11D0-94CC-0020AF68F0A3}'),
		# Method 'Robot' returns object of type 'FRCRobot'
		"Robot": (1, 2, (13, 0), (), "Robot", '{6D7E3A01-9ECC-11D0-94D5-0020AF68F0A3}'),
		"Text": (204, 2, (8, 0), (), "Text", None),
	}
	_prop_map_put_ = {
		"BinNoUpdate": ((205, LCID, 4, 0),()),
		"Binary": ((201, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ITask(DispatchBaseClass):
	'\x0bThe task object represents a running thread of execution on the controller.  A running task may be running different programs or program routines at various points in time.'
	CLSID = IID('{7745C8FE-4626-11D1-B745-00C04FBBE42A}')
	coclass_clsid = IID('{847A8F82-4626-11D1-B745-00C04FBBE42A}')

	def Abort(self, Force=defaultNamedOptArg, Cancel=defaultNamedOptArg):
		'\x0bAborts the current execution of the task.  '
		return self._oleobj_.InvokeTypes(250, LCID, 1, (24, 0), ((12, 17), (12, 17)),Force
			, Cancel)

	def Continue(self, LineNum=defaultNamedOptArg, Direction=defaultNamedOptArg):
		'\x0bExecutes a task after it has been stopped by the Pause method.'
		return self._oleobj_.InvokeTypes(252, LCID, 1, (24, 0), ((12, 17), (12, 17)),LineNum
			, Direction)

	# The method HoldCondition is actually a property, but must be used as a method to correctly pass the arguments
	def HoldCondition(self, HoldCondition=defaultNamedNotOptArg):
		'\x0bReturns the state of the various hold flags.'
		return self._oleobj_.InvokeTypes(205, LCID, 2, (11, 0), ((3, 1),),HoldCondition
			)

	# The method IgnoreAbort is actually a property, but must be used as a method to correctly pass the arguments
	def IgnoreAbort(self, IgnoreConstant=defaultNamedNotOptArg):
		'\x0bReturns/sets the ignore abort flags for the task.'
		return self._oleobj_.InvokeTypes(206, LCID, 2, (11, 0), ((3, 1),),IgnoreConstant
			)

	# The method IgnorePause is actually a property, but must be used as a method to correctly pass the arguments
	def IgnorePause(self, IgnoreConstant=defaultNamedNotOptArg):
		'\x0bReturns/sets the ignore pause flags for the task.'
		return self._oleobj_.InvokeTypes(207, LCID, 2, (11, 0), ((3, 1),),IgnoreConstant
			)

	# The method LockedArm is actually a property, but must be used as a method to correctly pass the arguments
	def LockedArm(self, GroupNum=defaultNamedNotOptArg):
		'\x0bReturns whether the task has any motion groups locked.'
		return self._oleobj_.InvokeTypes(214, LCID, 2, (11, 0), ((2, 1),),GroupNum
			)

	# The method MotionControl is actually a property, but must be used as a method to correctly pass the arguments
	def MotionControl(self, GroupNum=defaultNamedNotOptArg):
		'\x0bReturns whether the task has motion control of a group.'
		return self._oleobj_.InvokeTypes(215, LCID, 2, (11, 0), ((2, 1),),GroupNum
			)

	def Pause(self, Force=defaultNamedOptArg, Cancel=defaultNamedOptArg):
		'\x0bPauses the task at its current line.  '
		return self._oleobj_.InvokeTypes(251, LCID, 1, (24, 0), ((12, 17), (12, 17)),Force
			, Cancel)

	# The method SetIgnoreAbort is actually a property, but must be used as a method to correctly pass the arguments
	def SetIgnoreAbort(self, IgnoreConstant=defaultNamedNotOptArg, arg1=defaultUnnamedArg):
		'\x0bReturns/sets the ignore abort flags for the task.'
		return self._oleobj_.InvokeTypes(206, LCID, 4, (24, 0), ((3, 1), (11, 1)),IgnoreConstant
			, arg1)

	# The method SetIgnorePause is actually a property, but must be used as a method to correctly pass the arguments
	def SetIgnorePause(self, IgnoreConstant=defaultNamedNotOptArg, arg1=defaultUnnamedArg):
		'\x0bReturns/sets the ignore pause flags for the task.'
		return self._oleobj_.InvokeTypes(207, LCID, 4, (24, 0), ((3, 1), (11, 1)),IgnoreConstant
			, arg1)

	# The method SetSuperMotion is actually a property, but must be used as a method to correctly pass the arguments
	def SetSuperMotion(self, GroupNum=defaultNamedNotOptArg, arg1=defaultUnnamedArg):
		'\x0bReturns/sets whether the task has supervisory motion control of any group.'
		return self._oleobj_.InvokeTypes(225, LCID, 4, (24, 0), ((2, 1), (11, 1)),GroupNum
			, arg1)

	def Skip(self, Number=defaultNamedOptArg):
		'\x0bCauses one or more statements to be skipped.  The next statement to be executed is determined by the current value of the StepType property.'
		return self._oleobj_.InvokeTypes(253, LCID, 1, (24, 0), ((12, 17),),Number
			)

	# The method SuperMotion is actually a property, but must be used as a method to correctly pass the arguments
	def SuperMotion(self, GroupNum=defaultNamedNotOptArg):
		'\x0bReturns/sets whether the task has supervisory motion control of any group.'
		return self._oleobj_.InvokeTypes(225, LCID, 2, (11, 0), ((2, 1),),GroupNum
			)

	_prop_map_get_ = {
		"BusyLampOff": (201, 2, (11, 0), (), "BusyLampOff", None),
		"CurLine": (202, 2, (3, 0), (), "CurLine", None),
		# Method 'CurProgram' returns object of type 'FRCProgram'
		"CurProgram": (203, 2, (13, 0), (), "CurProgram", '{D42AB5D5-8FFB-11D0-94CC-0020AF68F0A3}'),
		"CurRoutine": (204, 2, (8, 0), (), "CurRoutine", None),
		"Invisible": (208, 2, (11, 0), (), "Invisible", None),
		"Name": (216, 2, (8, 0), (), "Name", None),
		"NotCircularMotion": (217, 2, (11, 0), (), "NotCircularMotion", None),
		"NumChild": (218, 2, (2, 0), (), "NumChild", None),
		"NumMMR": (219, 2, (2, 0), (), "NumMMR", None),
		"PauseOnShift": (209, 2, (11, 0), (), "PauseOnShift", None),
		"Priority": (220, 2, (2, 0), (), "Priority", None),
		"ProgramType": (221, 2, (3, 0), (), "ProgramType", None),
		# Method 'Robot' returns object of type 'FRCRobot'
		"Robot": (1, 2, (13, 0), (), "Robot", '{6D7E3A01-9ECC-11D0-94D5-0020AF68F0A3}'),
		"StackSize": (222, 2, (3, 0), (), "StackSize", None),
		"Status": (223, 2, (3, 0), (), "Status", None),
		"StepType": (224, 2, (3, 0), (), "StepType", None),
		"SystemTask": (210, 2, (11, 0), (), "SystemTask", None),
		"TCDStatus": (227, 2, (3, 0), (), "TCDStatus", None),
		"TPMotion": (211, 2, (11, 0), (), "TPMotion", None),
		"TaskNum": (226, 2, (2, 0), (), "TaskNum", None),
		"TimeSlice": (228, 2, (3, 0), (), "TimeSlice", None),
		# Method 'TopProgram' returns object of type 'FRCProgram'
		"TopProgram": (230, 2, (13, 0), (), "TopProgram", '{D42AB5D5-8FFB-11D0-94CC-0020AF68F0A3}'),
		"TraceEnable": (212, 2, (11, 0), (), "TraceEnable", None),
		"TraceLength": (229, 2, (3, 0), (), "TraceLength", None),
		"VarWriteEnable": (213, 2, (11, 0), (), "VarWriteEnable", None),
	}
	_prop_map_put_ = {
		"BusyLampOff": ((201, LCID, 4, 0),()),
		"Invisible": ((208, LCID, 4, 0),()),
		"Name": ((216, LCID, 4, 0),()),
		"NotCircularMotion": ((217, LCID, 4, 0),()),
		"PauseOnShift": ((209, LCID, 4, 0),()),
		"Priority": ((220, LCID, 4, 0),()),
		"StepType": ((224, LCID, 4, 0),()),
		"SystemTask": ((210, LCID, 4, 0),()),
		"TPMotion": ((211, LCID, 4, 0),()),
		"TraceEnable": ((212, LCID, 4, 0),()),
		"TraceLength": ((229, LCID, 4, 0),()),
		"VarWriteEnable": ((213, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ITaskEvents:
	CLSID = CLSID_Sink = IID('{F22A6948-A310-11D1-B77A-00C04FBBE42A}')
	coclass_clsid = IID('{847A8F82-4626-11D1-B745-00C04FBBE42A}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        2 : "OnChange",
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
#	def OnChange(self, ChangeType=defaultNamedNotOptArg):
#		'\x0bThis event occurs if the StartMonitor method has been called and a task object changes.'


class ITasks(DispatchBaseClass):
	'\x0bThe tasks collection represents all interpreter (PXNN) tasks that are currently active on the controller.  This collection will contain one object for each active task.\x0b'
	CLSID = IID('{5F26BE72-4626-11D1-B745-00C04FBBE42A}')
	coclass_clsid = IID('{6B01CFFC-4626-11D1-B745-00C04FBBE42A}')

	def AbortAll(self, Cancel=defaultNamedOptArg):
		'\x0bAborts all active abortable interpreter tasks.'
		return self._oleobj_.InvokeTypes(250, LCID, 1, (24, 0), ((12, 17),),Cancel
			)

	# Result is of type FRCTask
	# The method GetItem is actually a property, but must be used as a method to correctly pass the arguments
	def GetItem(self, Index=defaultNamedOptArg, Name=defaultNamedOptArg):
		'\x0bItem returns a task object, specified by collection index or by name, from the collection to the caller.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (13, 0), ((12, 17), (12, 17)),Index
			, Name)
		if ret is not None:
			# See if this IUnknown is really an IDispatch
			try:
				ret = ret.QueryInterface(pythoncom.IID_IDispatch)
			except pythoncom.error:
				return ret
			ret = Dispatch(ret, 'GetItem', '{847A8F82-4626-11D1-B745-00C04FBBE42A}')
		return ret

	def PauseAll(self, Cancel=defaultNamedOptArg):
		'\x0bPauses all active pauseable interpreter tasks..'
		return self._oleobj_.InvokeTypes(251, LCID, 1, (24, 0), ((12, 17),),Cancel
			)

	def StartMonitor(self, Interval=defaultNamedNotOptArg):
		'\x0bThis method begins monitoring of all task objects in the collection for changes.'
		return self._oleobj_.InvokeTypes(252, LCID, 1, (24, 0), ((3, 1),),Interval
			)

	def StopMonitor(self):
		'\x0bThis method stops monitoring of all task objects in the collection for changes.'
		return self._oleobj_.InvokeTypes(253, LCID, 1, (24, 0), (),)

	def TryItem(self, Name=defaultNamedNotOptArg, Task=pythoncom.Missing):
		'\x0bTests if the specified task exists.  If it does, the FRCTask object to access it is returned.'
		return self._ApplyTypes_(254, 1, (11, 0), ((8, 1), (16397, 2)), 'TryItem', None,Name
			, Task)

	_prop_map_get_ = {
		"Count": (201, 2, (2, 0), (), "Count", None),
		"IsMonitoring": (202, 2, (11, 0), (), "IsMonitoring", None),
		# Method 'Item' returns object of type 'FRCTask'
		"Item": (0, 2, (13, 0), ((12, 17), (12, 17)), "Item", '{847A8F82-4626-11D1-B745-00C04FBBE42A}'),
		# Method 'Robot' returns object of type 'FRCRobot'
		"Robot": (1, 2, (13, 0), (), "Robot", '{6D7E3A01-9ECC-11D0-94D5-0020AF68F0A3}'),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedOptArg, Name=defaultNamedOptArg):
		'\x0bItem returns a task object, specified by collection index or by name, from the collection to the caller.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (13, 0), ((12, 17), (12, 17)),Index
			, Name)
		if ret is not None:
			# See if this IUnknown is really an IDispatch
			try:
				ret = ret.QueryInterface(pythoncom.IID_IDispatch)
			except pythoncom.error:
				return ret
			ret = Dispatch(ret, '__call__', '{847A8F82-4626-11D1-B745-00C04FBBE42A}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(201, 2, (2, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ITasksEvents:
	CLSID = CLSID_Sink = IID('{48F075F8-4626-11D1-B745-00C04FBBE42A}')
	coclass_clsid = IID('{6B01CFFC-4626-11D1-B745-00C04FBBE42A}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        1 : "OnChange",
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
#	def OnChange(self, ChangeType=defaultNamedNotOptArg, Task=defaultNamedNotOptArg):
#		'\x0bThis event occurs if the StartMonitor method has been called and any task object in the collection changes.'


class ITransform(DispatchBaseClass):
	'\x0bRepresents the position of a single group of axes as a transformation matrix consisting of normal, orient, approach, and location vectors and a component specifying a configuration.'
	CLSID = IID('{A47A5882-056D-11D0-8901-0020AF68F0A3}')
	coclass_clsid = IID('{A47A5883-056D-11D0-8901-0020AF68F0A3}')

	_prop_map_get_ = {
		# Method 'Approach' returns object of type 'FRCVector'
		"Approach": (303, 2, (13, 0), (), "Approach", '{C1578510-0F7A-11D2-86F4-00C04F9184DB}'),
		# Method 'Config' returns object of type 'FRCConfig'
		"Config": (201, 2, (13, 0), (), "Config", '{C58B0E61-ECD4-11D0-9FA5-00A024329125}'),
		# Method 'Ext' returns object of type 'FRCAxesCollection'
		"Ext": (202, 2, (13, 0), (), "Ext", '{035505A1-1C41-11D0-8901-0020AF68F0A3}'),
		# Method 'Location' returns object of type 'FRCVector'
		"Location": (304, 2, (13, 0), (), "Location", '{C1578510-0F7A-11D2-86F4-00C04F9184DB}'),
		# Method 'Normal' returns object of type 'FRCVector'
		"Normal": (301, 2, (13, 0), (), "Normal", '{C1578510-0F7A-11D2-86F4-00C04F9184DB}'),
		# Method 'Orient' returns object of type 'FRCVector'
		"Orient": (302, 2, (13, 0), (), "Orient", '{C1578510-0F7A-11D2-86F4-00C04F9184DB}'),
		# Method 'Parent' returns object of type 'FRCPosition'
		"Parent": (203, 2, (13, 0), (), "Parent", '{D42AB5DB-8FFB-11D0-94CC-0020AF68F0A3}'),
		# Method 'Program' returns object of type 'FRCProgram'
		"Program": (101, 2, (13, 0), (), "Program", '{D42AB5D5-8FFB-11D0-94CC-0020AF68F0A3}'),
		# Method 'Robot' returns object of type 'FRCRobot'
		"Robot": (1, 2, (13, 0), (), "Robot", '{6D7E3A01-9ECC-11D0-94D5-0020AF68F0A3}'),
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

class IUOPIOSignal(DispatchBaseClass):
	'\x0bRepresents a User Operator Panel I/O signal.  '
	CLSID = IID('{714CC924-B4E5-11D0-A073-00A02436CF7E}')
	coclass_clsid = IID('{714CC92B-B4E5-11D0-A073-00A02436CF7E}')

	def Refresh(self):
		'\x0bReads new information of the signal from the robot.'
		return self._oleobj_.InvokeTypes(252, LCID, 1, (24, 0), (),)

	def StartMonitor(self, Latency=defaultNamedNotOptArg):
		'\x0bStarts the monitoring of the I/O signal for changes.'
		return self._oleobj_.InvokeTypes(150, LCID, 1, (24, 0), ((3, 0),),Latency
			)

	def StopMonitor(self):
		'\x0bStops the monitoring of the I/O signal for changes.'
		return self._oleobj_.InvokeTypes(151, LCID, 1, (24, 0), (),)

	def Update(self):
		"\x0bSends the local copy of this signal's information to the robot."
		return self._oleobj_.InvokeTypes(253, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"IsAssigned": (103, 2, (11, 0), (), "IsAssigned", None),
		"IsMonitoring": (105, 2, (11, 0), (), "IsMonitoring", None),
		"IsOffline": (104, 2, (11, 0), (), "IsOffline", None),
		"LogicalNum": (101, 2, (3, 0), (), "LogicalNum", None),
		"NoRefresh": (250, 2, (11, 0), (), "NoRefresh", None),
		"NoUpdate": (251, 2, (11, 0), (), "NoUpdate", None),
		# Method 'Parent' returns object of type 'FRCIOSignals'
		"Parent": (202, 2, (13, 0), (), "Parent", '{59DC16F8-AF91-11D0-A072-00A02436CF7E}'),
		# Method 'Robot' returns object of type 'FRCRobot'
		"Robot": (1, 2, (13, 0), (), "Robot", '{6D7E3A01-9ECC-11D0-94D5-0020AF68F0A3}'),
		"Value": (201, 2, (11, 0), (), "Value", None),
	}
	_prop_map_put_ = {
		"Comment": ((102, LCID, 4, 0),()),
		"NoRefresh": ((250, LCID, 4, 0),()),
		"NoUpdate": ((251, LCID, 4, 0),()),
		"Value": ((201, LCID, 4, 0),()),
	}
	# Default property for this class is 'Value'
	def __call__(self):
		return self._ApplyTypes_(*(201, 2, (11, 0), (), "Value", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IUserIOSignal(DispatchBaseClass):
	CLSID = IID('{59DC16FE-AF91-11D0-A072-00A02436CF7E}')
	coclass_clsid = IID('{59DC16FF-AF91-11D0-A072-00A02436CF7E}')

	def StartMonitor(self, Latency=defaultNamedNotOptArg):
		'\x0bStarts the monitoring of the I/O signal for changes.'
		return self._oleobj_.InvokeTypes(150, LCID, 1, (24, 0), ((3, 0),),Latency
			)

	def StopMonitor(self):
		'\x0bStops the monitoring of the I/O signal for changes.'
		return self._oleobj_.InvokeTypes(151, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"CanComplement": (211, 2, (11, 0), (), "CanComplement", None),
		"CanInvert": (210, 2, (11, 0), (), "CanInvert", None),
		"CanSimulate": (209, 2, (11, 0), (), "CanSimulate", None),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"Complementary": (206, 2, (11, 0), (), "Complementary", None),
		"Index": (201, 2, (3, 0), (), "Index", None),
		"IsAssigned": (103, 2, (11, 0), (), "IsAssigned", None),
		"IsBoolean": (208, 2, (11, 0), (), "IsBoolean", None),
		"IsInput": (207, 2, (11, 0), (), "IsInput", None),
		"IsMonitoring": (105, 2, (11, 0), (), "IsMonitoring", None),
		"IsOffline": (104, 2, (11, 0), (), "IsOffline", None),
		"LogicalNum": (101, 2, (3, 0), (), "LogicalNum", None),
		"LogicalType": (202, 2, (2, 0), (), "LogicalType", None),
		# Method 'Parent' returns object of type 'FRCUserIOSignals'
		"Parent": (212, 2, (13, 0), (), "Parent", '{59DC16FA-AF91-11D0-A072-00A02436CF7E}'),
		"Polarity": (205, 2, (11, 0), (), "Polarity", None),
		# Method 'Robot' returns object of type 'FRCRobot'
		"Robot": (1, 2, (13, 0), (), "Robot", '{6D7E3A01-9ECC-11D0-94D5-0020AF68F0A3}'),
		"Simulate": (204, 2, (11, 0), (), "Simulate", None),
		"Value": (203, 2, (12, 0), (), "Value", None),
	}
	_prop_map_put_ = {
		"Comment": ((102, LCID, 4, 0),()),
		"Complementary": ((206, LCID, 4, 0),()),
		"Index": ((201, LCID, 4, 0),()),
		"Polarity": ((205, LCID, 4, 0),()),
		"Simulate": ((204, LCID, 4, 0),()),
		"Value": ((203, LCID, 4, 0),()),
	}
	# Default property for this class is 'Value'
	def __call__(self):
		return self._ApplyTypes_(*(203, 2, (12, 0), (), "Value", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IUserIOSignals(DispatchBaseClass):
	CLSID = IID('{59DC16F9-AF91-11D0-A072-00A02436CF7E}')
	coclass_clsid = IID('{59DC16FA-AF91-11D0-A072-00A02436CF7E}')

	# Result is of type FRCUserIOSignal
	def Add(self, LogicalType=defaultNamedNotOptArg, LogicalNum=defaultNamedNotOptArg, Index=defaultNamedOptArg):
		ret = self._oleobj_.InvokeTypes(151, LCID, 1, (13, 0), ((2, 1), (3, 1), (12, 17)),LogicalType
			, LogicalNum, Index)
		if ret is not None:
			# See if this IUnknown is really an IDispatch
			try:
				ret = ret.QueryInterface(pythoncom.IID_IDispatch)
			except pythoncom.error:
				return ret
			ret = Dispatch(ret, 'Add', '{59DC16FF-AF91-11D0-A072-00A02436CF7E}')
		return ret

	# Result is of type FRCUserIOSignal
	# The method GetItem is actually a property, but must be used as a method to correctly pass the arguments
	def GetItem(self, LogicalType=defaultNamedOptArg, LogicalNum=defaultNamedOptArg, Index=defaultNamedOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (13, 0), ((12, 17), (12, 17), (12, 17)),LogicalType
			, LogicalNum, Index)
		if ret is not None:
			# See if this IUnknown is really an IDispatch
			try:
				ret = ret.QueryInterface(pythoncom.IID_IDispatch)
			except pythoncom.error:
				return ret
			ret = Dispatch(ret, 'GetItem', '{59DC16FF-AF91-11D0-A072-00A02436CF7E}')
		return ret

	def Remove(self, LogicalType=defaultNamedOptArg, LogicalNum=defaultNamedOptArg, Index=defaultNamedOptArg):
		return self._oleobj_.InvokeTypes(152, LCID, 1, (24, 0), ((12, 17), (12, 17), (12, 17)),LogicalType
			, LogicalNum, Index)

	def StartMonitor(self, Latency=defaultNamedNotOptArg):
		'\x0bStarts the monitoring of the I/O signal for changes.'
		return self._oleobj_.InvokeTypes(153, LCID, 1, (24, 0), ((3, 0),),Latency
			)

	def StopMonitor(self):
		'\x0bStops the monitoring of the I/O signal for changes.'
		return self._oleobj_.InvokeTypes(154, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"Count": (101, 2, (3, 0), (), "Count", None),
		"IsMonitoring": (103, 2, (11, 0), (), "IsMonitoring", None),
		# Method 'Item' returns object of type 'FRCUserIOSignal'
		"Item": (0, 2, (13, 0), ((12, 17), (12, 17), (12, 17)), "Item", '{59DC16FF-AF91-11D0-A072-00A02436CF7E}'),
		# Method 'Parent' returns object of type 'FRCUserIOType'
		"Parent": (102, 2, (13, 0), (), "Parent", '{59DC16F6-AF91-11D0-A072-00A02436CF7E}'),
		# Method 'Robot' returns object of type 'FRCRobot'
		"Robot": (1, 2, (13, 0), (), "Robot", '{6D7E3A01-9ECC-11D0-94D5-0020AF68F0A3}'),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, LogicalType=defaultNamedOptArg, LogicalNum=defaultNamedOptArg, Index=defaultNamedOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (13, 0), ((12, 17), (12, 17), (12, 17)),LogicalType
			, LogicalNum, Index)
		if ret is not None:
			# See if this IUnknown is really an IDispatch
			try:
				ret = ret.QueryInterface(pythoncom.IID_IDispatch)
			except pythoncom.error:
				return ret
			ret = Dispatch(ret, '__call__', '{59DC16FF-AF91-11D0-A072-00A02436CF7E}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(101, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IUserIOSignalsEvents:
	CLSID = CLSID_Sink = IID('{C240AAA1-F86F-11D0-A093-00A02436CF7E}')
	coclass_clsid = IID('{59DC16FA-AF91-11D0-A072-00A02436CF7E}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        1 : "OnCreate",
		        2 : "OnDelete",
		        3 : "OnRefresh",
		        4 : "OnChange",
		        5 : "OnSimulate",
		        6 : "OnUnsimulate",
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
#	def OnCreate(self, UserIOSignal=defaultNamedNotOptArg):
#	def OnDelete(self, UserIOSignal=defaultNamedNotOptArg):
#	def OnRefresh(self):
#	def OnChange(self, UserIOSignal=defaultNamedNotOptArg):
#	def OnSimulate(self, IOSignal=defaultNamedNotOptArg):
#	def OnUnsimulate(self, IOSignal=defaultNamedNotOptArg):


class IUserIOType(DispatchBaseClass):
	CLSID = IID('{59DC16F5-AF91-11D0-A072-00A02436CF7E}')
	coclass_clsid = IID('{59DC16F6-AF91-11D0-A072-00A02436CF7E}')

	_prop_map_get_ = {
		"Lock": (203, 2, (11, 0), (), "Lock", None),
		"Name": (201, 2, (8, 0), (), "Name", None),
		# Method 'Parent' returns object of type 'FRCIOTypes'
		"Parent": (102, 2, (13, 0), (), "Parent", '{59DC16ED-AF91-11D0-A072-00A02436CF7E}'),
		# Method 'Robot' returns object of type 'FRCRobot'
		"Robot": (1, 2, (13, 0), (), "Robot", '{6D7E3A01-9ECC-11D0-94D5-0020AF68F0A3}'),
		# Method 'Signals' returns object of type 'FRCUserIOSignals'
		"Signals": (202, 2, (13, 0), (), "Signals", '{59DC16FA-AF91-11D0-A072-00A02436CF7E}'),
		"Type": (101, 2, (2, 0), (), "Type", None),
	}
	_prop_map_put_ = {
		"Lock": ((203, LCID, 4, 0),()),
		"Name": ((201, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IUserIOTypeEvents:
	CLSID = CLSID_Sink = IID('{95741D17-F9F1-11D0-B6EE-00C04FB9E76B}')
	coclass_clsid = IID('{59DC16F6-AF91-11D0-A072-00A02436CF7E}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        1 : "OnDelete",
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
#	def OnDelete(self):


class IVar(DispatchBaseClass):
	'\x0bProvides access to the attributes and value of program and system variables.'
	CLSID = IID('{8C8ACC80-4F57-11D0-BC32-444553540000}')
	coclass_clsid = IID('{8C8ACC81-4F57-11D0-BC32-444553540000}')

	def Copy(self, SourceVar=defaultNamedNotOptArg):
		'\x0bCopies the data from the supplied FRVar object into this one.'
		return self._oleobj_.InvokeTypes(403, LCID, 1, (24, 0), ((13, 1),),SourceVar
			)

	def Refresh(self):
		'\x0bImmediately updates the value cached in the Robot Server with a "fresh" one read from the robot controller.'
		return self._oleobj_.InvokeTypes(252, LCID, 1, (24, 0), (),)

	def StartMonitor(self, Latency=defaultNamedNotOptArg):
		'\x0bTells the controller to monitor a variable and raise an event when its value changes.'
		return self._oleobj_.InvokeTypes(250, LCID, 1, (24, 0), ((3, 0),),Latency
			)

	def StopMonitor(self):
		'\x0bTells the controller to stop monitoring the variable for value changes.'
		return self._oleobj_.InvokeTypes(251, LCID, 1, (24, 0), (),)

	def Uninitialize(self):
		'\x0bUninitializes a variable.'
		return self._oleobj_.InvokeTypes(351, LCID, 1, (24, 0), (),)

	def Update(self):
		"\x0bSends the local copy of this variable's value to the robot."
		return self._oleobj_.InvokeTypes(402, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"AccessCode": (307, 2, (3, 0), (), "AccessCode", None),
		"FieldName": (201, 2, (8, 0), (), "FieldName", None),
		"GroupNum": (303, 2, (2, 0), (), "GroupNum", None),
		"IsInitialized": (310, 2, (11, 0), (), "IsInitialized", None),
		"IsMonitoring": (203, 2, (11, 0), (), "IsMonitoring", None),
		"MaxStringLen": (304, 2, (2, 0), (), "MaxStringLen", None),
		"MaxValue": (305, 2, (12, 0), (), "MaxValue", None),
		"MinValue": (306, 2, (12, 0), (), "MinValue", None),
		"NoRefresh": (204, 2, (11, 0), (), "NoRefresh", None),
		"NoUpdate": (401, 2, (11, 0), (), "NoUpdate", None),
		"Override": (400, 2, (3, 0), (), "Override", None),
		# Method 'Parent' returns object of type 'FRCVars'
		"Parent": (309, 2, (13, 0), (), "Parent", '{88B57BCB-D0CA-11CF-959F-00A024329125}'),
		# Method 'Program' returns object of type 'FRCProgram'
		"Program": (101, 2, (13, 0), (), "Program", '{D42AB5D5-8FFB-11D0-94CC-0020AF68F0A3}'),
		# Method 'Robot' returns object of type 'FRCRobot'
		"Robot": (1, 2, (13, 0), (), "Robot", '{6D7E3A01-9ECC-11D0-94D5-0020AF68F0A3}'),
		"Size": (404, 2, (3, 0), (), "Size", None),
		"StorageClass": (308, 2, (3, 0), (), "StorageClass", None),
		"TypeCode": (301, 2, (3, 0), (), "TypeCode", None),
		"TypeName": (302, 2, (8, 0), (), "TypeName", None),
		"Value": (0, 2, (12, 0), (), "Value", None),
		"VarName": (202, 2, (8, 0), (), "VarName", None),
	}
	_prop_map_put_ = {
		"NoRefresh": ((204, LCID, 4, 0),()),
		"NoUpdate": ((401, LCID, 4, 0),()),
		"Override": ((400, LCID, 4, 0),()),
		"Value": ((0, LCID, 4, 0),()),
	}
	# Default property for this class is 'Value'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (12, 0), (), "Value", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IVarEvents:
	CLSID = CLSID_Sink = IID('{C19FE67C-A462-11D0-B304-00A02479C928}')
	coclass_clsid = IID('{8C8ACC81-4F57-11D0-BC32-444553540000}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        2 : "OnDelete",
		        3 : "OnChange",
		        4 : "OnRename",
		        6 : "OnCommentChange",
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
#	def OnDelete(self):
#		'\x0bOccurs after a variable is deleted.'
#	def OnChange(self):
#		'\x0bOccurs after a variable is changed.'
#	def OnRename(self):
#		'\x0bOccurs after a variable is renamed.'
#	def OnCommentChange(self):
#		'\x0bOccurs after a numeric register comment is changed.'


class IVarObject(DispatchBaseClass):
	CLSID = IID('{A6F54250-DE6F-11D0-9F9F-00A024329125}')
	coclass_clsid = None

	def Refresh(self):
		'\x0bImmediately updates the value cached in the Robot Server with a "fresh" one read from the robot controller.'
		return self._oleobj_.InvokeTypes(252, LCID, 1, (24, 0), (),)

	def StartMonitor(self, Latency=defaultNamedNotOptArg):
		'\x0bTells the controller to monitor a variable and raise an event when its value changes.'
		return self._oleobj_.InvokeTypes(250, LCID, 1, (24, 0), ((3, 0),),Latency
			)

	def StopMonitor(self):
		'\x0bTells the controller to stop monitoring the variable for value changes.'
		return self._oleobj_.InvokeTypes(251, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"FieldName": (201, 2, (8, 0), (), "FieldName", None),
		"IsMonitoring": (203, 2, (11, 0), (), "IsMonitoring", None),
		"NoRefresh": (204, 2, (11, 0), (), "NoRefresh", None),
		# Method 'Program' returns object of type 'FRCProgram'
		"Program": (101, 2, (13, 0), (), "Program", '{D42AB5D5-8FFB-11D0-94CC-0020AF68F0A3}'),
		# Method 'Robot' returns object of type 'FRCRobot'
		"Robot": (1, 2, (13, 0), (), "Robot", '{6D7E3A01-9ECC-11D0-94D5-0020AF68F0A3}'),
		"VarName": (202, 2, (8, 0), (), "VarName", None),
	}
	_prop_map_put_ = {
		"NoRefresh": ((204, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IVarObject2(DispatchBaseClass):
	CLSID = IID('{D0EDFE01-C6AC-11D2-8727-00C04F81118D}')
	coclass_clsid = None

	def Refresh(self):
		'\x0bImmediately updates the value cached in the Robot Server with a "fresh" one read from the robot controller.'
		return self._oleobj_.InvokeTypes(252, LCID, 1, (24, 0), (),)

	def StartMonitor(self, Latency=defaultNamedNotOptArg):
		'\x0bTells the controller to monitor a variable and raise an event when its value changes.'
		return self._oleobj_.InvokeTypes(250, LCID, 1, (24, 0), ((3, 0),),Latency
			)

	def StopMonitor(self):
		'\x0bTells the controller to stop monitoring the variable for value changes.'
		return self._oleobj_.InvokeTypes(251, LCID, 1, (24, 0), (),)

	def Update(self):
		"\x0bSends the local copy of this variable's value to the robot."
		return self._oleobj_.InvokeTypes(402, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"FieldName": (201, 2, (8, 0), (), "FieldName", None),
		"IsMonitoring": (203, 2, (11, 0), (), "IsMonitoring", None),
		"NoRefresh": (204, 2, (11, 0), (), "NoRefresh", None),
		"NoUpdate": (401, 2, (11, 0), (), "NoUpdate", None),
		"Override": (400, 2, (3, 0), (), "Override", None),
		# Method 'Program' returns object of type 'FRCProgram'
		"Program": (101, 2, (13, 0), (), "Program", '{D42AB5D5-8FFB-11D0-94CC-0020AF68F0A3}'),
		# Method 'Robot' returns object of type 'FRCRobot'
		"Robot": (1, 2, (13, 0), (), "Robot", '{6D7E3A01-9ECC-11D0-94D5-0020AF68F0A3}'),
		"VarName": (202, 2, (8, 0), (), "VarName", None),
	}
	_prop_map_put_ = {
		"NoRefresh": ((204, LCID, 4, 0),()),
		"NoUpdate": ((401, LCID, 4, 0),()),
		"Override": ((400, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IVarPosition(DispatchBaseClass):
	'\x0bProvides access to the positional data for a position stored as a variable on the controller.'
	CLSID = IID('{E3FFB438-2613-11D1-B702-00C04FB9C401}')
	coclass_clsid = IID('{E3FFB439-2613-11D1-B702-00C04FB9C401}')

	def CheckReach(self, From=defaultNamedNotOptArg, MoType=6, OrientType=2, Destination=defaultNamedNotOptArg
			, MotionErrorInfo=0):
		'\x0bReturns a Boolean indicating if the robot can reach the position or not.'
		return self._ApplyTypes_(305, 1, (11, 0), ((12, 17), (3, 49), (3, 49), (12, 17), (16397, 50)), 'CheckReach', None,From
			, MoType, OrientType, Destination, MotionErrorInfo)

	def Copy(self, Position=defaultNamedNotOptArg):
		'\x0bCopies the positional data from another object into this one.'
		return self._oleobj_.InvokeTypes(304, LCID, 1, (24, 0), ((9, 1),),Position
			)

	# The method Formats is actually a property, but must be used as a method to correctly pass the arguments
	def Formats(self, Type=defaultNamedNotOptArg):
		'\x0bReturns positional data in the specified format.'
		ret = self._oleobj_.InvokeTypes(203, LCID, 2, (9, 0), ((3, 1),),Type
			)
		if ret is not None:
			ret = Dispatch(ret, 'Formats', None)
		return ret

	# The method IsEqualTo is actually a property, but must be used as a method to correctly pass the arguments
	def IsEqualTo(self, TargetPos=defaultNamedNotOptArg):
		"Returns a boolean value that indicates if the positional data contained in the current object is 'almost equal to' the positional data of another object."
		return self._oleobj_.InvokeTypes(302, LCID, 2, (11, 0), ((9, 1),),TargetPos
			)

	# The method IsReachable is actually a property, but must be used as a method to correctly pass the arguments
	def IsReachable(self, From=defaultNamedNotOptArg, MoType=6, OrientType=2, Destination=defaultNamedNotOptArg
			, MotionErrorInfo=0):
		'\x0bReturns a Boolean indicating if the robot can reach the position or not.'
		return self._ApplyTypes_(303, 2, (11, 0), ((12, 17), (3, 49), (3, 49), (12, 17), (16397, 50)), 'IsReachable', None,From
			, MoType, OrientType, Destination, MotionErrorInfo)

	def MatInv(self, InputPos=defaultNamedNotOptArg):
		'\x0bInvert the input position transformation matrix and set the results to this position.'
		return self._oleobj_.InvokeTypes(259, LCID, 1, (24, 0), ((9, 1),),InputPos
			)

	def MatMul(self, LeftPos=defaultNamedNotOptArg, RightPos=defaultNamedNotOptArg):
		'\x0bMultiply two input positions’ transformation matrices and set the results to this position.'
		return self._oleobj_.InvokeTypes(258, LCID, 1, (24, 0), ((9, 1), (9, 1)),LeftPos
			, RightPos)

	def Moveto(self):
		'\x0bMoves the robot to this position.'
		return self._oleobj_.InvokeTypes(253, LCID, 1, (24, 0), (),)

	def Record(self):
		'\x0bRecords the current position of the robot to this position.'
		return self._oleobj_.InvokeTypes(254, LCID, 1, (24, 0), (),)

	def Refresh(self):
		'\x0bClears all changes to the position since the last update of the position.'
		return self._oleobj_.InvokeTypes(252, LCID, 1, (24, 0), (),)

	def StartMonitor(self, Latency=defaultNamedNotOptArg):
		'\x0bEnables the Change event, with specified latency.'
		return self._oleobj_.InvokeTypes(255, LCID, 1, (24, 0), ((3, 1),),Latency
			)

	def StopMonitor(self):
		'\x0bStops the Change event from occurring.'
		return self._oleobj_.InvokeTypes(256, LCID, 1, (24, 0), (),)

	def Uninitialize(self):
		'\x0bUninitializes the position. '
		return self._oleobj_.InvokeTypes(257, LCID, 1, (24, 0), (),)

	def Update(self):
		'\x0bUpdates any changes to the position back to the controller.'
		return self._oleobj_.InvokeTypes(251, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"AutomaticUpdate": (201, 2, (11, 0), (), "AutomaticUpdate", None),
		"GroupNum": (204, 2, (2, 0), (), "GroupNum", None),
		"Id": (205, 2, (3, 0), (), "Id", None),
		"IsAtCurPosition": (206, 2, (11, 0), (), "IsAtCurPosition", None),
		"IsInitialized": (207, 2, (11, 0), (), "IsInitialized", None),
		"IsMonitoring": (210, 2, (11, 0), (), "IsMonitoring", None),
		# Method 'Parent' returns object of type 'FRCVar'
		"Parent": (301, 2, (13, 0), (), "Parent", '{8C8ACC81-4F57-11D0-BC32-444553540000}'),
		# Method 'Program' returns object of type 'FRCProgram'
		"Program": (101, 2, (13, 0), (), "Program", '{D42AB5D5-8FFB-11D0-94CC-0020AF68F0A3}'),
		# Method 'Robot' returns object of type 'FRCRobot'
		"Robot": (1, 2, (13, 0), (), "Robot", '{6D7E3A01-9ECC-11D0-94D5-0020AF68F0A3}'),
		"Type": (202, 2, (3, 0), (), "Type", None),
		"UserFrame": (208, 2, (3, 0), (), "UserFrame", None),
		"UserTool": (209, 2, (3, 0), (), "UserTool", None),
	}
	_prop_map_put_ = {
		"AutomaticUpdate": ((201, LCID, 4, 0),()),
		"Type": ((202, LCID, 4, 0),()),
		"UserFrame": ((208, LCID, 4, 0),()),
		"UserTool": ((209, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IVars(DispatchBaseClass):
	'\x0bProvides access to robot controller variables, including system and program variables.'
	CLSID = IID('{88B57BCA-D0CA-11CF-959F-00A024329125}')
	coclass_clsid = IID('{88B57BCB-D0CA-11CF-959F-00A024329125}')

	def Copy(self, SourceVars=defaultNamedNotOptArg):
		'\x0bCopies the data from the supplied FRVars object into this one.'
		return self._oleobj_.InvokeTypes(403, LCID, 1, (24, 0), ((13, 1),),SourceVars
			)

	# The method GetItem is actually a property, but must be used as a method to correctly pass the arguments
	def GetItem(self, Name=defaultNamedOptArg, Index=defaultNamedOptArg):
		'\x0bReturns a variable object from the collection. '
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 17), (12, 17)),Name
			, Index)
		if ret is not None:
			ret = Dispatch(ret, 'GetItem', None)
		return ret

	def Refresh(self):
		'\x0bImmediately updates the value cached in the Robot Server with a "fresh" one read from the robot controller.'
		return self._oleobj_.InvokeTypes(252, LCID, 1, (24, 0), (),)

	def StartMonitor(self, Latency=defaultNamedNotOptArg):
		'\x0bTells the controller to monitor a variable and raise an event when its value changes.'
		return self._oleobj_.InvokeTypes(250, LCID, 1, (24, 0), ((3, 0),),Latency
			)

	def StopMonitor(self):
		'\x0bTells the controller to stop monitoring the variable for value changes.'
		return self._oleobj_.InvokeTypes(251, LCID, 1, (24, 0), (),)

	def TryItem(self, Name=defaultNamedNotOptArg, Index=defaultNamedNotOptArg, Item=pythoncom.Missing):
		'\x0bTests if the specified variable exists. If it does, the FRCVar or FRCVars object to access it is returned.'
		return self._ApplyTypes_(405, 1, (11, 0), ((12, 17), (12, 17), (16393, 2)), 'TryItem', None,Name
			, Index, Item)

	def Update(self):
		'\x0bSends the local copy of the values for this whole structure to the robot.'
		return self._oleobj_.InvokeTypes(402, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"Count": (301, 2, (2, 0), (), "Count", None),
		"FieldName": (201, 2, (8, 0), (), "FieldName", None),
		"IsMonitoring": (203, 2, (11, 0), (), "IsMonitoring", None),
		"Item": (0, 2, (9, 0), ((12, 17), (12, 17)), "Item", None),
		"NoRefresh": (204, 2, (11, 0), (), "NoRefresh", None),
		"NoUpdate": (401, 2, (11, 0), (), "NoUpdate", None),
		"Override": (400, 2, (3, 0), (), "Override", None),
		"Parent": (302, 2, (9, 0), (), "Parent", None),
		# Method 'Program' returns object of type 'FRCProgram'
		"Program": (101, 2, (13, 0), (), "Program", '{D42AB5D5-8FFB-11D0-94CC-0020AF68F0A3}'),
		# Method 'Robot' returns object of type 'FRCRobot'
		"Robot": (1, 2, (13, 0), (), "Robot", '{6D7E3A01-9ECC-11D0-94D5-0020AF68F0A3}'),
		"Size": (404, 2, (3, 0), (), "Size", None),
		"VarName": (202, 2, (8, 0), (), "VarName", None),
	}
	_prop_map_put_ = {
		"NoRefresh": ((204, LCID, 4, 0),()),
		"NoUpdate": ((401, LCID, 4, 0),()),
		"Override": ((400, LCID, 4, 0),()),
	}
	# Default method for this class is 'Item'
	def __call__(self, Name=defaultNamedOptArg, Index=defaultNamedOptArg):
		'\x0bReturns a variable object from the collection. '
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 17), (12, 17)),Name
			, Index)
		if ret is not None:
			ret = Dispatch(ret, '__call__', None)
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(301, 2, (2, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IVarsEvents:
	CLSID = CLSID_Sink = IID('{0AFC1567-101D-11D1-B6F6-00C04FB9E76B}')
	coclass_clsid = IID('{88B57BCB-D0CA-11CF-959F-00A024329125}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        1 : "OnCreate",
		        2 : "OnDelete",
		        3 : "OnChange",
		        4 : "OnRename",
		        5 : "OnRealloc",
		        6 : "OnCommentChange",
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
#	def OnCreate(self, Var=defaultNamedNotOptArg):
#		'\x0bOccurs after a variable is created.'
#	def OnDelete(self, Var=defaultNamedNotOptArg):
#		'\x0bOccurs after a variable is deleted.'
#	def OnChange(self, Var=defaultNamedNotOptArg):
#		'\x0bOccurs after a variable is changed.'
#	def OnRename(self, Var=defaultNamedNotOptArg):
#		'\x0bOccurs after a variable is renamed.'
#	def OnRealloc(self, Var=defaultNamedNotOptArg):
#		'\x0bOccurs after an array variable is reallocated or a path node is inserted, appended, or deleted from a path variable.'
#	def OnCommentChange(self, Var=defaultNamedNotOptArg):
#		'\x0bOccurs after a numeric register comment is changed.'


class IVector(DispatchBaseClass):
	'\x0bProvides access to individual components of a vector.'
	CLSID = IID('{924CC060-0F7A-11D2-86F4-00C04F9184DB}')
	coclass_clsid = IID('{C1578510-0F7A-11D2-86F4-00C04F9184DB}')

	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, ValueNum=defaultNamedNotOptArg):
		'\x0bReturns/sets the component values for the vector.'
		return self._oleobj_.InvokeTypes(0, LCID, 2, (5, 0), ((2, 1),),ValueNum
			)

	# The method SetItem is actually a property, but must be used as a method to correctly pass the arguments
	def SetItem(self, ValueNum=defaultNamedNotOptArg, arg1=defaultUnnamedArg):
		'\x0bReturns/sets the component values for the vector.'
		return self._oleobj_.InvokeTypes(0, LCID, 4, (24, 0), ((2, 1), (5, 1)),ValueNum
			, arg1)

	_prop_map_get_ = {
		"Parent": (204, 2, (9, 0), (), "Parent", None),
		# Method 'Program' returns object of type 'FRCProgram'
		"Program": (101, 2, (13, 0), (), "Program", '{D42AB5D5-8FFB-11D0-94CC-0020AF68F0A3}'),
		# Method 'Robot' returns object of type 'FRCRobot'
		"Robot": (1, 2, (13, 0), (), "Robot", '{6D7E3A01-9ECC-11D0-94D5-0020AF68F0A3}'),
		"X": (201, 2, (5, 0), (), "X", None),
		"Y": (202, 2, (5, 0), (), "Y", None),
		"Z": (203, 2, (5, 0), (), "Z", None),
	}
	_prop_map_put_ = {
		"X": ((201, LCID, 4, 0),()),
		"Y": ((202, LCID, 4, 0),()),
		"Z": ((203, LCID, 4, 0),()),
	}
	# Default method for this class is 'Item'
	def __call__(self, ValueNum=defaultNamedNotOptArg):
		'\x0bReturns/sets the component values for the vector.'
		return self._oleobj_.InvokeTypes(0, LCID, 2, (5, 0), ((2, 1),),ValueNum
			)

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IXyzWpr(DispatchBaseClass):
	'\x0bRepresents the position of a single group of axes consisting of three real components specifying a Cartesian location (x,y,z), three real components specifying an orientation (w,p,r), and a component specifying a configuration.'
	CLSID = IID('{A47A5884-056D-11D0-8901-0020AF68F0A3}')
	coclass_clsid = IID('{A47A5885-056D-11D0-8901-0020AF68F0A3}')

	def GetAll(self, X=pythoncom.Missing, Y=pythoncom.Missing, Z=pythoncom.Missing, W=pythoncom.Missing
			, P=pythoncom.Missing, R=pythoncom.Missing):
		'\x0bReturns the location and orientation values in one call.'
		return self._ApplyTypes_(307, 1, (24, 0), ((16389, 2), (16389, 2), (16389, 2), (16389, 2), (16389, 2), (16389, 2)), 'GetAll', None,X
			, Y, Z, W, P, R
			)

	def SetAll(self, X=defaultNamedNotOptArg, Y=defaultNamedNotOptArg, Z=defaultNamedNotOptArg, W=defaultNamedNotOptArg
			, P=defaultNamedNotOptArg, R=defaultNamedNotOptArg):
		'\x0bSets the location and orientation values in one call.'
		return self._oleobj_.InvokeTypes(308, LCID, 1, (24, 0), ((5, 1), (5, 1), (5, 1), (5, 1), (5, 1), (5, 1)),X
			, Y, Z, W, P, R
			)

	_prop_map_get_ = {
		# Method 'Config' returns object of type 'FRCConfig'
		"Config": (201, 2, (13, 0), (), "Config", '{C58B0E61-ECD4-11D0-9FA5-00A024329125}'),
		# Method 'Ext' returns object of type 'FRCAxesCollection'
		"Ext": (202, 2, (13, 0), (), "Ext", '{035505A1-1C41-11D0-8901-0020AF68F0A3}'),
		"P": (305, 2, (5, 0), (), "P", None),
		# Method 'Parent' returns object of type 'FRCPosition'
		"Parent": (203, 2, (13, 0), (), "Parent", '{D42AB5DB-8FFB-11D0-94CC-0020AF68F0A3}'),
		# Method 'Program' returns object of type 'FRCProgram'
		"Program": (101, 2, (13, 0), (), "Program", '{D42AB5D5-8FFB-11D0-94CC-0020AF68F0A3}'),
		"R": (306, 2, (5, 0), (), "R", None),
		# Method 'Robot' returns object of type 'FRCRobot'
		"Robot": (1, 2, (13, 0), (), "Robot", '{6D7E3A01-9ECC-11D0-94D5-0020AF68F0A3}'),
		"W": (304, 2, (5, 0), (), "W", None),
		"X": (301, 2, (5, 0), (), "X", None),
		"Y": (302, 2, (5, 0), (), "Y", None),
		"Z": (303, 2, (5, 0), (), "Z", None),
	}
	_prop_map_put_ = {
		"P": ((305, LCID, 4, 0),()),
		"R": ((306, LCID, 4, 0),()),
		"W": ((304, LCID, 4, 0),()),
		"X": ((301, LCID, 4, 0),()),
		"Y": ((302, LCID, 4, 0),()),
		"Z": ((303, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

from win32com.client import CoClassBaseClass
class FRCAlarm(CoClassBaseClass): # A CoClass
	# This object contains error and cause data for the item selected from the FRCAlarms collection.
	CLSID = IID('{7C37F237-A494-11D0-A37F-0020AF39BE5A}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IAlarm,
	]
	default_interface = IAlarm

class FRCAlarms(CoClassBaseClass): # A CoClass
	# The FRCAlarms object is a collection of FRCAlarm objects.  This collection contains all the alarms that have occurred since the last time that the log was cleared, up to a predefined number.
	CLSID = IID('{7C37F235-A494-11D0-A37F-0020AF39BE5A}')
	coclass_sources = [
		IAlarmNotify,
	]
	default_source = IAlarmNotify
	coclass_interfaces = [
		IAlarms,
	]
	default_interface = IAlarms

class FRCAnalogIOSignal(CoClassBaseClass): # A CoClass
	# Represents an analog I/O signal.  
	CLSID = IID('{714CC922-B4E5-11D0-A073-00A02436CF7E}')
	coclass_sources = [
		IIOSignalEvents,
	]
	default_source = IIOSignalEvents
	coclass_interfaces = [
		IAnalogIOSignal,
	]
	default_interface = IAnalogIOSignal

class FRCAnalogIOType(CoClassBaseClass): # A CoClass
	# This object is used to access both I/O signal and I/O configuration collections.
	CLSID = IID('{714CC916-B4E5-11D0-A073-00A02436CF7E}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IConfigurableIOType,
	]
	default_interface = IConfigurableIOType

class FRCApplications(CoClassBaseClass): # A CoClass
	# This object is a general-purpose collection of application specific objects.
	CLSID = IID('{679622C3-E50A-11D1-B778-00C04FB99C75}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IApplications,
	]
	default_interface = IApplications

class FRCAxesCollection(CoClassBaseClass): # A CoClass
	# Represents the extended axes for a position. 
	CLSID = IID('{035505A1-1C41-11D0-8901-0020AF68F0A3}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IAxesCollection,
	]
	default_interface = IAxesCollection

class FRCCommonAssoc(CoClassBaseClass): # A CoClass
	# This object is used to access standard associated data common for all KAREL path motion groups.
	CLSID = IID('{15AAA600-1108-11D2-86F4-00C04F9184DB}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ICommonAssoc,
	]
	default_interface = ICommonAssoc

class FRCConfig(CoClassBaseClass): # A CoClass
	# Represents a Cartesian position’s configuration.
	CLSID = IID('{C58B0E61-ECD4-11D0-9FA5-00A024329125}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IConfig,
	]
	default_interface = IConfig

class FRCCurGroupPosition(CoClassBaseClass): # A CoClass
	# Provides access to the current position of the robot for a specific motion group.
	CLSID = IID('{75CEF1D7-1E43-11D1-B6FF-00C04FB9C401}')
	coclass_sources = [
		ICurGroupPositionEvents,
	]
	default_source = ICurGroupPositionEvents
	coclass_interfaces = [
		ICurGroupPosition,
	]
	default_interface = ICurGroupPosition

class FRCCurPosition(CoClassBaseClass): # A CoClass
	# Provides access to the current position of the robot for all motion groups.
	CLSID = IID('{E2686FA9-1E42-11D1-B6FF-00C04FB9C401}')
	coclass_sources = [
		ICurPositionEvents,
	]
	default_source = ICurPositionEvents
	coclass_interfaces = [
		ICurPosition,
	]
	default_interface = ICurPosition

class FRCDigitalIOSignal(CoClassBaseClass): # A CoClass
	# Represents a digital I/O signal object.  
	CLSID = IID('{59DC16FD-AF91-11D0-A072-00A02436CF7E}')
	coclass_sources = [
		IIOSignalEvents,
	]
	default_source = IIOSignalEvents
	coclass_interfaces = [
		IDigitalIOSignal,
	]
	default_interface = IDigitalIOSignal

class FRCDigitalIOType(CoClassBaseClass): # A CoClass
	# This object is used to access both I/O signal and I/O configuration collections.
	CLSID = IID('{59DC16F4-AF91-11D0-A072-00A02436CF7E}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IConfigurableIOType,
	]
	default_interface = IConfigurableIOType

class FRCFeature(CoClassBaseClass): # A CoClass
	# This object represents a single feature loaded on the controller.  
	CLSID = IID('{2AF44186-9273-11D1-B6F9-00C04FA3BD85}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IFeature,
	]
	default_interface = IFeature

class FRCFeatures(CoClassBaseClass): # A CoClass
	# The features collection is a representation of all currently loaded controller features.  This collection will contain one object for each feature.  
	CLSID = IID('{2AF44184-9273-11D1-B6F9-00C04FA3BD85}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IFeatures,
	]
	default_interface = IFeatures

class FRCFlagSignal(CoClassBaseClass): # A CoClass
	# Represents a Flag signal.  
	CLSID = IID('{1A191D0B-ECA1-42E1-A200-1FC17400A54E}')
	coclass_sources = [
		IIOSignalEvents,
	]
	default_source = IIOSignalEvents
	coclass_interfaces = [
		IRobotIOSignal,
	]
	default_interface = IRobotIOSignal

class FRCFlagType(CoClassBaseClass): # A CoClass
	# This object is used to access Flag signals.
	CLSID = IID('{A16B2E95-219A-4FA8-9DE8-021D429B8805}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ISystemIOType,
	]
	default_interface = ISystemIOType

class FRCGroupAssoc(CoClassBaseClass): # A CoClass
	# This object is used to access standard associated data for all KAREL path motion groups.
	CLSID = IID('{4DE6A770-1108-11D2-86F4-00C04F9184DB}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IGroupAssoc,
	]
	default_interface = IGroupAssoc

class FRCGroupIOSignal(CoClassBaseClass): # A CoClass
	# Represents a group I/O signal.  
	CLSID = IID('{714CC923-B4E5-11D0-A073-00A02436CF7E}')
	coclass_sources = [
		IIOSignalEvents,
	]
	default_source = IIOSignalEvents
	coclass_interfaces = [
		IAnalogIOSignal,
	]
	default_interface = IAnalogIOSignal

class FRCGroupIOType(CoClassBaseClass): # A CoClass
	# This object is used to access both I/O signal and I/O configuration collections.
	CLSID = IID('{714CC917-B4E5-11D0-A073-00A02436CF7E}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IConfigurableIOType,
	]
	default_interface = IConfigurableIOType

class FRCGroupPosition(CoClassBaseClass): # A CoClass
	# Provides access to the positional data of a TP position for a specific motion group.
	CLSID = IID('{A47A5881-056D-11D0-8901-0020AF68F0A3}')
	coclass_sources = [
		IGroupPositionEvents,
	]
	default_source = IGroupPositionEvents
	coclass_interfaces = [
		IGroupPosition,
	]
	default_interface = IGroupPosition

class FRCIOConfig(CoClassBaseClass): # A CoClass
	# This object represents an input or output configuration.
	CLSID = IID('{59DC1703-AF91-11D0-A072-00A02436CF7E}')
	coclass_sources = [
		IIOConfigEvents,
	]
	default_source = IIOConfigEvents
	coclass_interfaces = [
		IIOConfig,
	]
	default_interface = IIOConfig

class FRCIOConfigs(CoClassBaseClass): # A CoClass
	# This object is used to access all I/O configurations for a particular I/O type.
	CLSID = IID('{59DC1701-AF91-11D0-A072-00A02436CF7E}')
	coclass_sources = [
		IIOConfigsEvents,
	]
	default_source = IIOConfigsEvents
	coclass_interfaces = [
		IIOConfigs,
	]
	default_interface = IIOConfigs

class FRCIOSignal(CoClassBaseClass): # A CoClass
	# Represents an I/O signal.  
	CLSID = IID('{59DC170B-AF91-11D0-A072-00A02436CF7E}')
	coclass_sources = [
		IIOSignalEvents,
	]
	default_source = IIOSignalEvents
	coclass_interfaces = [
		IIOSignal2,
	]
	default_interface = IIOSignal2

class FRCIOSignals(CoClassBaseClass): # A CoClass
	# This object is used to access all I/O signals for a particular I/O type.
	CLSID = IID('{59DC16F8-AF91-11D0-A072-00A02436CF7E}')
	coclass_sources = [
		IIOSignalsEvents,
	]
	default_source = IIOSignalsEvents
	coclass_interfaces = [
		IIOSignals,
	]
	default_interface = IIOSignals

class FRCIOType(CoClassBaseClass): # A CoClass
	# This object is used to access both I/O signal and I/O configuration collections.
	CLSID = IID('{59DC16F1-AF91-11D0-A072-00A02436CF7E}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IIOType,
	]
	default_interface = IIOType

class FRCIOTypes(CoClassBaseClass): # A CoClass
	# Represents the collection of all the I/O types currently set up on the controller.
	CLSID = IID('{59DC16ED-AF91-11D0-A072-00A02436CF7E}')
	coclass_sources = [
		IIOTypesEvents,
	]
	default_source = IIOTypesEvents
	coclass_interfaces = [
		IIOTypes,
	]
	default_interface = IIOTypes

class FRCIndGroupPosition(CoClassBaseClass): # A CoClass
	# Provides access to the positional data of an Independant position for a specific motion group.
	CLSID = IID('{DBE7F3B9-01E5-4935-A211-B5CC9D3A1048}')
	coclass_sources = [
		IIndGroupPositionEvents,
	]
	default_source = IIndGroupPositionEvents
	coclass_interfaces = [
		IIndGroupPosition,
	]
	default_interface = IIndGroupPosition

class FRCIndPosition(CoClassBaseClass): # A CoClass
	# Enables you to work with position data without requiring you to create the position on the controller or find an existing one to use.
	CLSID = IID('{B4819F73-FC65-4475-97D3-974ACF6EE03E}')
	coclass_sources = [
		IIndPositionEvents,
	]
	default_source = IIndPositionEvents
	coclass_interfaces = [
		IIndPosition,
	]
	default_interface = IIndPosition

class FRCJoint(CoClassBaseClass): # A CoClass
	# Represents the position data for a single group as simple joint axes. 
	CLSID = IID('{A47A5887-056D-11D0-8901-0020AF68F0A3}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IJoint,
	]
	default_interface = IJoint

class FRCKARELProgram(CoClassBaseClass): # A CoClass
	# Represents a KAREL program on the robot controller.  
	CLSID = IID('{DA462B71-DD0D-11D0-A083-00A02436CF7E}')
	coclass_sources = [
		IKARELProgramEvents,
	]
	default_source = IKARELProgramEvents
	coclass_interfaces = [
		IKARELProgram,
	]
	default_interface = IKARELProgram

class FRCLaserAnalogIOSignal(CoClassBaseClass): # A CoClass
	# Represents a laser analog I/O signal.  
	CLSID = IID('{714CC92E-B4E5-11D0-A073-00A02436CF7E}')
	coclass_sources = [
		IIOSignalEvents,
	]
	default_source = IIOSignalEvents
	coclass_interfaces = [
		IAnalogIOSignal,
	]
	default_interface = IAnalogIOSignal

class FRCLaserAnalogIOType(CoClassBaseClass): # A CoClass
	# This object is used to access both I/O signal and I/O configuration collections.
	CLSID = IID('{714CC91F-B4E5-11D0-A073-00A02436CF7E}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IConfigurableIOType,
	]
	default_interface = IConfigurableIOType

class FRCLaserDigitalIOSignal(CoClassBaseClass): # A CoClass
	# Represents a laser digital I/O signal.  
	CLSID = IID('{714CC92D-B4E5-11D0-A073-00A02436CF7E}')
	coclass_sources = [
		IIOSignalEvents,
	]
	default_source = IIOSignalEvents
	coclass_interfaces = [
		IDigitalIOSignal,
	]
	default_interface = IDigitalIOSignal

class FRCLaserDigitalIOType(CoClassBaseClass): # A CoClass
	# This object is used to access both I/O signal and I/O configuration collections.
	CLSID = IID('{714CC91E-B4E5-11D0-A073-00A02436CF7E}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IConfigurableIOType,
	]
	default_interface = IConfigurableIOType

class FRCMarkerSignal(CoClassBaseClass): # A CoClass
	# Represents a Marker signal.  
	CLSID = IID('{A5F1E1FE-F2B7-40AB-9D33-6932112978BD}')
	coclass_sources = [
		IIOSignalEvents,
	]
	default_source = IIOSignalEvents
	coclass_interfaces = [
		IRobotIOSignal,
	]
	default_interface = IRobotIOSignal

class FRCMarkerType(CoClassBaseClass): # A CoClass
	# This object is used to access Marker signals.
	CLSID = IID('{1C9FC454-C455-4A41-80EF-0894FEB07BF8}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ISystemIOType,
	]
	default_interface = ISystemIOType

class FRCMotionErrorInfo(CoClassBaseClass): # A CoClass
	# Provides access to the status of a motion operation.
	CLSID = IID('{EE912848-BB81-427A-951F-5D9DC0FE74A7}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IMotionErrorInfo,
	]
	default_interface = IMotionErrorInfo

class FRCPLCIOSignal(CoClassBaseClass): # A CoClass
	# Represents a PLC I/O signal.  
	CLSID = IID('{714CC92B-B4E5-11D0-A073-00A02436CF7E}')
	coclass_sources = [
		IIOSignalEvents,
	]
	default_source = IIOSignalEvents
	coclass_interfaces = [
		IUOPIOSignal,
	]
	default_interface = IUOPIOSignal

class FRCPLCIOType(CoClassBaseClass): # A CoClass
	# This object is used to access both I/O signal and I/O configuration collections.
	CLSID = IID('{714CC91C-B4E5-11D0-A073-00A02436CF7E}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IConfigurableIOType,
	]
	default_interface = IConfigurableIOType

class FRCPacket(CoClassBaseClass): # A CoClass
	# Provides access to the information received in a ROS packet.
	CLSID = IID('{64AF4546-9331-11D1-B751-00C04FB99C75}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IPacket,
	]
	default_interface = IPacket

class FRCPacketEvent(CoClassBaseClass): # A CoClass
	# Raises an event when the desired ROS Packet is received from the controller. 
	CLSID = IID('{FCCE9E5F-9420-11D1-B751-00C04FB99C75}')
	coclass_sources = [
		IPacketEventEvents,
	]
	default_source = IPacketEventEvents
	coclass_interfaces = [
		IPacketEvent,
	]
	default_interface = IPacketEvent

class FRCPipe(CoClassBaseClass): # A CoClass
	# Provides access to a pipe defined on the controller.
	CLSID = IID('{B475BC95-3AF1-11D4-9F66-00105AE428C3}')
	coclass_sources = [
		IPipeEvents,
	]
	default_source = IPipeEvents
	coclass_interfaces = [
		IPipe,
	]
	default_interface = IPipe

class FRCPipeField(CoClassBaseClass): # A CoClass
	# Provides access to data values received from a pipe.
	CLSID = IID('{B475BC99-3AF1-11D4-9F66-00105AE428C3}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IPipeField,
	]
	default_interface = IPipeField

class FRCPipeFields(CoClassBaseClass): # A CoClass
	# Provides access to data blocks from a pipe as a set of named fields.
	CLSID = IID('{B475BC97-3AF1-11D4-9F66-00105AE428C3}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IPipeFields,
	]
	default_interface = IPipeFields

class FRCPipePosition(CoClassBaseClass): # A CoClass
	CLSID = IID('{B475BC9B-3AF1-11D4-9F66-00105AE428C3}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IPipePosition,
	]
	default_interface = IPipePosition

class FRCPipes(CoClassBaseClass): # A CoClass
	# Provides access to pipes defined on the controller.
	CLSID = IID('{B475BC91-3AF1-11D4-9F66-00105AE428C3}')
	coclass_sources = [
		IPipesEvents,
	]
	default_source = IPipesEvents
	coclass_interfaces = [
		IPipes,
	]
	default_interface = IPipes

class FRCPosition(CoClassBaseClass): # A CoClass
	# Provides access to the positional data.
	CLSID = IID('{D42AB5DB-8FFB-11D0-94CC-0020AF68F0A3}')
	coclass_sources = [
		IPositionEvents,
	]
	default_source = IPositionEvents
	coclass_interfaces = [
		IPosition2,
	]
	default_interface = IPosition2

class FRCProgram(CoClassBaseClass): # A CoClass
	# Represents a program on the robot controller. 
	CLSID = IID('{D42AB5D5-8FFB-11D0-94CC-0020AF68F0A3}')
	coclass_sources = [
		IProgramEvents,
	]
	default_source = IProgramEvents
	coclass_interfaces = [
		IProgram,
	]
	default_interface = IProgram

class FRCPrograms(CoClassBaseClass): # A CoClass
	# Represents the collection of all programs currently loaded on the robot controller, i.e. Teach Pendant, KAREL, and VR programs.
	CLSID = IID('{1FBD567D-8F13-11D0-94CB-0020AF68F0A3}')
	coclass_sources = [
		IProgramsEvents,
	]
	default_source = IProgramsEvents
	coclass_interfaces = [
		IPrograms,
	]
	default_interface = IPrograms

class FRCRegNumeric(CoClassBaseClass): # A CoClass
	# This object allows access to numeric registers on the robot controller.
	CLSID = IID('{6B51A441-212A-11D0-959F-00A024329125}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IRegNumeric,
	]
	default_interface = IRegNumeric

class FRCRegString(CoClassBaseClass): # A CoClass
	# This object allows access to string registers on the robot controller.
	CLSID = IID('{B5BD1EBA-FEC8-49CC-965B-7DD03974CDB8}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IRegString,
	]
	default_interface = IRegString

# This CoClass is known by the name 'FRRobot.FRCRobManProxy'
class FRCRobManProxy(CoClassBaseClass): # A CoClass
	CLSID = IID('{53D6E5D2-F5E2-11D3-9F35-00500409FF06}')
	coclass_sources = [
		IRobManProxyEvents,
	]
	default_source = IRobManProxyEvents
	coclass_interfaces = [
		IRobManProxy,
	]
	default_interface = IRobManProxy

# This CoClass is known by the name 'FRRobot.FRCRobot'
class FRCRobot(CoClassBaseClass): # A CoClass
	# Top level Robot Object interface used to establish connections and get references objects representing other system areas.
	CLSID = IID('{6D7E3A01-9ECC-11D0-94D5-0020AF68F0A3}')
	coclass_sources = [
		IRobotEvents,
	]
	default_source = IRobotEvents
	coclass_interfaces = [
		IRobot2,
	]
	default_interface = IRobot2

class FRCRobotErrorInfo(CoClassBaseClass): # A CoClass
	# Object used to access extended error information after an error has been thrown (raised) and caught.
	CLSID = IID('{5BBFA760-09C6-11D2-871C-00C04F98D092}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IRobotErrorInfo,
	]
	default_interface = IRobotErrorInfo

class FRCRobotIOSignal(CoClassBaseClass): # A CoClass
	# Represents a robot I/O signal.  
	CLSID = IID('{714CC927-B4E5-11D0-A073-00A02436CF7E}')
	coclass_sources = [
		IIOSignalEvents,
	]
	default_source = IIOSignalEvents
	coclass_interfaces = [
		IRobotIOSignal,
	]
	default_interface = IRobotIOSignal

class FRCRobotIOType(CoClassBaseClass): # A CoClass
	# This object is used to access both I/O signal and I/O configuration collections.
	CLSID = IID('{714CC919-B4E5-11D0-A073-00A02436CF7E}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ISystemIOType,
	]
	default_interface = ISystemIOType

class FRCSOPIOSignal(CoClassBaseClass): # A CoClass
	# Represents a Standard Operator Panel I/O signal.  
	CLSID = IID('{714CC928-B4E5-11D0-A073-00A02436CF7E}')
	coclass_sources = [
		IIOSignalEvents,
	]
	default_source = IIOSignalEvents
	coclass_interfaces = [
		IUOPIOSignal,
	]
	default_interface = IUOPIOSignal

class FRCSOPIOType(CoClassBaseClass): # A CoClass
	# This object is used to access both I/O signal and I/O configuration collections.
	CLSID = IID('{714CC91A-B4E5-11D0-A073-00A02436CF7E}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ISystemIOType,
	]
	default_interface = ISystemIOType

class FRCScatteredAccess(CoClassBaseClass): # A CoClass
	# Enables you to access a group of independent variables and I/O signals with minimum network overhead.
	CLSID = IID('{6F33A4D1-91F3-11D3-877C-00C04F81118D}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IScatteredAccess,
	]
	default_interface = IScatteredAccess

class FRCSelectedLines(CoClassBaseClass): # A CoClass
	CLSID = IID('{58ADC520-9395-11D2-877C-00C04FB9C401}')
	coclass_sources = [
		ISelectedLinesEvents,
	]
	default_source = ISelectedLinesEvents
	coclass_interfaces = [
		ISelectedLines,
	]
	default_interface = ISelectedLines

class FRCSynchApplData(CoClassBaseClass): # A CoClass
	CLSID = IID('{8FAFC8E8-B2B8-11D1-B705-00C04FA3BD85}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ISynchApplData,
	]
	default_interface = ISynchApplData

class FRCSynchApplDataItem(CoClassBaseClass): # A CoClass
	CLSID = IID('{8FAFC8EA-B2B8-11D1-B705-00C04FA3BD85}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ISynchApplDataItem,
	]
	default_interface = ISynchApplDataItem

class FRCSynchData(CoClassBaseClass): # A CoClass
	#  This object is used to access all other controller feature/option synchronization objects.
	CLSID = IID('{2AF44182-9273-11D1-B6F9-00C04FA3BD85}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ISynchData,
	]
	default_interface = ISynchData

class FRCSysGroupPosition(CoClassBaseClass): # A CoClass
	# Provides access to the positional data of a controller system position for a specific motion group.
	CLSID = IID('{DC2FA0C8-FFAB-11D0-B6F4-00C04FB9C401}')
	coclass_sources = [
		ISysGroupPositionEvents,
	]
	default_source = ISysGroupPositionEvents
	coclass_interfaces = [
		ISysGroupPosition,
	]
	default_interface = ISysGroupPosition

class FRCSysInfo(CoClassBaseClass): # A CoClass
	# Provides access to robot controller system information.
	CLSID = IID('{4553DA63-ACA1-11D3-8783-00C04F81118D}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ISysInfo,
	]
	default_interface = ISysInfo

class FRCSysPosition(CoClassBaseClass): # A CoClass
	# Provides access to a single controller system position.
	CLSID = IID('{6055D699-FFAE-11D0-B6F4-00C04FB9C401}')
	coclass_sources = [
		ISysPositionEvents,
	]
	default_source = ISysPositionEvents
	coclass_interfaces = [
		ISysPosition,
	]
	default_interface = ISysPosition

class FRCSysPositions(CoClassBaseClass): # A CoClass
	# Provides access to a collection of controller system positions.
	CLSID = IID('{6055D69B-FFAE-11D0-B6F4-00C04FB9C401}')
	coclass_sources = [
		ISysPositionsEvents,
	]
	default_source = ISysPositionsEvents
	coclass_interfaces = [
		ISysPositions,
	]
	default_interface = ISysPositions

class FRCTPApplDataCollection(CoClassBaseClass): # A CoClass
	CLSID = IID('{70F06EE1-DCE0-11D0-A083-00A02436CF7E}')
	coclass_sources = [
		ITPApplDataCollectionEvents,
	]
	default_source = ITPApplDataCollectionEvents
	coclass_interfaces = [
		ITPApplDataCollection,
	]
	default_interface = ITPApplDataCollection

class FRCTPApplDataHelper(CoClassBaseClass): # A CoClass
	CLSID = IID('{51FF0460-DCE1-11D0-A083-00A02436CF7E}')
	coclass_sources = [
		ITPApplDataEvents,
	]
	default_source = ITPApplDataEvents
	coclass_interfaces = [
		ITPApplDataHelper,
	]
	default_interface = ITPApplDataHelper

class FRCTPIOSignal(CoClassBaseClass): # A CoClass
	# Represents a Teach Pendant I/O signal.  
	CLSID = IID('{714CC929-B4E5-11D0-A073-00A02436CF7E}')
	coclass_sources = [
		IIOSignalEvents,
	]
	default_source = IIOSignalEvents
	coclass_interfaces = [
		IUOPIOSignal,
	]
	default_interface = IUOPIOSignal

class FRCTPIOType(CoClassBaseClass): # A CoClass
	# This object is used to access both I/O signal and I/O configuration collections.
	CLSID = IID('{714CC91B-B4E5-11D0-A073-00A02436CF7E}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ISystemIOType,
	]
	default_interface = ISystemIOType

class FRCTPInstruction(CoClassBaseClass): # A CoClass
	CLSID = IID('{3C05D270-9BE8-11D1-B6FC-00C04FA3BD85}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ITPInstruction,
	]
	default_interface = ITPInstruction

class FRCTPInstructions(CoClassBaseClass): # A CoClass
	CLSID = IID('{3C05D26E-9BE8-11D1-B6FC-00C04FA3BD85}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ITPInstructions,
	]
	default_interface = ITPInstructions

class FRCTPLabel(CoClassBaseClass): # A CoClass
	CLSID = IID('{C3FB0D03-58D6-11D0-8901-0020AF68F0A3}')
	coclass_sources = [
		ITPLabelEvents,
	]
	default_source = ITPLabelEvents
	coclass_interfaces = [
		ITPLabel,
	]
	default_interface = ITPLabel

class FRCTPLabels(CoClassBaseClass): # A CoClass
	CLSID = IID('{C3FB0D01-58D6-11D0-8901-0020AF68F0A3}')
	coclass_sources = [
		ITPLabelsEvents,
	]
	default_source = ITPLabelsEvents
	coclass_interfaces = [
		ITPLabels,
	]
	default_interface = ITPLabels

class FRCTPLineHelper(CoClassBaseClass): # A CoClass
	CLSID = IID('{FC761641-4CEA-11D0-8901-0020AF68F0A3}')
	coclass_sources = [
		ITPLineEvents,
	]
	default_source = ITPLineEvents
	coclass_interfaces = [
		ITPLineHelper,
	]
	default_interface = ITPLineHelper

class FRCTPLines(CoClassBaseClass): # A CoClass
	CLSID = IID('{F5C31107-46AE-11D0-8901-0020AF68F0A3}')
	coclass_sources = [
		ITPLinesEvents,
	]
	default_source = ITPLinesEvents
	coclass_interfaces = [
		ITPLines,
	]
	default_interface = ITPLines

class FRCTPPosition(CoClassBaseClass): # A CoClass
	# Provides access to a single position in a TP program.
	CLSID = IID('{3A49BE61-F5B9-11CF-8901-0020AF68F0A3}')
	coclass_sources = [
		ITPPositionEvents,
	]
	default_source = ITPPositionEvents
	coclass_interfaces = [
		ITPPosition,
	]
	default_interface = ITPPosition

class FRCTPPositions(CoClassBaseClass): # A CoClass
	# Provides access to the collection of positions in a TP program. 
	CLSID = IID('{A16AD1C7-F45A-11CF-8901-0020AF68F0A3}')
	coclass_sources = [
		ITPPositionsEvents,
	]
	default_source = ITPPositionsEvents
	coclass_interfaces = [
		ITPPositions,
	]
	default_interface = ITPPositions

class FRCTPProgram(CoClassBaseClass): # A CoClass
	# Represents a TP program on the robot controller.
	CLSID = IID('{F5C31101-46AE-11D0-8901-0020AF68F0A3}')
	coclass_sources = [
		ITPProgramEvents,
	]
	default_source = ITPProgramEvents
	coclass_interfaces = [
		ITPProgram,
	]
	default_interface = ITPProgram

class FRCTPScreen(CoClassBaseClass): # A CoClass
	CLSID = IID('{660E6870-E286-11D0-8BB6-0020AF39BE5A}')
	coclass_sources = [
		ITPScreenEvents,
	]
	default_source = ITPScreenEvents
	coclass_interfaces = [
		ITPScreen,
	]
	default_interface = ITPScreen

class FRCTPSimpleLine(CoClassBaseClass): # A CoClass
	CLSID = IID('{6C473F20-B5F0-11D2-8781-00C04F98D092}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ITPSimpleLine,
	]
	default_interface = ITPSimpleLine

class FRCTask(CoClassBaseClass): # A CoClass
	# The task object represents a running thread of execution on the controller.  A running task may be running different programs or program routines at various points in time.
	CLSID = IID('{847A8F82-4626-11D1-B745-00C04FBBE42A}')
	coclass_sources = [
		ITaskEvents,
	]
	default_source = ITaskEvents
	coclass_interfaces = [
		ITask,
	]
	default_interface = ITask

class FRCTasks(CoClassBaseClass): # A CoClass
	# The tasks collection represents all interpreter (PXNN) tasks that are currently active on the controller.  This collection will contain one object for each active task.
	CLSID = IID('{6B01CFFC-4626-11D1-B745-00C04FBBE42A}')
	coclass_sources = [
		ITasksEvents,
	]
	default_source = ITasksEvents
	coclass_interfaces = [
		ITasks,
	]
	default_interface = ITasks

class FRCTransform(CoClassBaseClass): # A CoClass
	# Represents the position of a single group of axes as a transformation matrix consisting of normal, orient, approach, and location vectors and a component specifying a configuration.
	CLSID = IID('{A47A5883-056D-11D0-8901-0020AF68F0A3}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ITransform,
	]
	default_interface = ITransform

class FRCUOPIOSignal(CoClassBaseClass): # A CoClass
	# Represents a User Operator Panel I/O signal.  
	CLSID = IID('{714CC925-B4E5-11D0-A073-00A02436CF7E}')
	coclass_sources = [
		IIOSignalEvents,
	]
	default_source = IIOSignalEvents
	coclass_interfaces = [
		IUOPIOSignal,
	]
	default_interface = IUOPIOSignal

class FRCUOPIOType(CoClassBaseClass): # A CoClass
	# This object is used to access both I/O signal and I/O configuration collections.
	CLSID = IID('{714CC918-B4E5-11D0-A073-00A02436CF7E}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IConfigurableIOType,
	]
	default_interface = IConfigurableIOType

class FRCUserIOSignal(CoClassBaseClass): # A CoClass
	CLSID = IID('{59DC16FF-AF91-11D0-A072-00A02436CF7E}')
	coclass_sources = [
		IIOSignalEvents,
	]
	default_source = IIOSignalEvents
	coclass_interfaces = [
		IUserIOSignal,
	]
	default_interface = IUserIOSignal

class FRCUserIOSignals(CoClassBaseClass): # A CoClass
	CLSID = IID('{59DC16FA-AF91-11D0-A072-00A02436CF7E}')
	coclass_sources = [
		IUserIOSignalsEvents,
	]
	default_source = IUserIOSignalsEvents
	coclass_interfaces = [
		IUserIOSignals,
	]
	default_interface = IUserIOSignals

class FRCUserIOType(CoClassBaseClass): # A CoClass
	CLSID = IID('{59DC16F6-AF91-11D0-A072-00A02436CF7E}')
	coclass_sources = [
		IUserIOTypeEvents,
	]
	default_source = IUserIOTypeEvents
	coclass_interfaces = [
		IUserIOType,
	]
	default_interface = IUserIOType

class FRCVRProgram(CoClassBaseClass): # A CoClass
	# Represents a system or variable program on the robot controller. 
	CLSID = IID('{8C8ACC9A-4F57-11D0-BC32-444553540000}')
	coclass_sources = [
		IProgramEvents,
	]
	default_source = IProgramEvents
	coclass_interfaces = [
		IProgram,
	]
	default_interface = IProgram

class FRCVar(CoClassBaseClass): # A CoClass
	# Provides access to the attributes and value of program and system variables.
	CLSID = IID('{8C8ACC81-4F57-11D0-BC32-444553540000}')
	coclass_sources = [
		IVarEvents,
	]
	default_source = IVarEvents
	coclass_interfaces = [
		IVar,
	]
	default_interface = IVar

class FRCVarPosition(CoClassBaseClass): # A CoClass
	# Provides access to the positional data for a position stored as a variable on the controller.
	CLSID = IID('{E3FFB439-2613-11D1-B702-00C04FB9C401}')
	coclass_sources = [
		IPositionEvents,
	]
	default_source = IPositionEvents
	coclass_interfaces = [
		IVarPosition,
	]
	default_interface = IVarPosition

class FRCVars(CoClassBaseClass): # A CoClass
	# Provides access to robot controller variables, including system and program variables.
	CLSID = IID('{88B57BCB-D0CA-11CF-959F-00A024329125}')
	coclass_sources = [
		IVarsEvents,
	]
	default_source = IVarsEvents
	coclass_interfaces = [
		IVars,
	]
	default_interface = IVars

class FRCVector(CoClassBaseClass): # A CoClass
	# Provides access to individual components of a vector.
	CLSID = IID('{C1578510-0F7A-11D2-86F4-00C04F9184DB}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IVector,
	]
	default_interface = IVector

class FRCWeldDigitalIOSignal(CoClassBaseClass): # A CoClass
	# Represents a weld digital I/O signal.  
	CLSID = IID('{714CC92C-B4E5-11D0-A073-00A02436CF7E}')
	coclass_sources = [
		IIOSignalEvents,
	]
	default_source = IIOSignalEvents
	coclass_interfaces = [
		IDigitalIOSignal,
	]
	default_interface = IDigitalIOSignal

class FRCWeldDigitalIOType(CoClassBaseClass): # A CoClass
	# This object is used to access both I/O signal and I/O configuration collections.
	CLSID = IID('{714CC91D-B4E5-11D0-A073-00A02436CF7E}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IConfigurableIOType,
	]
	default_interface = IConfigurableIOType

class FRCWeldStickIOSignal(CoClassBaseClass): # A CoClass
	# Represents a weld stick I/O signal.  
	CLSID = IID('{714CC92F-B4E5-11D0-A073-00A02436CF7E}')
	coclass_sources = [
		IIOSignalEvents,
	]
	default_source = IIOSignalEvents
	coclass_interfaces = [
		IDigitalIOSignal,
	]
	default_interface = IDigitalIOSignal

class FRCWeldStickIOType(CoClassBaseClass): # A CoClass
	# This object is used to access both I/O signal and I/O configuration collections.
	CLSID = IID('{714CC920-B4E5-11D0-A073-00A02436CF7E}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IConfigurableIOType,
	]
	default_interface = IConfigurableIOType

class FRCXyzWpr(CoClassBaseClass): # A CoClass
	# Represents the position of a single group of axes consisting of three real components specifying a Cartesian location (x,y,z), three real components specifying an orientation (w,p,r), and a component specifying a configuration.
	CLSID = IID('{A47A5885-056D-11D0-8901-0020AF68F0A3}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IXyzWpr,
	]
	default_interface = IXyzWpr

IAlarm_vtables_dispatch_ = 1
IAlarm_vtables_ = [
	(( 'ErrorFacility' , 'ErrorFacility' , ), 201, (201, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'ErrorSeverity' , 'ErrorSeverity' , ), 202, (202, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'ErrorExecution' , 'ErrorExecution' , ), 203, (203, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'ErrorMotion' , 'ErrorMotion' , ), 204, (204, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'ErrorNumber' , 'ErrorNumber' , ), 205, (205, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'ErrorMessage' , 'ErrorMessage' , ), 206, (206, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'CauseFacility' , 'CauseFacility' , ), 207, (207, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'CauseNumber' , 'CauseNumber' , ), 208, (208, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'CauseMessage' , 'CauseMessage' , ), 209, (209, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'TimeStamp' , 'TimeStamp' , ), 210, (210, (), [ (16391, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'SeverityMessage' , 'SeverityMessage' , ), 211, (211, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Index' , 'Index' , ), 212, (212, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'ErrorMnemonic' , 'ErrorMnemonic' , ), 213, (213, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'CauseMnemonic' , 'CauseMnemonic' , ), 214, (214, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'ErrorClass' , 'ErrorClass' , ), 215, (215, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'HostName' , 'HostName' , ), 216, (216, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'IPAddress' , 'IPAddress' , ), 217, (217, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
]

IAlarms_vtables_dispatch_ = 1
IAlarms_vtables_ = [
	(( '_NewEnum' , 'NewEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'Index' , 'Alarm' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16397, 10, None, "IID('{7C37F237-A494-11D0-A37F-0020AF39BE5A}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'Count' , ), 201, (201, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Max' , 'Number' , ), 203, (203, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Max' , 'Number' , ), 203, (203, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'ActiveAlarms' , 'ActiveAlarms' , ), 204, (204, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Reset' , ), 205, (205, (), [ ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
]

IAnalogIOSignal_vtables_dispatch_ = 1
IAnalogIOSignal_vtables_ = [
	(( 'Value' , 'Value' , ), 201, (201, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Value' , 'Value' , ), 201, (201, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Simulate' , 'Simulate' , ), 202, (202, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Simulate' , 'Simulate' , ), 202, (202, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 203, (203, (), [ (16397, 10, None, "IID('{59DC16F8-AF91-11D0-A072-00A02436CF7E}')") , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'NoRefresh' , 'NoRefresh' , ), 250, (250, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'NoRefresh' , 'NoRefresh' , ), 250, (250, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'NoUpdate' , 'NoUpdate' , ), 251, (251, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'NoUpdate' , 'NoUpdate' , ), 251, (251, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'Refresh' , ), 252, (252, (), [ ], 1 , 1 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'Update' , ), 253, (253, (), [ ], 1 , 1 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
]

IApplications_vtables_dispatch_ = 1
IApplications_vtables_ = [
	(( '_NewEnum' , 'NewEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'Key' , 'Item' , ), 0, (0, (), [ (8, 1, None, None) , 
			 (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'Count' , ), 101, (101, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Add' , 'AppObject' , 'Key' , ), 151, (151, (), [ (9, 1, None, None) , 
			 (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Remove' , 'Key' , ), 152, (152, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
]

IAxesCollection_vtables_dispatch_ = 1
IAxesCollection_vtables_ = [
	(( '_NewEnum' , 'NewEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'JointNum' , 'Value' , ), 0, (0, (), [ (2, 1, None, None) , 
			 (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'JointNum' , 'Value' , ), 0, (0, (), [ (2, 1, None, None) , 
			 (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'Count' , ), 101, (101, (), [ (16386, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

ICartesianFormat_vtables_dispatch_ = 1
ICartesianFormat_vtables_ = [
	(( 'Program' , 'Program' , ), 101, (101, (), [ (16397, 10, None, "IID('{D42AB5D5-8FFB-11D0-94CC-0020AF68F0A3}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Config' , 'Config' , ), 201, (201, (), [ (16397, 10, None, "IID('{C58B0E61-ECD4-11D0-9FA5-00A024329125}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Ext' , 'Ext' , ), 202, (202, (), [ (16397, 10, None, "IID('{035505A1-1C41-11D0-8901-0020AF68F0A3}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 203, (203, (), [ (16397, 10, None, "IID('{D42AB5DB-8FFB-11D0-94CC-0020AF68F0A3}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

ICommonAssoc_vtables_dispatch_ = 1
ICommonAssoc_vtables_ = [
	(( 'Program' , 'Program' , ), 101, (101, (), [ (16397, 10, None, "IID('{D42AB5D5-8FFB-11D0-94CC-0020AF68F0A3}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'SegTermType' , 'SegTermType' , ), 201, (201, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'SegTermType' , 'SegTermType' , ), 201, (201, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'SegDecelTol' , 'SegDecelTol' , ), 202, (202, (), [ (16386, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'SegDecelTol' , 'SegDecelTol' , ), 202, (202, (), [ (2, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'SegRelAccel' , 'SegRelAccel' , ), 203, (203, (), [ (16386, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'SegRelAccel' , 'SegRelAccel' , ), 203, (203, (), [ (2, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'SegTimeShift' , 'SegTimeShift' , ), 204, (204, (), [ (16386, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'SegTimeShift' , 'SegTimeShift' , ), 204, (204, (), [ (2, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 205, (205, (), [ (16397, 10, None, "IID('{8C8ACC81-4F57-11D0-BC32-444553540000}')") , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
]

IConfig_vtables_dispatch_ = 1
IConfig_vtables_ = [
	(( 'Program' , 'Program' , ), 101, (101, (), [ (16397, 10, None, "IID('{D42AB5D5-8FFB-11D0-94CC-0020AF68F0A3}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Text' , 'Text' , ), 0, (0, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Text' , 'Text' , ), 0, (0, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'TurnNum' , 'Index' , 'TurnNum' , ), 201, (201, (), [ (2, 1, None, None) , 
			 (16386, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'TurnNum' , 'Index' , 'TurnNum' , ), 201, (201, (), [ (2, 1, None, None) , 
			 (2, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Flip' , 'Flip' , ), 202, (202, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Flip' , 'Flip' , ), 202, (202, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Left' , 'Left' , ), 203, (203, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Left' , 'Left' , ), 203, (203, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Up' , 'Up' , ), 204, (204, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Up' , 'Up' , ), 204, (204, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Front' , 'Front' , ), 205, (205, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Front' , 'Front' , ), 205, (205, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 206, (206, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
]

IConfigurableIOType_vtables_dispatch_ = 1
IConfigurableIOType_vtables_ = [
	(( 'Configs' , 'IOConfigs' , ), 301, (301, (), [ (16397, 10, None, "IID('{59DC1701-AF91-11D0-A072-00A02436CF7E}')") , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
]

ICurGroupPosition_vtables_dispatch_ = 1
ICurGroupPosition_vtables_ = [
	(( 'Parent' , 'Parent' , ), 301, (301, (), [ (16397, 10, None, "IID('{E2686FA9-1E42-11D1-B6FF-00C04FB9C401}')") , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'IsEqualTo' , 'TargetPos' , 'IsEqualTo' , ), 302, (302, (), [ (9, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'IsReachable' , 'From' , 'MoType' , 'OrientType' , 'Destination' , 
			 'MotionErrorInfo' , 'IsReachable' , ), 303, (303, (), [ (12, 17, None, None) , (3, 49, '6', None) , 
			 (3, 49, '2', None) , (12, 17, None, None) , (16397, 50, '0', "IID('{EE912848-BB81-427A-951F-5D9DC0FE74A7}')") , (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'Copy' , 'Position' , ), 304, (304, (), [ (9, 1, None, None) , ], 1 , 1 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'CheckReach' , 'From' , 'MoType' , 'OrientType' , 'Destination' , 
			 'MotionErrorInfo' , 'IsReachable' , ), 305, (305, (), [ (12, 17, None, None) , (3, 49, '6', None) , 
			 (3, 49, '2', None) , (12, 17, None, None) , (16397, 50, '0', "IID('{EE912848-BB81-427A-951F-5D9DC0FE74A7}')") , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
]

ICurPosition_vtables_dispatch_ = 1
ICurPosition_vtables_ = [
	(( 'GroupMask' , 'GroupNum' , 'Mask' , ), 201, (201, (), [ (2, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Group' , 'GroupNum' , 'DisplayType' , 'Position' , ), 202, (202, (), [ 
			 (2, 1, None, None) , (3, 1, None, None) , (16397, 10, None, "IID('{75CEF1D7-1E43-11D1-B6FF-00C04FB9C401}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'NumGroups' , 'NumGroups' , ), 203, (203, (), [ (16386, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'IsMonitoring' , 'IsMonitoring' , ), 204, (204, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'StartMonitor' , 'Latency' , ), 250, (250, (), [ (3, 0, None, None) , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'StopMonitor' , ), 251, (251, (), [ ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'GroupBitMask' , 'GroupBitMask' , ), 252, (252, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
]

IDigitalIOSignal_vtables_dispatch_ = 1
IDigitalIOSignal_vtables_ = [
	(( 'Value' , 'Value' , ), 201, (201, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Value' , 'Value' , ), 201, (201, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Simulate' , 'Simulate' , ), 202, (202, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Simulate' , 'Simulate' , ), 202, (202, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Polarity' , 'Polarity' , ), 203, (203, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Polarity' , 'Polarity' , ), 203, (203, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'Complementary' , 'Complementary' , ), 204, (204, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Complementary' , 'Complementary' , ), 204, (204, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 205, (205, (), [ (16397, 10, None, "IID('{59DC16F8-AF91-11D0-A072-00A02436CF7E}')") , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'NoRefresh' , 'NoRefresh' , ), 250, (250, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'NoRefresh' , 'NoRefresh' , ), 250, (250, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'NoUpdate' , 'NoUpdate' , ), 251, (251, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'NoUpdate' , 'NoUpdate' , ), 251, (251, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'Refresh' , ), 252, (252, (), [ ], 1 , 1 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'Update' , ), 253, (253, (), [ ], 1 , 1 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
]

IFeature_vtables_dispatch_ = 1
IFeature_vtables_ = [
	(( 'OrderNumber' , 'OrderNumber' , ), 101, (101, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'Name' , ), 102, (102, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Version' , 'Version' , ), 103, (103, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
]

IFeatures_vtables_dispatch_ = 1
IFeatures_vtables_ = [
	(( '_NewEnum' , 'NewEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'OrderNumber' , 'Index' , 'Feature' , ), 0, (0, (), [ 
			 (12, 17, None, None) , (12, 17, None, None) , (16397, 10, None, "IID('{2AF44186-9273-11D1-B6F9-00C04FA3BD85}')") , ], 1 , 2 , 4 , 2 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'OrderNumber' , 'Index' , 'Feature' , ), 0, (0, (), [ 
			 (12, 17, None, None) , (12, 17, None, None) , (16397, 10, None, "IID('{2AF44186-9273-11D1-B6F9-00C04FA3BD85}')") , ], 1 , 2 , 4 , 2 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'Count' , ), 101, (101, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'IsValid' , 'OrderNumber' , 'IsValid' , ), 102, (102, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Refresh' , ), 150, (150, (), [ ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
]

IGroupAssoc_vtables_dispatch_ = 1
IGroupAssoc_vtables_ = [
	(( 'Program' , 'Program' , ), 101, (101, (), [ (16397, 10, None, "IID('{D42AB5D5-8FFB-11D0-94CC-0020AF68F0A3}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'SegRelSpeed' , 'SegRelSpeed' , ), 201, (201, (), [ (16386, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'SegRelSpeed' , 'SegRelSpeed' , ), 201, (201, (), [ (2, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'SegMoType' , 'SegMoType' , ), 202, (202, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'SegMoType' , 'SegMoType' , ), 202, (202, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'SegOrientType' , 'SegOrientType' , ), 203, (203, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'SegOrientType' , 'SegOrientType' , ), 203, (203, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'SegBreak' , 'SegBreak' , ), 204, (204, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'SegBreak' , 'SegBreak' , ), 204, (204, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 205, (205, (), [ (16397, 10, None, "IID('{8C8ACC81-4F57-11D0-BC32-444553540000}')") , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
]

IGroupPosition_vtables_dispatch_ = 1
IGroupPosition_vtables_ = [
	(( 'Program' , 'Program' , ), 101, (101, (), [ (16397, 10, None, "IID('{D42AB5D5-8FFB-11D0-94CC-0020AF68F0A3}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'AutomaticUpdate' , 'AutomaticUpdate' , ), 201, (201, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'AutomaticUpdate' , 'AutomaticUpdate' , ), 201, (201, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Type' , 'Type' , ), 202, (202, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Type' , 'Type' , ), 202, (202, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Formats' , 'Type' , 'Format' , ), 203, (203, (), [ (3, 1, None, None) , 
			 (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'GroupNum' , 'GroupNum' , ), 204, (204, (), [ (16386, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Id' , 'Id' , ), 205, (205, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'IsAtCurPosition' , 'IsAtCurPosition' , ), 206, (206, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'IsInitialized' , 'IsInitialized' , ), 207, (207, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'UserFrame' , 'UserFrame' , ), 208, (208, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'UserFrame' , 'UserFrame' , ), 208, (208, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'UserTool' , 'UserTool' , ), 209, (209, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'UserTool' , 'UserTool' , ), 209, (209, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'IsMonitoring' , 'IsMonitoring' , ), 210, (210, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Update' , ), 251, (251, (), [ ], 1 , 1 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'Refresh' , ), 252, (252, (), [ ], 1 , 1 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'Moveto' , ), 253, (253, (), [ ], 1 , 1 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'Record' , ), 254, (254, (), [ ], 1 , 1 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'StartMonitor' , 'Latency' , ), 255, (255, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'StopMonitor' , ), 256, (256, (), [ ], 1 , 1 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'Uninitialize' , ), 257, (257, (), [ ], 1 , 1 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'MatMul' , 'LeftPos' , 'RightPos' , ), 258, (258, (), [ (9, 1, None, None) , 
			 (9, 1, None, None) , ], 1 , 1 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'MatInv' , 'InputPos' , ), 259, (259, (), [ (9, 1, None, None) , ], 1 , 1 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 301, (301, (), [ (16397, 10, None, "IID('{3A49BE61-F5B9-11CF-8901-0020AF68F0A3}')") , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'IsEqualTo' , 'TargetPos' , 'IsEqualTo' , ), 302, (302, (), [ (9, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'IsReachable' , 'From' , 'MoType' , 'OrientType' , 'Destination' , 
			 'MotionErrorInfo' , 'IsReachable' , ), 303, (303, (), [ (12, 17, None, None) , (3, 49, '6', None) , 
			 (3, 49, '2', None) , (12, 17, None, None) , (16397, 50, '0', "IID('{EE912848-BB81-427A-951F-5D9DC0FE74A7}')") , (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'Copy' , 'Position' , ), 304, (304, (), [ (9, 1, None, None) , ], 1 , 1 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'CheckReach' , 'From' , 'MoType' , 'OrientType' , 'Destination' , 
			 'MotionErrorInfo' , 'IsReachable' , ), 305, (305, (), [ (12, 17, None, None) , (3, 49, '6', None) , 
			 (3, 49, '2', None) , (12, 17, None, None) , (16397, 50, '0', "IID('{EE912848-BB81-427A-951F-5D9DC0FE74A7}')") , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
]

IIOConfig_vtables_dispatch_ = 1
IIOConfig_vtables_ = [
	(( 'FirstLogicalNum' , 'FirstLogicalNum' , ), 101, (101, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'NumSignals' , 'NumSignals' , ), 102, (102, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'NumSignals' , 'NumSignals' , ), 102, (102, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Rack' , 'Rack' , ), 103, (103, (), [ (16386, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Rack' , 'Rack' , ), 103, (103, (), [ (2, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Slot' , 'Slot' , ), 104, (104, (), [ (16386, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Slot' , 'Slot' , ), 104, (104, (), [ (2, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'PhysicalType' , 'PhysicalType' , ), 105, (105, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'PhysicalType' , 'PhysicalType' , ), 105, (105, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'FirstPhysicalNum' , 'FirstPhysicalNum' , ), 106, (106, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'FirstPhysicalNum' , 'FirstPhysicalNum' , ), 106, (106, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'IsValid' , 'IsValid' , ), 107, (107, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 108, (108, (), [ (16397, 10, None, "IID('{59DC1701-AF91-11D0-A072-00A02436CF7E}')") , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
]

IIOConfigs_vtables_dispatch_ = 1
IIOConfigs_vtables_ = [
	(( '_NewEnum' , 'NewEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'FirstLogicalNum' , 'Index' , 'IOConfig' , ), 0, (0, (), [ 
			 (12, 17, None, None) , (12, 17, None, None) , (16397, 10, None, "IID('{59DC1703-AF91-11D0-A072-00A02436CF7E}')") , ], 1 , 2 , 4 , 2 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'FirstLogicalNum' , 'Index' , 'IOConfig' , ), 0, (0, (), [ 
			 (12, 17, None, None) , (12, 17, None, None) , (16397, 10, None, "IID('{59DC1703-AF91-11D0-A072-00A02436CF7E}')") , ], 1 , 2 , 4 , 2 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'Count' , ), 101, (101, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 102, (102, (), [ (16397, 10, None, "IID('{59DC16F1-AF91-11D0-A072-00A02436CF7E}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Add' , 'FirstLogicalNum' , 'IOConfig' , ), 151, (151, (), [ (12, 17, None, None) , 
			 (16397, 10, None, "IID('{59DC1703-AF91-11D0-A072-00A02436CF7E}')") , ], 1 , 1 , 4 , 1 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Remove' , 'FirstLogicalNum' , 'Index' , ), 152, (152, (), [ (12, 17, None, None) , 
			 (12, 17, None, None) , ], 1 , 1 , 4 , 2 , 104 , (3, 0, None, None) , 0 , )),
]

IIOSignal_vtables_dispatch_ = 1
IIOSignal_vtables_ = [
	(( 'LogicalNum' , 'LogicalNum' , ), 101, (101, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Comment' , 'Comment' , ), 102, (102, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Comment' , 'Comment' , ), 102, (102, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'IsAssigned' , 'IsAssigned' , ), 103, (103, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'IsOffline' , 'IsOffline' , ), 104, (104, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'IsMonitoring' , 'IsMonitoring' , ), 105, (105, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'StartMonitor' , 'Latency' , ), 150, (150, (), [ (3, 0, None, None) , ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'StopMonitor' , ), 151, (151, (), [ ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
]

IIOSignal2_vtables_dispatch_ = 1
IIOSignal2_vtables_ = [
	(( 'Value' , 'Value' , ), 201, (201, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Value' , 'Value' , ), 201, (201, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Simulate' , 'Simulate' , ), 202, (202, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Simulate' , 'Simulate' , ), 202, (202, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'LogicalNum' , 'LogicalNum' , ), 101, (101, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Comment' , 'Comment' , ), 102, (102, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Comment' , 'Comment' , ), 102, (102, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'IsAssigned' , 'IsAssigned' , ), 103, (103, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'IsOffline' , 'IsOffline' , ), 104, (104, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'IsMonitoring' , 'IsMonitoring' , ), 105, (105, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'StartMonitor' , 'Latency' , ), 150, (150, (), [ (3, 0, None, None) , ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'StopMonitor' , ), 151, (151, (), [ ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'NoRefresh' , 'NoRefresh' , ), 250, (250, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'NoRefresh' , 'NoRefresh' , ), 250, (250, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'NoUpdate' , 'NoUpdate' , ), 251, (251, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'NoUpdate' , 'NoUpdate' , ), 251, (251, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Refresh' , ), 252, (252, (), [ ], 1 , 1 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Update' , ), 253, (253, (), [ ], 1 , 1 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
]

IIOSignals_vtables_dispatch_ = 1
IIOSignals_vtables_ = [
	(( '_NewEnum' , 'NewEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'LogicalNum' , 'Index' , 'IOSignal' , ), 0, (0, (), [ 
			 (12, 17, None, None) , (12, 17, None, None) , (16397, 10, None, "IID('{59DC170B-AF91-11D0-A072-00A02436CF7E}')") , ], 1 , 2 , 4 , 2 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'LogicalNum' , 'Index' , 'IOSignal' , ), 0, (0, (), [ 
			 (12, 17, None, None) , (12, 17, None, None) , (16397, 10, None, "IID('{59DC170B-AF91-11D0-A072-00A02436CF7E}')") , ], 1 , 2 , 4 , 2 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'Count' , ), 101, (101, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 102, (102, (), [ (16397, 10, None, "IID('{59DC16F1-AF91-11D0-A072-00A02436CF7E}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'IsMonitoring' , 'IsMonitoring' , ), 103, (103, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'NoRefresh' , 'NoRefresh' , ), 104, (104, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'NoRefresh' , 'NoRefresh' , ), 104, (104, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'StartMonitor' , 'Latency' , ), 150, (150, (), [ (3, 0, None, None) , ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'StopMonitor' , ), 151, (151, (), [ ], 1 , 1 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Refresh' , ), 152, (152, (), [ ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
]

IIOType_vtables_dispatch_ = 1
IIOType_vtables_ = [
	(( 'Type' , 'Type' , ), 101, (101, (), [ (16386, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Signals' , 'IOSignals' , ), 202, (202, (), [ (16397, 10, None, "IID('{59DC16F8-AF91-11D0-A072-00A02436CF7E}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 102, (102, (), [ (16397, 10, None, "IID('{59DC16ED-AF91-11D0-A072-00A02436CF7E}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

IIOTypes_vtables_dispatch_ = 1
IIOTypes_vtables_ = [
	(( '_NewEnum' , 'NewEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'Type' , 'Index' , 'IOType' , ), 0, (0, (), [ 
			 (12, 17, None, None) , (12, 17, None, None) , (16397, 10, None, "IID('{59DC16F1-AF91-11D0-A072-00A02436CF7E}')") , ], 1 , 2 , 4 , 2 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'Type' , 'Index' , 'IOType' , ), 0, (0, (), [ 
			 (12, 17, None, None) , (12, 17, None, None) , (16397, 10, None, "IID('{59DC16F1-AF91-11D0-A072-00A02436CF7E}')") , ], 1 , 2 , 4 , 2 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'Count' , ), 101, (101, (), [ (16386, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 102, (102, (), [ (16397, 10, None, "IID('{6D7E3A01-9ECC-11D0-94D5-0020AF68F0A3}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Add' , 'Type' , 'UserIOType' , ), 151, (151, (), [ (12, 17, None, None) , 
			 (16397, 10, None, "IID('{59DC16F6-AF91-11D0-A072-00A02436CF7E}')") , ], 1 , 1 , 4 , 1 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Remove' , 'Type' , 'Index' , ), 152, (152, (), [ (12, 17, None, None) , 
			 (12, 17, None, None) , ], 1 , 1 , 4 , 2 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Save' , 'FileName' , ), 153, (153, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Unsimulate' , ), 154, (154, (), [ ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'DryRun' , 'DryRun' , ), 103, (103, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'DryRun' , 'DryRun' , ), 103, (103, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
]

IIndGroupPosition_vtables_dispatch_ = 1
IIndGroupPosition_vtables_ = [
	(( 'Parent' , 'Parent' , ), 301, (301, (), [ (16397, 10, None, "IID('{B4819F73-FC65-4475-97D3-974ACF6EE03E}')") , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'IsEqualTo' , 'TargetPos' , 'IsEqualTo' , ), 302, (302, (), [ (9, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'IsReachable' , 'From' , 'MoType' , 'OrientType' , 'Destination' , 
			 'MotionErrorInfo' , 'IsReachable' , ), 303, (303, (), [ (12, 17, None, None) , (3, 49, '6', None) , 
			 (3, 49, '2', None) , (12, 17, None, None) , (16397, 50, '0', "IID('{EE912848-BB81-427A-951F-5D9DC0FE74A7}')") , (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'Copy' , 'Position' , ), 304, (304, (), [ (9, 1, None, None) , ], 1 , 1 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'CheckReach' , 'From' , 'MoType' , 'OrientType' , 'Destination' , 
			 'MotionErrorInfo' , 'IsReachable' , ), 305, (305, (), [ (12, 17, None, None) , (3, 49, '6', None) , 
			 (3, 49, '2', None) , (12, 17, None, None) , (16397, 50, '0', "IID('{EE912848-BB81-427A-951F-5D9DC0FE74A7}')") , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
]

IIndPosition_vtables_dispatch_ = 1
IIndPosition_vtables_ = [
	(( 'Comment' , 'Comment' , ), 201, (201, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Comment' , 'Comment' , ), 201, (201, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Group' , 'GroupNum' , 'Position' , ), 202, (202, (), [ (2, 1, None, None) , 
			 (16397, 10, None, "IID('{DBE7F3B9-01E5-4935-A211-B5CC9D3A1048}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'GroupMask' , 'GroupNum' , 'Mask' , ), 203, (203, (), [ (2, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Id' , 'Id' , ), 204, (204, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'IsAtCurPosition' , 'IsAtCurPosition' , ), 205, (205, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'IsInitialized' , 'IsInitialized' , ), 206, (206, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'IsReachable' , 'From' , 'MoType' , 'OrientType' , 'Destination' , 
			 'MotionErrorInfo' , 'IsReachable' , ), 207, (207, (), [ (12, 17, None, None) , (3, 49, '6', None) , 
			 (3, 49, '2', None) , (12, 17, None, None) , (16397, 50, '0', "IID('{EE912848-BB81-427A-951F-5D9DC0FE74A7}')") , (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Copy' , 'Position' , ), 250, (250, (), [ (9, 1, None, None) , ], 1 , 1 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Moveto' , ), 251, (251, (), [ ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Record' , ), 253, (253, (), [ ], 1 , 1 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Uninitialize' , ), 254, (254, (), [ ], 1 , 1 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'GroupBitMask' , 'GroupBitMask' , ), 255, (255, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'CheckReach' , 'From' , 'MoType' , 'OrientType' , 'Destination' , 
			 'MotionErrorInfo' , 'IsReachable' , ), 256, (256, (), [ (12, 17, None, None) , (3, 49, '6', None) , 
			 (3, 49, '2', None) , (12, 17, None, None) , (16397, 50, '0', "IID('{EE912848-BB81-427A-951F-5D9DC0FE74A7}')") , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
]

IJoint_vtables_dispatch_ = 1
IJoint_vtables_ = [
	(( 'Program' , 'Program' , ), 101, (101, (), [ (16397, 10, None, "IID('{D42AB5D5-8FFB-11D0-94CC-0020AF68F0A3}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'NewEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'JointNum' , 'Value' , ), 0, (0, (), [ (2, 1, None, None) , 
			 (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'JointNum' , 'Value' , ), 0, (0, (), [ (2, 1, None, None) , 
			 (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 201, (201, (), [ (16397, 10, None, "IID('{D42AB5DB-8FFB-11D0-94CC-0020AF68F0A3}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'Count' , ), 202, (202, (), [ (16386, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
]

IKARELProgram_vtables_dispatch_ = 1
IKARELProgram_vtables_ = [
	(( 'Run' , 'StepType' , 'LineNum' , 'Direction' , ), 250, (250, (), [ 
			 (12, 17, None, None) , (12, 17, None, None) , (12, 17, None, None) , ], 1 , 1 , 4 , 3 , 336 , (3, 0, None, None) , 0 , )),
	(( 'SubType' , 'SubType' , ), 203, (203, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
]

IMotionErrorInfo_vtables_dispatch_ = 1
IMotionErrorInfo_vtables_ = [
	(( 'GroupNum' , 'GroupNum' , ), 101, (101, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'JointBitMask' , 'JointBitMask' , ), 102, (102, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'MoTaskId' , 'MoTaskId' , ), 103, (103, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'MoTaskParam' , 'MoTaskParam' , ), 104, (104, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'RlibId' , 'RlibId' , ), 105, (105, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'RlibParam' , 'RlibParam' , ), 106, (106, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'RobotErrorInfo' , 'RobotErrorInfo' , ), 107, (107, (), [ (16397, 10, None, "IID('{5BBFA760-09C6-11D2-871C-00C04F98D092}')") , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'UpperLimMask' , 'UpperLimMask' , ), 108, (108, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
]

IPacket_vtables_dispatch_ = 1
IPacket_vtables_ = [
	(( 'Body' , 'Body' , ), 101, (101, (), [ (24593, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'ItrDepth' , 'ItrDepth' , ), 102, (102, (), [ (16401, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'PacketID' , 'PacketID' , ), 103, (103, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'PacketType' , 'PacketType' , ), 104, (104, (), [ (16401, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'RequestCode' , 'RequestCode' , ), 105, (105, (), [ (16401, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'RequestorID' , 'RequestorID' , ), 106, (106, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Status' , 'Status' , ), 107, (107, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'SubSystemCode' , 'SubSystemCode' , ), 108, (108, (), [ (16401, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'DecodeBody' , 'Item' , 'Value' , ), 151, (151, (), [ (3, 1, None, None) , 
			 (16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
]

IPacketEvent_vtables_dispatch_ = 1
IPacketEvent_vtables_ = [
	(( 'PacketID' , 'PacketID' , ), 101, (101, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'RequestCode' , 'RequestCode' , ), 102, (102, (), [ (16401, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'SubSystemCode' , 'SubSystemCode' , ), 103, (103, (), [ (16401, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
]

IPipe_vtables_dispatch_ = 1
IPipe_vtables_ = [
	(( 'Flush' , ), 201, (201, (), [ ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Id' , 'Id' , ), 202, (202, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'IsMonitoring' , 'IsMonitoring' , ), 203, (203, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'IsOverflowed' , 'IsOverflowed' , ), 204, (204, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 205, (205, (), [ (16397, 10, None, "IID('{B475BC91-3AF1-11D4-9F66-00105AE428C3}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'StartMonitor' , 'FlushTime' , ), 206, (206, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'StopMonitor' , ), 207, (207, (), [ ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'TypeName' , 'TypeName' , ), 208, (208, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'TypeProgName' , 'TypeProgName' , ), 209, (209, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
]

IPipeField_vtables_dispatch_ = 1
IPipeField_vtables_ = [
	(( 'Value' , 'Value' , ), 0, (0, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'FieldName' , 'FieldName' , ), 201, (201, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'FullName' , 'FullName' , ), 202, (202, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'IsInitialized' , 'IsInitialized' , ), 203, (203, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 204, (204, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Pipe' , 'Pipe' , ), 205, (205, (), [ (16397, 10, None, "IID('{B475BC95-3AF1-11D4-9F66-00105AE428C3}')") , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'TypeCode' , 'TypeCode' , ), 206, (206, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'TypeName' , 'TypeName' , ), 207, (207, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
]

IPipeFields_vtables_dispatch_ = 1
IPipeFields_vtables_ = [
	(( '_NewEnum' , 'NewEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'Name' , 'Index' , 'Item' , ), 0, (0, (), [ 
			 (12, 17, None, None) , (12, 17, None, None) , (16393, 10, None, None) , ], 1 , 2 , 4 , 2 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'Name' , 'Index' , 'Item' , ), 0, (0, (), [ 
			 (12, 17, None, None) , (12, 17, None, None) , (16393, 10, None, None) , ], 1 , 2 , 4 , 2 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'Count' , ), 201, (201, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'FieldName' , 'FieldName' , ), 202, (202, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'FullName' , 'FullName' , ), 203, (203, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 204, (204, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Pipe' , 'Pipe' , ), 205, (205, (), [ (16397, 10, None, "IID('{B475BC95-3AF1-11D4-9F66-00105AE428C3}')") , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
]

IPipePosition_vtables_dispatch_ = 1
IPipePosition_vtables_ = [
	(( 'Formats' , 'Type' , 'Format' , ), 201, (201, (), [ (3, 1, None, None) , 
			 (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'GroupNum' , 'GroupNum' , ), 202, (202, (), [ (16386, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'IsAtCurPosition' , 'IsAtCurPosition' , ), 203, (203, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'IsEqualTo' , 'TargetPos' , 'IsEqualTo' , ), 204, (204, (), [ (9, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'IsInitialized' , 'IsInitialized' , ), 205, (205, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 206, (206, (), [ (16397, 10, None, "IID('{B475BC99-3AF1-11D4-9F66-00105AE428C3}')") , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Pipe' , 'Pipe' , ), 207, (207, (), [ (16397, 10, None, "IID('{B475BC95-3AF1-11D4-9F66-00105AE428C3}')") , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Type' , 'Type' , ), 208, (208, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
]

IPipes_vtables_dispatch_ = 1
IPipes_vtables_ = [
	(( '_NewEnum' , 'NewEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'Id' , 'Index' , 'Pipe' , ), 0, (0, (), [ 
			 (12, 17, None, None) , (12, 17, None, None) , (16397, 10, None, "IID('{B475BC95-3AF1-11D4-9F66-00105AE428C3}')") , ], 1 , 2 , 4 , 2 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'Id' , 'Index' , 'Pipe' , ), 0, (0, (), [ 
			 (12, 17, None, None) , (12, 17, None, None) , (16397, 10, None, "IID('{B475BC95-3AF1-11D4-9F66-00105AE428C3}')") , ], 1 , 2 , 4 , 2 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'Count' , ), 201, (201, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
]

IPosition_vtables_dispatch_ = 1
IPosition_vtables_ = [
	(( 'Program' , 'Program' , ), 101, (101, (), [ (16397, 10, None, "IID('{D42AB5D5-8FFB-11D0-94CC-0020AF68F0A3}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'AutomaticUpdate' , 'AutomaticUpdate' , ), 201, (201, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'AutomaticUpdate' , 'AutomaticUpdate' , ), 201, (201, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Type' , 'Type' , ), 202, (202, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Type' , 'Type' , ), 202, (202, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Formats' , 'Type' , 'Format' , ), 203, (203, (), [ (3, 1, None, None) , 
			 (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'GroupNum' , 'GroupNum' , ), 204, (204, (), [ (16386, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Id' , 'Id' , ), 205, (205, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'IsAtCurPosition' , 'IsAtCurPosition' , ), 206, (206, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'IsInitialized' , 'IsInitialized' , ), 207, (207, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'UserFrame' , 'UserFrame' , ), 208, (208, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'UserFrame' , 'UserFrame' , ), 208, (208, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'UserTool' , 'UserTool' , ), 209, (209, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'UserTool' , 'UserTool' , ), 209, (209, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'IsMonitoring' , 'IsMonitoring' , ), 210, (210, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Update' , ), 251, (251, (), [ ], 1 , 1 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'Refresh' , ), 252, (252, (), [ ], 1 , 1 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'Moveto' , ), 253, (253, (), [ ], 1 , 1 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'Record' , ), 254, (254, (), [ ], 1 , 1 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'StartMonitor' , 'Latency' , ), 255, (255, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'StopMonitor' , ), 256, (256, (), [ ], 1 , 1 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'Uninitialize' , ), 257, (257, (), [ ], 1 , 1 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'MatMul' , 'LeftPos' , 'RightPos' , ), 258, (258, (), [ (9, 1, None, None) , 
			 (9, 1, None, None) , ], 1 , 1 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'MatInv' , 'InputPos' , ), 259, (259, (), [ (9, 1, None, None) , ], 1 , 1 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
]

IPosition2_vtables_dispatch_ = 1
IPosition2_vtables_ = [
	(( 'Program' , 'Program' , ), 101, (101, (), [ (16397, 10, None, "IID('{D42AB5D5-8FFB-11D0-94CC-0020AF68F0A3}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'AutomaticUpdate' , 'AutomaticUpdate' , ), 201, (201, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'AutomaticUpdate' , 'AutomaticUpdate' , ), 201, (201, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Type' , 'Type' , ), 202, (202, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Type' , 'Type' , ), 202, (202, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Formats' , 'Type' , 'Format' , ), 203, (203, (), [ (3, 1, None, None) , 
			 (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'GroupNum' , 'GroupNum' , ), 204, (204, (), [ (16386, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Id' , 'Id' , ), 205, (205, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'IsAtCurPosition' , 'IsAtCurPosition' , ), 206, (206, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'IsInitialized' , 'IsInitialized' , ), 207, (207, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'UserFrame' , 'UserFrame' , ), 208, (208, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'UserFrame' , 'UserFrame' , ), 208, (208, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'UserTool' , 'UserTool' , ), 209, (209, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'UserTool' , 'UserTool' , ), 209, (209, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'IsMonitoring' , 'IsMonitoring' , ), 210, (210, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Update' , ), 251, (251, (), [ ], 1 , 1 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'Refresh' , ), 252, (252, (), [ ], 1 , 1 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'Moveto' , ), 253, (253, (), [ ], 1 , 1 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'Record' , ), 254, (254, (), [ ], 1 , 1 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'StartMonitor' , 'Latency' , ), 255, (255, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'StopMonitor' , ), 256, (256, (), [ ], 1 , 1 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'Uninitialize' , ), 257, (257, (), [ ], 1 , 1 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'MatMul' , 'LeftPos' , 'RightPos' , ), 258, (258, (), [ (9, 1, None, None) , 
			 (9, 1, None, None) , ], 1 , 1 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'MatInv' , 'InputPos' , ), 259, (259, (), [ (9, 1, None, None) , ], 1 , 1 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'IsEqualTo' , 'TargetPos' , 'IsEqualTo' , ), 260, (260, (), [ (9, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'IsReachable' , 'From' , 'MoType' , 'OrientType' , 'Destination' , 
			 'MotionErrorInfo' , 'IsReachable' , ), 261, (261, (), [ (12, 17, None, None) , (3, 49, '6', None) , 
			 (3, 49, '2', None) , (12, 17, None, None) , (16397, 50, '0', "IID('{EE912848-BB81-427A-951F-5D9DC0FE74A7}')") , (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'Copy' , 'Position' , ), 262, (262, (), [ (9, 1, None, None) , ], 1 , 1 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'CheckReach' , 'From' , 'MoType' , 'OrientType' , 'Destination' , 
			 'MotionErrorInfo' , 'IsReachable' , ), 263, (263, (), [ (12, 17, None, None) , (3, 49, '6', None) , 
			 (3, 49, '2', None) , (12, 17, None, None) , (16397, 50, '0', "IID('{EE912848-BB81-427A-951F-5D9DC0FE74A7}')") , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
]

IProgram_vtables_dispatch_ = 1
IProgram_vtables_ = [
	(( 'Name' , 'Name' , ), 0, (0, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Variables' , 'Variables' , ), 101, (101, (), [ (16397, 10, None, "IID('{88B57BCB-D0CA-11CF-959F-00A024329125}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'AccessMode' , 'AccessMode' , ), 102, (102, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'RejectMode' , 'RejectMode' , ), 103, (103, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 104, (104, (), [ (16397, 10, None, "IID('{1FBD567D-8F13-11D0-94CB-0020AF68F0A3}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Comment' , 'Comment' , ), 105, (105, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Comment' , 'Comment' , ), 105, (105, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Created' , 'Created' , ), 106, (106, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'LastModified' , 'LastModified' , ), 107, (107, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'OriginalName' , 'OriginalName' , ), 108, (108, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Version' , 'Version' , ), 109, (109, (), [ (16386, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Size' , 'Size' , ), 110, (110, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Protection' , 'Protection' , ), 111, (111, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Protection' , 'Protection' , ), 111, (111, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'StackSize' , 'StackSize' , ), 112, (112, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'StackSize' , 'StackSize' , ), 112, (112, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'Priority' , 'Priority' , ), 113, (113, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'Priority' , 'Priority' , ), 113, (113, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'TimeSlice' , 'TimeSlice' , ), 114, (114, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'TimeSlice' , 'TimeSlice' , ), 114, (114, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'BusyLampOff' , 'BusyLampOff' , ), 115, (115, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'BusyLampOff' , 'BusyLampOff' , ), 115, (115, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'DefaultGroup' , 'GroupNumber' , 'DefaultGroup' , ), 116, (116, (), [ (2, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'DefaultGroup' , 'GroupNumber' , 'DefaultGroup' , ), 116, (116, (), [ (2, 1, None, None) , 
			 (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'IgnoreAbort' , 'IgnoreConstant' , 'IgnoreAbort' , ), 117, (117, (), [ (3, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'IgnoreAbort' , 'IgnoreConstant' , 'IgnoreAbort' , ), 117, (117, (), [ (3, 1, None, None) , 
			 (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'IgnorePause' , 'IgnoreConstant' , 'IgnorePause' , ), 118, (118, (), [ (3, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'IgnorePause' , 'IgnoreConstant' , 'IgnorePause' , ), 118, (118, (), [ (3, 1, None, None) , 
			 (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'Invisible' , 'Invisible' , ), 119, (119, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'Invisible' , 'Invisible' , ), 119, (119, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'Owner' , 'Owner' , ), 120, (120, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'Owner' , 'Owner' , ), 120, (120, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'ReOpen' , 'AccessMode' , 'RejectMode' , ), 150, (150, (), [ (3, 1, None, None) , 
			 (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'Save' , 'FileName' , 'Option' , 'SaveClass' , ), 151, (151, (), [ 
			 (8, 1, None, None) , (12, 17, None, None) , (12, 17, None, None) , ], 1 , 1 , 4 , 2 , 328 , (3, 0, None, None) , 0 , )),
]

IProgramObject_vtables_dispatch_ = 1
IProgramObject_vtables_ = [
	(( 'Program' , 'Program' , ), 101, (101, (), [ (16397, 10, None, "IID('{D42AB5D5-8FFB-11D0-94CC-0020AF68F0A3}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
]

IPrograms_vtables_dispatch_ = 1
IPrograms_vtables_ = [
	(( '_NewEnum' , 'NewEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'Name' , 'NewReference' , 'AccessMode' , 'RejectMode' , 
			 'Program' , ), 0, (0, (), [ (12, 1, None, None) , (12, 17, None, None) , (12, 17, None, None) , 
			 (12, 17, None, None) , (16397, 10, None, "IID('{D42AB5D5-8FFB-11D0-94CC-0020AF68F0A3}')") , ], 1 , 2 , 4 , 3 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'Count' , ), 101, (101, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Selected' , 'Selected' , ), 102, (102, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Selected' , 'Selected' , ), 102, (102, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 103, (103, (), [ (16397, 10, None, "IID('{6D7E3A01-9ECC-11D0-94D5-0020AF68F0A3}')") , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Add' , 'Name' , 'Type' , 'Program' , ), 150, (150, (), [ 
			 (8, 1, None, None) , (3, 1, None, None) , (16397, 10, None, "IID('{D42AB5D5-8FFB-11D0-94CC-0020AF68F0A3}')") , ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Remove' , 'Name' , ), 151, (151, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'TryItem' , 'Name' , 'NewReference' , 'AccessMode' , 'RejectMode' , 
			 'Program' , 'Result' , ), 152, (152, (), [ (8, 1, None, None) , (12, 17, None, None) , 
			 (12, 17, None, None) , (12, 17, None, None) , (16397, 2, None, "IID('{D42AB5D5-8FFB-11D0-94CC-0020AF68F0A3}')") , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
]

IRegNumeric_vtables_dispatch_ = 1
IRegNumeric_vtables_ = [
	(( 'Program' , 'Program' , ), 101, (101, (), [ (16397, 10, None, "IID('{D42AB5D5-8FFB-11D0-94CC-0020AF68F0A3}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Comment' , 'Comment' , ), 201, (201, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Comment' , 'Comment' , ), 201, (201, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'RegLong' , 'RegLong' , ), 202, (202, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'RegLong' , 'RegLong' , ), 202, (202, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'RegFloat' , 'RegFloat' , ), 203, (203, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'RegFloat' , 'RegFloat' , ), 203, (203, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Type' , 'Type' , ), 204, (204, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 205, (205, (), [ (16397, 10, None, "IID('{8C8ACC81-4F57-11D0-BC32-444553540000}')") , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
]

IRegString_vtables_dispatch_ = 1
IRegString_vtables_ = [
	(( 'Program' , 'Program' , ), 101, (101, (), [ (16397, 10, None, "IID('{D42AB5D5-8FFB-11D0-94CC-0020AF68F0A3}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Comment' , 'Comment' , ), 201, (201, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Comment' , 'Comment' , ), 201, (201, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Value' , 'Value' , ), 202, (202, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Value' , 'Value' , ), 202, (202, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 205, (205, (), [ (16397, 10, None, "IID('{8C8ACC81-4F57-11D0-BC32-444553540000}')") , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
]

IRobManProxy_vtables_dispatch_ = 1
IRobManProxy_vtables_ = [
	(( 'GetRobot' , 'Robot' , ), 101, (101, (), [ (16393, 10, None, "IID('{6C779F22-4383-11D0-8901-0020AF68F0A3}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'ReleaseRobot' , 'RefCnt' , ), 102, (102, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
]

IRobot_vtables_dispatch_ = 1
IRobot_vtables_ = [
	(( 'HostName' , 'HostName' , ), 101, (101, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'CurPosition' , 'CurPosition' , ), 102, (102, (), [ (16397, 10, None, "IID('{E2686FA9-1E42-11D1-B6FF-00C04FB9C401}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Devices' , 'Devices' , ), 103, (103, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Programs' , 'Programs' , ), 104, (104, (), [ (16397, 10, None, "IID('{1FBD567D-8F13-11D0-94CB-0020AF68F0A3}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'RegPositions' , 'RegPositions' , ), 105, (105, (), [ (16397, 10, None, "IID('{6055D69B-FFAE-11D0-B6F4-00C04FB9C401}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'RegNumerics' , 'RegNumerics' , ), 106, (106, (), [ (16397, 10, None, "IID('{88B57BCB-D0CA-11CF-959F-00A024329125}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'SysVariables' , 'SysVariables' , ), 107, (107, (), [ (16397, 10, None, "IID('{88B57BCB-D0CA-11CF-959F-00A024329125}')") , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'RemoteMotionMaster' , 'RemoteMotionMaster' , ), 108, (108, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'RemoteMotionMaster' , 'RemoteMotionMaster' , ), 108, (108, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Alarms' , 'Alarms' , ), 109, (109, (), [ (16397, 10, None, "IID('{7C37F235-A494-11D0-A37F-0020AF39BE5A}')") , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'IOTypes' , 'IOTypes' , ), 110, (110, (), [ (16397, 10, None, "IID('{59DC16ED-AF91-11D0-A072-00A02436CF7E}')") , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'TPScreen' , 'TPScreen' , ), 111, (111, (), [ (16397, 10, None, "IID('{660E6870-E286-11D0-8BB6-0020AF39BE5A}')") , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Language' , 'Language' , ), 112, (112, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Language' , 'Language' , ), 112, (112, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'ToolFrames' , 'ToolFrames' , ), 113, (113, (), [ (16397, 10, None, "IID('{6055D69B-FFAE-11D0-B6F4-00C04FB9C401}')") , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'UserFrames' , 'UserFrames' , ), 114, (114, (), [ (16397, 10, None, "IID('{6055D69B-FFAE-11D0-B6F4-00C04FB9C401}')") , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'JogFrames' , 'JogFrames' , ), 115, (115, (), [ (16397, 10, None, "IID('{6055D69B-FFAE-11D0-B6F4-00C04FB9C401}')") , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'Tasks' , 'Tasks' , ), 116, (116, (), [ (16397, 10, None, "IID('{6B01CFFC-4626-11D1-B745-00C04FBBE42A}')") , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'SynchData' , 'SynchData' , ), 117, (117, (), [ (16397, 10, None, "IID('{2AF44182-9273-11D1-B6F9-00C04FA3BD85}')") , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'Applications' , 'Applications' , ), 118, (118, (), [ (16397, 10, None, "IID('{679622C3-E50A-11D1-B778-00C04FB99C75}')") , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'TPMotionSource' , 'TPMotionSource' , ), 119, (119, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'TPMotionSource' , 'TPMotionSource' , ), 119, (119, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'IsOffline' , 'IsOffline' , ), 120, (120, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'IsEventLogger' , 'IsEventLogger' , ), 121, (121, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'Connect' , 'HostName' , ), 151, (151, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'PostAlarm' , 'ErrorSeverity' , 'ErrorFacility' , 'ErrorNumber' , 'CauseFacility' , 
			 'CauseNumber' , 'ArgumentsForError' , ), 152, (152, (), [ (3, 1, None, None) , (3, 1, None, None) , 
			 (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (24588, 1, None, None) , ], 1 , 1 , 4 , -1 , 256 , (3, 0, None, None) , 0 , )),
	(( 'Load' , 'FileName' , 'Option' , ), 153, (153, (), [ (8, 1, None, None) , 
			 (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'CreatePacketEvent' , 'SubSystemCode' , 'RequestCode' , 'PacketID' , 'PacketEvent' , 
			 ), 154, (154, (), [ (12, 17, None, None) , (12, 17, None, None) , (12, 17, None, None) , (16397, 10, None, "IID('{FCCE9E5F-9420-11D1-B751-00C04FB99C75}')") , ], 1 , 1 , 4 , 3 , 272 , (3, 0, None, None) , 0 , )),
	(( 'OfflineConnect' , 'HostName' , 'MDPath' , 'FRSPath' , 'IgnoreVersion' , 
			 ), 155, (155, (), [ (12, 17, None, None) , (12, 17, None, None) , (12, 17, None, None) , (12, 17, None, None) , ], 1 , 1 , 4 , 4 , 280 , (3, 0, None, None) , 0 , )),
	(( 'GetErrorInfo' , 'RobotErrorInfo' , ), 156, (156, (), [ (16397, 10, None, "IID('{5BBFA760-09C6-11D2-871C-00C04F98D092}')") , ], 1 , 1 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'EventLoggerConnect' , ), 157, (157, (), [ ], 1 , 1 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'KCL' , 'Command' , 'Wait' , ), 158, (158, (), [ (8, 1, None, None) , 
			 (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'SPRUNCMD' , 'FileName' , ), 159, (159, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'OutputDebugMessage' , 'Message' , ), 160, (160, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'ConnectEx' , 'HostName' , 'NoWait' , 'NumRetries' , 'Period' , 
			 ), 161, (161, (), [ (8, 1, None, None) , (11, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'IsConnected' , 'IsConnected' , ), 162, (162, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'CreateScatteredAccess' , 'ObjectList' , 'ScatteredAccess' , ), 163, (163, (), [ (24588, 1, None, None) , 
			 (16397, 10, None, "IID('{6F33A4D1-91F3-11D3-877C-00C04F81118D}')") , ], 1 , 1 , 4 , -1 , 344 , (3, 0, None, None) , 0 , )),
	(( 'SysInfo' , 'SysInfo' , ), 164, (164, (), [ (16397, 10, None, "IID('{4553DA63-ACA1-11D3-8783-00C04F81118D}')") , ], 1 , 2 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'Pipes' , 'Pipes' , ), 165, (165, (), [ (16397, 10, None, "IID('{B475BC91-3AF1-11D4-9F66-00105AE428C3}')") , ], 1 , 2 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'CreateIndependentPosition' , 'GroupBitMask' , 'IndPosition' , ), 166, (166, (), [ (3, 49, '0', None) , 
			 (16397, 10, None, "IID('{B4819F73-FC65-4475-97D3-974ACF6EE03E}')") , ], 1 , 1 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'ProcessID' , 'ProcessID' , ), 167, (167, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'RegStrings' , 'RegStrings' , ), 168, (168, (), [ (16397, 10, None, "IID('{88B57BCB-D0CA-11CF-959F-00A024329125}')") , ], 1 , 2 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
]

IRobot2_vtables_dispatch_ = 1
IRobot2_vtables_ = [
	(( 'HostName' , 'HostName' , ), 101, (101, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'CurPosition' , 'CurPosition' , ), 102, (102, (), [ (16397, 10, None, "IID('{E2686FA9-1E42-11D1-B6FF-00C04FB9C401}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Devices' , 'Devices' , ), 103, (103, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Programs' , 'Programs' , ), 104, (104, (), [ (16397, 10, None, "IID('{1FBD567D-8F13-11D0-94CB-0020AF68F0A3}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'RegPositions' , 'RegPositions' , ), 105, (105, (), [ (16397, 10, None, "IID('{6055D69B-FFAE-11D0-B6F4-00C04FB9C401}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'RegNumerics' , 'RegNumerics' , ), 106, (106, (), [ (16397, 10, None, "IID('{88B57BCB-D0CA-11CF-959F-00A024329125}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'SysVariables' , 'SysVariables' , ), 107, (107, (), [ (16397, 10, None, "IID('{88B57BCB-D0CA-11CF-959F-00A024329125}')") , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'RemoteMotionMaster' , 'RemoteMotionMaster' , ), 108, (108, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'RemoteMotionMaster' , 'RemoteMotionMaster' , ), 108, (108, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Alarms' , 'Alarms' , ), 109, (109, (), [ (16397, 10, None, "IID('{7C37F235-A494-11D0-A37F-0020AF39BE5A}')") , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'IOTypes' , 'IOTypes' , ), 110, (110, (), [ (16397, 10, None, "IID('{59DC16ED-AF91-11D0-A072-00A02436CF7E}')") , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'TPScreen' , 'TPScreen' , ), 111, (111, (), [ (16397, 10, None, "IID('{660E6870-E286-11D0-8BB6-0020AF39BE5A}')") , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Language' , 'Language' , ), 112, (112, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Language' , 'Language' , ), 112, (112, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'ToolFrames' , 'ToolFrames' , ), 113, (113, (), [ (16397, 10, None, "IID('{6055D69B-FFAE-11D0-B6F4-00C04FB9C401}')") , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'UserFrames' , 'UserFrames' , ), 114, (114, (), [ (16397, 10, None, "IID('{6055D69B-FFAE-11D0-B6F4-00C04FB9C401}')") , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'JogFrames' , 'JogFrames' , ), 115, (115, (), [ (16397, 10, None, "IID('{6055D69B-FFAE-11D0-B6F4-00C04FB9C401}')") , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'Tasks' , 'Tasks' , ), 116, (116, (), [ (16397, 10, None, "IID('{6B01CFFC-4626-11D1-B745-00C04FBBE42A}')") , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'SynchData' , 'SynchData' , ), 117, (117, (), [ (16397, 10, None, "IID('{2AF44182-9273-11D1-B6F9-00C04FA3BD85}')") , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'Applications' , 'Applications' , ), 118, (118, (), [ (16397, 10, None, "IID('{679622C3-E50A-11D1-B778-00C04FB99C75}')") , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'TPMotionSource' , 'TPMotionSource' , ), 119, (119, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'TPMotionSource' , 'TPMotionSource' , ), 119, (119, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'IsOffline' , 'IsOffline' , ), 120, (120, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'IsEventLogger' , 'IsEventLogger' , ), 121, (121, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'Connect' , 'HostName' , ), 151, (151, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'PostAlarm' , 'ErrorSeverity' , 'ErrorFacility' , 'ErrorNumber' , 'CauseFacility' , 
			 'CauseNumber' , 'ArgumentsForError' , ), 152, (152, (), [ (3, 1, None, None) , (3, 1, None, None) , 
			 (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (24588, 1, None, None) , ], 1 , 1 , 4 , -1 , 256 , (3, 0, None, None) , 0 , )),
	(( 'Load' , 'FileName' , 'Option' , ), 153, (153, (), [ (8, 1, None, None) , 
			 (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'CreatePacketEvent' , 'SubSystemCode' , 'RequestCode' , 'PacketID' , 'PacketEvent' , 
			 ), 154, (154, (), [ (12, 17, None, None) , (12, 17, None, None) , (12, 17, None, None) , (16397, 10, None, "IID('{FCCE9E5F-9420-11D1-B751-00C04FB99C75}')") , ], 1 , 1 , 4 , 3 , 272 , (3, 0, None, None) , 0 , )),
	(( 'OfflineConnect' , 'HostName' , 'MDPath' , 'FRSPath' , 'IgnoreVersion' , 
			 ), 155, (155, (), [ (12, 17, None, None) , (12, 17, None, None) , (12, 17, None, None) , (12, 17, None, None) , ], 1 , 1 , 4 , 4 , 280 , (3, 0, None, None) , 0 , )),
	(( 'GetErrorInfo' , 'RobotErrorInfo' , ), 156, (156, (), [ (16397, 10, None, "IID('{5BBFA760-09C6-11D2-871C-00C04F98D092}')") , ], 1 , 1 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'EventLoggerConnect' , ), 157, (157, (), [ ], 1 , 1 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'KCL' , 'Command' , 'Wait' , ), 158, (158, (), [ (8, 1, None, None) , 
			 (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'SPRUNCMD' , 'FileName' , ), 159, (159, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'OutputDebugMessage' , 'Message' , ), 160, (160, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'ConnectEx' , 'HostName' , 'NoWait' , 'NumRetries' , 'Period' , 
			 ), 161, (161, (), [ (8, 1, None, None) , (11, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'IsConnected' , 'IsConnected' , ), 162, (162, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'CreateScatteredAccess' , 'ObjectList' , 'ScatteredAccess' , ), 163, (163, (), [ (24588, 1, None, None) , 
			 (16397, 10, None, "IID('{6F33A4D1-91F3-11D3-877C-00C04F81118D}')") , ], 1 , 1 , 4 , -1 , 344 , (3, 0, None, None) , 0 , )),
	(( 'SysInfo' , 'SysInfo' , ), 164, (164, (), [ (16397, 10, None, "IID('{4553DA63-ACA1-11D3-8783-00C04F81118D}')") , ], 1 , 2 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'Pipes' , 'Pipes' , ), 165, (165, (), [ (16397, 10, None, "IID('{B475BC91-3AF1-11D4-9F66-00105AE428C3}')") , ], 1 , 2 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'CreateIndependentPosition' , 'GroupBitMask' , 'IndPosition' , ), 166, (166, (), [ (3, 49, '0', None) , 
			 (16397, 10, None, "IID('{B4819F73-FC65-4475-97D3-974ACF6EE03E}')") , ], 1 , 1 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'ProcessID' , 'ProcessID' , ), 167, (167, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'RegStrings' , 'RegStrings' , ), 168, (168, (), [ (16397, 10, None, "IID('{88B57BCB-D0CA-11CF-959F-00A024329125}')") , ], 1 , 2 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
]

IRobotErrorInfo_vtables_dispatch_ = 1
IRobotErrorInfo_vtables_ = [
	(( 'Facility' , 'Facility' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Severity' , 'Severity' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Number' , 'Number' , ), 3, (3, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Description' , 'Description' , ), 4, (4, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'GUID' , 'GUID' , ), 5, (5, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'HelpContext' , 'HelpContext' , ), 6, (6, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'HelpFile' , 'HelpFile' , ), 7, (7, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Source' , 'Source' , ), 8, (8, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
]

IRobotIOSignal_vtables_dispatch_ = 1
IRobotIOSignal_vtables_ = [
	(( 'Value' , 'Value' , ), 201, (201, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Value' , 'Value' , ), 201, (201, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Simulate' , 'Simulate' , ), 202, (202, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Simulate' , 'Simulate' , ), 202, (202, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Polarity' , 'Polarity' , ), 203, (203, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Polarity' , 'Polarity' , ), 203, (203, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'Complementary' , 'Complementary' , ), 204, (204, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Complementary' , 'Complementary' , ), 204, (204, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 205, (205, (), [ (16397, 10, None, "IID('{59DC16F8-AF91-11D0-A072-00A02436CF7E}')") , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'NoRefresh' , 'NoRefresh' , ), 250, (250, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'NoRefresh' , 'NoRefresh' , ), 250, (250, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'NoUpdate' , 'NoUpdate' , ), 251, (251, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'NoUpdate' , 'NoUpdate' , ), 251, (251, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'Refresh' , ), 252, (252, (), [ ], 1 , 1 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'Update' , ), 253, (253, (), [ ], 1 , 1 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
]

IRobotObject_vtables_dispatch_ = 1
IRobotObject_vtables_ = [
	(( 'Robot' , 'Robot' , ), 1, (1, (), [ (16397, 10, None, "IID('{6D7E3A01-9ECC-11D0-94D5-0020AF68F0A3}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
]

IScatteredAccess_vtables_dispatch_ = 1
IScatteredAccess_vtables_ = [
	(( 'Refresh' , ), 101, (101, (), [ ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Update' , ), 102, (102, (), [ ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

ISelectedLines_vtables_dispatch_ = 1
ISelectedLines_vtables_ = [
	(( 'Count' , 'Count' , ), 201, (201, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'IsSelected' , 'LineNum' , 'IsSelected' , ), 202, (202, (), [ (3, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Add' , 'StartLine' , 'EndLine' , ), 251, (251, (), [ (3, 1, None, None) , 
			 (3, 17, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Copy' , ), 252, (252, (), [ ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Cut' , ), 253, (253, (), [ ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Paste' , 'LineNum' , 'PasteType' , ), 254, (254, (), [ (3, 1, None, None) , 
			 (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Remove' , 'LineNum' , ), 255, (255, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'RemoveAll' , ), 256, (256, (), [ ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
]

ISynchApplData_vtables_dispatch_ = 1
ISynchApplData_vtables_ = [
	(( '_NewEnum' , 'NewEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'Name' , 'CollectionIndex' , 'ApplicationID' , 'SynchApplDataItem' , 
			 ), 0, (0, (), [ (12, 17, None, None) , (12, 17, None, None) , (12, 17, None, None) , (16397, 10, None, "IID('{8FAFC8EA-B2B8-11D1-B705-00C04FA3BD85}')") , ], 1 , 2 , 4 , 3 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'Name' , 'CollectionIndex' , 'ApplicationID' , 'SynchApplDataItem' , 
			 ), 0, (0, (), [ (12, 17, None, None) , (12, 17, None, None) , (12, 17, None, None) , (16397, 10, None, "IID('{8FAFC8EA-B2B8-11D1-B705-00C04FA3BD85}')") , ], 1 , 2 , 4 , 3 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'Count' , ), 101, (101, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Add' , 'Name' , 'ApplicationID' , 'ApplProgID' , 'EditProgID' , 
			 'SynchApplDataItem' , ), 150, (150, (), [ (8, 1, None, None) , (12, 17, None, None) , (8, 1, None, None) , 
			 (8, 1, None, None) , (16397, 10, None, "IID('{8FAFC8EA-B2B8-11D1-B705-00C04FA3BD85}')") , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Remove' , 'Name' , 'ApplicationID' , ), 151, (151, (), [ (8, 1, None, None) , 
			 (12, 17, None, None) , ], 1 , 1 , 4 , 1 , 96 , (3, 0, None, None) , 0 , )),
]

ISynchApplDataItem_vtables_dispatch_ = 1
ISynchApplDataItem_vtables_ = [
	(( 'Name' , 'Name' , ), 101, (101, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'ApplicationID' , 'ApplicationID' , ), 102, (102, (), [ (16386, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'ApplProgID' , 'ApplProgID' , ), 103, (103, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'ApplProgID' , 'ApplProgID' , ), 103, (103, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'EditProgID' , 'EditProgID' , ), 104, (104, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'EditProgID' , 'EditProgID' , ), 104, (104, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
]

ISynchData_vtables_dispatch_ = 1
ISynchData_vtables_ = [
	(( 'Features' , 'Features' , ), 101, (101, (), [ (16397, 10, None, "IID('{2AF44184-9273-11D1-B6F9-00C04FA3BD85}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'TPInstructions' , 'TPInstructions' , ), 102, (102, (), [ (16397, 10, None, "IID('{3C05D26E-9BE8-11D1-B6FC-00C04FA3BD85}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'TPApplData' , 'TPApplData' , ), 103, (103, (), [ (16397, 10, None, "IID('{8FAFC8E8-B2B8-11D1-B705-00C04FA3BD85}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
]

ISysGroupPosition_vtables_dispatch_ = 1
ISysGroupPosition_vtables_ = [
	(( 'Parent' , 'Parent' , ), 301, (301, (), [ (16397, 10, None, "IID('{6055D699-FFAE-11D0-B6F4-00C04FB9C401}')") , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'Comment' , 'Comment' , ), 302, (302, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'Comment' , 'Comment' , ), 302, (302, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'IsEqualTo' , 'TargetPos' , 'IsEqualTo' , ), 303, (303, (), [ (9, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'IsReachable' , 'From' , 'MoType' , 'OrientType' , 'Destination' , 
			 'MotionErrorInfo' , 'IsReachable' , ), 304, (304, (), [ (12, 17, None, None) , (3, 49, '6', None) , 
			 (3, 49, '2', None) , (12, 17, None, None) , (16397, 50, '0', "IID('{EE912848-BB81-427A-951F-5D9DC0FE74A7}')") , (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'Copy' , 'Position' , ), 305, (305, (), [ (9, 1, None, None) , ], 1 , 1 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'CheckReach' , 'From' , 'MoType' , 'OrientType' , 'Destination' , 
			 'MotionErrorInfo' , 'IsReachable' , ), 306, (306, (), [ (12, 17, None, None) , (3, 49, '6', None) , 
			 (3, 49, '2', None) , (12, 17, None, None) , (16397, 50, '0', "IID('{EE912848-BB81-427A-951F-5D9DC0FE74A7}')") , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
]

ISysInfo_vtables_dispatch_ = 1
ISysInfo_vtables_ = [
	(( 'Clock' , 'DateTime' , ), 101, (101, (), [ (16391, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Clock' , 'DateTime' , ), 101, (101, (), [ (7, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'CMOS' , 'CMOS' , ), 102, (102, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'DRAM' , 'DRAM' , ), 103, (103, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'From' , 'From' , ), 104, (104, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'PermMemTotal' , 'PermMemTotal' , ), 105, (105, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'PermMemFree' , 'PermMemFree' , ), 106, (106, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'PermMemLargestFreeBlock' , 'PermMemLargestFreeBlock' , ), 107, (107, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'PermMemUsed' , 'PermMemUsed' , ), 108, (108, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'TempMemTotal' , 'TempMemTotal' , ), 109, (109, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'TempMemFree' , 'TempMemFree' , ), 110, (110, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'TempMemLargestFreeBlock' , 'TempMemLargestFreeBlock' , ), 111, (111, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'TempMemUsed' , 'TempMemUsed' , ), 112, (112, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'TPPMemTotal' , 'TPPMemTotal' , ), 113, (113, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'TPPMemFree' , 'TPPMemFree' , ), 114, (114, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'TPPMemLargestFreeBlock' , 'TPPMemLargestFreeBlock' , ), 115, (115, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'TPPMemUsed' , 'TPPMemUsed' , ), 116, (116, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'SystemMemTotal' , 'SystemMemTotal' , ), 117, (117, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'SystemMemFree' , 'SystemMemFree' , ), 118, (118, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'SystemMemLargestFreeBlock' , 'SystemMemLargestFreeBlock' , ), 119, (119, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'SystemMemUsed' , 'SystemMemUsed' , ), 120, (120, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'FROMType' , 'FROMType' , ), 121, (121, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'StartMode' , 'StartMode' , ), 122, (122, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
]

ISysPosition_vtables_dispatch_ = 1
ISysPosition_vtables_ = [
	(( 'Id' , 'Id' , ), 201, (201, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'GroupMask' , 'GroupNum' , 'Mask' , ), 202, (202, (), [ (2, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Group' , 'GroupNum' , 'Position' , ), 203, (203, (), [ (2, 1, None, None) , 
			 (16397, 10, None, "IID('{DC2FA0C8-FFAB-11D0-B6F4-00C04FB9C401}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'IsAtCurPosition' , 'IsAtCurPosition' , ), 204, (204, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Moveto' , ), 251, (251, (), [ ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Record' , ), 252, (252, (), [ ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Uninitialize' , ), 253, (253, (), [ ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'IsInitialized' , 'IsInitialized' , ), 205, (205, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Refresh' , ), 254, (254, (), [ ], 1 , 1 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Update' , ), 255, (255, (), [ ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'IsReachable' , 'From' , 'MoType' , 'OrientType' , 'Destination' , 
			 'MotionErrorInfo' , 'IsReachable' , ), 256, (256, (), [ (12, 17, None, None) , (3, 49, '6', None) , 
			 (3, 49, '2', None) , (12, 17, None, None) , (16397, 50, '0', "IID('{EE912848-BB81-427A-951F-5D9DC0FE74A7}')") , (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Copy' , 'Position' , ), 257, (257, (), [ (9, 1, None, None) , ], 1 , 1 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'GroupBitMask' , 'GroupBitMask' , ), 258, (258, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'CheckReach' , 'From' , 'MoType' , 'OrientType' , 'Destination' , 
			 'MotionErrorInfo' , 'IsReachable' , ), 259, (259, (), [ (12, 17, None, None) , (3, 49, '6', None) , 
			 (3, 49, '2', None) , (12, 17, None, None) , (16397, 50, '0', "IID('{EE912848-BB81-427A-951F-5D9DC0FE74A7}')") , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
]

ISysPositions_vtables_dispatch_ = 1
ISysPositions_vtables_ = [
	(( '_NewEnum' , 'NewEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'Id' , 'Index' , 'Position' , ), 0, (0, (), [ 
			 (12, 17, None, None) , (12, 17, None, None) , (16397, 10, None, "IID('{6055D699-FFAE-11D0-B6F4-00C04FB9C401}')") , ], 1 , 2 , 4 , 2 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'Id' , 'Index' , 'Position' , ), 0, (0, (), [ 
			 (12, 17, None, None) , (12, 17, None, None) , (16397, 10, None, "IID('{6055D699-FFAE-11D0-B6F4-00C04FB9C401}')") , ], 1 , 2 , 4 , 2 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'Count' , ), 201, (201, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Selected' , 'GroupNum' , 'Selected' , ), 202, (202, (), [ (2, 1, None, None) , 
			 (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Selected' , 'GroupNum' , 'Selected' , ), 202, (202, (), [ (2, 1, None, None) , 
			 (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Refresh' , ), 203, (203, (), [ ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Update' , ), 204, (204, (), [ ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
]

ISystemIOType_vtables_dispatch_ = 1
ISystemIOType_vtables_ = [
	(( 'Name' , 'Name' , ), 201, (201, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Signals' , 'IOSignals' , ), 202, (202, (), [ (16397, 10, None, "IID('{59DC16F8-AF91-11D0-A072-00A02436CF7E}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'IsInput' , 'IsInput' , ), 203, (203, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'IsBoolean' , 'IsBoolean' , ), 204, (204, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'CanConfigure' , 'CanConfigure' , ), 205, (205, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'CanSimulate' , 'CanSimulate' , ), 206, (206, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'CanInvert' , 'CanInvert' , ), 207, (207, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'CanComplement' , 'CanComplement' , ), 208, (208, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
]

ITPApplDataCollection_vtables_dispatch_ = 1
ITPApplDataCollection_vtables_ = [
	(( 'Program' , 'Program' , ), 101, (101, (), [ (16397, 10, None, "IID('{D42AB5D5-8FFB-11D0-94CC-0020AF68F0A3}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'NewEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'Name' , 'Index1' , 'Index2' , 'ApplData' , 
			 ), 0, (0, (), [ (12, 17, None, None) , (12, 17, None, None) , (12, 17, None, None) , (16393, 10, None, None) , ], 1 , 2 , 4 , 3 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'Name' , 'Index1' , 'Index2' , 'ApplData' , 
			 ), 0, (0, (), [ (12, 17, None, None) , (12, 17, None, None) , (12, 17, None, None) , (16393, 10, None, None) , ], 1 , 2 , 4 , 3 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'Count' , ), 201, (201, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Add' , 'Name' , 'Index1' , 'Index2' , 'ApplData' , 
			 ), 251, (251, (), [ (8, 1, None, None) , (12, 17, None, None) , (12, 17, None, None) , (16393, 10, None, None) , ], 1 , 1 , 4 , 2 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Remove' , 'Name' , 'Index1' , 'Index2' , ), 252, (252, (), [ 
			 (12, 17, None, None) , (12, 17, None, None) , (12, 17, None, None) , ], 1 , 1 , 4 , 3 , 104 , (3, 0, None, None) , 0 , )),
]

ITPApplDataHelper_vtables_dispatch_ = 1
ITPApplDataHelper_vtables_ = [
	(( 'Program' , 'Program' , ), 101, (101, (), [ (16397, 10, None, "IID('{D42AB5D5-8FFB-11D0-94CC-0020AF68F0A3}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'Name' , ), 201, (201, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Index1' , 'Index1' , ), 202, (202, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Index2' , 'Index2' , ), 203, (203, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'ApplDataChanged' , ), 251, (251, (), [ ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
]

ITPInstruction_vtables_dispatch_ = 1
ITPInstruction_vtables_ = [
	(( 'LMCode' , 'LMCode' , ), 101, (101, (), [ (16386, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'OptionID1' , 'OptionID1' , ), 102, (102, (), [ (16386, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'OptionID2' , 'OptionID2' , ), 103, (103, (), [ (16386, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'OptionID3' , 'OptionID3' , ), 104, (104, (), [ (16386, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Caption' , 'Caption' , ), 105, (105, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Caption' , 'Caption' , ), 105, (105, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'LinesProgID' , 'LinesProgID' , ), 106, (106, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'LinesProgID' , 'LinesProgID' , ), 106, (106, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'EditProgID' , 'EditProgID' , ), 107, (107, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'EditProgID' , 'EditProgID' , ), 107, (107, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'PictureName' , 'PictureName' , ), 108, (108, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'PictureName' , 'PictureName' , ), 108, (108, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'IsMotionAppend' , 'IsMotionAppend' , ), 109, (109, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'IsMotionAppend' , 'IsMotionAppend' , ), 109, (109, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
]

ITPInstructions_vtables_dispatch_ = 1
ITPInstructions_vtables_ = [
	(( '_NewEnum' , 'NewEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'LMCode' , 'Index' , 'OptParam1' , 'OptParam2' , 
			 'OptParam3' , 'TPInstruction' , ), 0, (0, (), [ (12, 17, None, None) , (12, 17, None, None) , 
			 (12, 17, None, None) , (12, 17, None, None) , (12, 17, None, None) , (16397, 10, None, "IID('{3C05D270-9BE8-11D1-B6FC-00C04FA3BD85}')") , ], 1 , 2 , 4 , 5 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'LMCode' , 'Index' , 'OptParam1' , 'OptParam2' , 
			 'OptParam3' , 'TPInstruction' , ), 0, (0, (), [ (12, 17, None, None) , (12, 17, None, None) , 
			 (12, 17, None, None) , (12, 17, None, None) , (12, 17, None, None) , (16397, 10, None, "IID('{3C05D270-9BE8-11D1-B6FC-00C04FA3BD85}')") , ], 1 , 2 , 4 , 5 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'Count' , ), 101, (101, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'IsValid' , 'LMCode' , 'OptParam1' , 'OptParam2' , 'OptParam3' , 
			 'IsValid' , ), 102, (102, (), [ (2, 1, None, None) , (12, 17, None, None) , (12, 17, None, None) , 
			 (12, 17, None, None) , (16395, 10, None, None) , ], 1 , 2 , 4 , 3 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Add' , 'LMCode' , 'OptParam1' , 'OptParam2' , 'OptParam3' , 
			 'Caption' , 'LinesProgID' , 'EditProgID' , 'PictureName' , 'IsMotionAppend' , 
			 'TPInstruction' , ), 150, (150, (), [ (2, 1, None, None) , (12, 17, None, None) , (12, 17, None, None) , 
			 (12, 17, None, None) , (8, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , 
			 (11, 1, None, None) , (16397, 10, None, "IID('{3C05D270-9BE8-11D1-B6FC-00C04FA3BD85}')") , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Remove' , 'LMCode' , 'OptParam1' , 'OptParam2' , 'OptParam3' , 
			 ), 151, (151, (), [ (2, 1, None, None) , (12, 17, None, None) , (12, 17, None, None) , (12, 17, None, None) , ], 1 , 1 , 4 , 3 , 104 , (3, 0, None, None) , 0 , )),
]

ITPLabel_vtables_dispatch_ = 1
ITPLabel_vtables_ = [
	(( 'Program' , 'Program' , ), 101, (101, (), [ (16397, 10, None, "IID('{D42AB5D5-8FFB-11D0-94CC-0020AF68F0A3}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Id' , 'Id' , ), 201, (201, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Line' , 'Line' , ), 202, (202, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
]

ITPLabels_vtables_dispatch_ = 1
ITPLabels_vtables_ = [
	(( 'Program' , 'Program' , ), 101, (101, (), [ (16397, 10, None, "IID('{D42AB5D5-8FFB-11D0-94CC-0020AF68F0A3}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'NewEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'LabelID' , 'Label' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16397, 10, None, "IID('{C3FB0D03-58D6-11D0-8901-0020AF68F0A3}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'Count' , ), 201, (201, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

ITPLineHelper_vtables_dispatch_ = 1
ITPLineHelper_vtables_ = [
	(( 'Program' , 'Program' , ), 101, (101, (), [ (16397, 10, None, "IID('{D42AB5D5-8FFB-11D0-94CC-0020AF68F0A3}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Number' , 'Number' , ), 201, (201, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'LineChanged' , ), 251, (251, (), [ ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
]

ITPLines_vtables_dispatch_ = 1
ITPLines_vtables_ = [
	(( 'Program' , 'Program' , ), 101, (101, (), [ (16397, 10, None, "IID('{D42AB5D5-8FFB-11D0-94CC-0020AF68F0A3}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'NewEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'LineNum' , 'Line' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'Count' , ), 201, (201, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'CurLineNum' , 'CurLineNum' , ), 202, (202, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'CurLineNum' , 'CurLineNum' , ), 202, (202, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'SelectedLines' , 'SelectedLines' , ), 203, (203, (), [ (16397, 10, None, "IID('{58ADC520-9395-11D2-877C-00C04FB9C401}')") , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Remove' , 'LineNum' , ), 251, (251, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Add' , 'MnCode' , 'InsertLine' , 'OptParam1' , 'OptParam2' , 
			 'OptParam3' , 'NewLine' , ), 252, (252, (), [ (2, 1, None, None) , (3, 1, None, None) , 
			 (12, 17, None, None) , (12, 17, None, None) , (12, 17, None, None) , (16393, 10, None, None) , ], 1 , 1 , 4 , 3 , 128 , (3, 0, None, None) , 0 , )),
	(( 'FullText' , 'Text' , ), 204, (204, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'InsertText' , 'TextLines' , 'LineNum' , 'InsertMode' , ), 253, (253, (), [ 
			 (24584, 1, None, None) , (3, 1, None, None) , (12, 17, None, None) , ], 1 , 1 , 4 , 1 , 144 , (3, 0, None, None) , 0 , )),
]

ITPPosition_vtables_dispatch_ = 1
ITPPosition_vtables_ = [
	(( 'Program' , 'Program' , ), 101, (101, (), [ (16397, 10, None, "IID('{D42AB5D5-8FFB-11D0-94CC-0020AF68F0A3}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Comment' , 'Comment' , ), 201, (201, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Comment' , 'Comment' , ), 201, (201, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Id' , 'Id' , ), 202, (202, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'GroupMask' , 'GroupNum' , 'Mask' , ), 203, (203, (), [ (2, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Group' , 'GroupNum' , 'Position' , ), 204, (204, (), [ (2, 1, None, None) , 
			 (16397, 10, None, "IID('{A47A5881-056D-11D0-8901-0020AF68F0A3}')") , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'IsAtCurPosition' , 'IsAtCurPosition' , ), 205, (205, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'ReferenceCount' , 'ReferenceCount' , ), 206, (206, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Binary' , 'BinaryPosData' , ), 207, (207, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Binary' , 'BinaryPosData' , ), 207, (207, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Moveto' , ), 251, (251, (), [ ], 1 , 1 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Record' , ), 252, (252, (), [ ], 1 , 1 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Uninitialize' , ), 253, (253, (), [ ], 1 , 1 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'IsInitialized' , 'IsInitialized' , ), 208, (208, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'Refresh' , ), 254, (254, (), [ ], 1 , 1 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Update' , ), 255, (255, (), [ ], 1 , 1 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'IsReachable' , 'From' , 'MoType' , 'OrientType' , 'Destination' , 
			 'MotionErrorInfo' , 'IsReachable' , ), 256, (256, (), [ (12, 17, None, None) , (3, 49, '6', None) , 
			 (3, 49, '2', None) , (12, 17, None, None) , (16397, 50, '0', "IID('{EE912848-BB81-427A-951F-5D9DC0FE74A7}')") , (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'Copy' , 'Position' , ), 257, (257, (), [ (9, 1, None, None) , ], 1 , 1 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'GroupBitMask' , 'GroupBitMask' , ), 258, (258, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'FirstExistGroup' , 'XyzWpr' , ), 259, (259, (), [ (16397, 10, None, "IID('{A47A5885-056D-11D0-8901-0020AF68F0A3}')") , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'CheckReach' , 'From' , 'MoType' , 'OrientType' , 'Destination' , 
			 'MotionErrorInfo' , 'IsReachable' , ), 260, (260, (), [ (12, 17, None, None) , (3, 49, '6', None) , 
			 (3, 49, '2', None) , (12, 17, None, None) , (16397, 50, '0', "IID('{EE912848-BB81-427A-951F-5D9DC0FE74A7}')") , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
]

ITPPositions_vtables_dispatch_ = 1
ITPPositions_vtables_ = [
	(( 'Program' , 'Program' , ), 101, (101, (), [ (16397, 10, None, "IID('{D42AB5D5-8FFB-11D0-94CC-0020AF68F0A3}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'NewEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'Id' , 'Index' , 'Position' , ), 0, (0, (), [ 
			 (12, 17, None, None) , (12, 17, None, None) , (16397, 10, None, "IID('{3A49BE61-F5B9-11CF-8901-0020AF68F0A3}')") , ], 1 , 2 , 4 , 2 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'Id' , 'Index' , 'Position' , ), 0, (0, (), [ 
			 (12, 17, None, None) , (12, 17, None, None) , (16397, 10, None, "IID('{3A49BE61-F5B9-11CF-8901-0020AF68F0A3}')") , ], 1 , 2 , 4 , 2 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'Count' , ), 201, (201, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'NewPosID' , 'NewPosID' , ), 202, (202, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'RenumberAll' , ), 251, (251, (), [ ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'GetGroupXyzWprByIndex' , 'GroupNum' , 'Index' , 'X' , 'Y' , 
			 'Z' , 'W' , 'P' , 'R' , 'pResult' , 
			 ), 203, (203, (), [ (2, 1, None, None) , (3, 1, None, None) , (16389, 2, None, None) , (16389, 2, None, None) , 
			 (16389, 2, None, None) , (16389, 2, None, None) , (16389, 2, None, None) , (16389, 2, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
]

ITPProgram_vtables_dispatch_ = 1
ITPProgram_vtables_ = [
	(( 'Name' , 'Name' , ), 0, (0, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Variables' , 'Variables' , ), 101, (101, (), [ (16397, 10, None, "IID('{88B57BCB-D0CA-11CF-959F-00A024329125}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'AccessMode' , 'AccessMode' , ), 102, (102, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'RejectMode' , 'RejectMode' , ), 103, (103, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 104, (104, (), [ (16397, 10, None, "IID('{1FBD567D-8F13-11D0-94CB-0020AF68F0A3}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Comment' , 'Comment' , ), 105, (105, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Comment' , 'Comment' , ), 105, (105, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Created' , 'Created' , ), 106, (106, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'LastModified' , 'LastModified' , ), 107, (107, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'OriginalName' , 'OriginalName' , ), 108, (108, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Version' , 'Version' , ), 109, (109, (), [ (16386, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Size' , 'Size' , ), 110, (110, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Protection' , 'Protection' , ), 111, (111, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Protection' , 'Protection' , ), 111, (111, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'StackSize' , 'StackSize' , ), 112, (112, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'StackSize' , 'StackSize' , ), 112, (112, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'Priority' , 'Priority' , ), 113, (113, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'Priority' , 'Priority' , ), 113, (113, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'TimeSlice' , 'TimeSlice' , ), 114, (114, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'TimeSlice' , 'TimeSlice' , ), 114, (114, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'BusyLampOff' , 'BusyLampOff' , ), 115, (115, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'BusyLampOff' , 'BusyLampOff' , ), 115, (115, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'DefaultGroup' , 'GroupNumber' , 'DefaultGroup' , ), 116, (116, (), [ (2, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'DefaultGroup' , 'GroupNumber' , 'DefaultGroup' , ), 116, (116, (), [ (2, 1, None, None) , 
			 (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'IgnoreAbort' , 'IgnoreConstant' , 'IgnoreAbort' , ), 117, (117, (), [ (3, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'IgnoreAbort' , 'IgnoreConstant' , 'IgnoreAbort' , ), 117, (117, (), [ (3, 1, None, None) , 
			 (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'IgnorePause' , 'IgnoreConstant' , 'IgnorePause' , ), 118, (118, (), [ (3, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'IgnorePause' , 'IgnoreConstant' , 'IgnorePause' , ), 118, (118, (), [ (3, 1, None, None) , 
			 (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'Invisible' , 'Invisible' , ), 119, (119, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'Invisible' , 'Invisible' , ), 119, (119, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'Owner' , 'Owner' , ), 120, (120, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'Owner' , 'Owner' , ), 120, (120, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'ReOpen' , 'AccessMode' , 'RejectMode' , ), 150, (150, (), [ (3, 1, None, None) , 
			 (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'Save' , 'FileName' , 'Option' , 'SaveClass' , ), 151, (151, (), [ 
			 (8, 1, None, None) , (12, 17, None, None) , (12, 17, None, None) , ], 1 , 1 , 4 , 2 , 328 , (3, 0, None, None) , 0 , )),
	(( 'Positions' , 'Positions' , ), 201, (201, (), [ (16397, 10, None, "IID('{A16AD1C7-F45A-11CF-8901-0020AF68F0A3}')") , ], 1 , 2 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'Lines' , 'Lines' , ), 202, (202, (), [ (16397, 10, None, "IID('{F5C31107-46AE-11D0-8901-0020AF68F0A3}')") , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'SubType' , 'SubType' , ), 203, (203, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'SubType' , 'SubType' , ), 203, (203, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'ApplData' , 'ApplData' , ), 204, (204, (), [ (16397, 10, None, "IID('{70F06EE1-DCE0-11D0-A083-00A02436CF7E}')") , ], 1 , 2 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'Labels' , 'Labels' , ), 205, (205, (), [ (16397, 10, None, "IID('{C3FB0D01-58D6-11D0-8901-0020AF68F0A3}')") , ], 1 , 2 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'Run' , 'StepType' , 'LineNum' , 'Direction' , ), 250, (250, (), [ 
			 (12, 17, None, None) , (12, 17, None, None) , (12, 17, None, None) , ], 1 , 1 , 4 , 3 , 384 , (3, 0, None, None) , 0 , )),
	(( 'Rename' , 'NewProgName' , ), 251, (251, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'DefaultGroupBitMask' , 'GroupBitMask' , ), 252, (252, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'Close' , ), 253, (253, (), [ ], 1 , 1 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
	(( 'EditLine' , 'LineNum' , 'ColNum' , ), 254, (254, (), [ (3, 1, None, None) , 
			 (12, 17, None, None) , ], 1 , 1 , 4 , 1 , 416 , (3, 0, None, None) , 0 , )),
	(( 'StorageType' , 'StorageType' , ), 255, (255, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 424 , (3, 0, None, None) , 0 , )),
	(( 'StorageType' , 'StorageType' , ), 255, (255, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 432 , (3, 0, None, None) , 0 , )),
]

ITPScreen_vtables_dispatch_ = 1
ITPScreen_vtables_ = [
	(( 'GetCurScreen' , 'SoftpartID' , 'ScreenID' , 'Title' , ), 101, (101, (), [ 
			 (16387, 2, None, None) , (16387, 2, None, None) , (16392, 2, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'SimKeys' , 'Keys' , ), 102, (102, (), [ (12, 1, None, None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'ForceMenu' , 'Softpart' , 'ScreenID' , ), 103, (103, (), [ (3, 1, None, None) , 
			 (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'TPLinkExecUrl' , 'TPConnID' , 'Url' , ), 104, (104, (), [ (3, 1, None, None) , 
			 (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

ITPSimpleLine_vtables_dispatch_ = 1
ITPSimpleLine_vtables_ = [
	(( 'Program' , 'Program' , ), 101, (101, (), [ (16397, 10, None, "IID('{D42AB5D5-8FFB-11D0-94CC-0020AF68F0A3}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Binary' , 'Binary' , ), 201, (201, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Binary' , 'Binary' , ), 201, (201, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Number' , 'Number' , ), 202, (202, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'MnCode' , 'MnCode' , ), 203, (203, (), [ (16401, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Text' , 'Text' , ), 204, (204, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'BinNoUpdate' , 'NoUpdate' , ), 205, (205, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'BinNoUpdate' , 'NoUpdate' , ), 205, (205, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'BinUpdate' , ), 206, (206, (), [ ], 1 , 1 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'BinGetFloat' , 'IndexOfByte' , 'pfRetValue' , ), 207, (207, (), [ (3, 1, None, None) , 
			 (16388, 10, None, None) , ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'BinSetFloat' , 'IndexOfByte' , 'fNewValue' , ), 208, (208, (), [ (3, 1, None, None) , 
			 (4, 1, None, None) , ], 1 , 1 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'ChangeLine' , 'Text' , ), 209, (209, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
]

ITask_vtables_dispatch_ = 1
ITask_vtables_ = [
	(( 'BusyLampOff' , 'BusyLampOff' , ), 201, (201, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'BusyLampOff' , 'BusyLampOff' , ), 201, (201, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'CurLine' , 'CurLine' , ), 202, (202, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'CurProgram' , 'CurProgram' , ), 203, (203, (), [ (16397, 10, None, "IID('{D42AB5D5-8FFB-11D0-94CC-0020AF68F0A3}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'CurRoutine' , 'CurRoutine' , ), 204, (204, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'HoldCondition' , 'HoldCondition' , 'HoldState' , ), 205, (205, (), [ (3, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'IgnoreAbort' , 'IgnoreConstant' , 'Ignore' , ), 206, (206, (), [ (3, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'IgnoreAbort' , 'IgnoreConstant' , 'Ignore' , ), 206, (206, (), [ (3, 1, None, None) , 
			 (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'IgnorePause' , 'IgnoreConstant' , 'Ignore' , ), 207, (207, (), [ (3, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'IgnorePause' , 'IgnoreConstant' , 'Ignore' , ), 207, (207, (), [ (3, 1, None, None) , 
			 (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Invisible' , 'Invisible' , ), 208, (208, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Invisible' , 'Invisible' , ), 208, (208, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'PauseOnShift' , 'PauseOnShift' , ), 209, (209, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'PauseOnShift' , 'PauseOnShift' , ), 209, (209, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'SystemTask' , 'SystemTask' , ), 210, (210, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'SystemTask' , 'SystemTask' , ), 210, (210, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'TPMotion' , 'TPMotion' , ), 211, (211, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'TPMotion' , 'TPMotion' , ), 211, (211, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'TraceEnable' , 'TraceEnable' , ), 212, (212, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'TraceEnable' , 'TraceEnable' , ), 212, (212, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'VarWriteEnable' , 'VarWriteEnable' , ), 213, (213, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'VarWriteEnable' , 'VarWriteEnable' , ), 213, (213, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'LockedArm' , 'GroupNum' , 'LockedArm' , ), 214, (214, (), [ (2, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'MotionControl' , 'GroupNum' , 'MotionControl' , ), 215, (215, (), [ (2, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'Name' , ), 216, (216, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'Name' , ), 216, (216, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'NotCircularMotion' , 'NotCircularMotion' , ), 217, (217, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'NotCircularMotion' , 'NotCircularMotion' , ), 217, (217, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'NumChild' , 'NumChild' , ), 218, (218, (), [ (16386, 10, None, None) , ], 1 , 2 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'NumMMR' , 'NumMMR' , ), 219, (219, (), [ (16386, 10, None, None) , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'Priority' , 'Priority' , ), 220, (220, (), [ (16386, 10, None, None) , ], 1 , 2 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'Priority' , 'Priority' , ), 220, (220, (), [ (2, 1, None, None) , ], 1 , 4 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'ProgramType' , 'ProgramType' , ), 221, (221, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'StackSize' , 'StackSize' , ), 222, (222, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'Status' , 'Status' , ), 223, (223, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'StepType' , 'StepType' , ), 224, (224, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'StepType' , 'StepType' , ), 224, (224, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'SuperMotion' , 'GroupNum' , 'SuperMotion' , ), 225, (225, (), [ (2, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'SuperMotion' , 'GroupNum' , 'SuperMotion' , ), 225, (225, (), [ (2, 1, None, None) , 
			 (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'TaskNum' , 'TaskNum' , ), 226, (226, (), [ (16386, 10, None, None) , ], 1 , 2 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'TCDStatus' , 'TCDStatus' , ), 227, (227, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'TimeSlice' , 'TimeSlice' , ), 228, (228, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'TraceLength' , 'TraceLength' , ), 229, (229, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'TraceLength' , 'TraceLength' , ), 229, (229, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
	(( 'TopProgram' , 'TopProgram' , ), 230, (230, (), [ (16397, 10, None, "IID('{D42AB5D5-8FFB-11D0-94CC-0020AF68F0A3}')") , ], 1 , 2 , 4 , 0 , 416 , (3, 0, None, None) , 0 , )),
	(( 'Abort' , 'Force' , 'Cancel' , ), 250, (250, (), [ (12, 17, None, None) , 
			 (12, 17, None, None) , ], 1 , 1 , 4 , 2 , 424 , (3, 0, None, None) , 0 , )),
	(( 'Pause' , 'Force' , 'Cancel' , ), 251, (251, (), [ (12, 17, None, None) , 
			 (12, 17, None, None) , ], 1 , 1 , 4 , 2 , 432 , (3, 0, None, None) , 0 , )),
	(( 'Continue' , 'LineNum' , 'Direction' , ), 252, (252, (), [ (12, 17, None, None) , 
			 (12, 17, None, None) , ], 1 , 1 , 4 , 2 , 440 , (3, 0, None, None) , 0 , )),
	(( 'Skip' , 'Number' , ), 253, (253, (), [ (12, 17, None, None) , ], 1 , 1 , 4 , 1 , 448 , (3, 0, None, None) , 0 , )),
]

ITasks_vtables_dispatch_ = 1
ITasks_vtables_ = [
	(( '_NewEnum' , 'NewEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'Index' , 'Name' , 'Task' , ), 0, (0, (), [ 
			 (12, 17, None, None) , (12, 17, None, None) , (16397, 10, None, "IID('{847A8F82-4626-11D1-B745-00C04FBBE42A}')") , ], 1 , 2 , 4 , 2 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'Index' , 'Name' , 'Task' , ), 0, (0, (), [ 
			 (12, 17, None, None) , (12, 17, None, None) , (16397, 10, None, "IID('{847A8F82-4626-11D1-B745-00C04FBBE42A}')") , ], 1 , 2 , 4 , 2 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'Count' , ), 201, (201, (), [ (16386, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'IsMonitoring' , 'IsMonitoring' , ), 202, (202, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'AbortAll' , 'Cancel' , ), 250, (250, (), [ (12, 17, None, None) , ], 1 , 1 , 4 , 1 , 96 , (3, 0, None, None) , 0 , )),
	(( 'PauseAll' , 'Cancel' , ), 251, (251, (), [ (12, 17, None, None) , ], 1 , 1 , 4 , 1 , 104 , (3, 0, None, None) , 0 , )),
	(( 'StartMonitor' , 'Interval' , ), 252, (252, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'StopMonitor' , ), 253, (253, (), [ ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'TryItem' , 'Name' , 'Task' , 'Result' , ), 254, (254, (), [ 
			 (8, 1, None, None) , (16397, 2, None, "IID('{847A8F82-4626-11D1-B745-00C04FBBE42A}')") , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
]

ITransform_vtables_dispatch_ = 1
ITransform_vtables_ = [
	(( 'Normal' , 'Normal' , ), 301, (301, (), [ (16397, 10, None, "IID('{C1578510-0F7A-11D2-86F4-00C04F9184DB}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Orient' , 'Orient' , ), 302, (302, (), [ (16397, 10, None, "IID('{C1578510-0F7A-11D2-86F4-00C04F9184DB}')") , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Approach' , 'Approach' , ), 303, (303, (), [ (16397, 10, None, "IID('{C1578510-0F7A-11D2-86F4-00C04F9184DB}')") , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Location' , 'Location' , ), 304, (304, (), [ (16397, 10, None, "IID('{C1578510-0F7A-11D2-86F4-00C04F9184DB}')") , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
]

IUOPIOSignal_vtables_dispatch_ = 1
IUOPIOSignal_vtables_ = [
	(( 'Value' , 'Value' , ), 201, (201, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Value' , 'Value' , ), 201, (201, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 202, (202, (), [ (16397, 10, None, "IID('{59DC16F8-AF91-11D0-A072-00A02436CF7E}')") , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'NoRefresh' , 'NoRefresh' , ), 250, (250, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'NoRefresh' , 'NoRefresh' , ), 250, (250, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'NoUpdate' , 'NoUpdate' , ), 251, (251, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'NoUpdate' , 'NoUpdate' , ), 251, (251, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Refresh' , ), 252, (252, (), [ ], 1 , 1 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'Update' , ), 253, (253, (), [ ], 1 , 1 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
]

IUserIOSignal_vtables_dispatch_ = 1
IUserIOSignal_vtables_ = [
	(( 'Index' , 'Index' , ), 201, (201, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Index' , 'Index' , ), 201, (201, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'LogicalType' , 'LogicalType' , ), 202, (202, (), [ (16386, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Value' , 'Value' , ), 203, (203, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Value' , 'Value' , ), 203, (203, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Simulate' , 'Simulate' , ), 204, (204, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'Simulate' , 'Simulate' , ), 204, (204, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Polarity' , 'Polarity' , ), 205, (205, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'Polarity' , 'Polarity' , ), 205, (205, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'Complementary' , 'Complementary' , ), 206, (206, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'Complementary' , 'Complementary' , ), 206, (206, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'IsInput' , 'IsInput' , ), 207, (207, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'IsBoolean' , 'IsBoolean' , ), 208, (208, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'CanSimulate' , 'CanSimulate' , ), 209, (209, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'CanInvert' , 'CanInvert' , ), 210, (210, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'CanComplement' , 'CanComplement' , ), 211, (211, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 212, (212, (), [ (16397, 10, None, "IID('{59DC16FA-AF91-11D0-A072-00A02436CF7E}')") , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
]

IUserIOSignals_vtables_dispatch_ = 1
IUserIOSignals_vtables_ = [
	(( '_NewEnum' , 'NewEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'LogicalType' , 'LogicalNum' , 'Index' , 'UserIOSignal' , 
			 ), 0, (0, (), [ (12, 17, None, None) , (12, 17, None, None) , (12, 17, None, None) , (16397, 10, None, "IID('{59DC16FF-AF91-11D0-A072-00A02436CF7E}')") , ], 1 , 2 , 4 , 3 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'LogicalType' , 'LogicalNum' , 'Index' , 'UserIOSignal' , 
			 ), 0, (0, (), [ (12, 17, None, None) , (12, 17, None, None) , (12, 17, None, None) , (16397, 10, None, "IID('{59DC16FF-AF91-11D0-A072-00A02436CF7E}')") , ], 1 , 2 , 4 , 3 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'Count' , ), 101, (101, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 102, (102, (), [ (16397, 10, None, "IID('{59DC16F6-AF91-11D0-A072-00A02436CF7E}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'IsMonitoring' , 'IsMonitoring' , ), 103, (103, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Add' , 'LogicalType' , 'LogicalNum' , 'Index' , 'UserIOSignal' , 
			 ), 151, (151, (), [ (2, 1, None, None) , (3, 1, None, None) , (12, 17, None, None) , (16397, 10, None, "IID('{59DC16FF-AF91-11D0-A072-00A02436CF7E}')") , ], 1 , 1 , 4 , 1 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Remove' , 'LogicalType' , 'LogicalNum' , 'Index' , ), 152, (152, (), [ 
			 (12, 17, None, None) , (12, 17, None, None) , (12, 17, None, None) , ], 1 , 1 , 4 , 3 , 112 , (3, 0, None, None) , 0 , )),
	(( 'StartMonitor' , 'Latency' , ), 153, (153, (), [ (3, 0, None, None) , ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'StopMonitor' , ), 154, (154, (), [ ], 1 , 1 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
]

IUserIOType_vtables_dispatch_ = 1
IUserIOType_vtables_ = [
	(( 'Name' , 'Name' , ), 201, (201, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'Name' , ), 201, (201, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Signals' , 'UserIOSignals' , ), 202, (202, (), [ (16397, 10, None, "IID('{59DC16FA-AF91-11D0-A072-00A02436CF7E}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Lock' , 'Lock' , ), 203, (203, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Lock' , 'Lock' , ), 203, (203, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
]

IVar_vtables_dispatch_ = 1
IVar_vtables_ = [
	(( 'Value' , 'Value' , ), 0, (0, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Value' , 'Value' , ), 0, (0, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'TypeCode' , 'TypeCode' , ), 301, (301, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'TypeName' , 'TypeName' , ), 302, (302, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'GroupNum' , 'GroupNum' , ), 303, (303, (), [ (16386, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'MaxStringLen' , 'MaxStringLen' , ), 304, (304, (), [ (16386, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'MaxValue' , 'MaxValue' , ), 305, (305, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'MinValue' , 'MinValue' , ), 306, (306, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'AccessCode' , 'AccessCode' , ), 307, (307, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'StorageClass' , 'StorageClass' , ), 308, (308, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 309, (309, (), [ (16397, 10, None, "IID('{88B57BCB-D0CA-11CF-959F-00A024329125}')") , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'IsInitialized' , 'IsInitialized' , ), 310, (310, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'Uninitialize' , ), 351, (351, (), [ ], 1 , 1 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'Override' , 'Override' , ), 400, (400, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'Override' , 'Override' , ), 400, (400, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'NoUpdate' , 'NoUpdate' , ), 401, (401, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'NoUpdate' , 'NoUpdate' , ), 401, (401, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'Update' , ), 402, (402, (), [ ], 1 , 1 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'Copy' , 'SourceVar' , ), 403, (403, (), [ (13, 1, None, "IID('{8C8ACC81-4F57-11D0-BC32-444553540000}')") , ], 1 , 1 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'Size' , 'Size' , ), 404, (404, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
]

IVarObject_vtables_dispatch_ = 1
IVarObject_vtables_ = [
	(( 'Program' , 'Program' , ), 101, (101, (), [ (16397, 10, None, "IID('{D42AB5D5-8FFB-11D0-94CC-0020AF68F0A3}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'FieldName' , 'FieldName' , ), 201, (201, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'VarName' , 'VarName' , ), 202, (202, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'IsMonitoring' , 'IsMonitoring' , ), 203, (203, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'NoRefresh' , 'NoRefresh' , ), 204, (204, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'NoRefresh' , 'NoRefresh' , ), 204, (204, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'StartMonitor' , 'Latency' , ), 250, (250, (), [ (3, 0, None, None) , ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'StopMonitor' , ), 251, (251, (), [ ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Refresh' , ), 252, (252, (), [ ], 1 , 1 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
]

IVarObject2_vtables_dispatch_ = 1
IVarObject2_vtables_ = [
	(( 'Override' , 'Override' , ), 400, (400, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Override' , 'Override' , ), 400, (400, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'NoUpdate' , 'NoUpdate' , ), 401, (401, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'NoUpdate' , 'NoUpdate' , ), 401, (401, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Update' , ), 402, (402, (), [ ], 1 , 1 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
]

IVarPosition_vtables_dispatch_ = 1
IVarPosition_vtables_ = [
	(( 'Parent' , 'Parent' , ), 301, (301, (), [ (16397, 10, None, "IID('{8C8ACC81-4F57-11D0-BC32-444553540000}')") , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'IsEqualTo' , 'TargetPos' , 'IsEqualTo' , ), 302, (302, (), [ (9, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'IsReachable' , 'From' , 'MoType' , 'OrientType' , 'Destination' , 
			 'MotionErrorInfo' , 'IsReachable' , ), 303, (303, (), [ (12, 17, None, None) , (3, 49, '6', None) , 
			 (3, 49, '2', None) , (12, 17, None, None) , (16397, 50, '0', "IID('{EE912848-BB81-427A-951F-5D9DC0FE74A7}')") , (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'Copy' , 'Position' , ), 304, (304, (), [ (9, 1, None, None) , ], 1 , 1 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'CheckReach' , 'From' , 'MoType' , 'OrientType' , 'Destination' , 
			 'MotionErrorInfo' , 'IsReachable' , ), 305, (305, (), [ (12, 17, None, None) , (3, 49, '6', None) , 
			 (3, 49, '2', None) , (12, 17, None, None) , (16397, 50, '0', "IID('{EE912848-BB81-427A-951F-5D9DC0FE74A7}')") , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
]

IVars_vtables_dispatch_ = 1
IVars_vtables_ = [
	(( '_NewEnum' , 'NewEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'Name' , 'Index' , 'Item' , ), 0, (0, (), [ 
			 (12, 17, None, None) , (12, 17, None, None) , (16393, 10, None, None) , ], 1 , 2 , 4 , 2 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'Name' , 'Index' , 'Item' , ), 0, (0, (), [ 
			 (12, 17, None, None) , (12, 17, None, None) , (16393, 10, None, None) , ], 1 , 2 , 4 , 2 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'Count' , ), 301, (301, (), [ (16386, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 302, (302, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Override' , 'Override' , ), 400, (400, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'Override' , 'Override' , ), 400, (400, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'NoUpdate' , 'NoUpdate' , ), 401, (401, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'NoUpdate' , 'NoUpdate' , ), 401, (401, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'Update' , ), 402, (402, (), [ ], 1 , 1 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'Copy' , 'SourceVars' , ), 403, (403, (), [ (13, 1, None, "IID('{88B57BCB-D0CA-11CF-959F-00A024329125}')") , ], 1 , 1 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'Size' , 'Size' , ), 404, (404, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'TryItem' , 'Name' , 'Index' , 'Item' , 'Result' , 
			 ), 405, (405, (), [ (12, 17, None, None) , (12, 17, None, None) , (16393, 2, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
]

IVector_vtables_dispatch_ = 1
IVector_vtables_ = [
	(( 'Program' , 'Program' , ), 101, (101, (), [ (16397, 10, None, "IID('{D42AB5D5-8FFB-11D0-94CC-0020AF68F0A3}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'NewEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'ValueNum' , 'Value' , ), 0, (0, (), [ (2, 1, None, None) , 
			 (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'ValueNum' , 'Value' , ), 0, (0, (), [ (2, 1, None, None) , 
			 (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'X' , 'X' , ), 201, (201, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'X' , 'X' , ), 201, (201, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Y' , 'Y' , ), 202, (202, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Y' , 'Y' , ), 202, (202, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Z' , 'Z' , ), 203, (203, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Z' , 'Z' , ), 203, (203, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 204, (204, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
]

IXyzWpr_vtables_dispatch_ = 1
IXyzWpr_vtables_ = [
	(( 'X' , 'X' , ), 301, (301, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'X' , 'X' , ), 301, (301, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Y' , 'Y' , ), 302, (302, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Y' , 'Y' , ), 302, (302, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Z' , 'Z' , ), 303, (303, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Z' , 'Z' , ), 303, (303, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'W' , 'W' , ), 304, (304, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'W' , 'W' , ), 304, (304, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'P' , 'P' , ), 305, (305, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'P' , 'P' , ), 305, (305, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'R' , 'R' , ), 306, (306, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'R' , 'R' , ), 306, (306, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'GetAll' , 'X' , 'Y' , 'Z' , 'W' , 
			 'P' , 'R' , ), 307, (307, (), [ (16389, 2, None, None) , (16389, 2, None, None) , 
			 (16389, 2, None, None) , (16389, 2, None, None) , (16389, 2, None, None) , (16389, 2, None, None) , ], 1 , 1 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'SetAll' , 'X' , 'Y' , 'Z' , 'W' , 
			 'P' , 'R' , ), 308, (308, (), [ (5, 1, None, None) , (5, 1, None, None) , 
			 (5, 1, None, None) , (5, 1, None, None) , (5, 1, None, None) , (5, 1, None, None) , ], 1 , 1 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
]

RecordMap = {
}

CLSIDToClassMap = {
	'{52A6CF60-4732-11D2-8738-00C04F98D092}' : IRobotEvents,
	'{115069C0-09C5-11D2-871C-00C04F98D092}' : IRobotErrorInfo,
	'{5BBFA760-09C6-11D2-871C-00C04F98D092}' : FRCRobotErrorInfo,
	'{6C779F22-4383-11D0-8901-0020AF68F0A3}' : IRobot,
	'{E2686FA8-1E42-11D1-B6FF-00C04FB9C401}' : ICurPosition,
	'{EF22631E-87A8-11D1-B765-00C04FBBE42A}' : ICurPositionEvents,
	'{E2686FA9-1E42-11D1-B6FF-00C04FB9C401}' : FRCCurPosition,
	'{D42AB5D4-8FFB-11D0-94CC-0020AF68F0A3}' : IRobotObject,
	'{A6861F10-5F34-4053-ABE4-55C55F595814}' : IRobot2,
	'{6D7E3A01-9ECC-11D0-94D5-0020AF68F0A3}' : FRCRobot,
	'{18F67740-46A8-11D0-8901-0020AF68F0A3}' : IPrograms,
	'{BB944831-DB7C-11D0-A083-00A02436CF7E}' : IProgramsEvents,
	'{1FBD567D-8F13-11D0-94CB-0020AF68F0A3}' : FRCPrograms,
	'{8C8ACC99-4F57-11D0-BC32-444553540000}' : IProgram,
	'{18254511-DC4C-11D0-A083-00A02436CF7E}' : IProgramEvents,
	'{D42AB5D5-8FFB-11D0-94CC-0020AF68F0A3}' : FRCProgram,
	'{88B57BCA-D0CA-11CF-959F-00A024329125}' : IVars,
	'{0AFC1567-101D-11D1-B6F6-00C04FB9E76B}' : IVarsEvents,
	'{88B57BCB-D0CA-11CF-959F-00A024329125}' : FRCVars,
	'{A6F54250-DE6F-11D0-9F9F-00A024329125}' : IVarObject,
	'{D42AB5D3-8FFB-11D0-94CC-0020AF68F0A3}' : ITPProgram,
	'{F96C81C1-DCD9-11D0-A083-00A02436CF7E}' : ITPProgramEvents,
	'{F5C31101-46AE-11D0-8901-0020AF68F0A3}' : FRCTPProgram,
	'{A16AD1C6-F45A-11CF-8901-0020AF68F0A3}' : ITPPositions,
	'{10CB2FD0-DCDC-11D0-A083-00A02436CF7E}' : ITPPositionsEvents,
	'{A16AD1C7-F45A-11CF-8901-0020AF68F0A3}' : FRCTPPositions,
	'{3A49BE60-F5B9-11CF-8901-0020AF68F0A3}' : ITPPosition,
	'{21CB68D1-DCDE-11D0-A083-00A02436CF7E}' : ITPPositionEvents,
	'{3A49BE61-F5B9-11CF-8901-0020AF68F0A3}' : FRCTPPosition,
	'{A47A5880-056D-11D0-8901-0020AF68F0A3}' : IGroupPosition,
	'{18B02B4D-9DA9-11D1-B73B-00C04FB9E76B}' : IGroupPositionEvents,
	'{A47A5881-056D-11D0-8901-0020AF68F0A3}' : FRCGroupPosition,
	'{50F24196-4CB8-4375-96C3-A05885F4189D}' : IMotionErrorInfo,
	'{EE912848-BB81-427A-951F-5D9DC0FE74A7}' : FRCMotionErrorInfo,
	'{A47A5884-056D-11D0-8901-0020AF68F0A3}' : IXyzWpr,
	'{A47A5885-056D-11D0-8901-0020AF68F0A3}' : FRCXyzWpr,
	'{D42AB5DC-8FFB-11D0-94CC-0020AF68F0A3}' : ICartesianFormat,
	'{C58B0E60-ECD4-11D0-9FA5-00A024329125}' : IConfig,
	'{C58B0E61-ECD4-11D0-9FA5-00A024329125}' : FRCConfig,
	'{035505A0-1C41-11D0-8901-0020AF68F0A3}' : IAxesCollection,
	'{035505A1-1C41-11D0-8901-0020AF68F0A3}' : FRCAxesCollection,
	'{E494B8E1-A59A-11D2-8724-00C04F918427}' : IPosition2,
	'{D6219FE0-87A0-11D1-B765-00C04FBBE42A}' : IPositionEvents,
	'{D42AB5DB-8FFB-11D0-94CC-0020AF68F0A3}' : FRCPosition,
	'{F5C31106-46AE-11D0-8901-0020AF68F0A3}' : ITPLines,
	'{2D9F8871-DCDA-11D0-A083-00A02436CF7E}' : ITPLinesEvents,
	'{F5C31107-46AE-11D0-8901-0020AF68F0A3}' : FRCTPLines,
	'{12585150-9394-11D2-877C-00C04FB9C401}' : ISelectedLines,
	'{26466EE1-9393-11D2-877C-00C04FB9C401}' : ISelectedLinesEvents,
	'{58ADC520-9395-11D2-877C-00C04FB9C401}' : FRCSelectedLines,
	'{A7E095A2-DCDE-11D0-A083-00A02436CF7E}' : ITPApplDataCollection,
	'{A7E095A1-DCDE-11D0-A083-00A02436CF7E}' : ITPApplDataCollectionEvents,
	'{70F06EE1-DCE0-11D0-A083-00A02436CF7E}' : FRCTPApplDataCollection,
	'{C3FB0D00-58D6-11D0-8901-0020AF68F0A3}' : ITPLabels,
	'{90E827A1-DCDB-11D0-A083-00A02436CF7E}' : ITPLabelsEvents,
	'{C3FB0D01-58D6-11D0-8901-0020AF68F0A3}' : FRCTPLabels,
	'{C3FB0D02-58D6-11D0-8901-0020AF68F0A3}' : ITPLabel,
	'{D81C9351-DCDB-11D0-A083-00A02436CF7E}' : ITPLabelEvents,
	'{C3FB0D03-58D6-11D0-8901-0020AF68F0A3}' : FRCTPLabel,
	'{6055D69A-FFAE-11D0-B6F4-00C04FB9C401}' : ISysPositions,
	'{94F57CE7-381B-11D1-B6FE-00C04FB9E76B}' : ISysPositionsEvents,
	'{6055D69B-FFAE-11D0-B6F4-00C04FB9C401}' : FRCSysPositions,
	'{6055D698-FFAE-11D0-B6F4-00C04FB9C401}' : ISysPosition,
	'{3AC7EA79-381C-11D1-B6FE-00C04FB9E76B}' : ISysPositionEvents,
	'{6055D699-FFAE-11D0-B6F4-00C04FB9C401}' : FRCSysPosition,
	'{DC2FA0C7-FFAB-11D0-B6F4-00C04FB9C401}' : ISysGroupPosition,
	'{6EA7D4AD-381C-11D1-B6FE-00C04FB9E76B}' : ISysGroupPositionEvents,
	'{DC2FA0C8-FFAB-11D0-B6F4-00C04FB9C401}' : FRCSysGroupPosition,
	'{D42AB5DA-8FFB-11D0-94CC-0020AF68F0A3}' : IPosition,
	'{7C37F232-A494-11D0-A37F-0020AF39BE5A}' : IAlarms,
	'{7DD25A00-AC49-11D0-8B7F-0020AF39BE5A}' : IAlarmNotify,
	'{7C37F235-A494-11D0-A37F-0020AF39BE5A}' : FRCAlarms,
	'{7C37F236-A494-11D0-A37F-0020AF39BE5A}' : IAlarm,
	'{7C37F237-A494-11D0-A37F-0020AF39BE5A}' : FRCAlarm,
	'{59DC16EB-AF91-11D0-A072-00A02436CF7E}' : IIOTypes,
	'{B23F3D71-F86A-11D0-A093-00A02436CF7E}' : IIOTypesEvents,
	'{59DC16ED-AF91-11D0-A072-00A02436CF7E}' : FRCIOTypes,
	'{59DC16EF-AF91-11D0-A072-00A02436CF7E}' : IIOType,
	'{59DC16F1-AF91-11D0-A072-00A02436CF7E}' : FRCIOType,
	'{59DC16F5-AF91-11D0-A072-00A02436CF7E}' : IUserIOType,
	'{95741D17-F9F1-11D0-B6EE-00C04FB9E76B}' : IUserIOTypeEvents,
	'{59DC16F6-AF91-11D0-A072-00A02436CF7E}' : FRCUserIOType,
	'{59DC16F9-AF91-11D0-A072-00A02436CF7E}' : IUserIOSignals,
	'{C240AAA1-F86F-11D0-A093-00A02436CF7E}' : IUserIOSignalsEvents,
	'{59DC16FA-AF91-11D0-A072-00A02436CF7E}' : FRCUserIOSignals,
	'{59DC16FE-AF91-11D0-A072-00A02436CF7E}' : IUserIOSignal,
	'{0DBE3EF1-F870-11D0-A093-00A02436CF7E}' : IIOSignalEvents,
	'{59DC16FF-AF91-11D0-A072-00A02436CF7E}' : FRCUserIOSignal,
	'{59DC16FB-AF91-11D0-A072-00A02436CF7E}' : IIOSignal,
	'{DEE5EAE0-E283-11D0-8BB6-0020AF39BE5A}' : ITPScreen,
	'{797CEA11-DD7B-11D2-8A28-00105AE42A59}' : ITPScreenEvents,
	'{660E6870-E286-11D0-8BB6-0020AF39BE5A}' : FRCTPScreen,
	'{5F26BE72-4626-11D1-B745-00C04FBBE42A}' : ITasks,
	'{48F075F8-4626-11D1-B745-00C04FBBE42A}' : ITasksEvents,
	'{6B01CFFC-4626-11D1-B745-00C04FBBE42A}' : FRCTasks,
	'{7745C8FE-4626-11D1-B745-00C04FBBE42A}' : ITask,
	'{F22A6948-A310-11D1-B77A-00C04FBBE42A}' : ITaskEvents,
	'{847A8F82-4626-11D1-B745-00C04FBBE42A}' : FRCTask,
	'{3C3988CD-9275-11D1-B6F9-00C04FA3BD85}' : ISynchData,
	'{2AF44182-9273-11D1-B6F9-00C04FA3BD85}' : FRCSynchData,
	'{2AF44183-9273-11D1-B6F9-00C04FA3BD85}' : IFeatures,
	'{2AF44184-9273-11D1-B6F9-00C04FA3BD85}' : FRCFeatures,
	'{2AF44185-9273-11D1-B6F9-00C04FA3BD85}' : IFeature,
	'{2AF44186-9273-11D1-B6F9-00C04FA3BD85}' : FRCFeature,
	'{3C05D26D-9BE8-11D1-B6FC-00C04FA3BD85}' : ITPInstructions,
	'{3C05D26E-9BE8-11D1-B6FC-00C04FA3BD85}' : FRCTPInstructions,
	'{3C05D26F-9BE8-11D1-B6FC-00C04FA3BD85}' : ITPInstruction,
	'{3C05D270-9BE8-11D1-B6FC-00C04FA3BD85}' : FRCTPInstruction,
	'{8FAFC8E7-B2B8-11D1-B705-00C04FA3BD85}' : ISynchApplData,
	'{8FAFC8E8-B2B8-11D1-B705-00C04FA3BD85}' : FRCSynchApplData,
	'{8FAFC8E9-B2B8-11D1-B705-00C04FA3BD85}' : ISynchApplDataItem,
	'{8FAFC8EA-B2B8-11D1-B705-00C04FA3BD85}' : FRCSynchApplDataItem,
	'{78063945-E50A-11D1-B778-00C04FB99C75}' : IApplications,
	'{679622C3-E50A-11D1-B778-00C04FB99C75}' : FRCApplications,
	'{FCCE9E60-9420-11D1-B751-00C04FB99C75}' : IPacketEvent,
	'{298DEBD5-9976-11D1-B753-00C04FB99C75}' : IPacketEventEvents,
	'{FCCE9E5F-9420-11D1-B751-00C04FB99C75}' : FRCPacketEvent,
	'{7B125AAE-9330-11D1-B751-00C04FB99C75}' : IPacket,
	'{64AF4546-9331-11D1-B751-00C04FB99C75}' : FRCPacket,
	'{6F33A4D2-91F3-11D3-877C-00C04F81118D}' : IScatteredAccess,
	'{6F33A4D1-91F3-11D3-877C-00C04F81118D}' : FRCScatteredAccess,
	'{4553DA61-ACA1-11D3-8783-00C04F81118D}' : ISysInfo,
	'{4553DA63-ACA1-11D3-8783-00C04F81118D}' : FRCSysInfo,
	'{B475BC90-3AF1-11D4-9F66-00105AE428C3}' : IPipes,
	'{B475BC92-3AF1-11D4-9F66-00105AE428C3}' : IPipesEvents,
	'{B475BC91-3AF1-11D4-9F66-00105AE428C3}' : FRCPipes,
	'{B475BC94-3AF1-11D4-9F66-00105AE428C3}' : IPipe,
	'{B475BC93-3AF1-11D4-9F66-00105AE428C3}' : IPipeEvents,
	'{B475BC95-3AF1-11D4-9F66-00105AE428C3}' : FRCPipe,
	'{D21DF523-8D4A-4A7C-B367-5725E53A21A1}' : IIndPosition,
	'{0872A5E4-398C-46A3-989D-1E9B1BCA72DC}' : IIndPositionEvents,
	'{B4819F73-FC65-4475-97D3-974ACF6EE03E}' : FRCIndPosition,
	'{1F6F314A-F81F-4B6D-AEDE-5AFD558256E8}' : IIndGroupPosition,
	'{82DDCEA2-3608-404D-90B2-E636F7E7DDD8}' : IIndGroupPositionEvents,
	'{DBE7F3B9-01E5-4935-A211-B5CC9D3A1048}' : FRCIndGroupPosition,
	'{75CEF1D6-1E43-11D1-B6FF-00C04FB9C401}' : ICurGroupPosition,
	'{2BF7E386-87A9-11D1-B765-00C04FBBE42A}' : ICurGroupPositionEvents,
	'{75CEF1D7-1E43-11D1-B6FF-00C04FB9C401}' : FRCCurGroupPosition,
	'{53D6E5D1-F5E2-11D3-9F35-00500409FF06}' : IRobManProxy,
	'{53D6E5D3-F5E2-11D3-9F35-00500409FF06}' : IRobManProxyEvents,
	'{53D6E5D2-F5E2-11D3-9F35-00500409FF06}' : FRCRobManProxy,
	'{D42AB5D9-8FFB-11D0-94CC-0020AF68F0A3}' : IProgramObject,
	'{8C8ACC9A-4F57-11D0-BC32-444553540000}' : FRCVRProgram,
	'{44E3D090-7178-11D1-B762-00C04FBBE42A}' : IKARELProgramEvents,
	'{73FF06C4-7178-11D1-B762-00C04FBBE42A}' : IKARELProgram,
	'{DA462B71-DD0D-11D0-A083-00A02436CF7E}' : FRCKARELProgram,
	'{A47A5882-056D-11D0-8901-0020AF68F0A3}' : ITransform,
	'{924CC060-0F7A-11D2-86F4-00C04F9184DB}' : IVector,
	'{C1578510-0F7A-11D2-86F4-00C04F9184DB}' : FRCVector,
	'{A47A5883-056D-11D0-8901-0020AF68F0A3}' : FRCTransform,
	'{A47A5886-056D-11D0-8901-0020AF68F0A3}' : IJoint,
	'{A47A5887-056D-11D0-8901-0020AF68F0A3}' : FRCJoint,
	'{C19FE67C-A462-11D0-B304-00A02479C928}' : IVarEvents,
	'{8C8ACC80-4F57-11D0-BC32-444553540000}' : IVar,
	'{8C8ACC81-4F57-11D0-BC32-444553540000}' : FRCVar,
	'{6B51A440-212A-11D0-959F-00A024329125}' : IRegNumeric,
	'{6B51A441-212A-11D0-959F-00A024329125}' : FRCRegNumeric,
	'{CADEF7CB-650F-45B7-BC95-9080FA32640B}' : IRegString,
	'{B5BD1EBA-FEC8-49CC-965B-7DD03974CDB8}' : FRCRegString,
	'{E3FFB438-2613-11D1-B702-00C04FB9C401}' : IVarPosition,
	'{E3FFB439-2613-11D1-B702-00C04FB9C401}' : FRCVarPosition,
	'{34E3E250-1107-11D2-86F4-00C04F9184DB}' : ICommonAssoc,
	'{15AAA600-1108-11D2-86F4-00C04F9184DB}' : FRCCommonAssoc,
	'{424160A0-1108-11D2-86F4-00C04F9184DB}' : IGroupAssoc,
	'{4DE6A770-1108-11D2-86F4-00C04F9184DB}' : FRCGroupAssoc,
	'{D0EDFE01-C6AC-11D2-8727-00C04F81118D}' : IVarObject2,
	'{0277AC51-DCDB-11D0-A083-00A02436CF7E}' : ITPLineEvents,
	'{FC761640-4CEA-11D0-8901-0020AF68F0A3}' : ITPLineHelper,
	'{FC761641-4CEA-11D0-8901-0020AF68F0A3}' : FRCTPLineHelper,
	'{9728B471-DCE0-11D0-A083-00A02436CF7E}' : ITPApplDataEvents,
	'{343D8EB1-DCE1-11D0-A083-00A02436CF7E}' : ITPApplDataHelper,
	'{51FF0460-DCE1-11D0-A083-00A02436CF7E}' : FRCTPApplDataHelper,
	'{6C473F21-B5F0-11D2-8781-00C04F98D092}' : ITPSimpleLine,
	'{6C473F20-B5F0-11D2-8781-00C04F98D092}' : FRCTPSimpleLine,
	'{59DC16F2-AF91-11D0-A072-00A02436CF7E}' : ISystemIOType,
	'{59DC16F7-AF91-11D0-A072-00A02436CF7E}' : IIOSignals,
	'{39A374D1-F86E-11D0-A093-00A02436CF7E}' : IIOSignalsEvents,
	'{59DC16F8-AF91-11D0-A072-00A02436CF7E}' : FRCIOSignals,
	'{D3EE1B91-8BB6-11D3-877C-00C04F81118D}' : IIOSignal2,
	'{59DC170B-AF91-11D0-A072-00A02436CF7E}' : FRCIOSignal,
	'{59DC16F3-AF91-11D0-A072-00A02436CF7E}' : IConfigurableIOType,
	'{59DC1700-AF91-11D0-A072-00A02436CF7E}' : IIOConfigs,
	'{021408E1-F879-11D0-A093-00A02436CF7E}' : IIOConfigsEvents,
	'{59DC1701-AF91-11D0-A072-00A02436CF7E}' : FRCIOConfigs,
	'{59DC1702-AF91-11D0-A072-00A02436CF7E}' : IIOConfig,
	'{051D0EE2-F930-11D0-B6EE-00C04FB9E76B}' : IIOConfigEvents,
	'{59DC1703-AF91-11D0-A072-00A02436CF7E}' : FRCIOConfig,
	'{59DC16F4-AF91-11D0-A072-00A02436CF7E}' : FRCDigitalIOType,
	'{714CC916-B4E5-11D0-A073-00A02436CF7E}' : FRCAnalogIOType,
	'{714CC917-B4E5-11D0-A073-00A02436CF7E}' : FRCGroupIOType,
	'{714CC918-B4E5-11D0-A073-00A02436CF7E}' : FRCUOPIOType,
	'{714CC919-B4E5-11D0-A073-00A02436CF7E}' : FRCRobotIOType,
	'{714CC91A-B4E5-11D0-A073-00A02436CF7E}' : FRCSOPIOType,
	'{714CC91B-B4E5-11D0-A073-00A02436CF7E}' : FRCTPIOType,
	'{714CC91C-B4E5-11D0-A073-00A02436CF7E}' : FRCPLCIOType,
	'{714CC91D-B4E5-11D0-A073-00A02436CF7E}' : FRCWeldDigitalIOType,
	'{714CC91E-B4E5-11D0-A073-00A02436CF7E}' : FRCLaserDigitalIOType,
	'{714CC91F-B4E5-11D0-A073-00A02436CF7E}' : FRCLaserAnalogIOType,
	'{714CC920-B4E5-11D0-A073-00A02436CF7E}' : FRCWeldStickIOType,
	'{A16B2E95-219A-4FA8-9DE8-021D429B8805}' : FRCFlagType,
	'{1C9FC454-C455-4A41-80EF-0894FEB07BF8}' : FRCMarkerType,
	'{59DC16FC-AF91-11D0-A072-00A02436CF7E}' : IDigitalIOSignal,
	'{59DC16FD-AF91-11D0-A072-00A02436CF7E}' : FRCDigitalIOSignal,
	'{714CC921-B4E5-11D0-A073-00A02436CF7E}' : IAnalogIOSignal,
	'{714CC922-B4E5-11D0-A073-00A02436CF7E}' : FRCAnalogIOSignal,
	'{714CC923-B4E5-11D0-A073-00A02436CF7E}' : FRCGroupIOSignal,
	'{714CC924-B4E5-11D0-A073-00A02436CF7E}' : IUOPIOSignal,
	'{714CC925-B4E5-11D0-A073-00A02436CF7E}' : FRCUOPIOSignal,
	'{714CC926-B4E5-11D0-A073-00A02436CF7E}' : IRobotIOSignal,
	'{714CC927-B4E5-11D0-A073-00A02436CF7E}' : FRCRobotIOSignal,
	'{1A191D0B-ECA1-42E1-A200-1FC17400A54E}' : FRCFlagSignal,
	'{A5F1E1FE-F2B7-40AB-9D33-6932112978BD}' : FRCMarkerSignal,
	'{714CC928-B4E5-11D0-A073-00A02436CF7E}' : FRCSOPIOSignal,
	'{714CC929-B4E5-11D0-A073-00A02436CF7E}' : FRCTPIOSignal,
	'{714CC92B-B4E5-11D0-A073-00A02436CF7E}' : FRCPLCIOSignal,
	'{714CC92C-B4E5-11D0-A073-00A02436CF7E}' : FRCWeldDigitalIOSignal,
	'{714CC92D-B4E5-11D0-A073-00A02436CF7E}' : FRCLaserDigitalIOSignal,
	'{714CC92E-B4E5-11D0-A073-00A02436CF7E}' : FRCLaserAnalogIOSignal,
	'{714CC92F-B4E5-11D0-A073-00A02436CF7E}' : FRCWeldStickIOSignal,
	'{B475BC96-3AF1-11D4-9F66-00105AE428C3}' : IPipeFields,
	'{B475BC97-3AF1-11D4-9F66-00105AE428C3}' : FRCPipeFields,
	'{B475BC98-3AF1-11D4-9F66-00105AE428C3}' : IPipeField,
	'{B475BC99-3AF1-11D4-9F66-00105AE428C3}' : FRCPipeField,
	'{B475BC9A-3AF1-11D4-9F66-00105AE428C3}' : IPipePosition,
	'{B475BC9B-3AF1-11D4-9F66-00105AE428C3}' : FRCPipePosition,
}
CLSIDToPackageMap = {}
win32com.client.CLSIDToClass.RegisterCLSIDsFromDict( CLSIDToClassMap )
VTablesToPackageMap = {}
VTablesToClassMap = {
	'{115069C0-09C5-11D2-871C-00C04F98D092}' : 'IRobotErrorInfo',
	'{6C779F22-4383-11D0-8901-0020AF68F0A3}' : 'IRobot',
	'{E2686FA8-1E42-11D1-B6FF-00C04FB9C401}' : 'ICurPosition',
	'{D42AB5D4-8FFB-11D0-94CC-0020AF68F0A3}' : 'IRobotObject',
	'{A6861F10-5F34-4053-ABE4-55C55F595814}' : 'IRobot2',
	'{18F67740-46A8-11D0-8901-0020AF68F0A3}' : 'IPrograms',
	'{8C8ACC99-4F57-11D0-BC32-444553540000}' : 'IProgram',
	'{88B57BCA-D0CA-11CF-959F-00A024329125}' : 'IVars',
	'{A6F54250-DE6F-11D0-9F9F-00A024329125}' : 'IVarObject',
	'{D42AB5D3-8FFB-11D0-94CC-0020AF68F0A3}' : 'ITPProgram',
	'{A16AD1C6-F45A-11CF-8901-0020AF68F0A3}' : 'ITPPositions',
	'{3A49BE60-F5B9-11CF-8901-0020AF68F0A3}' : 'ITPPosition',
	'{A47A5880-056D-11D0-8901-0020AF68F0A3}' : 'IGroupPosition',
	'{50F24196-4CB8-4375-96C3-A05885F4189D}' : 'IMotionErrorInfo',
	'{A47A5884-056D-11D0-8901-0020AF68F0A3}' : 'IXyzWpr',
	'{D42AB5DC-8FFB-11D0-94CC-0020AF68F0A3}' : 'ICartesianFormat',
	'{C58B0E60-ECD4-11D0-9FA5-00A024329125}' : 'IConfig',
	'{035505A0-1C41-11D0-8901-0020AF68F0A3}' : 'IAxesCollection',
	'{E494B8E1-A59A-11D2-8724-00C04F918427}' : 'IPosition2',
	'{F5C31106-46AE-11D0-8901-0020AF68F0A3}' : 'ITPLines',
	'{12585150-9394-11D2-877C-00C04FB9C401}' : 'ISelectedLines',
	'{A7E095A2-DCDE-11D0-A083-00A02436CF7E}' : 'ITPApplDataCollection',
	'{C3FB0D00-58D6-11D0-8901-0020AF68F0A3}' : 'ITPLabels',
	'{C3FB0D02-58D6-11D0-8901-0020AF68F0A3}' : 'ITPLabel',
	'{6055D69A-FFAE-11D0-B6F4-00C04FB9C401}' : 'ISysPositions',
	'{6055D698-FFAE-11D0-B6F4-00C04FB9C401}' : 'ISysPosition',
	'{DC2FA0C7-FFAB-11D0-B6F4-00C04FB9C401}' : 'ISysGroupPosition',
	'{D42AB5DA-8FFB-11D0-94CC-0020AF68F0A3}' : 'IPosition',
	'{7C37F232-A494-11D0-A37F-0020AF39BE5A}' : 'IAlarms',
	'{7C37F236-A494-11D0-A37F-0020AF39BE5A}' : 'IAlarm',
	'{59DC16EB-AF91-11D0-A072-00A02436CF7E}' : 'IIOTypes',
	'{59DC16EF-AF91-11D0-A072-00A02436CF7E}' : 'IIOType',
	'{59DC16F5-AF91-11D0-A072-00A02436CF7E}' : 'IUserIOType',
	'{59DC16F9-AF91-11D0-A072-00A02436CF7E}' : 'IUserIOSignals',
	'{59DC16FE-AF91-11D0-A072-00A02436CF7E}' : 'IUserIOSignal',
	'{59DC16FB-AF91-11D0-A072-00A02436CF7E}' : 'IIOSignal',
	'{DEE5EAE0-E283-11D0-8BB6-0020AF39BE5A}' : 'ITPScreen',
	'{5F26BE72-4626-11D1-B745-00C04FBBE42A}' : 'ITasks',
	'{7745C8FE-4626-11D1-B745-00C04FBBE42A}' : 'ITask',
	'{3C3988CD-9275-11D1-B6F9-00C04FA3BD85}' : 'ISynchData',
	'{2AF44183-9273-11D1-B6F9-00C04FA3BD85}' : 'IFeatures',
	'{2AF44185-9273-11D1-B6F9-00C04FA3BD85}' : 'IFeature',
	'{3C05D26D-9BE8-11D1-B6FC-00C04FA3BD85}' : 'ITPInstructions',
	'{3C05D26F-9BE8-11D1-B6FC-00C04FA3BD85}' : 'ITPInstruction',
	'{8FAFC8E7-B2B8-11D1-B705-00C04FA3BD85}' : 'ISynchApplData',
	'{8FAFC8E9-B2B8-11D1-B705-00C04FA3BD85}' : 'ISynchApplDataItem',
	'{78063945-E50A-11D1-B778-00C04FB99C75}' : 'IApplications',
	'{FCCE9E60-9420-11D1-B751-00C04FB99C75}' : 'IPacketEvent',
	'{7B125AAE-9330-11D1-B751-00C04FB99C75}' : 'IPacket',
	'{6F33A4D2-91F3-11D3-877C-00C04F81118D}' : 'IScatteredAccess',
	'{4553DA61-ACA1-11D3-8783-00C04F81118D}' : 'ISysInfo',
	'{B475BC90-3AF1-11D4-9F66-00105AE428C3}' : 'IPipes',
	'{B475BC94-3AF1-11D4-9F66-00105AE428C3}' : 'IPipe',
	'{D21DF523-8D4A-4A7C-B367-5725E53A21A1}' : 'IIndPosition',
	'{1F6F314A-F81F-4B6D-AEDE-5AFD558256E8}' : 'IIndGroupPosition',
	'{75CEF1D6-1E43-11D1-B6FF-00C04FB9C401}' : 'ICurGroupPosition',
	'{53D6E5D1-F5E2-11D3-9F35-00500409FF06}' : 'IRobManProxy',
	'{D42AB5D9-8FFB-11D0-94CC-0020AF68F0A3}' : 'IProgramObject',
	'{73FF06C4-7178-11D1-B762-00C04FBBE42A}' : 'IKARELProgram',
	'{A47A5882-056D-11D0-8901-0020AF68F0A3}' : 'ITransform',
	'{924CC060-0F7A-11D2-86F4-00C04F9184DB}' : 'IVector',
	'{A47A5886-056D-11D0-8901-0020AF68F0A3}' : 'IJoint',
	'{8C8ACC80-4F57-11D0-BC32-444553540000}' : 'IVar',
	'{6B51A440-212A-11D0-959F-00A024329125}' : 'IRegNumeric',
	'{CADEF7CB-650F-45B7-BC95-9080FA32640B}' : 'IRegString',
	'{E3FFB438-2613-11D1-B702-00C04FB9C401}' : 'IVarPosition',
	'{34E3E250-1107-11D2-86F4-00C04F9184DB}' : 'ICommonAssoc',
	'{424160A0-1108-11D2-86F4-00C04F9184DB}' : 'IGroupAssoc',
	'{D0EDFE01-C6AC-11D2-8727-00C04F81118D}' : 'IVarObject2',
	'{FC761640-4CEA-11D0-8901-0020AF68F0A3}' : 'ITPLineHelper',
	'{343D8EB1-DCE1-11D0-A083-00A02436CF7E}' : 'ITPApplDataHelper',
	'{6C473F21-B5F0-11D2-8781-00C04F98D092}' : 'ITPSimpleLine',
	'{59DC16F2-AF91-11D0-A072-00A02436CF7E}' : 'ISystemIOType',
	'{59DC16F7-AF91-11D0-A072-00A02436CF7E}' : 'IIOSignals',
	'{D3EE1B91-8BB6-11D3-877C-00C04F81118D}' : 'IIOSignal2',
	'{59DC16F3-AF91-11D0-A072-00A02436CF7E}' : 'IConfigurableIOType',
	'{59DC1700-AF91-11D0-A072-00A02436CF7E}' : 'IIOConfigs',
	'{59DC1702-AF91-11D0-A072-00A02436CF7E}' : 'IIOConfig',
	'{59DC16FC-AF91-11D0-A072-00A02436CF7E}' : 'IDigitalIOSignal',
	'{714CC921-B4E5-11D0-A073-00A02436CF7E}' : 'IAnalogIOSignal',
	'{714CC924-B4E5-11D0-A073-00A02436CF7E}' : 'IUOPIOSignal',
	'{714CC926-B4E5-11D0-A073-00A02436CF7E}' : 'IRobotIOSignal',
	'{B475BC96-3AF1-11D4-9F66-00105AE428C3}' : 'IPipeFields',
	'{B475BC98-3AF1-11D4-9F66-00105AE428C3}' : 'IPipeField',
	'{B475BC9A-3AF1-11D4-9F66-00105AE428C3}' : 'IPipePosition',
}


NamesToIIDMap = {
	'IRobotEvents' : '{52A6CF60-4732-11D2-8738-00C04F98D092}',
	'IRobotErrorInfo' : '{115069C0-09C5-11D2-871C-00C04F98D092}',
	'IRobot' : '{6C779F22-4383-11D0-8901-0020AF68F0A3}',
	'ICurPosition' : '{E2686FA8-1E42-11D1-B6FF-00C04FB9C401}',
	'ICurPositionEvents' : '{EF22631E-87A8-11D1-B765-00C04FBBE42A}',
	'IRobotObject' : '{D42AB5D4-8FFB-11D0-94CC-0020AF68F0A3}',
	'IRobot2' : '{A6861F10-5F34-4053-ABE4-55C55F595814}',
	'IPrograms' : '{18F67740-46A8-11D0-8901-0020AF68F0A3}',
	'IProgramsEvents' : '{BB944831-DB7C-11D0-A083-00A02436CF7E}',
	'IProgram' : '{8C8ACC99-4F57-11D0-BC32-444553540000}',
	'IProgramEvents' : '{18254511-DC4C-11D0-A083-00A02436CF7E}',
	'IVars' : '{88B57BCA-D0CA-11CF-959F-00A024329125}',
	'IVarsEvents' : '{0AFC1567-101D-11D1-B6F6-00C04FB9E76B}',
	'IVarObject' : '{A6F54250-DE6F-11D0-9F9F-00A024329125}',
	'ITPProgram' : '{D42AB5D3-8FFB-11D0-94CC-0020AF68F0A3}',
	'ITPProgramEvents' : '{F96C81C1-DCD9-11D0-A083-00A02436CF7E}',
	'ITPPositions' : '{A16AD1C6-F45A-11CF-8901-0020AF68F0A3}',
	'ITPPositionsEvents' : '{10CB2FD0-DCDC-11D0-A083-00A02436CF7E}',
	'ITPPosition' : '{3A49BE60-F5B9-11CF-8901-0020AF68F0A3}',
	'ITPPositionEvents' : '{21CB68D1-DCDE-11D0-A083-00A02436CF7E}',
	'IGroupPosition' : '{A47A5880-056D-11D0-8901-0020AF68F0A3}',
	'IGroupPositionEvents' : '{18B02B4D-9DA9-11D1-B73B-00C04FB9E76B}',
	'IMotionErrorInfo' : '{50F24196-4CB8-4375-96C3-A05885F4189D}',
	'IXyzWpr' : '{A47A5884-056D-11D0-8901-0020AF68F0A3}',
	'ICartesianFormat' : '{D42AB5DC-8FFB-11D0-94CC-0020AF68F0A3}',
	'IConfig' : '{C58B0E60-ECD4-11D0-9FA5-00A024329125}',
	'IAxesCollection' : '{035505A0-1C41-11D0-8901-0020AF68F0A3}',
	'IPosition2' : '{E494B8E1-A59A-11D2-8724-00C04F918427}',
	'IPositionEvents' : '{D6219FE0-87A0-11D1-B765-00C04FBBE42A}',
	'ITPLines' : '{F5C31106-46AE-11D0-8901-0020AF68F0A3}',
	'ITPLinesEvents' : '{2D9F8871-DCDA-11D0-A083-00A02436CF7E}',
	'ISelectedLines' : '{12585150-9394-11D2-877C-00C04FB9C401}',
	'ISelectedLinesEvents' : '{26466EE1-9393-11D2-877C-00C04FB9C401}',
	'ITPApplDataCollection' : '{A7E095A2-DCDE-11D0-A083-00A02436CF7E}',
	'ITPApplDataCollectionEvents' : '{A7E095A1-DCDE-11D0-A083-00A02436CF7E}',
	'ITPLabels' : '{C3FB0D00-58D6-11D0-8901-0020AF68F0A3}',
	'ITPLabelsEvents' : '{90E827A1-DCDB-11D0-A083-00A02436CF7E}',
	'ITPLabel' : '{C3FB0D02-58D6-11D0-8901-0020AF68F0A3}',
	'ITPLabelEvents' : '{D81C9351-DCDB-11D0-A083-00A02436CF7E}',
	'ISysPositions' : '{6055D69A-FFAE-11D0-B6F4-00C04FB9C401}',
	'ISysPositionsEvents' : '{94F57CE7-381B-11D1-B6FE-00C04FB9E76B}',
	'ISysPosition' : '{6055D698-FFAE-11D0-B6F4-00C04FB9C401}',
	'ISysPositionEvents' : '{3AC7EA79-381C-11D1-B6FE-00C04FB9E76B}',
	'ISysGroupPosition' : '{DC2FA0C7-FFAB-11D0-B6F4-00C04FB9C401}',
	'ISysGroupPositionEvents' : '{6EA7D4AD-381C-11D1-B6FE-00C04FB9E76B}',
	'IPosition' : '{D42AB5DA-8FFB-11D0-94CC-0020AF68F0A3}',
	'IAlarms' : '{7C37F232-A494-11D0-A37F-0020AF39BE5A}',
	'IAlarmNotify' : '{7DD25A00-AC49-11D0-8B7F-0020AF39BE5A}',
	'IAlarm' : '{7C37F236-A494-11D0-A37F-0020AF39BE5A}',
	'IIOTypes' : '{59DC16EB-AF91-11D0-A072-00A02436CF7E}',
	'IIOTypesEvents' : '{B23F3D71-F86A-11D0-A093-00A02436CF7E}',
	'IIOType' : '{59DC16EF-AF91-11D0-A072-00A02436CF7E}',
	'IUserIOType' : '{59DC16F5-AF91-11D0-A072-00A02436CF7E}',
	'IUserIOTypeEvents' : '{95741D17-F9F1-11D0-B6EE-00C04FB9E76B}',
	'IUserIOSignals' : '{59DC16F9-AF91-11D0-A072-00A02436CF7E}',
	'IUserIOSignalsEvents' : '{C240AAA1-F86F-11D0-A093-00A02436CF7E}',
	'IUserIOSignal' : '{59DC16FE-AF91-11D0-A072-00A02436CF7E}',
	'IIOSignalEvents' : '{0DBE3EF1-F870-11D0-A093-00A02436CF7E}',
	'IIOSignal' : '{59DC16FB-AF91-11D0-A072-00A02436CF7E}',
	'ITPScreen' : '{DEE5EAE0-E283-11D0-8BB6-0020AF39BE5A}',
	'ITPScreenEvents' : '{797CEA11-DD7B-11D2-8A28-00105AE42A59}',
	'ITasks' : '{5F26BE72-4626-11D1-B745-00C04FBBE42A}',
	'ITasksEvents' : '{48F075F8-4626-11D1-B745-00C04FBBE42A}',
	'ITask' : '{7745C8FE-4626-11D1-B745-00C04FBBE42A}',
	'ITaskEvents' : '{F22A6948-A310-11D1-B77A-00C04FBBE42A}',
	'ISynchData' : '{3C3988CD-9275-11D1-B6F9-00C04FA3BD85}',
	'IFeatures' : '{2AF44183-9273-11D1-B6F9-00C04FA3BD85}',
	'IFeature' : '{2AF44185-9273-11D1-B6F9-00C04FA3BD85}',
	'ITPInstructions' : '{3C05D26D-9BE8-11D1-B6FC-00C04FA3BD85}',
	'ITPInstruction' : '{3C05D26F-9BE8-11D1-B6FC-00C04FA3BD85}',
	'ISynchApplData' : '{8FAFC8E7-B2B8-11D1-B705-00C04FA3BD85}',
	'ISynchApplDataItem' : '{8FAFC8E9-B2B8-11D1-B705-00C04FA3BD85}',
	'IApplications' : '{78063945-E50A-11D1-B778-00C04FB99C75}',
	'IPacketEvent' : '{FCCE9E60-9420-11D1-B751-00C04FB99C75}',
	'IPacketEventEvents' : '{298DEBD5-9976-11D1-B753-00C04FB99C75}',
	'IPacket' : '{7B125AAE-9330-11D1-B751-00C04FB99C75}',
	'IScatteredAccess' : '{6F33A4D2-91F3-11D3-877C-00C04F81118D}',
	'ISysInfo' : '{4553DA61-ACA1-11D3-8783-00C04F81118D}',
	'IPipes' : '{B475BC90-3AF1-11D4-9F66-00105AE428C3}',
	'IPipesEvents' : '{B475BC92-3AF1-11D4-9F66-00105AE428C3}',
	'IPipe' : '{B475BC94-3AF1-11D4-9F66-00105AE428C3}',
	'IPipeEvents' : '{B475BC93-3AF1-11D4-9F66-00105AE428C3}',
	'IIndPosition' : '{D21DF523-8D4A-4A7C-B367-5725E53A21A1}',
	'IIndPositionEvents' : '{0872A5E4-398C-46A3-989D-1E9B1BCA72DC}',
	'IIndGroupPosition' : '{1F6F314A-F81F-4B6D-AEDE-5AFD558256E8}',
	'IIndGroupPositionEvents' : '{82DDCEA2-3608-404D-90B2-E636F7E7DDD8}',
	'ICurGroupPosition' : '{75CEF1D6-1E43-11D1-B6FF-00C04FB9C401}',
	'ICurGroupPositionEvents' : '{2BF7E386-87A9-11D1-B765-00C04FBBE42A}',
	'IRobManProxy' : '{53D6E5D1-F5E2-11D3-9F35-00500409FF06}',
	'IRobManProxyEvents' : '{53D6E5D3-F5E2-11D3-9F35-00500409FF06}',
	'IProgramObject' : '{D42AB5D9-8FFB-11D0-94CC-0020AF68F0A3}',
	'IKARELProgramEvents' : '{44E3D090-7178-11D1-B762-00C04FBBE42A}',
	'IKARELProgram' : '{73FF06C4-7178-11D1-B762-00C04FBBE42A}',
	'ITransform' : '{A47A5882-056D-11D0-8901-0020AF68F0A3}',
	'IVector' : '{924CC060-0F7A-11D2-86F4-00C04F9184DB}',
	'IJoint' : '{A47A5886-056D-11D0-8901-0020AF68F0A3}',
	'IVarEvents' : '{C19FE67C-A462-11D0-B304-00A02479C928}',
	'IVar' : '{8C8ACC80-4F57-11D0-BC32-444553540000}',
	'IRegNumeric' : '{6B51A440-212A-11D0-959F-00A024329125}',
	'IRegString' : '{CADEF7CB-650F-45B7-BC95-9080FA32640B}',
	'IVarPosition' : '{E3FFB438-2613-11D1-B702-00C04FB9C401}',
	'ICommonAssoc' : '{34E3E250-1107-11D2-86F4-00C04F9184DB}',
	'IGroupAssoc' : '{424160A0-1108-11D2-86F4-00C04F9184DB}',
	'IVarObject2' : '{D0EDFE01-C6AC-11D2-8727-00C04F81118D}',
	'ITPLineEvents' : '{0277AC51-DCDB-11D0-A083-00A02436CF7E}',
	'ITPLineHelper' : '{FC761640-4CEA-11D0-8901-0020AF68F0A3}',
	'ITPApplDataEvents' : '{9728B471-DCE0-11D0-A083-00A02436CF7E}',
	'ITPApplDataHelper' : '{343D8EB1-DCE1-11D0-A083-00A02436CF7E}',
	'ITPSimpleLine' : '{6C473F21-B5F0-11D2-8781-00C04F98D092}',
	'ISystemIOType' : '{59DC16F2-AF91-11D0-A072-00A02436CF7E}',
	'IIOSignals' : '{59DC16F7-AF91-11D0-A072-00A02436CF7E}',
	'IIOSignalsEvents' : '{39A374D1-F86E-11D0-A093-00A02436CF7E}',
	'IIOSignal2' : '{D3EE1B91-8BB6-11D3-877C-00C04F81118D}',
	'IConfigurableIOType' : '{59DC16F3-AF91-11D0-A072-00A02436CF7E}',
	'IIOConfigs' : '{59DC1700-AF91-11D0-A072-00A02436CF7E}',
	'IIOConfigsEvents' : '{021408E1-F879-11D0-A093-00A02436CF7E}',
	'IIOConfig' : '{59DC1702-AF91-11D0-A072-00A02436CF7E}',
	'IIOConfigEvents' : '{051D0EE2-F930-11D0-B6EE-00C04FB9E76B}',
	'IDigitalIOSignal' : '{59DC16FC-AF91-11D0-A072-00A02436CF7E}',
	'IAnalogIOSignal' : '{714CC921-B4E5-11D0-A073-00A02436CF7E}',
	'IUOPIOSignal' : '{714CC924-B4E5-11D0-A073-00A02436CF7E}',
	'IRobotIOSignal' : '{714CC926-B4E5-11D0-A073-00A02436CF7E}',
	'IPipeFields' : '{B475BC96-3AF1-11D4-9F66-00105AE428C3}',
	'IPipeField' : '{B475BC98-3AF1-11D4-9F66-00105AE428C3}',
	'IPipePosition' : '{B475BC9A-3AF1-11D4-9F66-00105AE428C3}',
}

win32com.client.constants.__dicts__.append(constants.__dict__)

