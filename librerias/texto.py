#!/usr/bin/env python
# -*- coding: utf-8 -*- 
'''
Created on 28/07/2013
@author: marco
'''

import wx

from pagina import objPagina


class obFont():
	def __init__(self):
		self.NombreFont="Arial"
		self.Alto=6
		self.Ancho=0
		self.Color=(255,255,255)
		self.Fondo=(0,0,0)
		self.negrilla=False
		self.italica=False
		self.subrayado=False
		
	def getNegrilla(self):
		if self.negrilla:
			return wx.BOLD
		else:
			return wx.NORMAL
	
	def getItalica(self):
		if self.italica:
			return wx.ITALIC
		else:
			return wx.NORMAL
	
class objTexto():
	'''
	classdocs
	
	'''

	def __init__(self):
		'''
		Constructor
		'''
		self.Texto=None
		self.Letra=obFont()
		self.justificar=0  #		self.Izquierda=0, self.Derecha=1, self.Centro=2, self.Izq_SinEspacio=3, self.Justificar=4
		self.PosX=0
		self.PosY=0
		self.DesX=0
		self.DesY=0
		self.DesXac=False
		self.DesYac=False
		self.AnchoDef=0
	
	def Alinear(self,valor):
		print "alinear:",valor
		if type(valor)==str:
			if valor.lower()=='izquierda':
				self.justificar=0
			elif valor.lower()=='derecha':
				self.justificar=1
			elif valor.lower()=='centro':
				self.justificar=2
			elif valor.lower()=='sin espacio':
				self.justificar=3
			elif valor.lower()=='justificar':
				self.justificar=4
			else:
				self.justificar=0
			
		else:
			if valor >=0 and valor <=4:
				self.justificar=valor
			else:
				self.justificar=0
	
	def MaxAncho(self):
		print "maxAncho", self.Texto
		print "type:",type(self.Texto)
		if self.Texto==None:
			return None
		if  type(self.Texto)!=list:
			return None
		
		maximo=0

		app=wx.App()
		bitmap = wx.Bitmap("tempo.png")
		dc = wx.MemoryDC(bitmap)
		dc.Clear()
		dc.SetMapMode(wx.MM_POINTS)
		dc.SetFont(wx.Font(self.Letra.Alto, wx.DEFAULT, self.Letra.getItalica(), self.Letra.getNegrilla(),False,self.Letra.NombreFont))
		
		

		for linea in self.Texto:
			valor = dc.GetFullTextExtent(linea)
			print valor
			if valor[0]>maximo:
				maximo=valor[0]
				
		del bitmap
		del dc
		return maximo
		
	def CalcularX(self):
		if self.DesXac:
			self.PosX=self.PosX +self.DesX
		else:
			self.PosX=self.PosX
			self.DesXac=True
		return self.PosX
	
	def CalcularY(self):
		if self.DesYac:
			altominimo = self.CalcularAlto('Lineaq')+2
			if self.DesY < altominimo:
				self.PosY=self.PosY + altominimo
			else:
				self.PosY=self.PosY +self.DesY
		else:
			self.PosY=self.PosY
			self.DesYac=True
			
		return self.PosY
	
	def CalcularAncho(self,linea):
		app=wx.App()
		bitmap = wx.Bitmap("tempo.png")
		dc = wx.MemoryDC(bitmap)
		dc.Clear()
		dc.SetMapMode(wx.MM_POINTS)
		dc.SetFont(wx.Font(self.Letra.Alto, wx.DEFAULT, self.Letra.getItalica(), self.Letra.getNegrilla(),False,self.Letra.NombreFont))		
		salida = dc.GetFullTextExtent(linea)
		del bitmap
		del dc
		return salida[0]
		
	def CalcularAlto(self,linea):
		app=wx.App()
		bitmap = wx.Bitmap("tempo.png")
		dc = wx.MemoryDC(bitmap)
		dc.Clear()
		dc.SetMapMode(wx.MM_POINTS)
		dc.SetFont(wx.Font(self.Letra.Alto, wx.DEFAULT, self.Letra.getItalica(), self.Letra.getNegrilla(),False,self.Letra.NombreFont))		
		salida = dc.GetFullTextExtent(linea)
		del bitmap
		del dc
		return salida[0]

	def Justificacion(self):
		print"justificacion"
		#1 comparar anchodef con ancho de linea
		#2 si el ancho de linea > anchodef
		#       mover la ultima palabra a la siguiente linea y volver paso 2
		#  No 
		#		contra palabras, calcular ancho del espacio, (anchodef-ancho lineas)/nropalabras
		
		

	def getPosicion(self):
		if self.Texto==None:
			return None
		if  type(self.Texto)!=list:
			return None
		salida =[]
		
		if self.AnchoDef>0:
			return self.Justificacion()
		
		for linea in self.Texto:
			if self.justificar==0:
				salida.append ([self.CalcularX(),self.CalcularY(), linea])
			elif self.justificar==1:
				ancho =self.CalcularX()- self.CalcularAncho(linea)
				print 'ancho,self.PosX',ancho,self.PosX
				salida.append ([ancho,self.CalcularY(), linea])
			elif self.justificar==2:
				ancho =self.CalcularX()- (self.CalcularAncho(linea)/2)
				print 'ancho,self.PosX',ancho,self.PosX
				salida.append ([ancho,self.CalcularY(), linea])
			elif self.justificar==3:
				linea=linea.lstrip()
				salida.append ([self.CalcularX(),self.CalcularY(), linea])
			#Falta Justificar..
			else:	
				linea=linea.lstrip()
				salida.append ([self.CalcularX(),self.CalcularY(), linea])
			
		return salida
		
#	def getPosY(self):


		
if __name__ == '__main__':
	
	Opag = objPagina()
	Opag.leerPagina("pagina1.txt")
	Otexto=objTexto()
	Otexto.Letra.Alto=10	
	Otexto.Texto = Opag.Seleccionar(prefijo='a',lineaInicial=1, nroLineas=2, nroCampo=1,  columna=0, nroColumnas=0)
	#print Otexto.Texto
	#print Otexto.MaxAncho()
	Otexto.PosX=1300
	Otexto.DesX=100
	Otexto.PosY=100
	Otexto.DesY=41
	Otexto.Alinear('izquierda')
	print Otexto.getPosicion()
	Otexto.Alinear('Derecha')
	print Otexto.getPosicion()
	Otexto.Alinear('Centro')
	print Otexto.getPosicion()
	Otexto.Alinear('sin espacio')
	print Otexto.getPosicion()
	