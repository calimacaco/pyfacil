#!/usr/bin/env python
# -*- coding: utf-8 -*- 
'''
Created on 19/03/2014

@author: marco
'''
# pertenece=4

from FormMapic import  D_AddAccion
import wx
import os,  glob

class ObjAccion():
	def __init__(self,padre,base):	
		print "ObjRelArchivo"
		self.ObaseD=base
		self.padre=padre
		self.formato=D_AddAccion(padre)
		self.salida=None
		self.llenarCombo()
		
		
		self.formato.Bind(wx.EVT_BUTTON, self.onSalir, self.formato.f2s_BtnCancelar)
		self.formato.Bind(wx.EVT_BUTTON, self.onAdicionar,self.formato.f2s_btnAdd)
		
		self.formato.f2s_txtPatron.SetFocus()
		
		self.formato.ShowModal()
				
	def onAdicionar(self,event):
		puntero=self.formato.f2s_choAccion.GetSelection()
		idaccion=self.formato.f2s_choAccion.GetClientData(puntero)
		txtaccion=self.formato.f2s_choAccion.GetString(puntero)
		patron=self.formato.f2s_txtPatron.GetValue()
		descripcion=self.formato.f2s_txtDescripcion.GetValue()
		if len(patron)==0:
			wx.MessageBox("No se a llenado el campo de patron","error",wx.ICON_ERROR)
			self.formato.f2s_txtPatron.SetFocus()
			return
		if len(descripcion)==0:
			wx.MessageBox("No se a llenado el campo de descripcion","error",wx.ICON_ERROR)
			self.formato.f2s_txtDescripcion.SetFocus()
			return
		if puntero ==wx.NOT_FOUND:
			wx.MessageBox("No se a Seleccionado accion","error",wx.ICON_ERROR)
			self.formato.f2s_choAccion.SetFocus()
			return
		self.salida=[patron,descripcion,txtaccion, idaccion]
		print self.salida
		
		self.formato.Destroy()
		

	def llenarCombo(self):
		ruta=self.ObaseD.SelectUno("texto", "tbl_Estado", "pertenecia=5 and valor=1")
		if ruta ==None:
			return
		ruta=ruta[0]
		print ruta
		
		if not os.path.isdir(ruta):
			wx.MessageBox("No existe directorio:\n%s"%(ruta),"Error",wx.ICON_ERROR)
			return
		
		ruta +=os.sep + "Ambientes"

		if not os.path.isdir(ruta):
			wx.MessageBox("No existe directorio:[%s]"%ruta,"Error grave",wx.ICON_ERROR)
			return
		
		for extension in ["*.dim","*.amb"]:
			for lista in glob.glob(ruta + os.sep + extension):
				lista =lista.replace(ruta + os.sep, '')
				self.formato.f2s_choAccion.Append(lista,lista)
	
	def onSalir(self,event):
		self.formato.Destroy()

	