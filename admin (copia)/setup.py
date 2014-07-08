# -*- coding: iso-8859-1 -*-
from distutils.core import setup
import py2exe
import os


Mydata_files = []
for files in os.listdir('imagenes/'):
    f1 = 'imagenes/' + files
    if os.path.isfile(f1): # skip directories
        f2 = 'imagenes', [f1]
        Mydata_files.append(f2)



setup(name="FACIL ADMIN",

version="0.02",
description="Administrador  FACIL",
author="SimpleSoft.com ltda",
author_email="soportesimplesoft@gmail.com",
url="www.cali2s.com",
license="GNU",

		
options={"py2exe": {"includes": "wx"}} ,
scripts=["administrador.py"],
windows=["administrador.py"],
#zipfile=None

)

