# -*- mode: python -*-
a = Analysis(['pycorreo.py'],
             pathex=['Z:\\pycorreo'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='pycorreo.exe',
          debug=False,
          strip=None,
          upx=True,
          console=True )
