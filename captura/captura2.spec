# -*- mode: python -*-
a = Analysis(['captura2.py'],
             pathex=['Z:\\genesis\\captura'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='captura2.exe',
          debug=False,
          strip=None,
          upx=True,
          console=True )
