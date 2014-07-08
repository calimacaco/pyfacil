#!/usr/bin/env python
# -*- coding: utf-8 -*- 

'''
Created on 10/04/2013

@author: marco
'''
import wx, sys,os
from FormMapic import D_Correo
from FormMapic import D_ProbarCorreo
from FormMapic import D_VisorHTML
from basedatos import ObjBase
from librerias.EnvioCorreo import Envio_Correo


class ObjCorreo():
	'''
	classdocs
	'''


	def __init__(self,padre,OBaseD=ObjBase):
		'''
		Constructor
		'''
		print "ObjCorreo"
		
		self.padre=padre
		self.posCorreo=1		#Puntero de la base de datos
		self.ObaseD=OBaseD
		self.estado=0     #1=Guardar 0=Adicionar
		
		#Crea la tabla si no existe
		self.ObaseD.CrearCorreo()
		
		
		self.Fcorreo=D_Correo(padre)
		self.Fcorreo.SetTitle("Confirguracion base de datos")
		self.Fcorreo.Center()
		
		
		self.VisorPos()		
		#Definicion de Botones
		self.Fcorreo.Bind(wx.EVT_BUTTON, self.onCorreoSiguiente,self.Fcorreo.Btn_siguiente)
		self.Fcorreo.Bind(wx.EVT_BUTTON, self.onCorreoAtras,self.Fcorreo.Btn_Atras)
		self.Fcorreo.Bind(wx.EVT_BUTTON, self.onPrimer,self.Fcorreo.Btn_Inicio)
		self.Fcorreo.Bind(wx.EVT_BUTTON, self.onUltimo,self.Fcorreo.Btn_Final)
		self.Fcorreo.Bind(wx.EVT_BUTTON, self.onCorreoAdicionar,self.Fcorreo.Btn_Adicionar)
		self.Fcorreo.Bind(wx.EVT_BUTTON,self.onCorreoModificar,self.Fcorreo.Btn_Modificar)
		self.Fcorreo.Bind(wx.EVT_CHECKBOX,self.onVerclave,self.Fcorreo.Chk_verclave)
		self.Fcorreo.Bind(wx.EVT_BUTTON,self.onProbar,self.Fcorreo.Btn_Probar)
		self.Fcorreo.Bind(wx.EVT_BUTTON,self.onSalir,self.Fcorreo.Btn_Salir)
		self.Fcorreo.Bind(wx.EVT_BUTTON,self.onVisorHML,self.Fcorreo.f2s_BtnValidarHML)
		
		
		#iniciar
		self.CorreoBuscarCampo()
		self.Fcorreo.Show()
	
	def onVisorHML(self,event):
		print 'onVisorHML'
		diag=D_VisorHTML(self.padre)
		diag.f2s_HtmlWin
		if "gtk2" in wx.PlatformInfo:
			print "gtk2"
			diag.f2s_HtmlWin.SetStandardFonts()
		print "texto:" , self.Fcorreo.Txt_HTML.GetValue()
		diag.f2s_HtmlWin.SetPage(self.Fcorreo.Txt_HTML.GetValue())
		diag.ShowModal()

	
	def onProbar(self,event):
		fprueba=D_ProbarCorreo(self.padre)
		obCorreo=Envio_Correo()
		port = int(self.Fcorreo.Txt_Puerto.GetValue())
		user=self.Fcorreo.Txt_Usuario.GetValue()
		clave=self.Fcorreo.Txt_Clave.GetValue()
		server =self.Fcorreo.Txt_Host.GetValue()
		tls=self.Fcorreo.Chk_TSL.GetValue()
		send_from=self.Fcorreo.Txt_enviado.GetValue()
		
		texto=obCorreo.pruebaConectar(server, port, tls, user, clave, send_from)
		print texto
		
		fprueba.m_textCtrl18.SetValue(texto)
		fprueba.ShowModal()
		
		
		
	
	def onSalir(self,event):
		self.Fcorreo.Destroy()
	
	
	
	def CorreoBuscarCampo(self):
		print '->CorreoBuscarCampo'
		campos  ='htmlcontenido, txtcontenido, puerto, usuario, clave,' 
		campos += 'servidor, tls, bandera, enviado, rutafinal, rutaanexo, estado'## fantaria -> archivoanexo, estado'
		condicion="id="+ str(self.posCorreo)
		tablas="tbl_correo"
		
		
		registro=self.ObaseD.SelectUno(campos,tablas, condicion)
		
		print registro
		
		
		if registro==None:
			self.estado=1
			self.posCorreo=0
			self.RegBlancos()
			return
		if len(registro)==0:
			self.posCorreo=0
			self.estado=1
			self.RegBlancos()
			return
		
		#SE activa modificar
		self.estado=2
		self.cambiarBoton()
		
		self.Fcorreo.Txt_HTML.SetValue(registro[0]) 
		self.Fcorreo.Txt_Texto.SetValue(registro[1])
		self.Fcorreo.Txt_Puerto.SetValue(str(registro[2]))
		self.Fcorreo.Txt_Usuario.SetValue(registro[3])
		self.Fcorreo.Txt_Clave.SetValue(registro[4])
		self.Fcorreo.Txt_Host.SetValue(registro[5])
		if registro[6]=='1':
			self.Fcorreo.Chk_TSL.SetValue(True)
		else:
			self.Fcorreo.Chk_TSL.SetValue(False)
		self.Fcorreo.Txt_Bandera.SetValue(registro[7])
		self.Fcorreo.Txt_enviado.SetValue(registro[8])
		self.Fcorreo.Txt_SalidaPDF.SetValue(registro[9])
		self.Fcorreo.Txt_RutaPDFadd.SetValue(registro[10])
		if registro[11]==1:
			self.Fcorreo.Chk_Estado.SetValue(True)
		else:
			self.Fcorreo.Chk_Estado.SetValue(False)
						
	def onCorreoModificar(self,event):
		print "onCorreoModificar"
						  
	  ## fantaria -> archivoanexo, estado'

		registro={
					'htmlcontenido':self.Fcorreo.Txt_HTML.GetValue(),
					'txtcontenido':self.Fcorreo.Txt_Texto.GetValue(),
					'puerto':self.Fcorreo.Txt_Puerto.GetValue(),
					'usuario':self.Fcorreo.Txt_Usuario.GetValue(), 
					'clave':self.Fcorreo.Txt_Clave.GetValue(),
					'servidor':self.Fcorreo.Txt_Host.GetValue(),
					'tls':'0', 
					'bandera':self.Fcorreo.Txt_Bandera.GetValue(), 
					'enviado':self.Fcorreo.Txt_enviado.GetValue(),
					'rutafinal':self.Fcorreo.Txt_SalidaPDF.GetValue(), 
					'rutaanexo':self.Fcorreo.Txt_RutaPDFadd.GetValue(), 
					'estado':'0'
				 
				  }

		if self.Fcorreo.Chk_TSL.GetValue():
			registro['tls']='1'
			
		if self.Fcorreo.Chk_Estado.GetValue():
			registro['estado']='1'

		condicion="id="+ str(self.posCorreo)
		tabla="tbl_correo"

		if self.ObaseD.ActualizarCampos(tabla,registro,condicion):
			wx.MessageBox("Registro Actualizado")
		else:
			wx.MessageBox("Problema para actualizar en la Base de Datos","Error",wx.ICON_ERROR)


	def onCorreoAdicionar(self,event):
		print self.posCorreo
		if self.estado==2: #adicionar campo nuevo
			print self.posCorreo
			self.posCorreo=self.TotalRegistro()+1
			self.estado=1	#cambio a guardar
			self.RegBlancos()			
			return
		
		
		
		if len (self.Fcorreo.Txt_Host.GetValue())<1:
			wx.MessageBox("El nombre del Host Es requerido")
			self.Fcorreo.Txt_Host.SetFocus()
			return
		
		campos  ='htmlcontenido, txtcontenido, puerto, usuario, clave,' 
		campos += 'servidor, tls, bandera, enviado, rutafinal, rutaanexo, estado'## fantaria -> archivoanexo, estado'
		
		
		
		valores="'"+self.Fcorreo.Txt_HTML.GetValue() +"','"+self.Fcorreo.Txt_Texto.GetValue()+"',"
		valores+="'"+self.Fcorreo.Txt_Puerto.GetValue()+"','"+self.Fcorreo.Txt_Usuario.GetValue()+"',"
		valores+="'"+self.Fcorreo.Txt_Clave.GetValue()+"','"+self.Fcorreo.Txt_Host.GetValue()+"',"
		if self.Fcorreo.Chk_TSL.GetValue():
			valores+="'1',"
		else:
			valores+="'1',"
		valores+="'"+self.Fcorreo.Txt_Bandera.GetValue()+"',"
		valores+="'"+self.Fcorreo.Txt_enviado.GetValue()+"'," 
		valores+="'"+self.Fcorreo.Txt_SalidaPDF.GetValue()+"',"
		valores+="'"+self.Fcorreo.Txt_RutaPDFadd.GetValue()+"',"
		if self.Fcorreo.Chk_Estado.GetValue():
			valores+="'1'"
		else:
			valores+="'0'"
		
		print valores
		#adiciona a la base de datos el nombre y archivo pdf archivo pcl
		inserto=self.ObaseD.Insertar ('tbl_correo', campos, valores)		
		print inserto
		wx.MessageBox("Campo adicionado")
		
		
		
		self.estado=2				#Cambio a Adicionar
		self.VisorPos()
		self.cambiarBoton()
		
	def onUltimo(self,event):
		self.posCorreo=self.TotalRegistro()
		self.CorreoBuscarCampo()
		self.VisorPos()
		
	def onPrimer(self,event):
		self.posCorreo=1
		self.CorreoBuscarCampo()
		self.VisorPos()
		
	def onCorreoSiguiente(self,event):
		if self.TotalRegistro() < self.posCorreo+1:
			wx.MessageBox("No hay mas registros","Siguiente")
			return
		self.posCorreo +=1
		self.CorreoBuscarCampo()
		self.VisorPos()
		
	def onCorreoAtras(self,event):
		print "boton Atras"
		if self.posCorreo-1==0:
			wx.MessageBox("No hay mas registros","Atras")
			return
		self.posCorreo -=1
		self.CorreoBuscarCampo()
		self.VisorPos()
		

	def CorreoMoverCampo(self):
		print "aqi mover campo"

	def RegBlancos(self):
		self.Fcorreo.Txt_HTML.SetValue('') 
		self.Fcorreo.Txt_Texto.SetValue('')
		self.Fcorreo.Txt_Puerto.SetValue('')
		self.Fcorreo.Txt_Usuario.SetValue('')
		self.Fcorreo.Txt_Clave.SetValue('')
		self.Fcorreo.Txt_Host.SetValue('')
		self.Fcorreo.Chk_TSL.SetValue(False)
		self.Fcorreo.Txt_Bandera.SetValue('')
		self.Fcorreo.Txt_enviado.SetValue('')
		self.Fcorreo.Txt_SalidaPDF.SetValue('')
		self.Fcorreo.Txt_RutaPDFadd.SetValue('')
		self.VisorPos()
		self.cambiarBoton()

	def cambiarBoton(self):
		if self.estado==1:
			self.Fcorreo.Btn_Adicionar.SetLabel("Guardar")
			self.Fcorreo.Btn_Modificar.Enable(False)
		elif self.estado==0:
			self.Fcorreo.Btn_Adicionar.SetLabel("Adicionar")
			self.Fcorreo.Btn_Modificar.Enable(False)
		elif self.estado==2:
			self.Fcorreo.Btn_Modificar.Enable(True)
			self.Fcorreo.Btn_Adicionar.SetLabel("Adicionar")

	def TotalRegistro(self):
		registros=self.ObaseD.SelectUno('COUNT (id) ' ,'tbl_correo')
		return registros[0]

	def VisorPos(self):
		print 'VisorPos'
		maximo=self.TotalRegistro()
		self.Fcorreo.Txt_PosRegistro.SetValue(str(self.posCorreo) + ' de ' + str(maximo))
		if maximo >0 : 
			
			self.Fcorreo.m_slider1.SetMin(1)
			self.Fcorreo.m_slider1.SetMax(maximo)
			self.Fcorreo.m_slider1.SetValue(self.posCorreo)
			self.Fcorreo.m_slider1.Enable(True)
		else:
			self.Fcorreo.m_slider1.Enable(False)
			#self.Fcorreo.m_slider1.SetMax(0)
			#self.Fcorreo.m_slider1.SetValue(0)

	def onVerclave(self,event):
		print "activar"
		if self.Fcorreo.Chk_verclave.GetValue():
			self.Fcorreo.Txt_Clave.SetStyle(1,len(self.Fcorreo.Txt_Clave.GetValue()), wx.TE_PASSWORD)
		else:		
			self.Fcorreo.Txt_Clave.SetStyle(1,len(self.Fcorreo.Txt_Clave.GetValue()),wx.NORMAL)
