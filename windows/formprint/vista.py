#!/usr/bin/env python
# -*- coding: utf-8 -*- 

'''
Created on 12/03/2014

@author: marco
'''
from datetime import date 
import wx, sys, os
import glob
import shutil


from registro import  RegistroWindows
from formprint import FrameGeneral 
from ctrgs import ObjGS

class IncioInterface(FrameGeneral):
	def __init__(self,archivo):
		self.rutaFormato=None
		self.archEntrada = archivo
		print "Entrada %s" %(self.archEntrada)
		FrameGeneral.__init__(self,None)
		FrameGeneral.SetTitle(self,u"Generador de Formularios FACIL")
			#iconFile = u"imagenes/2s.ico"
		#FrameGeneral.SetIcon(self,wx.Icon(iconFile, wx.BITMAP_TYPE_ICO))
		
		self.LleerFormatos()
		
		self.Bind(wx.EVT_BUTTON, self.OnNuevo, self.f2s_btnNuevo)
		self.Bind(wx.EVT_BUTTON, self.OnModificar, self.f2s_BtnActualizar)
		self.Bind(wx.EVT_CHOICE, self.OnActivarActualizar, self.f2s_choice)
		
	def LleerFormatos(self):
		prueba=RegistroWindows()
		self.rutaFormato =prueba.BuscarFacil()
		if self.rutaFormato[-1]==os.sep : self.rutaFormato=self.rutaFormato[:-1]
		
		if self.rutaFormato ==False:
			self.ErrorSalir("Facil no instalado")

		self.rutaFormato += os.sep + 'Formatos'
		if not os.path.isdir(self.rutaFormato):
			try:
				os.mkdir(self.rutaFormato)
			except:
				self.ErrorSalir("No es posible crear:[%s]"%(self.rutaFormato))
				
		lista = glob.glob1(self.rutaFormato, "*.frm")
		lista.sort()		
		self.f2s_choice.SetItems(lista)
		self.f2s_gauge1.SetValue(10)
				
	def ErrorSalir(self,mensaje):
		wx.MessageBox(mensaje,"Error",wx.ICON_ERROR)
		self.Destroy()
		
	def OnSalir(self,events):
		print 'IncioInterface->OnSalir'
		self.Destroy()
	
#		wx.MessageBox("Ya se ingreso al Sistemas","Correcto",wx.ICON_ASTERISK)
	
	def OnActivarActualizar(self,events):
		self.f2s_BtnActualizar.Enable(True)

	def NuevoNombre(self,origen):
		contador=0
		anterior = "%s_%s_%s.old"  %(origen,date.today(),contador)
		
		while  os.path.isfile(anterior):
			contador +=1
			anterior = "%s_%s_%s.old"  %(origen,date.today(),contador)
		return anterior
	
	def MoverFrm(self,origen,extension):

		if len(extension)>0:
			origen=origen[:-3] + extension	
			
		destino=self.NuevoNombre(origen)
		if os.path.isfile(origen):
			shutil.move(origen, destino)
		self.f2s_gauge1.SetValue(self.f2s_gauge1.GetValue()+5)
		self.f2s_gauge1.Refresh()

	def OnNuevo(self,events):		
		self.f2s_gauge1.SetValue(20)
		self.f2s_gauge1.Refresh()
		archSalida=self.rutaFormato + os.sep + self.f2s_nuevoNombre.GetValue() + ".frm"
		self.generar(archSalida)

	def OnModificar(self,events):
		self.f2s_gauge1.SetValue(20)
		self.f2s_gauge1.Refresh()
		archSalida=self.rutaFormato + os.sep + self.f2s_choice.GetString(self.f2s_choice.GetSelection())
		self.generar(archSalida)
		
	def generar(self,archSalida):
		#mover Formato
		self.MoverFrm(archSalida, '')
		#mover imange png Anterior
		self.MoverFrm(archSalida, 'png')
		#mover imagen eps anterior
		self.MoverFrm(archSalida, 'eps')	
		self.convertirPCL(archSalida)
		#crear eps.
		archSalida=archSalida[:-3] + 'eps'
		shutil.move(self.archEntrada,archSalida) 
		self.f2s_gauge1.SetValue(100)
		self.f2s_gauge1.Refresh()
		wx.MessageBox("Formularios convertidos","Finalizo",wx.ICON_ASTERISK)
		self.Destroy()
		
	def convertirPCL (self,nombresalida):
		print self.archEntrada
		print nombresalida
		self.f2s_gauge1.SetValue(self.f2s_gauge1.GetValue()+10)
		self.f2s_gauge1.Refresh()
		GsActua=ObjGS(self.archEntrada,nombresalida)
		GsActua.ProcesarPCL()
		self.f2s_gauge1.SetValue(self.f2s_gauge1.GetValue()+10)
		self.f2s_gauge1.Refresh()
		GsActua.ProcesarPNG()
		self.f2s_gauge1.SetValue(self.f2s_gauge1.GetValue()+10)
		self.f2s_gauge1.Refresh()
		
class ObjDebug(wx.App):
	def __init__(self, redirect=True, filename=None):
		print "App __init__"
		wx.App.__init__(self, redirect, filename)
		
	def OnInit(self):
		print "OnInit"
		frame_usuario = IncioInterface()
		frame_usuario.Show()
		print >> sys.stderr, "A pretend error message"
		return True	

class ObjInicio():
	def __init__(self,ActDebug=False,arch_entrada=None):
		# Lanzamos aplicación.
		#ActDebug=True
		# 
		print "inicio"
		if ActDebug:
			aplicacion = ObjDebug(redirect=True)
		else:
			aplicacion=wx.PySimpleApp()
			frame_usuario = IncioInterface(arch_entrada)			
			frame_usuario.Show()

		aplicacion.MainLoop()
		aplicacion.Destroy()

if __name__ == '__main__':	
	j=ObjInicio(False,"temporal")
	
	
