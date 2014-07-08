# -*- coding: iso-8859-1 -*-
#!/usr/bin/env python
## Log Rotativo
import os
import leerregistro
from datetime import datetime

class GenerarLog():
	def __init__(self,nombre):
		print os.getcwd()
		self.ruta=self.RutaFacil() + "\\enviocorreo\\logs"
		if not os.path.isdir(self.ruta):
			try:
				os.makedirs(self.ruta)
			except:
				print "Error No se puede crear ruta log:",self.ruta
				self.ruta=os.getcwd()
		self.ruta+="\\"+nombre+".lgo"
		print self.ruta
	
	def rotacion(self):
		print "Rotacion"
		ruta,archivo=os.path.split(self.ruta)
		print ruta
		print archivo
		self.moverlogs(ruta,archivo,7)
			

	def moverlogs (self,ruta,archivo,ciclo):
		if ciclo==0:
			return
		ciclo=ciclo-1
		print archivo,ciclo
		self.moverlogs (ruta,archivo,ciclo)
		
		#if os.path.isfile(self.ruta):
	
	
	def RutaFacil(self):
		registro=leerregistro.RegistroWindows()
		ruta=registro.LeerReg("programa")
		return str(ruta)
	
	def Guardar(self,dato):
		fecha =str (datetime.today())
		dato=fecha + " --> " + str(dato) + "\n"
		path_size = os.path.getsize(self.ruta)
		print path_size
		try:
			salida=file(self.ruta,"a")
			salida.write(dato)
			salida.close()
		except:
			print "Error grave no se puede guardar salida"
		self.rotacion()


if __name__ == "__main__":
	print "inicio"
	datos =GenerarLog("Control1")
	datos.Guardar("cocoloco")
	datos.Guardar("ocolococ")
	
