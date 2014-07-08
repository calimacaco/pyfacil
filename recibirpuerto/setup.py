# -*- coding: iso-8859-1 -*-
from distutils.core import setup
import py2exe
setup(name="Recibe Print Facil",
version="1.0.0",
description="Captura Spool de Impresion",
author="Marco Ankotnio Castro - SimpleSoft.com",
author_email="soportesimplesoft.com",
url="www.cali2s.com",
license="Copy Center",
options={"py2exe": {"bundle_files": 1,"optimize":2,'compressed': True}}, 
#options={"py2exe": {"bundle_files": 1,'compressed': True}}, 
zipfile=None,
 scripts=["recibeprint.py"],
console=["recibeprint.py"]
)
