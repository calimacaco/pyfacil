#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 12/03/2014

@author: marco
'''


########################## Incio del programa ###########################
from vista import ObjInicio
from registro import  RegistroWindows
import tempfile
import sys


if __name__ == "__main__":
	prueba=RegistroWindows()
	salida =prueba.BuscarGS()
	if salida == False:
		print "error no esta instalado  GhostScript"
		sys.exit()
	else:
		print salida
	
	salida=prueba.BuscarFacil()
	if salida == False:
		print "error no esta instalado Facil "
		sys.exit()
	else:
		print salida
	archivo= tempfile.NamedTemporaryFile(delete=False)
	data =sys.stdin.read()
	archivo.write (data)
	archivo.close()
	print archivo.name
	
	verFromato=ObjInicio(False,archivo.name)