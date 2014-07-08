#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import wx, sys,os
try:  
	import cPickle as pickle  
except ImportError:  
	import pickle  

###Formularios
from basedatos import ObjBase
from ManejoUsuario import ObjUsr
from ManejoAdjuntos import ObjAdjunto
from conver_pdf_pcl import ObConversor
from FormMapic import FrameGeneral
from FormMapic import D_GenerarPDF

from PlanoUsuario import ObjSubirArch
from ManejoCorreo import ObjCorreo
from manejoarchivo import ObjConfArchivo
from objGenerales import objGeneral
from ManejoAbrirBD import ObjManejoDB
from ServicioArchivo import ObjServArchivo
#from ObjConvertir import Pdf2Pcl

class IncioInterface(FrameGeneral):
	def __init__(self):
		self.Indice=-1
		self.CodCliente=-1
		self.paginas=0
		self.pagina=0	
		self.Campos=[]	
		self.ObaseD=None
		self.accion=0
		
		
		FrameGeneral.__init__(self,None)
		FrameGeneral.SetTitle(self,u"Controlador Manejo de Docuentos")
		iconFile = u"imagenes/2s.ico"
		FrameGeneral.SetIcon(self,wx.Icon(iconFile, wx.BITMAP_TYPE_ICO))
		#tam=self.m_bpButton1.GetSize()
		#FrameGeneral.SetDimensions()

		
		self.f_GenPcl=D_GenerarPDF(self)
		
		#Menus
		self.Bind(wx.EVT_MENU,self.PantallaAbrir,self.m_Abrir)
		self.Bind(wx.EVT_MENU,self.OnGenpcl,self.m_GenPCL)
		self.Bind(wx.EVT_MENU, self.VerPlano, self.m_SubrirPlano)
		self.Bind(wx.EVT_MENU, self.OnSalir,self.m_Salir)
		self.Bind(wx.EVT_MENU,self.verUsr,self.m_Verusr)
		self.Bind(wx.EVT_MENU, self.OnconfigCorreo,self.m_configCorreo)
		self.Bind(wx.EVT_MENU, self.OnVerAdjuntos,self.m_veradjuntos)
		self.Bind(wx.EVT_MENU, self.OnconfArchivos,self.m_confEnvioArchivo)
		self.Bind(wx.EVT_MENU, self.OnGenerales,self.m_generales)
		self.Bind(wx.EVT_MENU, self.OnEstadoArchivo,self.m_estadoArchivo)
		
		
		
		self.m_veradjuntos.Enable()

	def OnEstadoArchivo(self,event):
		#manejo de servicio envio de Archivo
		ObjServArchivo (self.Parent,self.ObaseD)

	def OnGenerales(self,event):
		objGeneral (self.Parent,self.ObaseD)

	def OnconfArchivos(self,event):
		ObjConfArchivo(self.Parent,self.ObaseD)
		
	def OnVerAdjuntos(self,event):
		print 'IncioInterface->OnVerAdjuntos' 
		ObjAdjunto (self.Parent,self.ObaseD)
		
	def verUsr(self,events):
		print 'IncioInterface->verUsr'
		ObjUsr (self.Parent,self.ObaseD)

	def OnSalir(self,events):
		print 'IncioInterface->OnSalir'
		self.Destroy()
	
	def OnconfigCorreo(self,events):
		print "IncioInterface->OnconfigCorreo"
		#wx.MessageBox('conf. correo')
		ObjCorreo(self,self.ObaseD)
		
	def VerPlano(self,events):
		print "IncioInterface->VerPlano"
		ObjSubirArch(self.Parent,self.ObaseD)
		#self.f_Subir.bt
		#self.f_GenPcl.Bind(wx.EVT_BUTTON,self.OnProcesarPDF,self.f_GenPcl.Btn_GenerarPCL)
	
	#------------------
	
	def OnProcesarPDF(self,events):
		ruta= self.f_GenPcl.dir_PDF.GetPath()
		if len(ruta.strip())==0:
			wx.MessageBox("Debe ingresar la ruta de proceso","Error",wx.ICON_ERROR)
			return
		
		ruta =self.f_GenPcl.Dir_Salida.GetPath()
		if len(ruta.strip())==0:
			wx.MessageBox("Debe ingresar la ruta de salida","Error",wx.ICON_ERROR)
			return
		if int(self.f_GenPcl.Txt_NroArchivos.GetValue())<100:
			wx.MessageBox("Debe colocarse por lo menos 100 archivos por carpeta","Error",wx.ICON_ERROR)
			self.f_GenPcl.Txt_Mensaje.SetValue('100')
			self.f_GenPcl.Txt_NroArchivos.SetFocus()
			return
		
		self.f_GenPcl.Txt_Mensaje.SetValue("Procesando...\n")
		convertir=ObConversor()		
		
		convertir.oMensaje(self.f_GenPcl.Txt_Mensaje)
		
		convertir.rutaEntrada=self.f_GenPcl.dir_PDF.GetPath()
		#convertir.rutaGS=self.f_GenPcl.Dir_GhostScript.GetPath()
		convertir.rutaSalida=self.f_GenPcl.Dir_Salida.GetPath()
		convertir.nroarch=int(self.f_GenPcl.Txt_NroArchivos.GetValue())
		convertir.bd=self.ObaseD.rutabase
		convertir.PDFaPCL()
		
		
		wx.MessageBox("Proceso Concluido","fin",wx.ICON_EXCLAMATION)		
			
	def OnGenpcl(self,events):
		
		self.f_GenPcl.SetTitle("Generador PCL")
		self.f_GenPcl.Center()
		self.f_GenPcl.Show()
		self.f_GenPcl.Btn_GenerarPCL.Bind(wx.EVT_BUTTON,self.OnProcesarPDF)
		self.f_GenPcl.Btn_BorrarResultado.Bind(wx.EVT_BUTTON,self.OnBorrarResultado)
		self.f_GenPcl.Btn_Resultado.Bind(wx.EVT_BUTTON,self.OnMuestraResultado)
			
	def OnBorrarResultado(self,events):
		print "Borrar Resultado"
		self.ObaseD.BorrarTablaTempProc()
		self.f_GenPcl.Txt_Mensaje.SetValue("Limpieza de log Concluida")
	
	def OnMuestraResultado(self,events):
		leer =self.ObaseD.SelectUno("COUNT (rutapdf)", 'tbl_temp1', "estado=1")
		if leer !=None:
			print "****", leer
			procesados=leer[0]		
		leer =self.ObaseD.SelectUno("COUNT (rutapdf)", 'tbl_temp1', "estado=0")
		if leer !=None:
			sinprocesar=leer[0]
		
		texto="Proceso Concluido\nProcesados:   %i\nsin procesar : %i\nTotal: %i\n" % (procesados,sinprocesar,procesados+sinprocesar)
		leer =self.ObaseD.LeerCampos("rutapdf", 'tbl_temp1', "estado=0")
		if leer !=None:
			texto +='******** sin procesar **************\n'
			for campo in leer:
				texto +=campo[0] + '\n'
			
		
		self.f_GenPcl.Txt_Mensaje.SetValue(texto)
			
	def PantallaAbrir(self,events):
		vista= ObjManejoDB(self)
		self.ObaseD=vista.ObaseD
		print self.ObaseD
		if not self.ObaseD==None:
			self.HabilitarMenus(True)


	
	def HabilitarMenus(self,valor):
		self.m_GenPCL.Enable(valor)
		self.m_SubrirPlano.Enable(valor)
		self.m_veradjuntos.Enable(valor)
		self.m_configCorreo.Enable(valor)
		self.m_Verusr.Enable(valor)
		self.m_VerEstado.Enable(valor)
		self.m_estadoArchivo.Enable(valor)
		self.m_confEnvioArchivo.Enable(valor)
		self.m_generales.Enable(valor)

			
	def GuardarUltimo(self,ruta):
		print ruta
		
		
		if os.path.isfile(ruta):
			arch=file(ruta,'r')
			lista=pickle.load(arch)
			arch.close()
			if len(lista)>9:
				lista.pop()
			if not ruta in lista:
				lista = [ruta] + lista
		else:
			lista=[ruta]
			
		arch=file(ruta,'w')
		pickle.dump(ruta, lista)  
		arch.close()
			
	
		#self.GuardarUltimo(self.ObaseD.rutabase)
					
						#3117199279 cesar garcia  garc7257@hotmail.com
		
	def llenarGrilla(self):
		print "Llenar Grilla Usuario"
		wx.MessageBox("Ya se ingreso al Sistemas","Correcto",wx.ICON_ASTERISK)
		
class ObjDebug(wx.App):
	def __init__(self, redirect=True, filename=None):
		print "App __init__"
		wx.App.__init__(self, redirect, filename)
		
	def OnInit(self):
		print "OnInit"
		frame_usuario = IncioInterface()
		frame_usuario.Maximize()
		frame_usuario.Show()
		print >> sys.stderr, "A pretend error message"
		return True
	
	#def OnExit(self):
	#	print "OnExit"

class ObjInicio():
	def __init__(self,ActDebug=False):
		# Lanzamos aplicación.
		#ActDebug=True
		# 
		print "inicio"
		if ActDebug:
			aplicacion = ObjDebug(redirect=True)
		else:
			aplicacion=wx.PySimpleApp()
			frame_usuario = IncioInterface()			
##			frame_usuario.Maximize()
			frame_usuario.Show()
			
		
		aplicacion.MainLoop()
		aplicacion.Destroy()






if __name__ == '__main__':
	# Lanzamos aplicación.
	
	j=ObjInicio(False)
	
	
#Nelson Moreno: ID: 671 959 285
#[13:01:57] Nelson Moreno: Clave: 1383
#[13:38:33] Llamada de Nelson Moreno, duración 38:08.
