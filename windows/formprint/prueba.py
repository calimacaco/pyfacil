#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

import _winreg

class RegistroWindows:
	def __init__(self):
		self.facil = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE,"Software\\GPL Ghostscript\\9.10")
	
	def LeerReg(self,llave):
		valor, type = _winreg.QueryValueEx(self.facil, llave)
		return (valor)
	
if __name__=="__main__":
	prueba=RegistroWindows()
	ruta = prueba.LeerReg ("GS_DLL")
	print ruta
