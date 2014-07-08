# -*- coding: iso-8859-1 -*-
from distutils.core import setup
import py2exe
setup(name="Envio Archivo",
version="0.0",
description="Envia archivo a impresora",
author="simplesoft.com",
author_email="soportesimplesoft@gmail.com",
url="url del proyecto",
license="tipo de licencia",
scripts=["envioarchivo.py"],
console=["envioarchivo.py"]
)