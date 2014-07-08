#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
recibe datos stdin, procesa colocando macro y guarda  en un plano.
'''

import sys
import os
import getopt

class objPrincipal():
	def __init__(self):
		self.formato = ""
		self.nromacro = 10 
		self.temp='temp'
		self.encabezado=""
		
	def uso(self):
		print 'convert  -e <Nombre archivo de imagen> -s <Nombre archivo de salida LGO>'
		print 'Parmetros adicionales'
		print '-f "nombre.frm"              --> Formato a unir'
		print '-t "Archivo.temp"            --> Nombre archivo tempora'
		print '-n "NroMacro"            	--> Numero del macro'
		print '-e "archivo.enc" 			--->Archivo encabezado'	
		print ''
		sys.exit(2)
		
		
		
	def procesar(self):
		argv = sys.argv[1:]
		if len(argv)==0:
			self.uso()

		try:
			opts, args = getopt.getopt(argv,"hf:n:t:e:",["formato=","nromacro=","temp=","arriba"])
		
		except getopt.GetoptError:
			self.uso()
			
		for opt, arg in opts:
			if opt == '-h':
				self.uso()
			elif opt in ("-f", "--formato"):
				self.formato = arg
			elif opt in ("-t", "--temp"):
				self.temp = arg
			elif opt in ("-n", "--nromacro"):
				self.nromacro = int(arg)
			elif opt in ("-e", "--arriba"):
				self.encabezado = arg

					
def validararchivo(nombre):
	if not os.path.isfile(nombre):
		print "Error no exite:[%s]" %(nombre)
		sys.exit()

def AbrirFormato(nombre,macro):
	validararchivo(nombre)
	datos="%s&f%iy0X" %(chr(27),macro) 
	ar=open(nombre,"rb")
	datos+=ar.read()
	ar.close()
	datos += "%s&f1x10X" %(chr(27))
	return datos

def llamarmacro(macro,datos,encabezado):
	validararchivo(encabezado)
	if datos[-1]!='\f':
		datos+='\f'
	arch=open(encabezado,'rb')
	cabeza=arch.read()
	arch.close()
	#print cabeza
	
	comando = "%s&f%iy3X\f" %(chr(27),macro)
	comando += cabeza
	datos=cabeza+datos
	datos=datos.replace('\f',comando)
	datos=datos[1: (len(cabeza)*-1)]
	return datos

########################## Incio del progr.ama ###########################
if __name__ == "__main__":
	parametros=objPrincipal()
	parametros.procesar()
	formato = AbrirFormato(parametros.formato,parametros.nromacro)
	datos =sys.stdin.read()
	datos=llamarmacro(parametros.nromacro, datos,parametros.encabezado)
	
	salida =open (parametros.temp,'wb')
	salida.write(formato)
	salida.write(datos)
	salida.close()
