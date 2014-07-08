#!/usr/bin/env python
# -*- coding: utf-8 -*- 

'''
Created on 21/03/2014

@author: marco
'''
from FormMapic import  D_ImportAccion
import wx

class objImport():
	def __init__(self,padre,base,indice):	
		print " objImport"
		self.ObaseD=base
		self.padre=padre
		self.salida=None
		self.formato=D_ImportAccion(padre)
		self.llenarCombo(indice)
		
		self.formato.Bind(wx.EVT_BUTTON, self.onSalir, self.formato.f2s_btnSalir)
		self.formato.Bind(wx.EVT_BUTTON, self.onImportar,self.formato.f2s_btnImportar)
		
		self.formato.ShowModal()

	def llenarCombo(self,indice):
		print "llenarCombo"
		for registro in self.ObaseD.LeerCampos("proceso,id", "tbl_envioarch","id !=%i" %(indice)):
			print registro
			self.formato.f2s_choProcesos.Append(registro[0],registro[1])

	def onSalir(self,event):
		self.formato.Destroy()

	def onImportar(self,event):
		print "onImportar"
		puntero=self.formato.f2s_choProcesos.GetSelection()
		if puntero == wx.NOT_FOUND:
			wx.MessageBox("No se ha seleccionado el proceso","Error",wx.ICON_ERROR)
			return
		
		print " reemplazar:", self.formato.F2s_chkReemplazar.Get3StateValue()
		
		self.salida={"proceso":self.formato.f2s_choProcesos.GetClientData(puntero),"reemplazar":self.formato.F2s_chkReemplazar.Get3StateValue()}
		self.formato.Destroy()
		