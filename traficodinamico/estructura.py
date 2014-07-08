#!/usr/bin/env python
# -*- coding: utf-8 -*- 

'''
Created on 14/08/2013

@author: marco
'''




class obEstructura():
	'''
	classdocs
	'''


	def __init__(self):
		'''
		Constructor
		'''
		self.campo=[]
		self.texto=[]

	def procesar(self):
		for linea in self.texto:
			self.separar(linea)

	def limpiarblanco(self,texto):
		final=[]
		for j in texto:
			final.append(j.strip())
		return final


	def separar(self,texto):
		temp=texto.split('As')
		temp=self.limpiarblanco(temp)
		
		if temp[1].upper()=='INTEGER':		self.campo.append ({temp[0]:(2,'h')})
		elif temp[1].upper()=='BYTE':		self.campo.append ({temp[0]:(1,'b')})
		elif temp[1].upper()=='BOOLEAN':	self.campo.append({temp[0]:(2,'B')})
		elif temp[1].upper()=='SINGLE':		self.campo.append({temp[0]:(4,'f')})
		elif temp[1].upper()=='LONG':		self.campo.append({temp[0]:(4,'i')})
		elif temp[1][0:6].upper()=='STRING':
			valor=temp[1].split('*')
			self.campo.append({temp[0]:(int(valor[1]),'%is'%int(valor[1]))})


	def AddTexto(self,texto):
		self.texto.append(texto)

if __name__ == '__main__':
	es=obEstructura()
	es.AddTexto('Modo As Integer')
	es.AddTexto('SepCampo     As String * 1')
	es.AddTexto('SaltoPag     As String * 1')
		
	es.procesar()
	for dato in es.campo:
		print dato
		
	print 'primero', es.campo[0]