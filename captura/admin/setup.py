# -*- coding: iso-8859-1 -*-
from distutils.core import setup
import py2exe
setup(name="Editor Spool",
version="0.0.1",
description="Administrador Editor Spool",
author="Marco Ankotnio Castro - SimpleSoft.com",
author_email="soportesimplesoft.com",
url="www.cali2s.com",
license="Copy Right",
scripts=["administrador.py"],
console=["administrador.py"]
)
