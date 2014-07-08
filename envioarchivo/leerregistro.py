#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

import _winreg

class RegistroWindows:
	def __init__(self):
		self.facil = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE,"Software\\SimpleSoft\\Facil")
	
	def LeerReg(self,llave):
		valor, type = _winreg.QueryValueEx(self.facil, llave)
		return (valor)

if __name__=="__main__":
	prueba=RegistroWindows()
	ruta = prueba.LeerReg ("Programa")
	ruta+='\\envioarchivo\\config.cfg'
	print ruta
	f = open(ruta)
	ciclo=0
	buscar=[]
	for linea in f:
		partir= linea.split("<|>")
		if partir[0]!='\n':
			buscar.append(partir[0])
	print len(buscar)
	
