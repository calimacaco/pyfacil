# -*- coding: iso-8859-1 -*-
from distutils.core import setup
import py2exe
setup(name="Generador Formatos Facil",
version="1.0.0",
description="Generador de Formatos",
author="Marco Antonio Castro - SimpleSoft.com",
author_email="soportesimplesoft.com",
url="www.cali2s.com",
license="Copy Center",
options={"py2exe": {"bundle_files": 1,"optimize":2,'compressed': True}}, 
 zipfile=None,
 scripts=["formularios.py"],
 console=["formularios.py"],
 windows=["formularios.py"]
)
