#!/usr/bin/env python
# -*- coding: utf-8 -*- 

'''
Created on 12/04/2013

@author: marco
'''
import wx,sys,os
from FormMapic import D_Grilla
from FormMapic import ID_Adelante
from FormMapic import ID_Atras


class ObGrilla():
	'''
	classdocs
	'''

	def __init__(self,padre,titulo):
		print "Constructor ObjGrilla"
		'''
		Constructor
		'''
		self.Cambiolim=True
		self.pagina=0
		self.ObaseD=None
		self.fusr=D_Grilla(padre)
		self.Indice=-1
		self.fusr.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnItemSelectIndex) #click
		self.fusr.m_toolBar1.Bind(wx.EVT_TOOL, self.Dialogo_Adelante,id=ID_Adelante)
		self.fusr.m_toolBar1.Bind(wx.EVT_TOOL, self.Dialogo_Atras,id=ID_Atras)
		self.fusr.f2s_Txt_BuscarID.Bind(wx.EVT_KEY_UP, self.onBusquedaSelectiva,self.fusr.f2s_Txt_BuscarID)
		self.fusr.f2s_CmbPaginas.Bind(wx.EVT_CHOICE,self.onMoverPagina,self.fusr.f2s_CmbPaginas)
		self.fusr.f2s_TxtLimite.Bind(wx.EVT_KEY_DOWN,self.onCambioTxtLimite,self.fusr.f2s_TxtLimite)
		
		
		self.fusr.SetTitle(titulo)
		self.fusr.Show()
		
	

	def onCambioTxtLimite(self,event):
		print "onCambioTxtLimite"
		keycode = event.GetKeyCode()
		if keycode == wx.WXK_RETURN:
			
			#calcular la posicion actual del registro..
			#posalctual=self.pagina * self.limite
			self.limite=int(self.fusr.f2s_TxtLimite.GetValue())
			tpag=self.TotalReg()
			#print tpag
			self.pagina=0
			self.Listar()
			
		elif keycode < 255:
			j=chr(keycode)
			#print keycode
			if j.isdigit() or j==8 or (keycode==wx.WXK_TAB|wx.WXK_BACK|wx.WXK_DELETE):
 				event.Skip()
 		else:
			event.Skip()
	 			
	def onMoverPagina(self,event):
		print "onMoverPagina"
		self.pagina=self.fusr.f2s_CmbPaginas.GetCurrentSelection()
		print "pagina:",self.pagina
		self.Listar()
		
	def onExportarCSV(self):
		print "OnExportarCSV"
		confirmar=wx.MessageBox("Iniciar CSV","Confirmacion",wx.ICON_EXCLAMATION|wx.YES_NO)
		if confirmar==wx.NO:return
		
		salida=file("export.csv",'w')
		separador=';'
		for titulo in self.titulo_col:
			titulo="'%s'%s" %(titulo,separador)
			salida.write(titulo)	
		salida.write('\n')
		registros=self.ObaseD.LeerCampos(self.campos,self.tabla, self.condicion)
		for registro in registros:
			for columna in registro:
				columna = "'%s'%s" %(columna,separador)
				salida.write(columna)
			salida.write('\n')
		salida.write ('Fin Reporte\n')
		salida.close()
		wx.MessageBox("Fin del Reporte")
		
		
		
		
		campos=self.campos.split(',')
		
	def onBusquedaSelectiva(self,event):
		print "onBusquedaSelectiva"
		buscar=self.fusr.f2s_Txt_BuscarID.GetValue()
		buscar=buscar.strip()
		if len(buscar)>0:
			self.condicion="%s LIKE '%s%%'" %(self.campobusqueda,buscar)
		else:
			self.condicion=""
		self.TotalReg()
		self.Listar()
	
	def VerftextoLimite(self):
		print "VerftextoLimite"
		self.fusr.f2s_TxtLimite.SetValue(str(self.limite))
			
	def Dialogo_Atras(self,event):
		print "Dialogo_Atras"
		self.VerftextoLimite()
		self.pagina -= 1
		if self.pagina < 0:
			self.pagina = 0
			wx.MessageBox ("Ha llegado al principio de las paginas")
		else:
			self.Listar()

	def Dialogo_Adelante(self,event):
		print "Dialogo_Adelante"
		self.VerftextoLimite()
		self.pagina+=1	
		if self.pagina  == self.fusr.f2s_CmbPaginas.GetCount():
			self.pagina=self.fusr.f2s_CmbPaginas.GetCount()
			wx.MessageBox ("Ha llegado al final de las paginas")
		else:
			self.fusr.f2s_CmbPaginas.SetSelection(self.pagina)
			self.Listar()
			
	def InfoBase(self,BaseDatos,tabla,campos,condicion="",orden="", limite=20,campobusqueda=''):
		print "InfoBase"
		self.ObaseD=BaseDatos
		self.campobusqueda=campobusqueda
		self.tabla=tabla
		self.campos=campos
		self.condicion=condicion
		self.orden=orden
		self.limite=limite
		self.fusr.f2s_TxtLimite.SetValue(str(self.limite))
		self.posicion=0
		
	def Titulos_columna(self,titulo=[],ancho=[]):
		print "Titulos_columna"
		self.titulo_col=titulo
		self.ancho_col=ancho
			
	def ColocarTitulos(self):
		print "ColocarTitulos"
		self.fusr.Lst_Usuarios.ClearAll()
		
		
		columna=0
		for texto in self.titulo_col: 
			if len(self.ancho_col) -1 >=columna:
				self.fusr.Lst_Usuarios.InsertColumn(columna,texto,width=self.ancho_col[columna])
			else:
				self.fusr.Lst_Usuarios.InsertColumn(columna,texto)
			columna+=1

	def TotalReg(self):
		print "TotalReg"
		cantidad=self.ObaseD.Contar(self.tabla,self.condicion)
		self.fusr.f2s_TxtNumeroReg.SetValue(str(cantidad))
		self.fusr.f2s_CmbPaginas.Clear()
		if cantidad ==0:
			self.fusr.f2s_CmbPaginas.Enable(False)
			return 0
		
		calculo =int (cantidad / self.limite)
		if cantidad % self.limite>0:calculo +=1
		if calculo==0:calculo=1
		
		itempag=[]
		print "Calculo:",calculo
		for i in range(0,calculo):
			itempag.append('pag:' + str(i+1))
		print itempag		
		self.fusr.f2s_CmbPaginas.AppendItems(itempag)
		self.fusr.f2s_CmbPaginas.SetSelection(0)
		return calculo
		
	def VerificarLimite(self):
		print "VerificarLimite"
		self.limite=int(self.fusr.f2s_TxtLimite.GetValue())
		if self.limite <3:
			self.limite=3
		
	def Listar(self):
		print "Listar"
		self.ColocarTitulos()
		self.Indice=-1
		if self.Cambiolim: 
			self.VerificarLimite()
			self.TotalReg()
			self.Cambiolim=False

		if self.pagina==0:
			self.posicion=0
		else:
			self.posicion=self.pagina * self.limite

		print "posicion",self.posicion

		limites="%i,%i" %(self.posicion,self.limite)
		registros=self.ObaseD.LeerCampos(self.campos,self.tabla, self.condicion , self.orden,limites)
		#print registros
		fila = 0
		if len(registros)<1:
			wx.MessageBox("No hay registro de clientes en este momento","Busqueda",wx.ICON_INFORMATION)
			#return
		
		for registro in registros:
			index = self.fusr.Lst_Usuarios.InsertStringItem(sys.maxint, str(fila + 1))
			if index % 2==0:
				self.fusr.Lst_Usuarios.SetItemBackgroundColour(index,(250,226,193))
			else:
				self.fusr.Lst_Usuarios.SetItemBackgroundColour(index,(240,227,220))
			columna=0
			for campo in registro:
				if type(campo) == int:
					self.fusr.Lst_Usuarios.SetStringItem(index,columna,str(campo))
				elif type(campo)==unicode or type(campo)==str:
					if campo=='img_impresora':
						imagen='imagenes' + os.sep + 'Print-32.png'
						bitmap = wx.BitmapFromImage(imagen)
						imageidx = self.fusr.Lst_Usuarios.Add(bitmap)
						self.fusr.Lst_Usuarios.SetItemColumnImage(index, columna, imageidx)
					else:
						self.fusr.Lst_Usuarios.SetStringItem(index,columna,campo)
				columna += 1

	def OnItemSelectIndex(self,event):
		print 'OnItemSelectIndex'
		print "indice Anterior:",self.Indice
		self.Indice=self.fusr.Lst_Usuarios.GetFirstSelected()
		print "indice Nuevo:",self.Indice
		#self.fusr.Lst_Usuarios.SetItemBackgroundColour(self.Indice,(200,200,200))






#		il=wx.ImageList(16,16,True)
#		pngs=wx.Bitmap('imagenes/PDF-File-16.png',wx.BITMAP_TYPE_PNG)
#		il_max=il.Add(pngs)
#		self.fusr.Lst_Usuarios.AssignImageList(il,wx.IMAGE_LIST_SMALL)
#		print "valor Max:", il_max
#		self.fusr.Lst_Usuarios.InsertImageStringItem(columna,"sumad",0)
