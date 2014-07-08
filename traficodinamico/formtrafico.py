# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Oct  8 2012)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class f2s_DiagTextoTrafico
###########################################################################

class f2s_DiagTextoTrafico ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Texto Trafico", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		self.m_staticText5.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer1.Add( self.m_staticText5, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		fgSizer1 = wx.FlexGridSizer( 0, 5, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Posicion:", wx.DefaultPosition, wx.Size( 80,-1 ), 0|wx.RAISED_BORDER )
		self.m_staticText7.Wrap( -1 )
		self.m_staticText7.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.m_staticText7.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		
		fgSizer1.Add( self.m_staticText7, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"X", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		fgSizer1.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.f2s_posX = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.f2s_posX, 0, wx.ALL, 5 )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Y", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		fgSizer1.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.f2s_posY = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.f2s_posY, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( fgSizer1, 0, wx.EXPAND, 5 )
		
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Texto Traf.:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		bSizer2.Add( self.m_staticText3, 0, wx.ALL, 5 )
		
		self.f2s_Texto = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,-1 ), 0 )
		bSizer2.Add( self.f2s_Texto, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer2, 0, wx.EXPAND, 5 )
		
		fgSizer2 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Alto Font", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.m_staticText6.Wrap( -1 )
		fgSizer2.Add( self.m_staticText6, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.f2s_AltoFont = wx.TextCtrl( self, wx.ID_ANY, u"10", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.f2s_AltoFont, 0, wx.ALL, 5 )
		
		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"% de Gris", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		fgSizer2.Add( self.m_staticText11, 0, wx.ALL, 5 )
		
		self.m_slider1 = wx.Slider( self, wx.ID_ANY, 0, 0, 90, wx.DefaultPosition, wx.Size( 240,-1 ), wx.SL_HORIZONTAL|wx.SL_LABELS )
		fgSizer2.Add( self.m_slider1, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( fgSizer2, 0, wx.EXPAND, 5 )
		
		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.f2s_BtnAceptar = wx.Button( self, wx.ID_ANY, u"Aceptar", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.f2s_BtnAceptar, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.f2s_BtnCancelar = wx.Button( self, wx.ID_ANY, u"Cancelar", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.f2s_BtnCancelar, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer1.Add( gSizer1, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		bSizer1.Fit( self )
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class FormGeneral
###########################################################################

class FormGeneral ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,500 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_notebook1 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel1 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer41 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText7 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Ambiente", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		bSizer5.Add( self.m_staticText7, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.f2s_FileAmbiente = wx.FilePickerCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.amb", wx.DefaultPosition, wx.Size( 400,-1 ), wx.FLP_DEFAULT_STYLE )
		self.f2s_FileAmbiente.SetMinSize( wx.Size( 400,30 ) )
		
		bSizer5.Add( self.f2s_FileAmbiente, 0, wx.ALL, 5 )
		
		
		bSizer41.Add( bSizer5, 0, wx.EXPAND, 5 )
		
		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.f2s_TreeManejo = wx.TreeCtrl( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.Size( 300,250 ), wx.TR_DEFAULT_STYLE )
		bSizer6.Add( self.f2s_TreeManejo, 0, wx.ALL, 5 )
		
		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel1, wx.ID_ANY, u"Nodos" ), wx.VERTICAL )
		
		self.f2s_BtnNuevaCopia = wx.Button( self.m_panel1, wx.ID_ANY, u"Copia Adicional", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer1.Add( self.f2s_BtnNuevaCopia, 0, wx.ALL, 5 )
		
		self.m_staticline1 = wx.StaticLine( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		sbSizer1.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.f2s_AdicionTexto = wx.Button( self.m_panel1, wx.ID_ANY, u"Adicionar Texto", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer1.Add( self.f2s_AdicionTexto, 0, wx.ALL, 5 )
		
		sbSizer6 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel1, wx.ID_ANY, u"Campos" ), wx.VERTICAL )
		
		self.f2s_BtnEditar = wx.Button( self.m_panel1, wx.ID_ANY, u"Editar", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer6.Add( self.f2s_BtnEditar, 0, wx.ALL, 5 )
		
		self.f2s_BtnBorrar = wx.Button( self.m_panel1, wx.ID_ANY, u"Borrar", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer6.Add( self.f2s_BtnBorrar, 0, wx.ALL, 5 )
		
		
		sbSizer1.Add( sbSizer6, 1, wx.EXPAND, 0 )
		
		
		bSizer6.Add( sbSizer1, 1, wx.EXPAND, 5 )
		
		
		bSizer41.Add( bSizer6, 0, wx.EXPAND, 5 )
		
		sbSizer7 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel1, wx.ID_ANY, u"label" ), wx.HORIZONTAL )
		
		self.m_staticText8 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Orden", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )
		sbSizer7.Add( self.m_staticText8, 0, wx.ALL, 5 )
		
		f2s_ChOrdenChoices = []
		self.f2s_ChOrden = wx.Choice( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.Size( 170,-1 ), f2s_ChOrdenChoices, 0 )
		self.f2s_ChOrden.SetSelection( 0 )
		sbSizer7.Add( self.f2s_ChOrden, 0, wx.ALL, 5 )
		
		self.label = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Control", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label.Wrap( -1 )
		sbSizer7.Add( self.label, 0, wx.ALL, 5 )
		
		f2s_ChControlChoices = []
		self.f2s_ChControl = wx.Choice( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.Size( 170,-1 ), f2s_ChControlChoices, 0 )
		self.f2s_ChControl.SetSelection( 0 )
		sbSizer7.Add( self.f2s_ChControl, 0, wx.ALL, 5 )
		
		
		bSizer41.Add( sbSizer7, 1, wx.EXPAND, 5 )
		
		self.f2s_BtnGuardar = wx.Button( self.m_panel1, wx.ID_ANY, u"Guardar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer41.Add( self.f2s_BtnGuardar, 0, wx.ALL, 5 )
		
		
		self.m_panel1.SetSizer( bSizer41 )
		self.m_panel1.Layout()
		bSizer41.Fit( self.m_panel1 )
		self.m_notebook1.AddPage( self.m_panel1, u"General", False )
		
		bSizer4.Add( self.m_notebook1, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer4 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

