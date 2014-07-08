#!/usr/bin/env python
# -*- coding: utf-8 -*- 
'''
Created on 7/02/2014

@author: marco
'''


import wx
from formgenerador import f2s_DialogPapel
from std_papel import lstPapel


class ObjPagina():
	'''
	classdocs
	'''


	def __init__(self,padre):
		'''
		Constructor
		'''
		self.obDialogo=f2s_DialogPapel(padre)
		
		#self.lstpapel={'Carta':(8.5,11),'Oficio':(8.5,13),'ExtraOficio':(8.5,13)}
		
		self.orientar=None
		self.papel=None
		
		self.obDialogo.Bind(wx.EVT_BUTTON, self.onAceptar ,self.obDialogo.f2s_aceptar)
		self.obDialogo.Bind(wx.EVT_BUTTON, self.onCancelar ,self.obDialogo.f2s_Cancelar)
		
		
		self.llenarPapel()
		self.llenarOrientacion()
		self.obDialogo.ShowModal()
		
		
	def llenarPapel(self):
		self.obDialogo.f2s_tamPapel.Clear()
		#self.obDialogo.f2s_tamPapel.AppendItems(self.lstpapel.keys())
		self.obDialogo.f2s_tamPapel.AppendItems(sorted(lstPapel.keys()))
		
		self.obDialogo.f2s_tamPapel.SetSelection(0)
	
	def llenarOrientacion(self):
		lstorientar=['Vertical','Horizontal','InvVertical','InvHorizontal']
		self.obDialogo.f2s_orientacion.Clear()
		self.obDialogo.f2s_orientacion.AppendItems(lstorientar)
		self.obDialogo.f2s_orientacion.SetSelection(0)
	
	def onAceptar(self,event):
		self.orientar=self.obDialogo.f2s_orientacion.GetSelection()
		print self.obDialogo.f2s_tamPapel.GetSelection()
		#self.papel=self.lstpapel[self.obDialogo.f2s_tamPapel.GetString(self.obDialogo.f2s_tamPapel.GetSelection())]
		self.papel=lstPapel[self.obDialogo.f2s_tamPapel.GetString(self.obDialogo.f2s_tamPapel.GetSelection())]
		self.obDialogo.Destroy()
	
	def onCancelar(self,event):
		print 'Cancelar'
		self.obDialogo.Destroy()
		