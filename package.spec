# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['src\\gateway.py'],
             pathex=['C:\\Git\\simumatik-gateway'],
             binaries=[],
             datas=[],
             hiddenimports=['numpy'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='SimumatikGateway',
          icon='icon.ico',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False)
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='gateway')
