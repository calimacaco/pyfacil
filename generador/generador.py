#!/usr/bin/env python
# -*- coding: utf-8 -*- 
'''
Created on 7/02/2014

@author: marco
Generador de ambientes FACIL 2014
'''


import wx

from formgenerador import FrameGeneral
from Dial_Pagina import ObjPagina


class IncioInterface(FrameGeneral):
	def __init__(self):
		#self.log = ObLog('Inicio programa')
		#self.log.setNivel(0)  #debug
		
		FrameGeneral.__init__(self,None)
		FrameGeneral.SetTitle(self,u"Administrador de Aplicacion FACIL")
		#iconFile = u"imagenes/2s.ico"
		#FrameGeneral.SetIcon(self,wx.Icon(iconFile, wx.BITMAP_TYPE_ICO))
		#self.Bind(wx.EVT_MENU, self.onConfig,self.f2s_mConfig)
		self.__inicio()
		self.dibujarPizarra()
		
		#Eventos Menu
		self.Bind(wx.EVT_MENU,self.onDefPagina,self.f2s_menuTamPapel)
		self.f2s_Pizarra.Bind(wx.EVT_PAINT, self.onPaint)
		
	def __inicio(self):
		#Asignacion Variables Globales
		self.Guadar=False
		self.borde=20
		self.AnchoPagina=8.5 * 72
		self.AltoPagina = 11 * 72
		self.objfacil=[]
		self.objFormatos=[]
		self._initBuffer()

		
	def onDefPagina(self,event):
		pagina= ObjPagina(self.Parent)
		if pagina.orientar==None : 
			return
		
		print pagina.orientar
		print pagina.papel
		
		if pagina.orientar ==0 or pagina.orientar==2: 	#Vertical
			self.AnchoPagina=pagina.papel[0] * 72
			self.AltoPagina=pagina.papel[1] * 72
		else:											#Horizontal
			self.AnchoPagina=pagina.papel[1] * 72
			self.AltoPagina=pagina.papel[0] * 72
			
		print self.AnchoPagina
		print self.AltoPagina
		
		self.dibujarPizarra()	
		self.wrapDC = lambda dc: dc
		
		
	def dibujarPizarra(self):
		print "dibujar Pizarra"
		self.f2s_Pizarra.SetBackgroundColour('white')
		self.f2s_Pizarra.EnableScrolling(True,True)
		self.f2s_Pizarra.SetScrollbars(20, 20, (self.AnchoPagina + self.borde *2) / 20, (self.AltoPagina + self.borde *2) / 20)
		
		
		
	
	def onPaint(self, event):
		print "onPaint"
		"""
		Called when the window is exposed.
		"""
		# Create a buffered paint DC.  It will create the real
		# wx.PaintDC and then blit the bitmap to it when dc is
		# deleted.
		dc = wx.BufferedPaintDC(self.f2s_Pizarra, self.buffer)

		# On Windows, if that's all we do things look a little rough
		# So in order to make scrolling more polished-looking
		# we iterate over the exposed regions and fill in unknown
		# areas with a fall-back pattern.

		dc.SetPen(wx.Pen(wx.BLUE,  1, wx.SOLID))
		dc.DrawRectangle(self.borde, self.borde, self.AnchoPagina, self.AltoPagina)
		print self.borde, self.borde, self.AnchoPagina, self.AltoPagina


		if wx.Platform != '__WXMSW__':
			return
		
		print "Windows?"


		# First get the update rects and subtract off the part that
		# self.buffer has correct already
		region = self.f2s_Pizarra.GetUpdateRegion()
		panelRect = self.f2s_Pizarra.GetClientRect()
		offset = list(self.f2s_Pizarra.CalcUnscrolledPosition(0,0))
		offset[0] -= self.saved_offset[0]
		offset[1] -= self.saved_offset[1]
		region.Subtract(-offset[0],- offset[1],panelRect.Width, panelRect.Height)

		# Now iterate over the remaining region rects and fill in with a pattern
		rgn_iter = wx.RegionIterator(region)
		if rgn_iter.HaveRects():
			self.setBackgroundMissingFillStyle(dc)
			offset = self.f2s_Pizarra.CalcUnscrolledPosition(0,0)
		while rgn_iter:
			r = rgn_iter.GetRect()
			if r.Size != self.f2s_Pizarra.ClientSize:
				dc.DrawRectangleRect(r)
			rgn_iter.Next()

	
	
	#def onConfig(self,env):
		#self.log.logger.info('onCofig')
		#image=ObjConfig(self.Parent,self.log.getNivel())




	def _initBuffer(self):
		print "_initBuffer"
		"""Initialize the bitmap used for buffering the display."""
		size = self.f2s_Pizarra.GetSize()
		self.buffer = wx.EmptyBitmap(max(1,size.width),max(1,size.height))
		dc = wx.BufferedDC(None, self.buffer)
		dc.SetBackground(wx.Brush(self.f2s_Pizarra.GetBackgroundColour()))
		dc.Clear()
		#self.drawContents(dc)
		del dc  # commits all drawing to the buffer
		self.saved_offset = self.f2s_Pizarra.CalcUnscrolledPosition(0,0)
		self._reInitBuffer = False



class ObjInicio():
	def __init__(self,ActDebug=False):
		# Lanzamos aplicación.
		#ActDebug=True
		# 
		#print "inicio"
		#if ActDebug:
		#	pass
		#	aplicacion = ObjDebug(redirect=True)
		#else:
		#	aplicacion=wx.PySimpleApp()
		#	frame_usuario = IncioInterface()			
		#	frame_usuario.Maximize()
		#	frame_usuario.Show()
		
		aplicacion=wx.PySimpleApp()
		frame_usuario = IncioInterface()			
		#frame_usuario.Maximize()
		frame_usuario.Show()
		aplicacion.MainLoop()		
		aplicacion.Destroy()






if __name__ == '__main__':
	# Lanzamos aplicación.
	
	j=ObjInicio(False)
