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
	prueba=Regisrowindows()
	print prueba.leerReg ("Programas")
	
	
