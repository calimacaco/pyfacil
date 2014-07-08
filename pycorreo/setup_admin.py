# -*- coding: iso-8859-1 -*-
##from distutils.core import setup
##import py2exe


##from py2exe.build_exe import py2exe
##from distutils.core import setup


import py2exe
from distutils.core import setup
setup(windows=[{"script" : "admin.py"}], options={"py2exe" : {"includes" : ["sip", "PyQt4._qt"]}})
##setup(name="Administracion Base de datos",
##version="0.1",
##description="Base Datos Correo",
##author="SimpleSoft.com ltda",
##author_email="soportesimplesoft@gmail.com",
##url="www.cali2s.com",
##license="GNU",
##scripts=["admin.py"],
##console=["admin.py"]
##)
