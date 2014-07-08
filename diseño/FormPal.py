# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun  6 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.aui
import wx.propgrid as pg

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_splitter1 = wx.SplitterWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D )
		self.m_splitter1.Bind( wx.EVT_IDLE, self.m_splitter1OnIdle )
		
		self.m_panel6 = wx.Panel( self.m_splitter1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer6 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_notebook3 = wx.Notebook( self.m_panel6, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel8 = wx.Panel( self.m_notebook3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_treeCtrl1 = wx.TreeCtrl( self.m_panel8, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_DEFAULT_STYLE )
		bSizer7.Add( self.m_treeCtrl1, 0, wx.ALL, 5 )
		
		
		self.m_panel8.SetSizer( bSizer7 )
		self.m_panel8.Layout()
		bSizer7.Fit( self.m_panel8 )
		self.m_notebook3.AddPage( self.m_panel8, u"Objetos", True )
		self.m_panel9 = wx.Panel( self.m_notebook3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_notebook3.AddPage( self.m_panel9, u"Datos", False )
		
		bSizer6.Add( self.m_notebook3, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.m_panel6.SetSizer( bSizer6 )
		self.m_panel6.Layout()
		bSizer6.Fit( self.m_panel6 )
		self.m_panel7 = wx.Panel( self.m_splitter1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_scrolledWindow5 = wx.ScrolledWindow( self.m_panel7, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.ALWAYS_SHOW_SB|wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow5.SetScrollRate( 5, 5 )
		bSizer5.Add( self.m_scrolledWindow5, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.m_panel7.SetSizer( bSizer5 )
		self.m_panel7.Layout()
		bSizer5.Fit( self.m_panel7 )
		self.m_splitter1.SplitVertically( self.m_panel6, self.m_panel7, 0 )
		bSizer1.Add( self.m_splitter1, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		self.m_statusBar1 = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menuArc = wx.Menu()
		self.f2s_menuSalir = wx.MenuItem( self.m_menuArc, wx.ID_ANY, u"Salir"+ u"\t" + u"CTRL X", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuArc.AppendItem( self.f2s_menuSalir )
		
		self.m_menubar1.Append( self.m_menuArc, u"Archivo" ) 
		
		self.SetMenuBar( self.m_menubar1 )
		
		self.m_auiToolBar1 = wx.aui.AuiToolBar( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.aui.AUI_TB_HORZ_LAYOUT ) 
		self.m_tool1 = self.m_auiToolBar1.AddTool( wx.ID_ANY, u"tool", wx.NullBitmap, wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.m_auiToolBar1.AddSeparator()
		
		self.m_tool2 = self.m_auiToolBar1.AddTool( wx.ID_ANY, u"tool", wx.NullBitmap, wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.m_auiToolBar1.Realize() 
		
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	
	def m_splitter1OnIdle( self, event ):
		self.m_splitter1.SetSashPosition( 0 )
		self.m_splitter1.Unbind( wx.EVT_IDLE )
	

###########################################################################
## Class f2s_DiagTexto
###########################################################################

class f2s_DiagTexto ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetFont( wx.Font( 11, 74, 90, 90, False, "Sans" ) )
		
		bSizer8 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_propertyGrid1 = pg.PropertyGrid(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.propgrid.PG_DEFAULT_STYLE|wx.ALWAYS_SHOW_SB|wx.HSCROLL|wx.RAISED_BORDER|wx.VSCROLL)
		bSizer8.Add( self.m_propertyGrid1, 0, wx.ALL, 5 )
		
		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button2 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.m_button2, 0, wx.ALL, 5 )
		
		self.m_button3 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.m_button3, 0, wx.ALL, 5 )
		
		self.m_button4 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.m_button4, 0, wx.ALL, 5 )
		
		
		bSizer8.Add( bSizer9, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer8 )
		self.Layout()
		bSizer8.Fit( self )
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

