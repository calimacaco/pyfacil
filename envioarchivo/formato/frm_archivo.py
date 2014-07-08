# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Sep  8 2010)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.aui

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 555,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_auinotebook1 = wx.aui.AuiNotebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.aui.AUI_NB_DEFAULT_STYLE )
		self.Panel1 = wx.Panel( self.m_auinotebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer1 = wx.GridSizer( 4, 2, 10, 0 )
		
		self.m_staticText1 = wx.StaticText( self.Panel1, wx.ID_ANY, u"Servicio", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		gSizer1.Add( self.m_staticText1, 0, wx.ALL, 5 )
		
		self.m_textCtrl1 = wx.TextCtrl( self.Panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_textCtrl1, 140, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText4 = wx.StaticText( self.Panel1, wx.ID_ANY, u"Ruta", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		gSizer1.Add( self.m_staticText4, 0, wx.ALL, 5 )
		
		self.m_textCtrl2 = wx.TextCtrl( self.Panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_textCtrl2, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText5 = wx.StaticText( self.Panel1, wx.ID_ANY, u"Impresora", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		gSizer1.Add( self.m_staticText5, 0, wx.ALL, 5 )
		
		self.m_textCtrl3 = wx.TextCtrl( self.Panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_textCtrl3, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_button1 = wx.Button( self.Panel1, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_button1, 0, wx.ALL, 5 )
		
		self.m_button2 = wx.Button( self.Panel1, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_button2, 0, wx.ALL, 5 )
		
		self.Panel1.SetSizer( gSizer1 )
		self.Panel1.Layout()
		gSizer1.Fit( self.Panel1 )
		self.m_auinotebook1.AddPage( self.Panel1, u"Configuracion", False, wx.NullBitmap )
		
		bSizer1.Add( self.m_auinotebook1, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.SetSizer( bSizer1 )
		self.Layout()
		self.m_statusBar1 = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.m_menu11 = wx.Menu()
		self.m_menu1.AppendSubMenu( self.m_menu11, u"MyMenu" )
		
		self.m_menubar1.Append( self.m_menu1, u"MyMenu" ) 
		
		self.SetMenuBar( self.m_menubar1 )
		
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

