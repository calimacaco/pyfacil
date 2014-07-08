#!/usr/bin/python
# -*- coding: utf8 -*- 

'''
Created on 21/02/2014

@author: marco
'''

class objNopcl():
	'''
	Elimina Pcl
	inicialmente solo comando
	Iniciados con ESC y terminados en Mayuscula
	'''


	def __init__(self):
		'''
		Constructor
		'''
		self.ESC=chr(27)
		
	
	def procesarlinea(self,linea):
		salida=''
		activoEsc=False
		
		if linea.find(self.ESC)<0:
			salida=linea
			return salida
				
		for letra in linea:
			if letra==self.ESC :
				activoEsc=True
				continue
			if activoEsc:
				#print letra,  letra.isalpha() 
				
				if letra.isalpha() and  letra == letra.upper():
					activoEsc=False
				continue
			else:
				salida +=letra
			
		return salida
		
		
if __name__ == '__main__':
	linea=chr(27) + 'olaFsalida'
	o=objNopcl()
	print o.procesarlinea(linea)