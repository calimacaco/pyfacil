#!/usr/bin/env python
# -*- coding: utf-8 -*- 
'''
Created on 27/03/2014

@author: marco
'''
import wx, os
from FormMapic import D_Abrir
from basedatos import ObjBase


class ObjManejoDB():
	def __init__(self,padre):	
		print "ObjManejoDB"
		self.ObaseD=None
		self.padre=padre
		self.formato =D_Abrir(padre)
		self.formato.SetTitle("Abrir Base de Datos")
		self.formato.Center()
		
		self.formato.ArchivoBase.Bind(wx.EVT_FILEPICKER_CHANGED, self.onActivarAbrir)
		#self.f_Abrir.BtnAbrir.Bind(wx.EVT_BUTTON, self.OnAbrirBase)
		self.formato.BtnSalir.Bind(wx.EVT_BUTTON, self.OnCerrarConfig)
		self.formato.BtnCrearBD.Bind(wx.EVT_BUTTON, self.onCrearBaseDatos)
		
		self.formato.ShowModal()		

	def OnCerrarConfig(self,event):
		self.ObaseD=None
		self.formato.Destroy()
	
	def onCrearBaseDatos(self,event):
		#Crear la base de datos de configuracion
		if len(self.formato.Txt_NombreBD.GetValue())<3:
			wx.MessageBox("Nombre de la base de datos muy pequeño/n minimo debe tener 3 caracteres","nombre base datos",wx.ICON_ERROR)
			return
		
		nombre=self.formato.Dir_BD.GetPath() + os.sep +  self.formato.Txt_NombreBD.GetValue()
		
		print "nombre salida:",nombre
		
		self.ObaseD=ObjBase(nombre +".db") #Automaticamente se crea la base y sus tablas
		if self.ObaseD.rutabase ==None:
			self.ObaseD=None
			wx.MessageBox("No Fue posible Crear la Base de datos:[%s]" %(self.formato.ArchivoBase.GetPath()),"Error base datos",wx.ICON_ERROR)
			return
		
		wx.MessageBox("Base de datos Creada","Crear BD",wx.ICON_EXCLAMATION)
		self.formato.Destroy()
		
	def onActivarAbrir(self,event):
		self.formato.ArchivoBase.GetPath()
		self.ObaseD=ObjBase(self.formato.ArchivoBase.GetPath())
		if self.ObaseD.rutabase ==None:
			self.ObaseD=None
			wx.MessageBox("No Fue posible abrir la Base de datos:[%s]" %(self.formato.ArchivoBase.GetPath()),"Error base datos",wx.ICON_ERROR)
			return
		else:
			wx.MessageBox("se Abrio la Base de datos:[%s]" %(self.ObaseD.rutabase),"Nombre de base datos",wx.ICON_ASTERISK)
		
		self.formato.Destroy()
				
