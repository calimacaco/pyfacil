#!/usr/bin/env python
# -*- coding: utf-8 -*- 
'''
Created on 18/12/2013

@author: marco
'''
# pertenece=5

import wx
import sys,os

from datetime import *

from FormMapic import  D_AddEnvioArchivo
from basedatos import ObjBase
from ObjaddAccion import ObjAccion
from objImportAccion import objImport

class ObjConfArchivo():
	def __init__(self,padre,base):	
		print "ObjRelArchivo"
		self.ObaseD=base
		self.padre=padre
		self.listaAcciones=[]
		self.tabla="tbl_envioarch"
		self.guadar=False
		self.indice=0
		#Vista
		self.formato=D_AddEnvioArchivo(padre)
		self.formato.Bind(wx.EVT_BUTTON, self.onSalir, self.formato.f2s_btnSalir)
		self.formato.Bind(wx.EVT_BUTTON, self.onNuevo, self.formato.f2s_BtnNuevoReg)
		self.formato.Bind(wx.EVT_BUTTON,self.onAdicionarAccion,self.formato.f2s_btnAddlista)				
		self.formato.Bind(wx.EVT_BUTTON,self.onGuardar,self.formato.f2s_btnGuardar)
		self.formato.Bind(wx.EVT_BUTTON,self.onAtras,self.formato.f2s_btnAnterior)
		self.formato.Bind(wx.EVT_BUTTON,self.onSiguiente,self.formato.f2s_btnSiguiente)
		self.formato.Bind(wx.EVT_BUTTON,self.onPrimero,self.formato.f2s_btnInicio)
		self.formato.Bind(wx.EVT_BUTTON,self.onUltimo,self.formato.f2s_btnFinal)
		self.formato.Bind(wx.EVT_BUTTON,self.onImportar,self.formato.f2s_btnImportar)		
		self.formato.Bind(wx.EVT_DIRPICKER_CHANGED,self.onBuscar,self.formato.f2s_DirPic)				
		self.formato.Bind(wx.EVT_LIST_ITEM_ACTIVATED,self.onActivarSeleccion,self.formato.f2s_listAcciones)
		self.formato.Bind(wx.EVT_LIST_ITEM_DESELECTED,self.onDesSeleccion,self.formato.f2s_listAcciones)
		self.formato.Bind(wx.EVT_BUTTON,self.onBorrarItem,self.formato.f2s_btnBorrarlista)

		#llenado Grilla
		self.InicioGrilla()
		
		self.IrAlregistro(1)
		self.Navegador()
		
		self.formato.ShowModal()

	def onImportar(self,event):
		d_importar=objImport(self.padre,self.ObaseD,self.indice)
		trabajo = d_importar.salida
		print "trabajo:",trabajo
		if trabajo==None:
			return
		if trabajo["reemplazar"]==1:
			self.InicioGrilla()
		
		campos="patron,ambiente,descrip"
		leerlista=self.ObaseD.LeerCampos(campos,"tbl_patrones","idproceso=%i" %(trabajo["proceso"]))
		
		print "lista actual:",self.listaAcciones
		
		for registro in leerlista:
			puntero = self.formato.f2s_listAcciones.InsertStringItem(sys.maxint,registro[0])
			self.formato.f2s_listAcciones.SetStringItem(puntero,1,registro[1])
			self.formato.f2s_listAcciones.SetStringItem(puntero,2,registro[2])
			
			self.listaAcciones.append(registro)
			print "registro:",  registro
			
		print self.listaAcciones

	def onNuevo(self,event):
		if self.guadar:
			wx.MessageBox("Se debe Guardar el registro \nAntes de ingresar uno nuevo","error",wx.ICON_ERROR)
			return
		self.guadar=True
		self.formato.f2s_txtDirectorio.SetValue("")
		self.formato.f2s_txtImpresora.SetValue("")
		self.formato.f2s_txtNombre.SetValue("")
		self.formato.f2s_ChkActivo.SetValue(True)
		self.formato.f2s_txtNombre.SetFocus()
		self.InicioGrilla()
		self.formato.f2s_BtnNuevoReg.Enable(False)

	def InicioGrilla(self):
		self.formato.f2s_listAcciones.ClearAll()
		self.formato.f2s_listAcciones.InsertColumn(0,"Patron",width=100)
		self.formato.f2s_listAcciones.InsertColumn(1,"Ambiente",width=250)
		self.formato.f2s_listAcciones.InsertColumn(2,"Descripcion",width=180)
		self.listaAcciones=[]

	def onUltimo(self,event):
		print "onUltimo"
		self.indice =self.ObaseD.Contar(self.tabla)
		self.IrAlregistro(self.indice)

	def onPrimero(self,event):
		print "onPrimero"
		self.indice=1
		self.IrAlregistro(self.indice)

	def onSiguiente(self,event):
		print "onSiguiente"
		self.indice +=1
		self.IrAlregistro(self.indice)

	def onAtras(self,event):
		print "onAtras"
		self.indice -=1
		self.IrAlregistro(self.indice)

	def onGuardar(self,event):
		print "onGuardar"
		impresora=self.formato.f2s_txtImpresora.GetValue()
		nombre=self.formato.f2s_txtNombre.GetValue()
		directorio=self.formato.f2s_txtDirectorio.GetValue()
		if len(nombre)<1:
			wx.MessageBox("Se requiere el nombre del proceso","Error",wx.ICON_ERROR)
			self.formato.f2s_txtNombre.SetFocus()
			return

		if len(impresora)<1:
			wx.MessageBox("Se requiere la impresora","Error",wx.ICON_ERROR)
			self.formato.f2s_txtImpresora.SetFocus()
			return
		
		if len(directorio)<1:
			wx.MessageBox("Se requiere la ruta para captura de spool","Error",wx.ICON_ERROR)
			self.formato.f2s_DirPic.SetFocus()
			return
		
		if not os.path.isdir(directorio):
			wx.MessageBox("La ruta no existe","Error",wx.ICON_ERROR)
			self.formato.f2s_txtDirectorio.SetFocus()
			self.formato.f2s_txtDirectorio.SelectAll()
			return
		
		if self.formato.f2s_listAcciones.GetItemCount()==0:
			wx.MessageBox("Se requiere Por lo menos una accion","Error",wx.ICON_ERROR)
			return
		
		estado=0
		if self.formato.f2s_ChkActivo.GetValue():
			estado=1

		fecha=str(date.today())
		if self.formato.f2s_BtnNuevoReg.Enabled:
				campos={"proceso":nombre,"impresora":impresora,"ruta":directorio,"fecha":fecha,"usuario":"Facil","estado":str(estado)}
				self.ObaseD.ActualizarCampos(self.tabla,campos,"id=%i" % (self.indice))
		else:
			campos="proceso,impresora,ruta,fecha,usuario,estado"
			valores="'%s','%s','%s','%s','Facil',%i" %(nombre,impresora,directorio,fecha,estado)
			self.indice=self.ObaseD.Insertar(self.tabla, campos, valores)

		print "indice=%i" %(self.indice)

		campos="patron,descrip,ambiente,idproceso"
		self.ObaseD.BorrarReg("tbl_patrones", 'idproceso=%i' %(self.indice))
		
		
		for lista in self.listaAcciones:
			valores ="'%s','%s','%s',%i" %(lista[0],lista[1],lista[3],self.indice)
			self.ObaseD.Insertar("tbl_patrones", campos, valores)
		
		self.Navegador()
		self.guadar=False
		self.formato.f2s_BtnNuevoReg.Enable(True)
		if self.formato.f2s_BtnNuevoReg.Enabled:
			wx.MessageBox ("Registro Actualizado","Estado",wx.ICON_ASTERISK)
		else:
			wx.MessageBox ("Registro nuevo Guardado","Estado",wx.ICON_ASTERISK)

	def onBuscar(self,event):
		self.formato.f2s_txtDirectorio.SetValue(self.formato.f2s_DirPic.GetPath())

	def IrAlregistro(self,indice=1):
		print self.tabla
		cantidad = self.ObaseD.Contar(self.tabla)
		if cantidad<1:
			return
			
		campos="proceso,impresora,ruta,estado"
		
		registro = self.ObaseD.SelectUno(campos, self.tabla,"id=%i" % (indice))
		if registro==None:
			wx.MessageBox("No hay registros","Info",wx.ICON_EXCLAMATION)
			self.indice=0
			return
		self.indice=indice
		self.formato.f2s_txtNombre.SetValue(registro[0])
		self.formato.f2s_txtImpresora.SetValue(registro[1])
		self.formato.f2s_txtDirectorio.SetValue(registro[2])
		if registro[3]==1:
			self.formato.f2s_ChkActivo.SetValue(True)
		else:
			self.formato.f2s_ChkActivo.SetValue(False)
		#llenado de la grilla
		campos="patron,ambiente,descrip"
		self.InicioGrilla()
		self.listaAcciones=self.ObaseD.LeerCampos(campos,"tbl_patrones ","idproceso=%i" %(self.indice))
		for registro in self.listaAcciones:
			puntero = self.formato.f2s_listAcciones.InsertStringItem(sys.maxint,registro[0])
			self.formato.f2s_listAcciones.SetStringItem(puntero,1,registro[1])
			self.formato.f2s_listAcciones.SetStringItem(puntero,2,registro[2])

		self.formato.f2s_BtnNuevoReg.Enable(True)
		self.Navegador()

	def Navegador(self):
		#j=ObjBase()
		cantidad = self.ObaseD.Contar(self.tabla)
		self.formato.f2s_lbCampos.SetLabel('%i / %i' %(self.indice,cantidad))
		
		
		if  cantidad ==1:
			self.formato.f2s_btnAnterior.Enable(False)
			self.formato.f2s_btnInicio.Enable(False)
			self.formato.f2s_btnSiguiente.Enable(False)
			self.formato.f2s_btnFinal.Enable(False)
		
		elif self.indice  == 1 and  cantidad >1:
			self.formato.f2s_btnAnterior.Enable(False)
			self.formato.f2s_btnInicio.Enable(False)
			self.formato.f2s_btnSiguiente.Enable(True)
			self.formato.f2s_btnFinal.Enable(True)
		
			
		elif self.indice  < cantidad and self.indice  > 1  :
			self.formato.f2s_btnAnterior.Enable(True)
			self.formato.f2s_btnInicio.Enable(True)
			self.formato.f2s_btnSiguiente.Enable(True)
			self.formato.f2s_btnFinal.Enable(True)
		
		elif self.indice == cantidad:
			self.formato.f2s_btnAnterior.Enable(True)
			self.formato.f2s_btnInicio.Enable(True)
			self.formato.f2s_btnSiguiente.Enable(False)
			self.formato.f2s_btnFinal.Enable(False)

	def onBorrarItem(self,event):
		print "onBorrarItem"
		puntero= self.formato.f2s_listAcciones.GetFirstSelected()
		print puntero
		self.formato.f2s_listAcciones.DeleteItem(puntero)
		print self.listaAcciones
		self.listaAcciones.pop(puntero)
		print self.listaAcciones

	def onActivarSeleccion(self,event):
		self.formato.f2s_btnBorrarlista.Enable(True)

	def onDesSeleccion(self,event):
		self.formato.f2s_btnBorrarlista.Enable(False)

	def onAdicionarAccion(self,event):
		print "onAdicionarAccion"
		objAccion=ObjAccion(self.padre,self.ObaseD)
		if objAccion.salida ==None:
			return
		
		print objAccion.salida
		puntero = self.formato.f2s_listAcciones.InsertStringItem(sys.maxint,objAccion.salida[0])
		self.formato.f2s_listAcciones.SetStringItem(puntero,1,objAccion.salida[2])
		self.formato.f2s_listAcciones.SetStringItem(puntero,2,objAccion.salida[1])
		self.listaAcciones.append(objAccion.salida)
		
	def onSalir(self,event):
		self.formato.Destroy()
