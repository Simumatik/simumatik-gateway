# -*- mode: python ; coding: utf-8 -*-

a = Analysis(
   ['src\\controller_bridge.py'],
   pathex=['C:\\Git\\simumatik-gateway'],
   binaries=[
      ('src\\drivers\\fanuc_roboguide\\RobotInterfaceDotNet.dll','.'),
      ('src\\drivers\\plcsim_advanced\\Siemens.Simatic.Simulation.Runtime.Api.x64.dll','.'),
      ('src\\drivers\\plcsim_advanced\\Siemens.Simatic.Simulation.Runtime.Api.x86.dll','.'),
      ('src\\drivers\\robodk_api\\robodk.py','.'),
      ('src\\drivers\\robodk_api\\robolink.py','.'),
      ('src\\Controller_Bridge_Setup.json','.'),
      ('CONTROLLER BRIDGE README.md','.'),
   ],
   datas=[],
   hiddenimports=['numpy','pyads','win32timezone'],
   hookspath=[],
   runtime_hooks=[],
   excludes=[],
   noarchive=False,
   optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
   pyz,
   a.scripts,
   [],
   exclude_binaries=True,
   name='ControllerBridge',
   icon='icon.ico',
   debug=False,
   bootloader_ignore_signals=False,
   strip=False,
   upx=True,
   console=True,
   disable_windowed_traceback=False,
   argv_emulation=False,
   target_arch=None,
   codesign_identity=None,
   entitlements_file=None,
   contents_directory='.',
)
coll = COLLECT(
   exe,
   a.binaries,
   a.datas,
   strip=False,
   upx=True,
   upx_exclude=[],
   name='ControllerBridge'
)
