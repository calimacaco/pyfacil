'''
Created on 9/10/2013

@author: marco

Control de la configuracion del Facil Exodo
'''
import os
import wx
from dialConfig import diag_config

from librerias.ctrlog import ObLog
from librerias.ctrlarchivo import ObCtrlArchivo

class ObjConfig ():
	
	def __init__(self,padre,nivellog=3):
		self.log=ObLog('configurar',nivellog)
		self.log.nivel=nivellog
		self.rutaconfig=''
		
		
		
		self.formato =diag_config(padre)
		self.formato.SetTitle("Confirguracion del sistema")
		self.formato.Center()
	
		self.formato.Bind(wx.EVT_BUTTON, self.onSalir, self.formato.f2s_btnSalir)
		
		
		items=['MySql','Sqlite']
		self.formato.f2s_choConector.SetItems(items)
		
		self.abrir()
		self.formato.ShowModal()


	def onSalir(self,evt):
		self.formato.Destroy()
		
		
	def abrir(self):
		self.log.logger.info('ObjConfig.abrir')
		archivo=ObCtrlArchivo(self.log.nivel)
		if archivo.error==1:
			wx.MessageBox('No existe archivo configuracion','Error',wx.ICON_ERROR)
			return
		self.rutaconfig=archivo.abrirConfig()
		