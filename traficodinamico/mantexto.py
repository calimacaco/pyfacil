#!/usr/bin/env python
# -*- coding: utf-8 -*- 
'''
Created on 13/08/2013

@author: marco
'''
import wx
from formtrafico import f2s_DiagTextoTrafico

class obTrafico():
	'''
	classdocs
	'''

	def __init__(self,padre=-1):
		'''
		Constructor
		'''
		self.padre=padre
		self.texto=''
		self.posx=100
		self.posy=100
		self.alto=10
		self.rotar=0
		self.estado=0
		
		self.FormIngreso=f2s_DiagTextoTrafico(padre)
		self.FormIngreso.SetTitle('Campos de textos para Trafico')
		self.FormIngreso.f2s_BtnCancelar.Bind(wx.EVT_BUTTON, self.OnSalir)
		self.FormIngreso.f2s_BtnAceptar.Bind(wx.EVT_BUTTON,self.OnGuardar)

	
	def OnSalir(self,evt):
		self.estado=0
		self.FormIngreso.Destroy()

	def OnGuardar(self,evt):
		self.estado=0
		self.alto=int(self.FormIngreso.f2s_AltoFont.GetValue())
		if self.alto<4:
			self.FormIngreso.f2s_AltoFont.SetValue('10')
			self.alto=10
			wx.MessageBox('Error, el alto del font no puede\nser menor a 4','error',wx.ICON_ASTERISK)
			
		self.posx=int(self.FormIngreso.f2s_posX.GetValue())
		self.posy=int(self.FormIngreso.f2s_posY.GetValue())
		self.texto=self.FormIngreso.f2s_Texto.GetValue()
		self.estado=1
		self.FormIngreso.Destroy()
	
	def visualizar(self):
		self.FormIngreso.f2s_AltoFont.SetValue(str(self.alto))
		self.FormIngreso.f2s_posX.SetValue(str(self.posx))
		self.FormIngreso.f2s_posY.SetValue(str(self.posy))
		self.FormIngreso.f2s_Texto.SetValue(self.texto)
		self.FormIngreso.f2s_posX.SetFocus()
		self.FormIngreso.ShowModal()
		

	def getValor(self):
		salida ={'texto':self.texto,'posx':self.posx,'posy':self.posy,'alto':self.alto,'rotar':self.rotar}
		return salida
	
	def setValor(self,obtexto):
		print 'setValor'
		if type (obtexto) != dict: return
		
		if obtexto.has_key('texto'): 	self.texto=obtexto['texto']
		if obtexto.has_key('posx'): 	self.posx=obtexto['posx']
		if obtexto.has_key('posy'): 	self.posy=obtexto['posy']
		if obtexto.has_key('alto'): 	self.alto=obtexto['alto']
		
		