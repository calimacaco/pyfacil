#!/usr/bin/env python
# -*- coding: utf-8 -*- 

'''
Created on 7/02/2014

@author: marco
Salto de Canal IBM

'''
import os,sys

class objCanal():
	'''
	Conversion salto de canal
	'''


	def __init__(self):
		'''
		Constructor
		'''
		self.control={' ':1,'0':2,'-':3,'+':0}
		self.inicio=True
		self.archsalida=None
		self.archentrada=None
	
	def selArchEntrada(self,nombre):
		if not os.path.isfile(nombre): return False
		try:
			self.archentrada=open(nombre,'r')
			self.archsalida=open(nombre+'.facil','w')

			return True
		except IOError as e:
			print "I/O error({0}): {1}".format(e.errno, e.strerror)
			return False
		except ValueError:
			print "Could not convert data to an integer."
			return False
		except:
			print "Unexpected error:", sys.exc_info()[0]
			return False
						
	def convertir(self,linea):
	
		if self.control.has_key(linea[0:1]):
			salida=linea[1:-1] + '\n' * self.control[linea[0:1]]
		else:
			if linea[0:1] =='1':
				if self.inicio==True:
					self.inicio=False
					return ''
				else:
					return '\f'
			else:
				salida=linea[1:-1]
			
		return salida

	def procesar(self,entrada):
		if not self.selArchEntrada(entrada):return False
		for linea in self.archentrada.readlines():
			self.archsalida.write(self.convertir(linea))
		
		self.archentrada.close()
		self.archsalida.close()
		self.inicio=True
if __name__ == '__main__':

	canal=objCanal()
	canal.procesar('spool/spoolnts1a.dat')
	canal.procesar('spool/spoolnts2a.dat')
	canal.procesar('spool/spoolnts3a.dat')
