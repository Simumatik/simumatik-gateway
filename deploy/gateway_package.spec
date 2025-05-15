# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
   ['../src/gateway.py'],
   pathex=['C:\\Git\\simumatik-gateway'],
   binaries=[
      ('C:\\Python312-32\\Lib\\site-packages\\driver_manager\\drivers\\fanuc_roboguide\\RobotInterfaceDotNet.dll','.'),
      ('C:\\Python312-32\\Lib\\site-packages\\driver_manager\\drivers\\plcsim_advanced\\Siemens.Simatic.Simulation.Runtime.Api.x64.dll','.'),
      ('C:\\Python312-32\\Lib\\site-packages\\driver_manager\\drivers\\plcsim_advanced\\Siemens.Simatic.Simulation.Runtime.Api.x86.dll','.'),
      ('C:\\Python312-32\\Lib\\site-packages\\driver_manager\\drivers\\robodk_api\\robodk.py','.'),
      ('C:\\Python312-32\\Lib\\site-packages\\driver_manager\\drivers\\robodk_api\\robolink.py','.'),
   ],
   datas=[],
   hiddenimports=['numpy','roslibpy','pyads','win32timezone'],
   hookspath=[],
   runtime_hooks=[],
   excludes=['IPython','win32com','matplotlib', 'qt5'],
   cipher=block_cipher,
)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(
   pyz,
   a.scripts,
   [],
   exclude_binaries=True,
   name='Gateway',
   icon='icon.ico',
   debug=False,
   bootloader_ignore_signals=False,
   strip=False,
   upx=True,
   console=False,
)
coll = COLLECT(
   exe,
   a.binaries,
   a.datas,
   strip=False,
   upx=True,
   name='Gateway'
)

