# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Sep  8 2010)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx

###########################################################################
## Class FramePal
###########################################################################

class FramePal ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 560,233 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		gbSizer1 = wx.GridBagSizer( 0, 0 )
		gbSizer1.SetFlexibleDirection( wx.BOTH )
		gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"grupo", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		gbSizer1.Add( self.m_staticText1, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_choice1Choices = []
		self.m_choice1 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 350,-1 ), m_choice1Choices, 0 )
		self.m_choice1.SetSelection( 0 )
		gbSizer1.Add( self.m_choice1, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.f2s_AddGrupo = wx.Button( self, wx.ID_ANY, u"Adicionar", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer1.Add( self.f2s_AddGrupo, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		bSizer1.Add( gbSizer1, 0, wx.EXPAND, 5 )
		
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Campos", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		bSizer1.Add( self.m_staticText3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		fgSizer1 = wx.FlexGridSizer( 1, 3, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl1.SetMinSize( wx.Size( 150,-1 ) )
		
		fgSizer1.Add( self.m_textCtrl1, 0, wx.ALL, 5 )
		
		self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl2.SetMinSize( wx.Size( 150,-1 ) )
		
		fgSizer1.Add( self.m_textCtrl2, 0, wx.ALL, 5 )
		
		self.m_textCtrl3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl3.SetMinSize( wx.Size( 220,-1 ) )
		
		fgSizer1.Add( self.m_textCtrl3, 0, wx.ALL, 5 )
		
		self.f2s_addCampo = wx.Button( self, wx.ID_ANY, u"Adicionar", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.f2s_addCampo, 0, wx.ALL, 5 )
		
		self.f2s_btnBorrar = wx.Button( self, wx.ID_ANY, u"Borrar", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.f2s_btnBorrar, 0, wx.ALL, 5 )
		
		bSizer1.Add( fgSizer1, 0, wx.EXPAND, 5 )
		
		gSizer3 = wx.GridSizer( 2, 5, 0, 0 )
		
		self.f2s_primero = wx.Button( self, wx.ID_ANY, u"|<", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.f2s_primero, 0, wx.ALL, 5 )
		
		self.f2s_btnAnterior = wx.Button( self, wx.ID_ANY, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.f2s_btnAnterior, 0, wx.ALL, 5 )
		
		self.m_staticText31 = wx.StaticText( self, wx.ID_ANY, u"0/0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText31.Wrap( -1 )
		gSizer3.Add( self.m_staticText31, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.f2s_btnSiguiente = wx.Button( self, wx.ID_ANY, u">", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.f2s_btnSiguiente, 0, wx.ALL, 5 )
		
		self.f2s_btnUltimo = wx.Button( self, wx.ID_ANY, u">|", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.f2s_btnUltimo, 0, wx.ALL, 5 )
		
		bSizer1.Add( gSizer3, 0, wx.EXPAND, 5 )
		
		self.SetSizer( bSizer1 )
		self.Layout()
	
	def __del__( self ):
		pass
	

