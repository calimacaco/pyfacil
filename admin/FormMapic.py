# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Sep  8 2010)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.html

ID_Plano = 1000
ID_VerUsuario = 1001
ID_ConfigCorreo = 1002
ID_Veradjuntos = 1003
ID_Atras = 1004
ID_Adelante = 1005
ID_Adicionar = 1006
ID_Editar = 1007
ID_ExportCSV = 1008

###########################################################################
## Class FrameGeneral
###########################################################################

class FrameGeneral ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetExtraStyle( wx.FRAME_EX_METAL )
		
		self.m_statusBar1 = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.m_Abrir = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Manejo Base Datos"+ u"\t" + u"CTRL-O", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.AppendItem( self.m_Abrir )
		
		self.f2s_menuRecientes = wx.Menu()
		self.m_menu1.AppendSubMenu( self.f2s_menuRecientes, u"Recientes" )
		
		self.m_menu1.AppendSeparator()
		
		self.m_generales = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Configuracion", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.AppendItem( self.m_generales )
		self.m_generales.Enable( False )
		
		self.m_menu1.AppendSeparator()
		
		self.m_Salir = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Salir", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.AppendItem( self.m_Salir )
		
		self.m_menubar1.Append( self.m_menu1, u"General" ) 
		
		self.m_menu4 = wx.Menu()
		self.m_SubrirPlano = wx.MenuItem( self.m_menu4, ID_Plano, u"Subir Plano", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu4.AppendItem( self.m_SubrirPlano )
		self.m_SubrirPlano.Enable( False )
		
		self.m_menu4.AppendSeparator()
		
		self.m_Verusr = wx.MenuItem( self.m_menu4, ID_VerUsuario, u"Ver Usuarios", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu4.AppendItem( self.m_Verusr )
		self.m_Verusr.Enable( False )
		
		self.m_menubar1.Append( self.m_menu4, u"Usuarios" ) 
		
		self.m_menu2 = wx.Menu()
		self.m_configCorreo = wx.MenuItem( self.m_menu2, ID_ConfigCorreo, u"Configurar", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.AppendItem( self.m_configCorreo )
		self.m_configCorreo.Enable( False )
		
		self.m_menu2.AppendSeparator()
		
		self.m_VerEstado = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"Estado", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.AppendItem( self.m_VerEstado )
		self.m_VerEstado.Enable( False )
		
		self.m_menubar1.Append( self.m_menu2, u"Correo" ) 
		
		self.m_menu5 = wx.Menu()
		self.m_GenPCL = wx.MenuItem( self.m_menu5, wx.ID_ANY, u"Generar Adjuntos"+ u"\t" + u"CTRL-G", u"Generador de Adjuntos PCL", wx.ITEM_NORMAL )
		self.m_menu5.AppendItem( self.m_GenPCL )
		self.m_GenPCL.Enable( False )
		
		self.m_menu5.AppendSeparator()
		
		self.m_veradjuntos = wx.MenuItem( self.m_menu5, ID_Veradjuntos, u"Ver Adjuntos", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu5.AppendItem( self.m_veradjuntos )
		self.m_veradjuntos.Enable( False )
		
		self.m_menubar1.Append( self.m_menu5, u"Adjuntos" ) 
		
		self.m_menu51 = wx.Menu()
		self.m_confEnvioArchivo = wx.MenuItem( self.m_menu51, wx.ID_ANY, u"Configuracion", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu51.AppendItem( self.m_confEnvioArchivo )
		self.m_confEnvioArchivo.Enable( False )
		
		self.m_estadoArchivo = wx.MenuItem( self.m_menu51, wx.ID_ANY, u"Estado", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu51.AppendItem( self.m_estadoArchivo )
		self.m_estadoArchivo.Enable( False )
		
		self.m_menubar1.Append( self.m_menu51, u"Envio Archivo" ) 
		
		self.SetMenuBar( self.m_menubar1 )
		
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_bpButton1 = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"imagenes/fondo.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer7.Add( self.m_bpButton1, 0, wx.ALL, 5 )
		
		self.SetSizer( bSizer7 )
		self.Layout()
		bSizer7.Fit( self )
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class D_Generales
###########################################################################

class D_Generales ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Generales", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer35 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_notebook2 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel9 = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer351 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer9 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel9, wx.ID_ANY, u"Rutas" ), wx.VERTICAL )
		
		fgSizer15 = wx.FlexGridSizer( 2, 3, 0, 0 )
		fgSizer15.SetFlexibleDirection( wx.BOTH )
		fgSizer15.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText36 = wx.StaticText( self.m_panel9, wx.ID_ANY, u"Ruta Modelos", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText36.Wrap( -1 )
		fgSizer15.Add( self.m_staticText36, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.f2s_dirModelos = wx.DirPickerCtrl( self.m_panel9, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.Size( 320,-1 ), wx.DIRP_DEFAULT_STYLE )
		self.f2s_dirModelos.SetMinSize( wx.Size( 320,30 ) )
		
		fgSizer15.Add( self.f2s_dirModelos, 0, wx.ALL, 5 )
		
		sbSizer9.Add( fgSizer15, 1, wx.EXPAND, 5 )
		
		self.m_staticText37 = wx.StaticText( self.m_panel9, wx.ID_ANY, u"Ambientes Disponibles", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText37.Wrap( -1 )
		sbSizer9.Add( self.m_staticText37, 0, wx.ALL, 5 )
		
		self.f2s_LstAmbientes = wx.ListCtrl( self.m_panel9, wx.ID_ANY, wx.DefaultPosition, wx.Size( 430,-1 ), wx.LC_HRULES|wx.LC_REPORT|wx.ALWAYS_SHOW_SB )
		sbSizer9.Add( self.f2s_LstAmbientes, 0, wx.ALL, 5 )
		
		bSizer351.Add( sbSizer9, 1, wx.EXPAND, 5 )
		
		bSizer36 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer351.Add( bSizer36, 1, wx.EXPAND, 5 )
		
		self.m_panel9.SetSizer( bSizer351 )
		self.m_panel9.Layout()
		bSizer351.Fit( self.m_panel9 )
		self.m_notebook2.AddPage( self.m_panel9, u"Modelos", True )
		self.m_panel10 = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer37 = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer16 = wx.FlexGridSizer( 2, 2, 0, 0 )
		fgSizer16.SetFlexibleDirection( wx.BOTH )
		fgSizer16.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText41 = wx.StaticText( self.m_panel10, wx.ID_ANY, u"Envio Archivo", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText41.Wrap( -1 )
		fgSizer16.Add( self.m_staticText41, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.f2s_DirArchivo = wx.DirPickerCtrl( self.m_panel10, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.Size( 300,-1 ), wx.DIRP_DEFAULT_STYLE )
		self.f2s_DirArchivo.SetMinSize( wx.Size( 300,30 ) )
		
		fgSizer16.Add( self.f2s_DirArchivo, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText42 = wx.StaticText( self.m_panel10, wx.ID_ANY, u"Envio Correo", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText42.Wrap( -1 )
		fgSizer16.Add( self.m_staticText42, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.f2s_dirCorreo = wx.DirPickerCtrl( self.m_panel10, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.Size( 300,-1 ), wx.DIRP_DEFAULT_STYLE )
		self.f2s_dirCorreo.SetMinSize( wx.Size( 300,30 ) )
		
		fgSizer16.Add( self.f2s_dirCorreo, 0, wx.ALL, 5 )
		
		bSizer37.Add( fgSizer16, 1, wx.EXPAND, 10 )
		
		self.m_panel10.SetSizer( bSizer37 )
		self.m_panel10.Layout()
		bSizer37.Fit( self.m_panel10 )
		self.m_notebook2.AddPage( self.m_panel10, u"Programas", False )
		
		bSizer35.Add( self.m_notebook2, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.f2s_BtnGuadar = wx.Button( self, wx.ID_ANY, u"Guardar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer35.Add( self.f2s_BtnGuadar, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.f2s_btnCancelar = wx.Button( self, wx.ID_ANY, u"Salir", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer35.Add( self.f2s_btnCancelar, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.SetSizer( bSizer35 )
		self.Layout()
		bSizer35.Fit( self )
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class D_GenerarPDF
###########################################################################

class D_GenerarPDF ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer14 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel8 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer6 = wx.FlexGridSizer( 2, 2, 0, 0 )
		fgSizer6.SetFlexibleDirection( wx.BOTH )
		fgSizer6.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText11 = wx.StaticText( self.m_panel8, wx.ID_ANY, u"Ruta de Busqueda", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		fgSizer6.Add( self.m_staticText11, 0, wx.ALL, 5 )
		
		self.dir_PDF = wx.DirPickerCtrl( self.m_panel8, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.Size( 200,-1 ), wx.DIRP_DEFAULT_STYLE )
		self.dir_PDF.SetMinSize( wx.Size( 300,30 ) )
		
		fgSizer6.Add( self.dir_PDF, 0, wx.ALL, 5 )
		
		self.m_staticText15 = wx.StaticText( self.m_panel8, wx.ID_ANY, u"Ruta Salida", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )
		fgSizer6.Add( self.m_staticText15, 0, wx.ALL, 5 )
		
		self.Dir_Salida = wx.DirPickerCtrl( self.m_panel8, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		self.Dir_Salida.SetMinSize( wx.Size( 300,30 ) )
		
		fgSizer6.Add( self.Dir_Salida, 0, wx.ALL, 5 )
		
		self.m_staticText19 = wx.StaticText( self.m_panel8, wx.ID_ANY, u"Arch. x Carpeta", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )
		fgSizer6.Add( self.m_staticText19, 0, wx.ALL, 5 )
		
		self.Txt_NroArchivos = wx.TextCtrl( self.m_panel8, wx.ID_ANY, u"5000", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer6.Add( self.Txt_NroArchivos, 0, wx.ALL, 5 )
		
		
		fgSizer6.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.Btn_GenerarPCL = wx.Button( self.m_panel8, wx.ID_ANY, u"Procesar", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer6.Add( self.Btn_GenerarPCL, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_panel8.SetSizer( fgSizer6 )
		self.m_panel8.Layout()
		fgSizer6.Fit( self.m_panel8 )
		bSizer14.Add( self.m_panel8, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer16 = wx.BoxSizer( wx.VERTICAL )
		
		self.Txt_Mensaje = wx.TextCtrl( self, wx.ID_ANY, u"En Espera..\n", wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.TE_MULTILINE|wx.HSCROLL|wx.VSCROLL )
		self.Txt_Mensaje.SetMinSize( wx.Size( 470,180 ) )
		
		bSizer16.Add( self.Txt_Mensaje, 0, wx.ALL, 5 )
		
		bSizer25 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.Btn_Resultado = wx.Button( self, wx.ID_ANY, u"Ver Resultado", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer25.Add( self.Btn_Resultado, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer25.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.Btn_BorrarResultado = wx.Button( self, wx.ID_ANY, u"Borrar Resultado", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer25.Add( self.Btn_BorrarResultado, 0, wx.ALL, 5 )
		
		bSizer16.Add( bSizer25, 1, wx.EXPAND, 5 )
		
		bSizer14.Add( bSizer16, 0, wx.EXPAND, 5 )
		
		self.SetSizer( bSizer14 )
		self.Layout()
		bSizer14.Fit( self )
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class D_AddUsuario
###########################################################################

class D_AddUsuario ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer8 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel3 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer6 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText7 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"Manejo de Campos", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticText7.Wrap( -1 )
		self.m_staticText7.SetFont( wx.Font( 12, 74, 90, 92, False, "Sans" ) )
		self.m_staticText7.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		
		bSizer6.Add( self.m_staticText7, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		fgSizer3 = wx.FlexGridSizer( 2, 2, 0, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText6 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"Indice de Busqueda", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		fgSizer3.Add( self.m_staticText6, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.Txt_Busqueda = wx.TextCtrl( self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 220,-1 ), 0 )
		fgSizer3.Add( self.Txt_Busqueda, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText8 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"Dirección de Correo", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )
		fgSizer3.Add( self.m_staticText8, 0, wx.ALL, 5 )
		
		self.Txt_Correo = wx.TextCtrl( self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 220,-1 ), 0 )
		fgSizer3.Add( self.Txt_Correo, 0, wx.ALL, 5 )
		
		
		fgSizer3.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.Ck_Imprimir = wx.CheckBox( self.m_panel3, wx.ID_ANY, u"Imprimir", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Ck_Imprimir.SetValue(True) 
		fgSizer3.Add( self.Ck_Imprimir, 0, wx.ALL, 5 )
		
		
		fgSizer3.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.Ck_Pdf = wx.CheckBox( self.m_panel3, wx.ID_ANY, u"Gen. PDF", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.Ck_Pdf, 0, wx.ALL, 5 )
		
		
		fgSizer3.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.Ck_EnvioCorreo = wx.CheckBox( self.m_panel3, wx.ID_ANY, u"Envio Correo", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.Ck_EnvioCorreo, 0, wx.ALL, 5 )
		
		bSizer6.Add( fgSizer3, 0, wx.EXPAND, 5 )
		
		gSizer1 = wx.GridSizer( 1, 4, 0, 0 )
		
		
		gSizer1.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.Btn_Aceptar = wx.Button( self.m_panel3, wx.ID_ANY, u"Aceptar", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.Btn_Aceptar, 0, wx.ALL, 5 )
		
		self.Btn_Cancelar = wx.Button( self.m_panel3, wx.ID_ANY, u"Cancelar", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.Btn_Cancelar, 0, wx.ALL, 5 )
		
		bSizer6.Add( gSizer1, 0, wx.EXPAND, 5 )
		
		self.m_panel3.SetSizer( bSizer6 )
		self.m_panel3.Layout()
		bSizer6.Fit( self.m_panel3 )
		bSizer8.Add( self.m_panel3, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.SetSizer( bSizer8 )
		self.Layout()
		bSizer8.Fit( self )
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class D_Abrir
###########################################################################

class D_Abrir ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer12 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel6 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_notebook1 = wx.Notebook( self.m_panel6, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel1 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer6 = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer4 = wx.FlexGridSizer( 2, 3, 0, 0 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText13 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Base de Datos", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_staticText13.Wrap( -1 )
		fgSizer4.Add( self.m_staticText13, 0, wx.ALL, 5 )
		
		self.ArchivoBase = wx.FilePickerCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.db", wx.DefaultPosition, wx.Size( 200,-1 ), wx.FLP_DEFAULT_STYLE )
		self.ArchivoBase.SetMinSize( wx.Size( 320,30 ) )
		
		fgSizer4.Add( self.ArchivoBase, 0, wx.ALL, 5 )
		
		bSizer6.Add( fgSizer4, 1, wx.EXPAND, 5 )
		
		self.BtnSalir = wx.Button( self.m_panel1, wx.ID_ANY, u"Salir", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.BtnSalir, 0, wx.ALL, 5 )
		
		self.m_panel1.SetSizer( bSizer6 )
		self.m_panel1.Layout()
		bSizer6.Fit( self.m_panel1 )
		self.m_notebook1.AddPage( self.m_panel1, u"Abrir", True )
		self.m_panel2 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer5 = wx.FlexGridSizer( 2, 2, 0, 0 )
		fgSizer5.SetFlexibleDirection( wx.BOTH )
		fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText14 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Ruta", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )
		fgSizer5.Add( self.m_staticText14, 0, wx.ALL, 5 )
		
		self.Dir_BD = wx.DirPickerCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		fgSizer5.Add( self.Dir_BD, 0, wx.ALL, 5 )
		
		self.m_staticText15 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Nombre", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )
		fgSizer5.Add( self.m_staticText15, 0, wx.ALL, 5 )
		
		self.Txt_NombreBD = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Txt_NombreBD.SetMinSize( wx.Size( 250,-1 ) )
		
		fgSizer5.Add( self.Txt_NombreBD, 0, wx.ALL, 5 )
		
		bSizer7.Add( fgSizer5, 1, wx.EXPAND, 5 )
		
		self.BtnCrearBD = wx.Button( self.m_panel2, wx.ID_ANY, u"Crear", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.BtnCrearBD, 0, wx.ALL, 5 )
		
		self.m_panel2.SetSizer( bSizer7 )
		self.m_panel2.Layout()
		bSizer7.Fit( self.m_panel2 )
		self.m_notebook1.AddPage( self.m_panel2, u"Crear", False )
		
		bSizer4.Add( self.m_notebook1, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel6.SetSizer( bSizer4 )
		self.m_panel6.Layout()
		bSizer4.Fit( self.m_panel6 )
		bSizer12.Add( self.m_panel6, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.SetSizer( bSizer12 )
		self.Layout()
		bSizer12.Fit( self )
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class D_Grilla
###########################################################################

class D_Grilla ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 960,600 ), style = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer15 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel7 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_scrolledWindow2 = wx.ScrolledWindow( self.m_panel7, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow2.SetScrollRate( 5, 5 )
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_toolBar1 = wx.ToolBar( self.m_scrolledWindow2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TB_HORIZONTAL ) 
		self.m_toolBar1.AddLabelTool( ID_Atras, u"Atras", wx.Bitmap( u"imagenes/Book-Previous-32.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Anterior", u"Anterior" ) 
		f2s_CmbPaginasChoices = []
		self.f2s_CmbPaginas = wx.Choice( self.m_toolBar1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, f2s_CmbPaginasChoices, 0 )
		self.f2s_CmbPaginas.SetSelection( 0 )
		self.m_toolBar1.AddControl( self.f2s_CmbPaginas )
		self.m_toolBar1.AddLabelTool( ID_Adelante, u"Adelante", wx.Bitmap( u"imagenes/Book-Next-32.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Siguiente Pagina", u"Siguiente" ) 
		self.m_toolBar1.AddSeparator()
		self.f2s_TxtLimite = wx.TextCtrl( self.m_toolBar1, wx.ID_ANY, u"20", wx.DefaultPosition, wx.Size( 30,-1 ), wx.TE_CENTRE )
		self.f2s_TxtLimite.SetMaxLength( 2 ) 
		self.m_toolBar1.AddControl( self.f2s_TxtLimite )
		self.m_toolBar1.AddSeparator()
		self.m_staticText23 = wx.StaticText( self.m_toolBar1, wx.ID_ANY, u"Registros", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23.Wrap( -1 )
		self.m_toolBar1.AddControl( self.m_staticText23 )
		self.f2s_TxtNumeroReg = wx.TextCtrl( self.m_toolBar1, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_toolBar1.AddControl( self.f2s_TxtNumeroReg )
		self.m_toolBar1.AddSeparator()
		self.m_staticText1 = wx.StaticText( self.m_toolBar1, wx.ID_ANY, u"Buscar", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		self.m_toolBar1.AddControl( self.m_staticText1 )
		self.f2s_Txt_BuscarID = wx.TextCtrl( self.m_toolBar1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
		self.f2s_Txt_BuscarID.SetMinSize( wx.Size( 300,-1 ) )
		
		self.m_toolBar1.AddControl( self.f2s_Txt_BuscarID )
		self.m_toolBar1.AddSeparator()
		self.m_toolBar1.AddLabelTool( ID_Adicionar, u"Adicicionar", wx.Bitmap( u"imagenes/Database-Add-32.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Adicionar", wx.EmptyString ) 
		self.m_toolBar1.AddLabelTool( ID_Editar, u"tool", wx.Bitmap( u"imagenes/Database-Edit-32.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Modificar", wx.EmptyString ) 
		self.m_toolBar1.AddSeparator()
		self.m_toolBar1.AddLabelTool( ID_Plano, u"tool", wx.Bitmap( u"imagenes/Database-upload-32.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Subir archivo Plano", wx.EmptyString ) 
		self.m_toolBar1.AddLabelTool( ID_ExportCSV, u"Exportar CSV", wx.Bitmap( u"imagenes/Export-32.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString ) 
		self.m_toolBar1.Realize()
		
		bSizer3.Add( self.m_toolBar1, 0, wx.EXPAND, 5 )
		
		self.Lst_Usuarios = wx.ListCtrl( self.m_scrolledWindow2, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.LC_HRULES|wx.LC_NO_SORT_HEADER|wx.LC_REPORT|wx.LC_VRULES|wx.HSCROLL|wx.VSCROLL )
		bSizer3.Add( self.Lst_Usuarios, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_scrolledWindow2.SetSizer( bSizer3 )
		self.m_scrolledWindow2.Layout()
		bSizer3.Fit( self.m_scrolledWindow2 )
		bSizer2.Add( self.m_scrolledWindow2, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel7.SetSizer( bSizer2 )
		self.m_panel7.Layout()
		bSizer2.Fit( self.m_panel7 )
		bSizer15.Add( self.m_panel7, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.SetSizer( bSizer15 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class D_Exportar
###########################################################################

class D_Exportar ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,150 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer27 = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer9 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer9.SetFlexibleDirection( wx.BOTH )
		fgSizer9.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText27 = wx.StaticText( self, wx.ID_ANY, u"Nombre", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText27.Wrap( -1 )
		fgSizer9.Add( self.m_staticText27, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrl21 = wx.TextCtrl( self, wx.ID_ANY, u"export.csv", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl21.SetMinSize( wx.Size( 250,30 ) )
		
		fgSizer9.Add( self.m_textCtrl21, 0, wx.ALL, 5 )
		
		self.m_staticText26 = wx.StaticText( self, wx.ID_ANY, u"Ruta", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText26.Wrap( -1 )
		fgSizer9.Add( self.m_staticText26, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_dirPicker4 = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Ruta exportacion", wx.DefaultPosition, wx.Size( 300,-1 ), wx.DIRP_DEFAULT_STYLE )
		self.m_dirPicker4.SetMinSize( wx.Size( 400,30 ) )
		
		fgSizer9.Add( self.m_dirPicker4, 0, wx.ALL, 5 )
		
		bSizer27.Add( fgSizer9, 1, wx.EXPAND, 5 )
		
		fgSizer10 = wx.FlexGridSizer( 0, 5, 0, 0 )
		fgSizer10.SetFlexibleDirection( wx.BOTH )
		fgSizer10.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		
		fgSizer10.AddSpacer( ( 100, 0), 1, wx.EXPAND, 5 )
		
		self.f2s_Exportar = wx.Button( self, wx.ID_ANY, u"Exportar", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer10.Add( self.f2s_Exportar, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		fgSizer10.AddSpacer( ( 100, 0), 1, wx.EXPAND, 5 )
		
		self.f2s_Salir = wx.Button( self, wx.ID_ANY, u"Salir", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer10.Add( self.f2s_Salir, 0, wx.ALL, 5 )
		
		bSizer27.Add( fgSizer10, 1, wx.EXPAND, 5 )
		
		self.SetSizer( bSizer27 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class D_SubirPlano
###########################################################################

class D_SubirPlano ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Subir Plano", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer15 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer15.SetMinSize( wx.Size( 500,300 ) ) 
		self.m_panel9 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer7 = wx.FlexGridSizer( 2, 1, 0, 0 )
		fgSizer7.SetFlexibleDirection( wx.BOTH )
		fgSizer7.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText16 = wx.StaticText( self.m_panel9, wx.ID_ANY, u"Ruta Archivo Plano", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )
		fgSizer7.Add( self.m_staticText16, 0, wx.ALL, 5 )
		
		self.Dir_Plano = wx.FilePickerCtrl( self.m_panel9, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE|wx.FLP_OPEN )
		self.Dir_Plano.SetMinSize( wx.Size( 400,30 ) )
		
		fgSizer7.Add( self.Dir_Plano, 0, wx.ALL, 5 )
		
		self.Medidor = wx.Gauge( self.m_panel9, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.Medidor.SetValue( 0 ) 
		self.Medidor.SetMinSize( wx.Size( 400,-1 ) )
		
		fgSizer7.Add( self.Medidor, 0, wx.ALL, 5 )
		
		self.m_panel9.SetSizer( fgSizer7 )
		self.m_panel9.Layout()
		fgSizer7.Fit( self.m_panel9 )
		bSizer15.Add( self.m_panel9, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.Lb_Status = wx.StaticText( self, wx.ID_ANY, u"Estructura del archivo Plano:\nIdentificador,dirección de correo,imprimir,GenerarPDF,Correo\n\nDonde las columnas imprimir,GenerarPDF,Correo, son bandera \nnumericas usadas asi:\n\nimprimir   =1   -> Activo para imprimir\nImprimir  = 0   ->  No imprimir", wx.Point( 20,20 ), wx.DefaultSize, 0|wx.ALWAYS_SHOW_SB|wx.FULL_REPAINT_ON_RESIZE|wx.HSCROLL|wx.RAISED_BORDER|wx.VSCROLL )
		self.Lb_Status.Wrap( -1 )
		bSizer15.Add( self.Lb_Status, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.SetSizer( bSizer15 )
		self.Layout()
		bSizer15.Fit( self )
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class D_ProbarCorreo
###########################################################################

class D_ProbarCorreo ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer25 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_textCtrl18 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		self.m_textCtrl18.SetMinSize( wx.Size( 480,300 ) )
		
		bSizer25.Add( self.m_textCtrl18, 0, wx.ALL, 5 )
		
		self.SetSizer( bSizer25 )
		self.Layout()
		bSizer25.Fit( self )
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class D_Correo
###########################################################################

class D_Correo ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer14 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_scrolledWindow2 = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow2.SetScrollRate( 5, 5 )
		self.m_scrolledWindow2.SetMinSize( wx.Size( 510,600 ) )
		
		bSizer28 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow2, wx.ID_ANY, u"Configuración Servidor" ), wx.VERTICAL )
		
		bSizer15 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.Txt_Host = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_TAB )
		self.Txt_Host.SetMinSize( wx.Size( 200,-1 ) )
		
		bSizer15.Add( self.Txt_Host, 0, wx.ALL, 5 )
		
		self.m_staticText14 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"Puerto", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )
		bSizer15.Add( self.m_staticText14, 0, wx.ALL, 5 )
		
		self.Txt_Puerto = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, u"25", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Txt_Puerto.SetMinSize( wx.Size( 80,-1 ) )
		
		bSizer15.Add( self.Txt_Puerto, 0, wx.ALL, 5 )
		
		self.Chk_TSL = wx.CheckBox( self.m_scrolledWindow2, wx.ID_ANY, u"TSL", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer15.Add( self.Chk_TSL, 0, wx.ALL, 5 )
		
		sbSizer1.Add( bSizer15, 0, wx.EXPAND, 5 )
		
		bSizer16 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText15 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"Usuario", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )
		bSizer16.Add( self.m_staticText15, 0, wx.ALL, 5 )
		
		self.Txt_Usuario = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Txt_Usuario.SetMinSize( wx.Size( 300,-1 ) )
		
		bSizer16.Add( self.Txt_Usuario, 0, wx.ALL, 5 )
		
		sbSizer1.Add( bSizer16, 0, wx.EXPAND, 5 )
		
		bSizer17 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText16 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"Clave", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )
		bSizer17.Add( self.m_staticText16, 0, wx.ALL, 5 )
		
		self.Txt_Clave = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		self.Txt_Clave.SetMinSize( wx.Size( 200,-1 ) )
		
		bSizer17.Add( self.Txt_Clave, 0, wx.ALL, 5 )
		
		self.Chk_verclave = wx.CheckBox( self.m_scrolledWindow2, wx.ID_ANY, u"Ver Clave", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer17.Add( self.Chk_verclave, 0, wx.ALL, 5 )
		
		sbSizer1.Add( bSizer17, 0, wx.EXPAND, 5 )
		
		bSizer28.Add( sbSizer1, 0, wx.EXPAND, 5 )
		
		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow2, wx.ID_ANY, u"Informacion Correo" ), wx.VERTICAL )
		
		bSizer192 = wx.BoxSizer( wx.HORIZONTAL )
		
		sbSizer2.Add( bSizer192, 0, wx.EXPAND, 5 )
		
		fgSizer8 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer8.SetFlexibleDirection( wx.BOTH )
		fgSizer8.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText18 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"Enviado por", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( -1 )
		fgSizer8.Add( self.m_staticText18, 0, wx.ALL, 5 )
		
		self.Txt_enviado = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Txt_enviado.SetMinSize( wx.Size( 300,-1 ) )
		
		fgSizer8.Add( self.Txt_enviado, 0, wx.ALL, 5 )
		
		self.m_staticText20 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"Bandera ID.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )
		fgSizer8.Add( self.m_staticText20, 0, wx.ALL, 5 )
		
		self.Txt_Bandera = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Txt_Bandera.SetMinSize( wx.Size( 300,-1 ) )
		
		fgSizer8.Add( self.Txt_Bandera, 0, wx.ALL, 5 )
		
		self.m_staticText201 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"Ruta Salida PDF", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText201.Wrap( -1 )
		fgSizer8.Add( self.m_staticText201, 0, wx.ALL, 5 )
		
		self.Txt_SalidaPDF = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Txt_SalidaPDF.SetMinSize( wx.Size( 300,-1 ) )
		
		fgSizer8.Add( self.Txt_SalidaPDF, 0, wx.ALL, 5 )
		
		self.m_staticText202 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"Ruta PDF Adicional", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText202.Wrap( -1 )
		fgSizer8.Add( self.m_staticText202, 0, wx.ALL, 5 )
		
		self.Txt_RutaPDFadd = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Txt_RutaPDFadd.SetMinSize( wx.Size( 300,-1 ) )
		
		fgSizer8.Add( self.Txt_RutaPDFadd, 0, wx.ALL, 5 )
		
		sbSizer2.Add( fgSizer8, 0, wx.EXPAND, 5 )
		
		bSizer193 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText203 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"Contenido Texto", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText203.Wrap( -1 )
		bSizer193.Add( self.m_staticText203, 0, wx.ALL, 5 )
		
		self.Txt_Texto = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.HSCROLL|wx.RAISED_BORDER|wx.VSCROLL )
		self.Txt_Texto.SetMinSize( wx.Size( 340,100 ) )
		
		bSizer193.Add( self.Txt_Texto, 0, wx.ALL, 5 )
		
		sbSizer2.Add( bSizer193, 0, wx.EXPAND, 5 )
		
		gbSizer1 = wx.GridBagSizer( 0, 0 )
		gbSizer1.SetFlexibleDirection( wx.BOTH )
		gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText2031 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"Contenido HTML", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2031.Wrap( -1 )
		gbSizer1.Add( self.m_staticText2031, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.f2s_BtnValidarHML = wx.BitmapButton( self.m_scrolledWindow2, wx.ID_ANY, wx.Bitmap( u"imagenes/Xhtml-Valid-32.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		gbSizer1.Add( self.f2s_BtnValidarHML, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.Txt_HTML = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.HSCROLL|wx.RAISED_BORDER|wx.VSCROLL )
		self.Txt_HTML.SetMinSize( wx.Size( 340,150 ) )
		
		gbSizer1.Add( self.Txt_HTML, wx.GBPosition( 0, 2 ), wx.GBSpan( 2, 1 ), wx.ALL, 5 )
		
		sbSizer2.Add( gbSizer1, 1, wx.EXPAND, 5 )
		
		bSizer28.Add( sbSizer2, 0, wx.EXPAND, 5 )
		
		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow2, wx.ID_ANY, u"Navegador Base Datos" ), wx.VERTICAL )
		
		bSizer31 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.Btn_Atras = wx.Button( self.m_scrolledWindow2, wx.ID_ANY, u"|<", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Btn_Atras.SetHelpText( u"Atras" )
		
		bSizer31.Add( self.Btn_Atras, 0, wx.ALL, 5 )
		
		self.Btn_Inicio = wx.Button( self.m_scrolledWindow2, wx.ID_ANY, u"<<", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Btn_Inicio.SetHelpText( u"Primer Registro" )
		
		bSizer31.Add( self.Btn_Inicio, 0, wx.ALL, 5 )
		
		self.Txt_PosRegistro = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTRE )
		self.Txt_PosRegistro.SetHelpText( u"Posicion Actual de registro" )
		
		bSizer31.Add( self.Txt_PosRegistro, 0, wx.ALL, 5 )
		
		self.Btn_Final = wx.Button( self.m_scrolledWindow2, wx.ID_ANY, u">>", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Btn_Final.SetHelpText( u"Final Registro" )
		
		bSizer31.Add( self.Btn_Final, 0, wx.ALL, 5 )
		
		self.Btn_siguiente = wx.Button( self.m_scrolledWindow2, wx.ID_ANY, u">|", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Btn_siguiente.SetHelpText( u"Siguiente" )
		
		bSizer31.Add( self.Btn_siguiente, 0, wx.ALL, 5 )
		
		sbSizer3.Add( bSizer31, 0, wx.EXPAND, 5 )
		
		bSizer23 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_slider1 = wx.Slider( self.m_scrolledWindow2, wx.ID_ANY, 1, 1, 1, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		self.m_slider1.SetMinSize( wx.Size( 400,-1 ) )
		
		bSizer23.Add( self.m_slider1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		sbSizer3.Add( bSizer23, 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer32 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.Btn_Adicionar = wx.Button( self.m_scrolledWindow2, wx.ID_ANY, u"Adicionar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer32.Add( self.Btn_Adicionar, 0, wx.ALL, 5 )
		
		self.Btn_Modificar = wx.Button( self.m_scrolledWindow2, wx.ID_ANY, u"Modificar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer32.Add( self.Btn_Modificar, 0, wx.ALL, 5 )
		
		
		bSizer32.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText23 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"Estado del Servidor:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23.Wrap( -1 )
		bSizer32.Add( self.m_staticText23, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.Chk_Estado = wx.CheckBox( self.m_scrolledWindow2, wx.ID_ANY, u"Activo", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Chk_Estado.SetHelpText( u"Determina si esta activo el servidor para funcionar" )
		
		bSizer32.Add( self.Chk_Estado, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		sbSizer3.Add( bSizer32, 0, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer28.Add( sbSizer3, 0, wx.EXPAND, 5 )
		
		fgSizer7 = wx.FlexGridSizer( 0, 3, 0, 50 )
		fgSizer7.AddGrowableCol( 10 )
		fgSizer7.SetFlexibleDirection( wx.BOTH )
		fgSizer7.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.Btn_Probar = wx.Button( self.m_scrolledWindow2, wx.ID_ANY, u"Probar Coneccion", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer7.Add( self.Btn_Probar, 0, wx.ALL, 5 )
		
		
		fgSizer7.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.Btn_Salir = wx.Button( self.m_scrolledWindow2, wx.ID_ANY, u"Salir", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer7.Add( self.Btn_Salir, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer28.Add( fgSizer7, 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_scrolledWindow2.SetSizer( bSizer28 )
		self.m_scrolledWindow2.Layout()
		bSizer28.Fit( self.m_scrolledWindow2 )
		bSizer14.Add( self.m_scrolledWindow2, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.SetSizer( bSizer14 )
		self.Layout()
		bSizer14.Fit( self )
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class D_VisorHTML
###########################################################################

class D_VisorHTML ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Visor HTML", pos = wx.DefaultPosition, size = wx.Size( 600,600 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.Size( 500,600 ), wx.DefaultSize )
		
		bSizer30 = wx.BoxSizer( wx.VERTICAL )
		
		self.f2s_HtmlWin = wx.html.HtmlWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 580,560 ), wx.html.HW_SCROLLBAR_AUTO )
		bSizer30.Add( self.f2s_HtmlWin, 0, wx.ALL, 5 )
		
		self.SetSizer( bSizer30 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class D_ImportAccion
###########################################################################

class D_ImportAccion ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Importar Acciones desde Procesos", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		sbSizer9 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Procesos" ), wx.VERTICAL )
		
		fgSizer15 = wx.FlexGridSizer( 2, 2, 0, 0 )
		fgSizer15.SetFlexibleDirection( wx.BOTH )
		fgSizer15.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText35 = wx.StaticText( self, wx.ID_ANY, u"Procesos", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText35.Wrap( -1 )
		fgSizer15.Add( self.m_staticText35, 0, wx.ALL, 5 )
		
		f2s_choProcesosChoices = []
		self.f2s_choProcesos = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 200,-1 ), f2s_choProcesosChoices, 0 )
		self.f2s_choProcesos.SetSelection( 0 )
		self.f2s_choProcesos.SetMaxSize( wx.Size( 200,-1 ) )
		
		fgSizer15.Add( self.f2s_choProcesos, 0, wx.ALL, 5 )
		
		
		fgSizer15.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.F2s_chkReemplazar = wx.CheckBox( self, wx.ID_ANY, u"Reemplazar Actual", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer15.Add( self.F2s_chkReemplazar, 0, wx.ALL, 5 )
		
		self.f2s_btnImportar = wx.Button( self, wx.ID_ANY, u"Importar", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer15.Add( self.f2s_btnImportar, 0, wx.ALL, 5 )
		
		self.f2s_btnSalir = wx.Button( self, wx.ID_ANY, u"Salir", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer15.Add( self.f2s_btnSalir, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		sbSizer9.Add( fgSizer15, 1, wx.EXPAND, 5 )
		
		self.SetSizer( sbSizer9 )
		self.Layout()
		sbSizer9.Fit( self )
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class D_AddEnvioArchivo
###########################################################################

class D_AddEnvioArchivo ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 410,510 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer29 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer6 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Navegacion" ), wx.HORIZONTAL )
		
		
		sbSizer6.AddSpacer( ( 50, 0), 0, wx.EXPAND, 5 )
		
		self.f2s_btnInicio = wx.Button( self, wx.ID_ANY, u"|<", wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
		self.f2s_btnInicio.Enable( False )
		
		sbSizer6.Add( self.f2s_btnInicio, 0, wx.ALL, 5 )
		
		self.f2s_btnAnterior = wx.Button( self, wx.ID_ANY, u"<<", wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
		self.f2s_btnAnterior.Enable( False )
		
		sbSizer6.Add( self.f2s_btnAnterior, 0, wx.ALL, 5 )
		
		self.f2s_lbCampos = wx.StaticText( self, wx.ID_ANY, u"0/0", wx.DefaultPosition, wx.Size( 150,20 ), wx.ALIGN_CENTRE|wx.RAISED_BORDER )
		self.f2s_lbCampos.Wrap( -1 )
		self.f2s_lbCampos.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )
		self.f2s_lbCampos.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNSHADOW ) )
		self.f2s_lbCampos.SetMinSize( wx.Size( 100,20 ) )
		self.f2s_lbCampos.SetMaxSize( wx.Size( 100,20 ) )
		
		sbSizer6.Add( self.f2s_lbCampos, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.f2s_btnSiguiente = wx.Button( self, wx.ID_ANY, u">>", wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
		self.f2s_btnSiguiente.Enable( False )
		
		sbSizer6.Add( self.f2s_btnSiguiente, 0, wx.ALL, 5 )
		
		self.f2s_btnFinal = wx.Button( self, wx.ID_ANY, u">|", wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
		self.f2s_btnFinal.Enable( False )
		
		sbSizer6.Add( self.f2s_btnFinal, 0, wx.ALL, 5 )
		
		bSizer29.Add( sbSizer6, 0, wx.EXPAND, 5 )
		
		sbSizer4 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Proceso" ), wx.VERTICAL )
		
		fgSizer11 = wx.FlexGridSizer( 2, 2, 0, 0 )
		fgSizer11.SetFlexibleDirection( wx.BOTH )
		fgSizer11.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText28 = wx.StaticText( self, wx.ID_ANY, u"nombre", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText28.Wrap( -1 )
		fgSizer11.Add( self.m_staticText28, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer32 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.f2s_txtNombre = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 220,-1 ), 0 )
		self.f2s_txtNombre.SetMaxLength( 255 ) 
		self.f2s_txtNombre.SetToolTipString( u"Nombre del Proceso" )
		
		bSizer32.Add( self.f2s_txtNombre, 0, wx.ALL, 5 )
		
		self.f2s_ChkActivo = wx.CheckBox( self, wx.ID_ANY, u"Activo", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer32.Add( self.f2s_ChkActivo, 0, wx.ALL, 5 )
		
		fgSizer11.Add( bSizer32, 1, wx.EXPAND, 5 )
		
		self.m_staticText29 = wx.StaticText( self, wx.ID_ANY, u"Impresora", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText29.Wrap( -1 )
		fgSizer11.Add( self.m_staticText29, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.f2s_txtImpresora = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
		fgSizer11.Add( self.f2s_txtImpresora, 0, wx.ALL, 5 )
		
		self.label1 = wx.StaticText( self, wx.ID_ANY, u"Directorio", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label1.Wrap( -1 )
		fgSizer11.Add( self.label1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		fgSizer13 = wx.FlexGridSizer( 1, 2, 0, 0 )
		fgSizer13.SetFlexibleDirection( wx.BOTH )
		fgSizer13.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.f2s_txtDirectorio = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.f2s_txtDirectorio.SetMinSize( wx.Size( 240,-1 ) )
		
		fgSizer13.Add( self.f2s_txtDirectorio, 0, wx.ALL, 5 )
		
		self.f2s_DirPic = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"seleccion Directorio", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		self.f2s_DirPic.SetMinSize( wx.Size( 50,30 ) )
		
		fgSizer13.Add( self.f2s_DirPic, 0, wx.ALL, 5 )
		
		fgSizer11.Add( fgSizer13, 1, wx.EXPAND, 5 )
		
		sbSizer4.Add( fgSizer11, 1, wx.EXPAND, 5 )
		
		gSizer4 = wx.GridSizer( 1, 3, 0, 0 )
		
		self.f2s_btnGuardar = wx.Button( self, wx.ID_ANY, u"Guardar", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.f2s_btnGuardar, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.f2s_BtnNuevoReg = wx.Button( self, wx.ID_ANY, u"Nuevo", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.f2s_BtnNuevoReg.Enable( False )
		
		gSizer4.Add( self.f2s_BtnNuevoReg, 0, wx.ALL, 5 )
		
		self.f2s_btnSalir = wx.Button( self, wx.ID_ANY, u"Salir", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.f2s_btnSalir, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		sbSizer4.Add( gSizer4, 0, wx.EXPAND, 5 )
		
		bSizer29.Add( sbSizer4, 0, wx.EXPAND, 5 )
		
		self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		self.m_staticline1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )
		
		bSizer29.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )
		
		sbSizer5 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Accion" ), wx.VERTICAL )
		
		bSizer30 = wx.BoxSizer( wx.VERTICAL )
		
		self.f2s_listAcciones = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 360,170 ), wx.LC_HRULES|wx.LC_NO_SORT_HEADER|wx.LC_REPORT|wx.LC_VRULES|wx.ALWAYS_SHOW_SB|wx.RAISED_BORDER )
		bSizer30.Add( self.f2s_listAcciones, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		gSizer3 = wx.GridSizer( 1, 3, 0, 0 )
		
		self.f2s_btnAddlista = wx.Button( self, wx.ID_ANY, u"Adicionar", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.f2s_btnAddlista, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.f2s_btnImportar = wx.Button( self, wx.ID_ANY, u"Importar", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.f2s_btnImportar, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.f2s_btnBorrarlista = wx.Button( self, wx.ID_ANY, u"Borrar", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.f2s_btnBorrarlista.Enable( False )
		
		gSizer3.Add( self.f2s_btnBorrarlista, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer30.Add( gSizer3, 1, wx.EXPAND, 5 )
		
		sbSizer5.Add( bSizer30, 1, wx.EXPAND, 5 )
		
		bSizer29.Add( sbSizer5, 0, wx.EXPAND, 5 )
		
		self.SetSizer( bSizer29 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class D_AddAccion
###########################################################################

class D_AddAccion ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer31 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer7 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Accion" ), wx.VERTICAL )
		
		fgSizer12 = wx.FlexGridSizer( 2, 2, 0, 0 )
		fgSizer12.SetFlexibleDirection( wx.BOTH )
		fgSizer12.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText32 = wx.StaticText( self, wx.ID_ANY, u"Patron", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText32.Wrap( -1 )
		fgSizer12.Add( self.m_staticText32, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.f2s_txtPatron = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,-1 ), 0 )
		fgSizer12.Add( self.f2s_txtPatron, 0, wx.ALL, 5 )
		
		self.m_staticText33 = wx.StaticText( self, wx.ID_ANY, u"Descripcion", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText33.Wrap( -1 )
		fgSizer12.Add( self.m_staticText33, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.f2s_txtDescripcion = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,-1 ), 0 )
		fgSizer12.Add( self.f2s_txtDescripcion, 0, wx.ALL, 5 )
		
		self.m_staticText34 = wx.StaticText( self, wx.ID_ANY, u"Ambiente", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText34.Wrap( -1 )
		fgSizer12.Add( self.m_staticText34, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		f2s_choAccionChoices = []
		self.f2s_choAccion = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 250,-1 ), f2s_choAccionChoices, 0 )
		self.f2s_choAccion.SetSelection( 0 )
		fgSizer12.Add( self.f2s_choAccion, 0, wx.ALL, 5 )
		
		sbSizer7.Add( fgSizer12, 1, wx.EXPAND, 5 )
		
		gSizer4 = wx.GridSizer( 2, 2, 0, 0 )
		
		self.f2s_btnAdd = wx.Button( self, wx.ID_ANY, u"Adicionar", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.f2s_btnAdd, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.f2s_BtnCancelar = wx.Button( self, wx.ID_ANY, u"Cancelar", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.f2s_BtnCancelar, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		sbSizer7.Add( gSizer4, 0, wx.EXPAND, 5 )
		
		bSizer31.Add( sbSizer7, 1, wx.EXPAND, 5 )
		
		self.SetSizer( bSizer31 )
		self.Layout()
		bSizer31.Fit( self )
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class D_AdminServArchivo
###########################################################################

class D_AdminServArchivo ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Administrador de servicios envio Archivo", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.CLOSE_BOX|wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		sbSizer11 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"label" ), wx.VERTICAL )
		
		bSizer38 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.f2s_lstServicios = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 300,300 ), wx.LC_HRULES|wx.LC_NO_SORT_HEADER|wx.LC_REPORT|wx.LC_VRULES|wx.ALWAYS_SHOW_SB|wx.FULL_REPAINT_ON_RESIZE )
		self.f2s_lstServicios.SetMinSize( wx.Size( 300,300 ) )
		
		bSizer38.Add( self.f2s_lstServicios, 0, wx.ALL, 5 )
		
		bSizer39 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer12 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Man. Servicios" ), wx.VERTICAL )
		
		self.f2s_BtnCrear = wx.Button( self, wx.ID_ANY, u"Crear", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer12.Add( self.f2s_BtnCrear, 0, wx.ALL, 5 )
		
		self.f2s_BtnIniciar = wx.Button( self, wx.ID_ANY, u"Iniciar", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer12.Add( self.f2s_BtnIniciar, 0, wx.ALL, 5 )
		
		self.f2s_btnDetener = wx.Button( self, wx.ID_ANY, u"Detener", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer12.Add( self.f2s_btnDetener, 0, wx.ALL, 5 )
		
		self.f2s_btnRefrescar = wx.Button( self, wx.ID_ANY, u"Refrescar", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer12.Add( self.f2s_btnRefrescar, 0, wx.ALL, 5 )
		
		
		sbSizer12.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.f2s_btnCancelar = wx.Button( self, wx.ID_ANY, u"Salir", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer12.Add( self.f2s_btnCancelar, 0, wx.ALL, 5 )
		
		bSizer39.Add( sbSizer12, 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer38.Add( bSizer39, 1, wx.EXPAND, 5 )
		
		sbSizer11.Add( bSizer38, 1, wx.EXPAND, 5 )
		
		self.SetSizer( sbSizer11 )
		self.Layout()
		sbSizer11.Fit( self )
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

