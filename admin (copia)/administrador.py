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
from FormMapic import D_Abrir
from FormMapic import D_GenerarPDF
from PlanoUsuario import ObjSubirArch
from ManejoCorreo import ObjCorreo
from manejoarchivo import ObjRelArchivo

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
		self.Bind(wx.EVT_MENU, self.OnVerArchivos,self.m_relarchivo)
		
		
		
		self.m_veradjuntos.Enable()

	def OnVerArchivos(self,event):
		ObjRelArchivo(self.Parent,self.ObaseD)
		
	def OnVerAdjuntos(self,event):
		print 'IncioInterface->OnVerAdjuntos' 
		x=ObjAdjunto (self.Parent,self.ObaseD)
		
	def verUsr(self,events):
		print 'IncioInterface->verUsr'
		x=ObjUsr (self.Parent,self.ObaseD)

	def OnSalir(self,events):
		print 'IncioInterface->OnSalir'
		self.Destroy()
	
	def OnconfigCorreo(self,events):
		print "IncioInterface->OnconfigCorreo"
		#wx.MessageBox('conf. correo')
		x= ObjCorreo(self,self.ObaseD)
		
	def VerPlano(self,events):
		print "IncioInterface->VerPlano"
		
		formato=ObjSubirArch(self.Parent,self.ObaseD)
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
		print "Abrir Base de datos"
		self.f_Abrir=D_Abrir(self)		
		self.f_Abrir.SetTitle("Abrir Base de Datos")
		self.f_Abrir.Center()
		self.f_Abrir.Show()
		self.f_Abrir.ArchivoBase.Bind(wx.EVT_FILEPICKER_CHANGED, self.onActivarAbrir)
		#self.f_Abrir.BtnAbrir.Bind(wx.EVT_BUTTON, self.OnAbrirBase)
		self.f_Abrir.BtnSalir.Bind(wx.EVT_BUTTON, self.OnCerrarConfig)
		self.f_Abrir.BtnCrearBD.Bind(wx.EVT_BUTTON, self.onCrearBaseDatos)
		

	#Eventos del panel inicio (Apertura de la base de datos)

#######
#

	def onCrearBaseDatos(self,event):
		#Crear la base de datos de configuracion
		if len(self.f_Abrir.Txt_NombreBD.GetValue())<3:
			wx.MessageBox("Nombre de la base de datos muy pequeño/n minimo debe tener 3 caracteres","nombre base datos",wx.ICON_ERROR)
			return
		
		nombre=self.f_Abrir.Dir_BD.GetPath() + os.sep +  self.f_Abrir.Txt_NombreBD.GetValue()
		
		print "nombre salida:",nombre
		
		self.ObaseD=ObjBase(nombre +".db") #Automaticamente se crea la base y sus tablas
		wx.MessageBox("Base de datos Creada","Crear BD",wx.ICON_EXCLAMATION)
		self.f_Abrir.Hide()
		#self.f_usuario.Show()
		self.llenarGrilla()
		self.HabilitarMenus()
	
	def HabilitarMenus(self):
		self.m_GenPCL.Enable()
		self.m_SubrirPlano.Enable()
		self.m_configCorreo.Enable()
		self.m_Verusr.Enable()
		#self.m_veradjuntos.Enable()
		#self.m_VerEstado().Enable()
			
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
			
	
	def onActivarAbrir(self,event):
		self.f_Abrir.ArchivoBase.GetPath()
		self.ObaseD=ObjBase(self.f_Abrir.ArchivoBase.GetPath())
		self.f_Abrir.Hide()
		#self.f_usuario.Show()
		self.llenarGrilla()
		self.m_GenPCL.Enable()
		self.m_SubrirPlano.Enable()
		self.m_veradjuntos.Enable()
		self.m_configCorreo.Enable()
		self.m_Verusr.Enable()
		self.m_VerEstado.Enable()
		#self.GuardarUltimo(self.ObaseD.rutabase)
					
						
	def OnCerrarConfig(self,event):
		self.panelInicio.Hide()
		
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
			frame_usuario.Maximize()
			frame_usuario.Show()
			
		
		aplicacion.MainLoop()
		
		aplicacion.Destroy()






if __name__ == '__main__':
	# Lanzamos aplicación.
	
	j=ObjInicio(False)
	
	
#Nelson Moreno: ID: 671 959 285
#[13:01:57] Nelson Moreno: Clave: 1383
#[13:38:33] Llamada de Nelson Moreno, duración 38:08.
