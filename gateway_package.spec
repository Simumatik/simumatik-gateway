# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

# IMPORTANT: Make sure all paths and DLLs point to same Python version

import sys
import sysconfig
from pathlib import Path

PYTHON_VERSION_INFO = sys.version_info
print(f"Python version: {PYTHON_VERSION_INFO.major}.{PYTHON_VERSION_INFO.minor}.{PYTHON_VERSION_INFO.micro}")

# Make sure the Python version of the current interpreter is 3.14.x.
assert PYTHON_VERSION_INFO >= (3, 14) and PYTHON_VERSION_INFO < (3, 15), "deploy_package.py requires Python 3.14.x"

PYTHON_SITE_PACKAGES_PATH = Path(sysconfig.get_path("purelib"))
assert PYTHON_SITE_PACKAGES_PATH.exists(), "Could not find the Python site-packages directory."

DRIVER_MANAGER_DRIVERS_FOLDER = PYTHON_SITE_PACKAGES_PATH / "driver_manager/drivers"
assert DRIVER_MANAGER_DRIVERS_FOLDER.exists(), "Could not find the driver_manager package's 'drivers' directory."

EXECUTABLE_NAME = "Gateway"

a = Analysis(
   ['src/gateway.py'],
   pathex=['./'],
   binaries=[
      (DRIVER_MANAGER_DRIVERS_FOLDER / 'fanuc_roboguide/RobotInterfaceDotNet.dll', '.'),
      (DRIVER_MANAGER_DRIVERS_FOLDER / 'plcsim_advanced/Siemens.Simatic.Simulation.Runtime.Api.x64.dll', '.'),
      (DRIVER_MANAGER_DRIVERS_FOLDER / 'plcsim_advanced/Siemens.Simatic.Simulation.Runtime.Api.x86.dll', '.'),
      (DRIVER_MANAGER_DRIVERS_FOLDER / 'robodk_api/robodk.py', '.'),
      (DRIVER_MANAGER_DRIVERS_FOLDER / 'robodk_api/robolink.py', '.'),
   ],
   datas=[
      ('icon.ico', '.'),
   ],
   hiddenimports=[
      'numpy',
      'roslibpy',
      'pyads',
      'win32timezone'
   ],
   hookspath=[],
   runtime_hooks=[],
   excludes=[
      'IPython',
      'win32com',
      'matplotlib', 
      'qt5'
   ],
   cipher=block_cipher,
)

pyz = PYZ(
   a.pure, 
   a.zipped_data,
   cipher=block_cipher
)

exe = EXE(
   pyz,
   a.scripts,
   [],
   exclude_binaries=True,
   name=EXECUTABLE_NAME,
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
   name=EXECUTABLE_NAME
)

