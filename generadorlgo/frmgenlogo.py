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
## Class f2s_framepal
###########################################################################

class f2s_framepal ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.f2s_menu_abrir = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Abrir Imagen", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.AppendItem( self.f2s_menu_abrir )
		
		self.f2s_menu_convert = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Convertir", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.AppendItem( self.f2s_menu_convert )
		
		self.m_menu1.AppendSeparator()
		
		self.f2s_menu_salir = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Salir", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.AppendItem( self.f2s_menu_salir )
		
		self.m_menubar1.Append( self.m_menu1, u"Archivo" ) 
		
		self.SetMenuBar( self.m_menubar1 )
		
		self.m_statusBar1 = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Imagen de entrada", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		fgSizer1.Add( self.m_staticText1, 0, wx.ALL, 5 )
		
		self.f2s_fpick_Imagen = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"Archivos de imagen |*.png;*.gif;*.bmp;*.jpg|", wx.DefaultPosition, wx.Size( 300,-1 ), wx.FLP_CHANGE_DIR|wx.FLP_DEFAULT_STYLE|wx.FLP_FILE_MUST_EXIST|wx.FLP_OPEN )
		self.f2s_fpick_Imagen.SetMinSize( wx.Size( 340,40 ) )
		
		fgSizer1.Add( self.f2s_fpick_Imagen, 0, wx.ALL, 5 )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"LGO de salida", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		fgSizer1.Add( self.m_staticText2, 0, wx.ALL, 5 )
		
		self.f2s_fpick_salida = wx.FilePickerCtrl( self, wx.ID_ANY, u"/home/marco/workspace/genesis/generadorlgo/sssss", u"Seleccione archivo", u"*.lgo", wx.DefaultPosition, wx.DefaultSize, wx.FLP_CHANGE_DIR|wx.FLP_OPEN )
		self.f2s_fpick_salida.SetMinSize( wx.Size( 340,40 ) )
		
		fgSizer1.Add( self.f2s_fpick_salida, 0, wx.ALL, 5 )
		
		self.m_checkBox1 = wx.CheckBox( self, wx.ID_ANY, u"Brillo", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_checkBox1, 0, wx.ALL, 5 )
		
		self.m_slider1 = wx.Slider( self, wx.ID_ANY, 0, 0, 100, wx.DefaultPosition, wx.Size( 200,-1 ), wx.SL_HORIZONTAL )
		fgSizer1.Add( self.m_slider1, 0, wx.ALL, 5 )
		
		self.m_checkBox2 = wx.CheckBox( self, wx.ID_ANY, u"Tamaño", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_checkBox2, 0, wx.ALL, 5 )
		
		self.m_slider2 = wx.Slider( self, wx.ID_ANY, 0, 0, 100, wx.DefaultPosition, wx.Size( 200,-1 ), wx.SL_HORIZONTAL )
		fgSizer1.Add( self.m_slider2, 0, wx.ALL, 5 )
		
		self.f2s_btn_Convertir = wx.Button( self, wx.ID_ANY, u"Convertir", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.f2s_btn_Convertir, 0, wx.ALL, 5 )
		
		
		self.SetSizer( fgSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

