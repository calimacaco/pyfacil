#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
'''
Created on 12/03/2014

@author: marco
'''

from _winreg import *

class RegistroWindows():
	def __init__(self):
		self.aReg = ConnectRegistry(None,HKEY_LOCAL_MACHINE)
		self.aKey =None
		
	def SetLlave(self,llave):
		self.aKey = OpenKey(self.aReg, llave)
		#print self.aKey
	
	def Cerrarllave(self):
		CloseKey(self.aKey)
		
	def ListaContenido(self):
		salida=[]
		for i in range(1024):
			try:
				asubkey_name=EnumKey(self.aKey,i)
				asubkey=OpenKey(self.aKey,asubkey_name)
				salida.append(asubkey_name)
			except EnvironmentError:
				#print "Fin"
				break
		return salida

	def GetContenido(self,llave):
		try:
			#print self.aKey, llave
			valor, type = QueryValueEx(self.aKey, llave)
			return (valor)
		except:
			print "Error no se encentra %s" % (llave)
			return False
			
	def BuscarGS(self):
		llave="Software\\GPL Ghostscript"
		self.SetLlave(llave)
		version=max(self.ListaContenido())
		if len(version)<=0:
			return False
		llave += '\\' + version
		self.SetLlave(llave)
		salida =self.GetContenido('GS_DLL')
		return salida
	
	def BuscarFacil(self):
		llave="Software\\Simplesoft\\Facil"
		self.SetLlave(llave)
		salida=self.GetContenido("Trabajo")
		return salida
	
	
if __name__=="__main__":
	prueba=RegistroWindows()
	salida =prueba.BuscarGS()
	if salida == False:
		print "error no existe GhostScript instalado"
	else:
		print salida
		
