# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun  6 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.propgrid as pg

###########################################################################
## Class FrameGeneral
###########################################################################

class FrameGeneral ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 600,500 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.f2s_menuTamPapel = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Configuración Pagina", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.AppendItem( self.f2s_menuTamPapel )
		
		self.m_menuItem3 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.AppendItem( self.m_menuItem3 )
		
		self.m_menuItem4 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.AppendItem( self.m_menuItem4 )
		
		self.m_menuItem5 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.AppendItem( self.m_menuItem5 )
		
		self.m_menu1.AppendSeparator()
		
		self.m_menubar1.Append( self.m_menu1, u"Archivo" ) 
		
		self.SetMenuBar( self.m_menubar1 )
		
		self.m_toolBar1 = self.CreateToolBar( wx.TB_HORIZONTAL, wx.ID_ANY ) 
		self.m_tool2 = self.m_toolBar1.AddLabelTool( wx.ID_ANY, u"tool", wx.ArtProvider.GetBitmap( wx.ART_HELP_SIDE_PANEL, wx.ART_TOOLBAR ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.m_tool3 = self.m_toolBar1.AddLabelTool( wx.ID_ANY, u"tool", wx.ArtProvider.GetBitmap( wx.ART_FILE_SAVE, wx.ART_TOOLBAR ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.m_toolBar1.AddSeparator()
		
		self.m_toolBar1.Realize() 
		
		self.m_statusBar1 = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.topPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SIMPLE_BORDER|wx.TAB_TRAVERSAL )
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_splitter1 = wx.SplitterWindow( self.topPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D )
		self.m_splitter1.Bind( wx.EVT_IDLE, self.m_splitter1OnIdle )
		
		self.m_panel2 = wx.Panel( self.m_splitter1, wx.ID_ANY, wx.DefaultPosition, wx.Size( 20,20 ), wx.TAB_TRAVERSAL )
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_splitter2 = wx.SplitterWindow( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D )
		self.m_splitter2.Bind( wx.EVT_IDLE, self.m_splitter2OnIdle )
		
		self.f2s_panelObjetos = wx.Panel( self.m_splitter2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.f2s_panelObjetos.SetBackgroundColour( wx.Colour( 246, 130, 68 ) )
		
		bSizer6 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_notebook3 = wx.Notebook( self.f2s_panelObjetos, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel6 = wx.Panel( self.m_notebook3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_treeCtrl2 = wx.TreeCtrl( self.m_panel6, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_DEFAULT_STYLE )
		bSizer7.Add( self.m_treeCtrl2, 0, wx.ALL, 5 )
		
		
		self.m_panel6.SetSizer( bSizer7 )
		self.m_panel6.Layout()
		bSizer7.Fit( self.m_panel6 )
		self.m_notebook3.AddPage( self.m_panel6, u"Texto", False )
		self.m_panel8 = wx.Panel( self.m_notebook3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_notebook3.AddPage( self.m_panel8, u"funciones", False )
		
		bSizer6.Add( self.m_notebook3, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.f2s_panelObjetos.SetSizer( bSizer6 )
		self.f2s_panelObjetos.Layout()
		bSizer6.Fit( self.f2s_panelObjetos )
		self.m_panel5 = wx.Panel( self.m_splitter2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		self.f2s_GridTexto = pg.PropertyGrid(self.m_panel5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.propgrid.PG_DEFAULT_STYLE|wx.ALWAYS_SHOW_SB)
		self.f2s_GridTextoID = self.f2s_GridTexto.Append( pg.StringProperty( u"Id.", u"Id." ) ) 
		self.f2s_GridTextoFont = self.f2s_GridTexto.Append( pg.FontProperty( u"Font", u"Font" ) ) 
		self.f2s_GridTextoColor = self.f2s_GridTexto.Append( pg.ColourProperty( u"Color", u"Color" ) ) 
		self.f2s_GridTextoAlinear = self.f2s_GridTexto.Append( pg.MultiChoiceProperty( u"Alinear", u"Alinear" ) ) 
		bSizer5.Add( self.f2s_GridTexto, 0, wx.ALL, 0 )
		
		bSizer10 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button3 = wx.Button( self.m_panel5, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_button3, 0, wx.ALL, 5 )
		
		self.m_button4 = wx.Button( self.m_panel5, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_button4, 0, wx.ALL, 5 )
		
		
		bSizer5.Add( bSizer10, 1, wx.EXPAND, 5 )
		
		
		self.m_panel5.SetSizer( bSizer5 )
		self.m_panel5.Layout()
		bSizer5.Fit( self.m_panel5 )
		self.m_splitter2.SplitHorizontally( self.f2s_panelObjetos, self.m_panel5, 0 )
		bSizer4.Add( self.m_splitter2, 1, wx.EXPAND, 5 )
		
		
		self.m_panel2.SetSizer( bSizer4 )
		self.m_panel2.Layout()
		self.f2s_Pizarra = wx.ScrolledWindow( self.m_splitter1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.f2s_Pizarra.SetScrollRate( 5, 5 )
		bSizer9 = wx.BoxSizer( wx.VERTICAL )
		
		
		self.f2s_Pizarra.SetSizer( bSizer9 )
		self.f2s_Pizarra.Layout()
		bSizer9.Fit( self.f2s_Pizarra )
		self.m_splitter1.SplitVertically( self.m_panel2, self.f2s_Pizarra, 226 )
		bSizer2.Add( self.m_splitter1, 1, wx.EXPAND, 5 )
		
		
		self.topPanel.SetSizer( bSizer2 )
		self.topPanel.Layout()
		bSizer2.Fit( self.topPanel )
		bSizer1.Add( self.topPanel, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	
	def m_splitter1OnIdle( self, event ):
		self.m_splitter1.SetSashPosition( 226 )
		self.m_splitter1.Unbind( wx.EVT_IDLE )
	
	def m_splitter2OnIdle( self, event ):
		self.m_splitter2.SetSashPosition( 0 )
		self.m_splitter2.Unbind( wx.EVT_IDLE )
	

###########################################################################
## Class f2s_DialogPapel
###########################################################################

class f2s_DialogPapel ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Definición Papel", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer2 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Tamaño de Papel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		fgSizer2.Add( self.m_staticText1, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		f2s_tamPapelChoices = []
		self.f2s_tamPapel = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 150,28 ), f2s_tamPapelChoices, 0 )
		self.f2s_tamPapel.SetSelection( 0 )
		fgSizer2.Add( self.f2s_tamPapel, 0, wx.ALL, 5 )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Orientación", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		fgSizer2.Add( self.m_staticText2, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		f2s_orientacionChoices = []
		self.f2s_orientacion = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 150,28 ), f2s_orientacionChoices, 0 )
		self.f2s_orientacion.SetSelection( 0 )
		fgSizer2.Add( self.f2s_orientacion, 0, wx.ALL, 5 )
		
		
		bSizer3.Add( fgSizer2, 1, wx.EXPAND, 5 )
		
		gSizer3 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.f2s_Cancelar = wx.Button( self, wx.ID_ANY, u"Cancelar", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.f2s_Cancelar, 0, wx.ALL, 5 )
		
		self.f2s_aceptar = wx.Button( self, wx.ID_ANY, u"Aceptar", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.f2s_aceptar, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		
		bSizer3.Add( gSizer3, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer3 )
		self.Layout()
		bSizer3.Fit( self )
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

