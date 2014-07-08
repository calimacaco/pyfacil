#!/usr/bin/env python
# -*- coding: utf-8 -*- 

'''
Created on 20/03/2013

@author: marco
'''
import wx

from FormMapic import ID_Adicionar
from FormMapic import ID_Editar
from FormMapic import ID_Plano
from PlanoUsuario import ObjSubirArch
from FormMapic import D_AddUsuario
from ObjGrilla import ObGrilla

class ObjUsr():
	def __init__(self,padre,base):	
		print "ObjUsr"
		self.ObaseD=base
		self.padre=padre
		tabla="tbl_cliente"
		campos="id, busqueda, dircorreo,CASE WHEN (imprimir=1) THEN 'X' ELSE '' END AS imp_x ,CASE WHEN (pdf=1) THEN 'X' ELSE '' END AS pdf_x, CASE WHEN (correo=1) THEN 'X' ELSE '' END AS correo_x"
		condicion=""
		limite=20
		orden ="id DESC"

		#Vista
		self.formato=ObGrilla(self.padre,u"Lista de Usuarios registrados")
		self.formato.InfoBase(self.ObaseD, tabla, campos, condicion, orden, limite,'busqueda')
		titulo=['Id','Identificador','Dirección Correo','impr.',"pdf","correo"]
		ancho=[40,250,420,45,45,45]
		self.formato.Titulos_columna(titulo, ancho)
		self.formato.Listar()
	
		#Eventos		
		self.formato.fusr.m_toolBar1.Bind(wx.EVT_TOOL,self.onAdicionar,id=ID_Adicionar)
		self.formato.fusr.m_toolBar1.Bind(wx.EVT_TOOL,self.onActualizar,id=ID_Editar)
		self.formato.fusr.m_toolBar1.Bind(wx.EVT_TOOL, self.onSubirPlano,id=ID_Plano)
		
	def onSubirPlano(self,event):
		formato=ObjSubirArch(self.padre,self.ObaseD)

		
		
	def onAdicionar(self,event):
		print "onAdicionar"
		self.usr_add=D_AddUsuario(self.padre)
		self.usr_add.SetTitle(u'Adicionar Usuario')
		self.usr_add.Btn_Aceptar.Bind(wx.EVT_BUTTON, self.Adicionar)
		self.usr_add.Bind(wx.EVT_BUTTON,self.onCerrar,self.usr_add.Btn_Cancelar)
		self.usr_add.ShowModal()
		
	def Adicionar(self,event):
		print "Adicionar campo"
		busqueda=''
		busqueda=self.usr_add.Txt_Busqueda.GetValue()
		if len(busqueda.strip()) <=0:
			wx.MessageBox("Es requerido el campo de busqueda: Error Campo Vacio","Campo Requerido",wx.ICON_ERROR)
			self.usr_add.Txt_Busqueda.SetFocus()
			return
		
		correo=self.usr_add.Txt_Correo.GetValue()
		correo=correo.strip()
		if correo.find("@") <4:
			wx.MessageBox("Es requerido la direccion de correo: nombre@server.com","Campo Requerido",wx.ICON_ERROR)
			self.usr_add.Txt_Correo.SetFocus()
			return
		
		if (self.usr_add.Ck_Imprimir.GetValue() == self.usr_add.Ck_EnvioCorreo.GetValue()) and (self.usr_add.Ck_Imprimir.GetValue()== self.usr_add.Ck_Pdf) and (self.usr_add.Ck_Imprimir==False):
			wx.MessageBox("Se debe seleccionar por lo menos una opcion","Seleccionar opcion",wx.ICON_ERROR)
			return
		
		ckimp=0
		ckpdf=0
		ckcor=0
		if self.usr_add.Ck_Imprimir.GetValue() :ckimp=1
		if self.usr_add.Ck_Pdf.GetValue():ckpdf=1
		if self.usr_add.Ck_EnvioCorreo.GetValue():ckcor=1
		campos=['busqueda','dircorreo','imprimir','pdf','correo','estado']
		valores=[(busqueda,correo,ckimp,ckpdf,ckcor,1)]
		if not self.ObaseD.InsertarVarios('tbl_cliente', campos, valores):
			wx.MessageBox("Ya existe el usuario","Error",wx.ICON_ERROR)
			return

		wx.MessageBox("Usuario adicionado","Adicionar",wx.ICON_EXCLAMATION)
		self.formato.Listar()
		#Limpiar
		self.usr_add.Txt_Busqueda.SetValue('')
		self.usr_add.Txt_Correo.SetValue('')
		self.usr_add.Ck_EnvioCorreo.SetValue(False)
		self.usr_add.Ck_Imprimir.SetValue(True)
		self.usr_add.Ck_Pdf.SetValue(False)
		self.usr_add.Txt_Busqueda.SetFocus()

	def onActualizar(self,event):
		if self.formato.Indice < 0:
			wx.MessageBox("Seleccione un registro, para la edicion")
			return
		wx.MessageBox('actualizar')
		self.usr_add=D_AddUsuario(self.padre)
		
		self.usr_add.Bind(wx.EVT_BUTTON, self.onModificar, self.usr_add.Btn_Aceptar)
		self.usr_add.Bind(wx.EVT_BUTTON,self.onCerrar,self.usr_add.Btn_Cancelar)
		self.usr_add.SetTitle(u'Editar Usuario')
		
		self.CodCliente= int(self.formato.fusr.Lst_Usuarios.GetItemText(self.formato.Indice))
		print "codigo",self.CodCliente
			
		if self.CodCliente<1:
			wx.MessageBox("No hay registro seleccionado","Error",wx.ICON_ERROR)
			print "error: 02"
			return
		try:
			campos="busqueda , dircorreo, imprimir ,pdf ,correo"
			condicion="id=%i"%(self.CodCliente)
			registro=self.ObaseD.SelectUno(campos, "tbl_cliente", condicion)
			print registro	
	
		except:
			wx.MessageBox("No hay registro seleccionado","Error",wx.ICON_ERROR)
			print "error: 01"
			return

		self.usr_add.Txt_Busqueda.SetValue(registro[0])
		self.usr_add.Txt_Correo.SetValue(registro[1])
		self.usr_add.Ck_Imprimir.SetValue(False)
		self.usr_add.Ck_EnvioCorreo.SetValue(False)
		self.usr_add.Ck_Pdf.SetValue(False)
		if registro[2]==1:self.usr_add.Ck_Imprimir.SetValue(True)
		if registro[4]==1:self.usr_add.Ck_EnvioCorreo.SetValue(True)
		if registro[3]==1:self.usr_add.Ck_Pdf.SetValue(True)
	
		
		self.usr_add.ShowModal()
	
	def onModificar(self,event):
		campo={'busqueda':self.usr_add.Txt_Busqueda.GetValue()}
		if len(campo['busqueda'].strip()) <=0:
			wx.MessageBox("Es requerido el campo de busqueda: Error Campo Vacio","Campo Requerido",wx.ICON_ERROR)
			self.usr_add.Txt_Busqueda.SetFocus()
			return
		
		campo['dircorreo']=self.usr_add.Txt_Correo.GetValue()
		campo['dircorreo']=campo['dircorreo'].strip()
		if campo['dircorreo'].find("@") <4:
			wx.MessageBox("Es requerido la direccion de correo: nombre@server.com","Campo Requerido",wx.ICON_ERROR)
			self.usr_add.Txt_Correo.SetFocus()
			return
		
		if (self.usr_add.Ck_Imprimir.GetValue() == self.usr_add.Ck_EnvioCorreo.GetValue()) and (self.usr_add.Ck_Imprimir.GetValue()== self.usr_add.Ck_Pdf) and (self.usr_add.Ck_Imprimir==False):
			wx.MessageBox("Se debe seleccionar por lo menos una opcion","Seleccionar opcion",wx.ICON_ERROR)
			return
		
		campo['imprimir']='0'
		campo['correo']='0'
		campo['pdf']='0'
		if self.usr_add.Ck_Imprimir.GetValue() :campo['imprimir']='1'
		if self.usr_add.Ck_Pdf.GetValue():campo['pdf']='1'
		if self.usr_add.Ck_EnvioCorreo.GetValue():campo['correo']='1'
		condicion='id=' + str(self.CodCliente)
		
		if not self.ObaseD.ActualizarCampos ('tbl_cliente', campo, condicion):
			wx.MessageBox("No es posible actualizar este campo..","Error",wx.ICON_ERROR)
			return
		self.formato.Listar()
		wx.MessageBox("Usuario Actualizado","Adicionar",wx.ICON_EXCLAMATION)
		self.usr_add.Destroy()

	def onCerrar(self,event):
		self.usr_add.Destroy()
		