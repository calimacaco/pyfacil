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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,350 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Generador ambiente Separación Spool", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		self.m_staticText1.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer1.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.Sel_Archivo = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.Size( 300,-1 ), wx.FLP_DEFAULT_STYLE )
		self.Sel_Archivo.SetMinSize( wx.Size( 300,30 ) )
		
		bSizer3.Add( self.Sel_Archivo, 0, wx.ALL, 5 )
		
		self.Btn_Abrir = wx.Button( self, wx.ID_ANY, u"Abrir", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.Btn_Abrir, 0, wx.ALL, 5 )
		
		bSizer1.Add( bSizer3, 1, wx.EXPAND, 5 )
		
		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"  Encabezado  " ), wx.VERTICAL )
		
		fgSizer1 = wx.FlexGridSizer( 2, 2, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Texto a Buscar", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		fgSizer1.Add( self.m_staticText2, 0, wx.ALL, 5 )
		
		self.Txt_Buscar = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
		fgSizer1.Add( self.Txt_Buscar, 0, wx.ALL, 5 )
		
		sbSizer2.Add( fgSizer1, 0, wx.EXPAND, 5 )
		
		fgSizer4 = wx.FlexGridSizer( 1, 5, 0, 0 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		
		fgSizer4.AddSpacer( ( 75, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Fila", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		fgSizer4.Add( self.m_staticText3, 0, wx.ALL, 5 )
		
		self.Txt_BusFila = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.Txt_BusFila, 0, wx.ALL, 5 )
		
		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Columna", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		fgSizer4.Add( self.m_staticText4, 0, wx.ALL, 5 )
		
		self.Txt_BusColumna = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.Txt_BusColumna, 0, wx.ALL, 5 )
		
		sbSizer2.Add( fgSizer4, 1, wx.EXPAND, 5 )
		
		bSizer1.Add( sbSizer2, 0, wx.EXPAND, 5 )
		
		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"  Selección campo nombre archivo  " ), wx.VERTICAL )
		
		fgSizer3 = wx.FlexGridSizer( 1, 6, 0, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Fila", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		fgSizer3.Add( self.m_staticText6, 0, wx.ALL, 5 )
		
		self.Txt_NomFila = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.Txt_NomFila, 0, wx.ALL, 5 )
		
		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Columna", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		fgSizer3.Add( self.m_staticText7, 0, wx.ALL, 5 )
		
		self.Txt_NomColumna = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.Txt_NomColumna, 0, wx.ALL, 5 )
		
		self.m_staticText71 = wx.StaticText( self, wx.ID_ANY, u"Col. Final", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText71.Wrap( -1 )
		fgSizer3.Add( self.m_staticText71, 0, wx.ALL, 5 )
		
		self.Txt_NomColFin = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.Txt_NomColFin, 0, wx.ALL, 5 )
		
		sbSizer3.Add( fgSizer3, 0, wx.EXPAND, 5 )
		
		bSizer1.Add( sbSizer3, 0, wx.EXPAND, 8 )
		
		sbSizer4 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"  Ruta de almacenamiento  " ), wx.VERTICAL )
		
		self.Txt_RutaGuardar = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 475,-1 ), 0 )
		sbSizer4.Add( self.Txt_RutaGuardar, 0, wx.ALL, 5 )
		
		bSizer1.Add( sbSizer4, 0, wx.EXPAND, 5 )
		
		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
		
		
		bSizer4.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.Btn_Guardar = wx.Button( self, wx.ID_ANY, u"Guardar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.Btn_Guardar, 0, wx.ALL, 5 )
		
		bSizer1.Add( bSizer4, 1, wx.EXPAND, 5 )
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

