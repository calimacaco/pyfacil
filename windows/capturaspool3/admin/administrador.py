#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
import wx
import os
import shutil


try:  
	import cPickle as pickle  
except ImportError:  
	import pickle

from FormCaptura import FramePal


class IncioInterface(FramePal):
	def __init__(self):
		FramePal.__init__(self,None)
		FramePal.SetTitle(self,u"Crear manejo spool")
		self.ambiente=""
		self.Btn_Abrir.Bind (wx.EVT_BUTTON, self.OnAbrir)
		self.Btn_Guardar.Bind (wx.EVT_BUTTON, self.OnGuardar)

	
	def OnAbrir(self,event):
		self.ambiente = self.Sel_Archivo.GetPath()	
		if not os.path.isfile(self.ambiente):
			return
		arc = open(self.ambiente, "r")  
		comandos=pickle.load(arc)
		control=pickle.load(arc)
		arc.close()
		self.Txt_Buscar.SetValue(comandos["buscar"])
		self.Txt_BusFila.SetValue(str(comandos["Fila"]))
		self.Txt_BusColumna.SetValue(str(comandos["Columna"]))
		self.Txt_RutaGuardar.SetValue(str(comandos["ruta"]))
		self.Txt_NomFila.SetValue(str(control["Fila"]))
		self.Txt_NomColumna.SetValue(str(control["Columna"]))
		self.Txt_NomColFin.SetValue(str(control["Columnas"]))

	def OnGuardar(self,event):
			comandos={
						"ruta":self.Txt_RutaGuardar.GetValue(),
						"buscar":self.Txt_Buscar.GetValue(),
						"Fila":int(self.Txt_BusFila.GetValue()),
						"Columna":int(self.Txt_BusColumna.GetValue())
					}  
			seleccion={
						"campocontrol":"1",
						"Fila":int(self.Txt_NomFila.GetValue()),
						"Columna":int(self.Txt_NomColumna.GetValue()),
						"Columnas":int(self.Txt_NomColFin.GetValue())
					}
			print comandos,seleccion
			
			if os.path.isfile(self.ambiente):
				shutil.copy(self.ambiente, self.ambiente + ".bak")

			arc=open(self.ambiente,'w')
			pickle.dump(comandos, arc, 2)			  
			pickle.dump(seleccion, arc, 2)
			arc.close()
		


if __name__ == '__main__':
	# Lanzamos aplicación.
	aplicacion = wx.PySimpleApp()
	frame_usuario = IncioInterface()
	frame_usuario.Show()
	aplicacion.MainLoop()



