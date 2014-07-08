# -*- mode: python -*-
a = Analysis(['administrador.py'],
             pathex=['Z:\\admin'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='administrador.exe',
          debug=False,
          strip=None,
          upx=True,
          console=True )
