#!/usr/bin/env python
# -*- coding: utf-8 -*- 


'''
Created on 17/10/2013

@author: marco
'''
import wx
from convert_lgo import convert_img	


ID_FILE_OPEN = wx.NewId()
ID_FILE_EXIT = wx.NewId()
ID_THRESHOLD = wx.NewId()

from frmgenlogo import f2s_framepal as FrameGeneral


class IncioInterface(FrameGeneral):
	def __init__(self):
		self.nivel=0
		self.imagenentrada=''
		self.imagensalida='salida'
		self.tam=-1
		self.brillo=-1
		
		FrameGeneral.__init__(self,None)
		FrameGeneral.SetTitle(self,u"Creacion de achivos LGO")
		#iconFile = u"imagenes/2s.ico"
		#FrameGeneral.SetIcon(self,wx.Icon(iconFile, wx.BITMAP_TYPE_ICO))
		#tam=self.m_bpButton1.GetSize()
		#FrameGeneral.SetDimensions()
		
		self.Bind(wx.EVT_MENU,self.PantallaAbrir,self.f2s_menu_abrir)
		self.Bind(wx.EVT_MENU,self.m_Convert,self.f2s_menu_convert)

		self.Bind(wx.EVT_FILEPICKER_CHANGED,self.On_selectimagen,self.f2s_fpick_Imagen)
		self.Bind(wx.EVT_FILEPICKER_CHANGED,self.On_selectsalida,self.f2s_fpick_salida)
		self.Bind(wx.EVT_BUTTON,self.On_Convertir,self.f2s_btn_Convertir)
		self.imagen=None



	def On_Convertir(self,evt):
		self.Convertir()
		

	def On_selectsalida(self,evt):
		self.imagensalida=self.f2s_fpick_salida.GetPath()

	def On_selectimagen(self,evt):
		self.imagenentrada=self.f2s_fpick_Imagen.GetPath()
		print "On_selectimagen  %s" % (self.imagenentrada)

	def PantallaAbrir(self,evt):
		print "pantalla abrir"
				
		wildcard = "Archivos de imagen |*.png;*.gif;*.bmp;*.jpg|" 	
		fd = wx.FileDialog(
            self, message="Seleccionar archivo",
            defaultFile="",
            wildcard=wildcard,
            style=wx.OPEN  | wx.CHANGE_DIR)
		
		if fd.ShowModal() == wx.ID_OK:
			self.imagenentrada= fd.GetPath()
			#self.imagen =Image.open(fd.GetPath())
			#self.imagen.show()	
		fd.Destroy()
		
	def m_Convert(self,evt):
		wildcard = "Archivos de logo |*.lgo|" 	
		fd = wx.FileDialog(
            self, message="Seleccionar archivo",
            defaultFile="",
            wildcard=wildcard,
            style=wx.SAVE  | wx.CHANGE_DIR)
		
		if fd.ShowModal() != wx.ID_OK:
			return
		self.imagensalida=fd.GetPath()
	
	
	
	def Convertir(self):
		objconv=convert_img(self.nivel)
		objconv.setImagen(self.imagenentrada)
		objconv.setArchivoSalida(self.imagensalida)
		#if obarg.escala!=-1:objconv.escalar(obarg.escala) 
		#if obarg.brillo!=-1:objconv.modify_img(obarg.brillo)
		objconv.procesar()
		wx.MessageBox("Conversion Finalizada")
			
		
		

if __name__ == '__main__':
	aplicacion=wx.PySimpleApp()
	frame_usuario = IncioInterface()			
	#frame_usuario.Maximize()
	frame_usuario.Show()
	aplicacion.MainLoop()	
	aplicacion.Destroy()
