#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

import _winreg

class RegistroWindows:
	def __init__(self):
		self.llave =None
		# _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE,"Software\\Artifex\\GPL Ghostscript")
	
	def defKey(self,valor):
		try:
			self.llave = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE,valor)
			return True
		except:
			return False

	#No funciona
	#def LeerReg(self,llave):
	#	valor = _winreg.QueryValue(self.llave, llave)
	#	return (valor)
		
	def LeerReg(self,valor):
		valor,tipo = _winreg.QueryValueEx(self.llave, valor)
		print valor
		return (valor,tipo)

	def ListarValor(self):
		valor=[]
		try:
			i=0
			while True:
				nombre =_winreg.EnumValue(self.llave,i)
				valor.append(nombre)
				#print nombre
				i +=1
		except WindowsError:
				print "Fin Lista"
		return valor


	def ListaKey(self):
		valor=[]
		try:
			i=0
			while True:
				nombre =_winreg.EnumKey(self.llave,i)
				valor.append(nombre)
				#print nombre
				i +=1
		except WindowsError:
				print "Fin Lista"
		return valor
		
	def GuardarReg(self,llave,lugar, valor):
		try:
		    key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, llave, 0, KEY_ALL_ACCESS)
		except:
		    key = _winreg.CreateKey(_winreg.HKEY_LOCAL_MACHINE, llave)
		_winreg.SetValueEx(key, lugar, 0, _winreg.REG_SZ, valor)
		_winreg.CloseKey(key)
		

if __name__=="__main__":
	ubicar=RegistroWindows()
	llave="Software\\GPL Ghostscript"
	if ubicar.defKey(llave):
		ultima=ubicar.ListaKey()
		llave+= '\\%s'%(ultima[-1])
		print llave
		ubicar.defKey(llave)	
		print ubicar.ListarValor()
		ruta,tipo = ubicar.LeerReg ("GS_DLL")
		print ruta
		print tipo
	else:
		print "error 1"

	#llave="System\\CurrentControlSet\\services\\FacilArchivo_id2\\Parameters"
	#lugar='Application'
    #    valor="c:\miau"
	#ubicar.GuardarReg(llave,lugar,valor)
        
	
	