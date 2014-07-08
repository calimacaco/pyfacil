#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 12/11/2012
@author: marco
Encriptador avansado base 64bit
'''
import base64
from string import maketrans   # Required to call maketrans function.


class Ob_Encriptar():
	'''
	classdocs
	'''

	def __init__(self):
		'''
		Constructor
		'''
		self.tabla1="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 ="
		self.tabla2="df3gPm4nbOI6UYTpoiuy5REWQAtr7eZ8XSDCwqV0FGh2jklBNHJ9MKLa1svcxz!$"


	def F_Encriptar(self,original):
		
		tabla = maketrans(self.tabla1, self.tabla2)
		original +=self.F_DigitoChequeo(original)
		original=original.translate(tabla);
		return base64.b64encode(original)

	def F_DigitoChequeo(self,texto):
		suma=0
		ping=3
		for caracter in texto:
			if ping==3:
				ping=1
			else:
				ping=3
			suma += (ord(caracter)*ping)
		suma=(suma % 27)+64
		return chr(suma)
		
		
		
	def F_DesEncriptar(self,original):
		tabla = maketrans(self.tabla2, self.tabla1)
		original = base64.b64decode(original)
		original = original.translate(tabla)
		if self.F_DigitoChequeo(original[:-1]) == original[-1]:
			return original[:-1]
		else:
			return None
		
	
	def Finger(self,clave,empresa,usos):
		clave=self.F_DesEncriptar(clave)
		largo=0
		campo=0
		#Check empresa
		for datos in clave:
			largo+=1
			campo += ord(datos)
			if largo>len(empresa):
				largo=1
			campo+=ord(empresa[largo-1])
			
		campo= campo % 77
		primer= hex(campo)	
		primer = primer[2:]	
		#Nro Licencia
		segundo=hex(int(usos))
		if len(segundo)==3:
			segundo ="0" + segundo[2:]
		else:
			segundo=segundo[2:]
			
		primer += segundo
		largo=0
		campo=int(usos)
		for datos in segundo:
			largo+=1
			campo+=ord(datos)*12
		
		segundo =hex(campo % 237)
		primer += segundo
		return primer
		




if __name__ == "__main__":
	e=Ob_Encriptar()
	entrada="Marco y Astrid licencia=Libre"
	print "entrada:",entrada
	x=e.F_Encriptar(entrada)
	print "Encriptado:",x
	print "desencriptado:",e.F_DesEncriptar(x)
