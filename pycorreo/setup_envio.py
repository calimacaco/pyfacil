# -*- coding: iso-8859-1 -*-
from distutils.core import setup
import py2exe
setup(name="Envio Correo",
version="0.0",
description="Enviar correos generados desde el producto FACIL",
author="SimpleSoft.com ltda",
author_email="soportesimplesoft@gmail.com",
url="www.cali2s.com",
license="GNU",
scripts=["pycorreo.py"],
console=["pycorreo.py"]
)