# -*- coding: iso-8859-1 -*-
from distutils.core import setup
import py2exe
setup(name="Unir Macro Facil",
version="0.0.1",
description="Captura Spool de Impresion",
author="Marco Ankotnio Castro - SimpleSoft.com",
author_email="soportesimplesoft.com",
url="www.cali2s.com",
license="Copy Center",
options={"py2exe": {"bundle_files": 1,"optimize":2,'compressed': True}}, 
 zipfile=None,
 scripts=["unir.py"],
 console=["unir.py"],
 windows=["unir.py"]
)
