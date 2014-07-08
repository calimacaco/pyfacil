#!/usr/bin/env python
# -*- coding: utf-8 -*- 

'''
Created on 7/06/2014

@author: marco
Salto de Canal IBM
desde un copySpoolFile

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
	

	def moverAbs(self,linea=''):
		'''Movimiento Absoluto'''
		#Leer 3 primeros texto
		if len(linea)<3:
			return -1
		if len(linea[0:3].strip())==0:
			return 0
		
		return int(linea[0:3])
		
		
	def addLnBlancas(self,lineas,inicio):
		'''Insert lineas blancas'''
		calculo=lineas - inicio
		salida =[]
		for ciclo in range(0,calculo):
			salida +=['\r\n']
		return salida

	def sobreEscribir(self,linea,nuevo):
		'''Sobre escribe el contenido de nuevo en linea y regresa un string'''
		
		if len(linea)==0:
			return nuevo
		
		linea=linea.replace("\r\n",'')
		nuevo=nuevo.replace("\r\n",'')
		
		posicion=0
		if len(linea) < len(nuevo):
			linea += ' ' * (len(nuevo)-len(linea))
		elif len(linea) > len(nuevo):
			nuevo += ' ' * (len(linea)-len(nuevo))
		
			
		salida=''
		for letra in nuevo:
			if letra !=' ':
				if linea[posicion]==' ':
					salida +=letra
				else:
					salida +=linea[posicion]
			else:
				salida +=linea[posicion]
				
			posicion +=1
		
		salida +='\r\n'
		return salida
		

	def saltoPag(self,pag):
		for linea in pag:
			self.archsalida.write(linea)
			#self.archsalida.write('\n')
		self.archsalida.write('\f')
	


	def procesar(self,entrada):
		if not self.selArchEntrada(entrada):return False
		pag=[]
		
		ctrLinesalida=1
		
		for linea in self.archentrada.readlines():
			#movimiento Absoluto
			moverln=self.moverAbs(linea)
			if moverln>len(pag):
				pag +=self.addLnBlancas(moverln,len(pag))
				ctrLinesalida=moverln
				pag[moverln-1]=self.sobreEscribir(pag[moverln-1],linea[4:])
			
			elif moverln ==len(pag):
				pag[len(pag)-1]=self.sobreEscribir(pag[len(pag)-1],linea[4:])
				ctrLinesalida=moverln
		
		
			elif moverln==-1:
				print "error Linea blanca"
		
			elif moverln==0:
				#movimiento relativo
				print "relativo"
				if linea[3]==" " :
					print "error"
				else:
					moverln=int(linea[3])
					if moverln==0:
						pag[len(pag)-1]=self.sobreEscribir(pag[len(pag)-1],linea[4:])
					else:
						moverln=moverln+len(pag)
						pag +=self.addLnBlancas(moverln,len(pag))
						pag[len(pag)-1]=self.sobreEscribir(pag[len(pag)-1],linea[4:])
				
		
		
			else: #salto de pagina
				self.saltoPag(pag)
				pag=[]
				pag=self.addLnBlancas(moverln,0)
		
		
		
		if len(pag)>0:
			self.saltoPag(pag)
		
				
		
		self.archentrada.close()
		self.archsalida.close()
		self.inicio=True

if __name__ == '__main__':
	canal=objCanal()
	print sys.argv
	if len(sys.argv) > 1:
		canal.procesar(sys.argv[1])
	else:	
		canal.procesar('salto canal/FACTURA1.TXT')
