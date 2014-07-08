# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Sep  8 2010)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx

###########################################################################
## Class FrameGeneral
###########################################################################

class FrameGeneral ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,150 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer1 = wx.FlexGridSizer( 2, 3, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Formulario", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		fgSizer1.Add( self.m_staticText1, 0, wx.ALL, 5 )
		
		f2s_choiceChoices = []
		self.f2s_choice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 300,-1 ), f2s_choiceChoices, 0 )
		self.f2s_choice.SetSelection( 0 )
		fgSizer1.Add( self.f2s_choice, 0, wx.ALL, 5 )
		
		self.f2s_BtnActualizar = wx.Button( self, wx.ID_ANY, u"Actualizar", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.f2s_BtnActualizar.Enable( False )
		
		fgSizer1.Add( self.f2s_BtnActualizar, 0, wx.ALL, 5 )
		
		self.StaticText2 = wx.StaticText( self, wx.ID_ANY, u"Nuevo", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.StaticText2.Wrap( -1 )
		fgSizer1.Add( self.StaticText2, 0, wx.ALL, 5 )
		
		self.f2s_nuevoNombre = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
		fgSizer1.Add( self.f2s_nuevoNombre, 0, wx.ALL, 5 )
		
		self.f2s_btnNuevo = wx.Button( self, wx.ID_ANY, u"Nuevo", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.f2s_btnNuevo, 0, wx.ALL, 5 )
		
		bSizer1.Add( fgSizer1, 0, wx.EXPAND, 5 )
		
		self.f2s_gauge1 = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.Size( 450,-1 ), wx.GA_HORIZONTAL )
		bSizer1.Add( self.f2s_gauge1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

