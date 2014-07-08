#!/usr/bin/env python
# -*- coding: utf-8 -*- 


'''
Created on 5/03/2014

@author: marco
'''

import wx, sys,os

from formvista import FramePal as FrameGeneral
#from librerias.ctrlog import ObLog

class IncioInterface(FrameGeneral):
	def __init__(self):
		#self.log = ObLog('Inicio programa')
		#self.log.setNivel(0)  #debug
		FrameGeneral.__init__(self,None)
		FrameGeneral.SetTitle(self,u"Administrador de Aplicacion FACIL")
		#iconFile = u"imagenes/2s.ico"
		#FrameGeneral.SetIcon(self,wx.Icon(iconFile, wx.BITMAP_TYPE_ICO))
		#self.Bind(wx.EVT_MENU, self.onConfig,self.f2s_mConfig)
		
		
		
#	def onConfig(self,env):
		#self.log.logger.info('onCofig')
		#image=ObjConfig(self.Parent,self.log.getNivel())





class ObjInicio():
	def __init__(self,ActDebug=False):
		# Lanzamos aplicación.
		#ActDebug=True
		# 
		print "inicio"
		if ActDebug:
			pass
			#aplicacion = ObjDebug(redirect=True)
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
