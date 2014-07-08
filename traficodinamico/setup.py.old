# -*- coding: utf-8 -*-

import sys
from distutils.core import setup

kwargs = {}
if 'py2exe' in sys.argv:
    import py2exe
    kwargs = {
        'console' : [{
            'script'         : 'trafdim.py',
            'description'    : 'Generador de trafico dinamico.',
            #'icon_resources' : [(0, 'icon.ico')]
            }],
        'zipfile' : None,
        'options' : { 'py2exe' : {
            'dll_excludes'   : ['w9xpopen.exe'],
            'bundle_files'   : 1,
            'compressed'     : True,
            'optimize'       : 2
            }},
         }

setup(
    name='traficodinamico',
    author='simplesoft.com ltda',
    author_email='soportesimplesoft@gmail.com',
    **kwargs)
