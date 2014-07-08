#!c:\python27\python.exe
# -*- coding: utf-8 -*- 
'''
Created on 13/08/2013

@author: marco
'''
import wx
import os

from encabezado import obEncabezado

from formtrafico import FormGeneral
from mantexto import obTrafico
from wx._controls import EVT_FILEPICKER_CHANGED

try:  
	import cPickle as pickle  
except ImportError:  
	import pickle  

class IncioInterface(FormGeneral):
	def __init__(self):
		FormGeneral.__init__(self,None)
		FormGeneral.SetTitle(self,u"Controlador Manejo de Docuentos")
		#Reinicio pantalla
		self.f2s_TreeManejo.DeleteAllItems()
		#Acciones de botones
		self.f2s_AdicionTexto.Bind(wx.EVT_BUTTON, self.OndiagTexto)
		self.f2s_BtnEditar.Bind(wx.EVT_BUTTON, self.OnEditar)
		self.f2s_BtnGuardar.Bind(wx.EVT_BUTTON, self.OnGuardar)
		self.f2s_BtnBorrar.Bind(wx.EVT_BUTTON,self.OnBorrar)
		self.f2s_BtnNuevaCopia.Bind(wx.EVT_BUTTON,self.NuevoNodo)
		#Control de archivo
		self.f2s_FileAmbiente.Bind(EVT_FILEPICKER_CHANGED, self.OnAbrirAmbiente)
		#Manejo del arbol
		self.f2s_TreeManejo.Bind(wx.EVT_TREE_ITEM_EXPANDED, self.OnItemExpandir)
		self.f2s_TreeManejo.Bind(wx.EVT_TREE_ITEM_ACTIVATED, self.OnItemActivado)
		self.f2s_TreeManejo.Bind(wx.EVT_TREE_SEL_CHANGED, self.OnCambiado)
		#Inicio de variables.
		self.G_ambiente=''
		self.G_formato=''
		self.G_ruta=''
		self.listaitems={}

		self.idItem=None
		self.cuenta=0
		self.InicioBotones()
		
		#lleando de combos
		self.f2s_ChControl.Clear()
		items=['Original','Original,copia']
		self.f2s_ChControl.SetItems(items)
		self.f2s_ChControl.SetSelection(0)
		self.f2s_ChOrden.Clear()
		items=['Original al principio','Original al final']
		self.f2s_ChOrden.SetItems(items)
		self.f2s_ChOrden.SetSelection(0)
		
	def OnItemExpandir(self,evt):
		print 'expandir:', self.f2s_TreeManejo.GetItemText(evt.GetItem())	
	def NuevoNodo(self,evt):
		root= self.f2s_TreeManejo.GetRootItem()
		self.f2s_TreeManejo.AppendItem(root,"[Texto para Copia]")    
	
	def BotonControl(self):
		print "botoncontrol"
		
		if self.f2s_TreeManejo.GetItemText(self.idItem)=='[Control]':
			self.f2s_AdicionTexto.Enable(False)
			self.f2s_BtnEditar.Enable(False)
			self.f2s_BtnBorrar.Enable(False)
			self.f2s_BtnNuevaCopia.Enable(True)
			return
		
		if self.f2s_TreeManejo.GetItemText(self.idItem)=='[Texto para Original]' or self.f2s_TreeManejo.GetItemText(self.idItem)=='[Texto para Copia]':
			self.f2s_AdicionTexto.Enable(True)
			self.f2s_BtnEditar.Enable(False)
			self.f2s_BtnBorrar.Enable(False)
			self.f2s_BtnNuevaCopia.Enable(False)
		else:
			self.f2s_AdicionTexto.Enable(False)
			self.f2s_BtnEditar.Enable(True)
			self.f2s_BtnBorrar.Enable(True)
			self.f2s_BtnNuevaCopia.Enable(False)

	def BuscarTradim(self):
		ruta=self.G_ruta + os.sep + self.G_ambiente[-4] + '.tradim'
		return os.path.isfile(ruta)

	def OnAbrirAmbiente(self,evt):
		print 'OnAbrirAmbinte'
		
		archivo = self.f2s_FileAmbiente.GetPath()
		self.G_ruta,self.G_ambiente= os.path.split(archivo)
		leeramb=obEncabezado()
		leeramb.convertir(archivo)
		self.G_formato = leeramb.extraerCampo('NombreFormFrente')
		
		self.f2s_TreeManejo.DeleteAllItems()
		self.listaitems={}
		
		root= self.f2s_TreeManejo.AddRoot('[Control]')
		
		
		rutaAmbiente=self.G_ruta + os.sep + self.G_ambiente[0:-4] + '.tradin.py'
		print 'Abrir Campo:',rutaAmbiente

		if os.path.isfile(rutaAmbiente):
			
			arch=open (rutaAmbiente,'r')
			while True:
				try:
					valor = pickle.load (arch)
					print 'datos',valor
					nombrenodo=valor.keys()
					nombrenodo=nombrenodo[0]
					
					if self.listaitems.has_key(nombrenodo):
						print 'otor'
						nodo=self.listaitems[nombrenodo]
					else:
						nodo = self.f2s_TreeManejo.AppendItem(root,nombrenodo)
						self.listaitems[nombrenodo]=nodo


					nodo2 = self.f2s_TreeManejo.AppendItem(nodo,valor[nombrenodo]["texto"])
					self.f2s_TreeManejo.SetItemPyData(nodo2,valor[nombrenodo])


				except:
					break
				
			arch.close()

		else:
			self.f2s_TreeManejo.AppendItem(root,"[Texto para Original]")    
			self.f2s_TreeManejo.AppendItem(root,"[Texto para Copia]")
		
		self.InicioBotones()
		self.f2s_BtnNuevaCopia.Enable(True)




	def InicioBotones(self):
		self.f2s_AdicionTexto.Enable(False)
		self.f2s_BtnEditar.Enable(False)
		self.f2s_BtnBorrar.Enable(False)
		self.f2s_BtnNuevaCopia.Enable(False)

	def OndiagTexto(self,evt):
		if self.idItem==None: return None	
		j=obTrafico(self.Parent)
		j.visualizar()
		print j.estado
		if j.estado==0: return None
		print 'guardar'
		nodo = self.f2s_TreeManejo.AppendItem(self.idItem,j.texto)
		valor=j.getValor()
		self.f2s_TreeManejo.SetItemPyData(nodo,valor)
		evt.Skip()

	def OnCambiado(self,evt):
		print 'OnCambiado:',self.f2s_TreeManejo.GetItemText(evt.GetItem())
		self.idItem=evt.GetItem()
		self.BotonControl()
		
	def OnItemActivado(self,evt):
		self.idItem=evt.GetItem()
		print 'OnItemActivado:',self.f2s_TreeManejo.GetItemText(self.idItem)
		if self.f2s_TreeManejo.GetItemText(self.idItem) =="[Texto para Original]": return
		if self.f2s_TreeManejo.GetItemText(self.idItem) =="[Texto para Copia]":return
		if self.f2s_TreeManejo.GetItemText(self.idItem) =="[Control]":return
		objtexto= self.f2s_TreeManejo.GetItemPyData(self.idItem)
		print objtexto
		self.editar(objtexto)
		
	def OnEditar(self,evt):
		objtexto= self.f2s_TreeManejo.GetItemPyData(self.idItem)
		print objtexto
		self.editar(objtexto)
		evt.Skip()	
		
	def OnBorrar(self,evt):
		print "borrar"
		self.f2s_TreeManejo.Delete(self.idItem)
		evt.Skip()
		
	def editar(self,objtexto=None):
		print 'editar'

		if self.f2s_TreeManejo.GetItemText(self.idItem) =="[Texto para Original]": return
		if self.f2s_TreeManejo.GetItemText(self.idItem) =="[Texto para Copia]":return
		if self.f2s_TreeManejo.GetItemText(self.idItem) =="[Control]":return

		j=obTrafico(self.Parent)
		if objtexto !=None:
			print "asignar"
			j.setValor(objtexto)
		j.visualizar()
		if j.estado==0: return None
		print 'guardar'
		self.f2s_TreeManejo.SetItemText(self.idItem,j.texto)
		valor=j.getValor()
		print valor
		self.f2s_TreeManejo.SetItemPyData(self.idItem,valor)		

	def OnGuardar(self,evt):
		print "Guardar archivo"
		root= self.f2s_TreeManejo.GetRootItem()
		print self.f2s_TreeManejo.GetItemText(root)		
		(nodo1, cookie1) = self.f2s_TreeManejo.GetFirstChild(root)
		#Cambiar el nombre de los formatos .frm .eps
		if not self.VerfFormatos():return False
		#cambiar el nombre de ambiente tradin
		if not self.VerfAmbiente():return False
		#Crear .tradin
		if self.CrearAmbTrafico()==None:return False
		
		while nodo1.IsOk():
			print "nive1:", self.f2s_TreeManejo.GetItemText(nodo1)
			(nodo2, cookie2) = self.f2s_TreeManejo.GetFirstChild(nodo1)
			self.GuardarItem(self.f2s_TreeManejo.GetItemText(nodo1))
			#verificar si es copia o original para definir el nombre del formato
			#guardar en el ambiente.tradin la relacion tipo ->formato
			inicio_nodo=0
			
			while nodo2.IsOk():
				print "nive2:", self.f2s_TreeManejo.GetItemText(nodo2)
				valor = self.f2s_TreeManejo.GetPyData(nodo2)		
				self.GenerarCampos(self.f2s_TreeManejo.GetItemText(nodo1), valor)
				self.GenerarFormato(self.f2s_TreeManejo.GetItemText(nodo1), valor,inicio_nodo)
				inicio_nodo=1	
				(nodo2, cookie2) = self.f2s_TreeManejo.GetNextChild(nodo1,cookie2)

			(nodo1, cookie1) = self.f2s_TreeManejo.GetNextChild(root,cookie1)
		#guardar datos orden y control
		self.GuardarOrdenControl()
		
	def GenerarCampos(self,grupo,campo):
		print 'Guardar Campo'
		
		guardar={grupo:campo}
		rutaAmbiente=self.G_ruta + os.sep + self.G_ambiente[0:-4] + '.tradin.py'
		arch=open (rutaAmbiente,'a')
		pickle.dump(guardar, arch)
		arch.close()
			
	def GenerarFormato(self,grupo,campo,nuevo):
		print 'GenerarFormato'
		
		rutaformato=  self.G_ruta.replace ('Ambientes', 'Formatos') + os.sep
		print self.G_formato
		
		if grupo =="[Texto para Original]": 
			guardar='%s%s__Trafico_Original' %(rutaformato,self.G_formato)
		else:
			guardar='%s%s__Trafico_copia' %(rutaformato,self.G_formato)
		print guardar

		
		escape=chr(27)
		salida='%s(s1p4101t3b%sV%s*p%sx%sY%s' %(escape,campo['alto'],escape,campo['posx'],campo['posy'],campo['texto'])
		
		if nuevo==0: 
			self.MoverArchivo(guardar + '.frm')
			arch=open(guardar + '.frm','wb')
		else:
			arch=open(guardar + '.frm','ab')
			
		arch.write(salida)
		arch.close()

		campo['posx'] = self.ConvPclPS(campo['posx'],0)
		campo['posy'] = self.ConvPclPS(campo['posy'],1)
		salida ='/Helvetica findfont %s scalefont setfont\n' %(campo['alto'])
		salida +='%s %s moveto\n' % (campo['posx'],campo['posy'])
		if campo['rotar'] >0:			salida +='%s rotate \n' %(campo['rotar'])
		salida += '(%s) show\n' %(campo['texto'])
		if campo['rotar'] >0:			salida +='-%s rotate \n' %(campo['rotar'])
		
		if nuevo==0: 
			self.MoverArchivo(guardar + '.eps')
			arch=open(guardar + '.eps','wb')
		else:
			arch=open(guardar + '.eps','ab')

		arch.write(salida)
		arch.close()

		
				#convertir la unidades de medida a pulgadas   1440 -> 1
				#generar archivo de formato PCL
				#invertir punto de inicio del eje Y
				#convertir de pulgadas a puntos           1 ->72
				#genera archivo de formato ps 		
		
		
	def ConvPclPS(self,valor,rotar=0):
		pos= valor/1440.0
		if rotar==1: 		pos=11-pos
		pos=pos * 72
		return pos
	
		
		
	def GuardarOrdenControl(self):	
		rutaAmbiente=self.G_ruta + os.sep + self.G_ambiente[0:-4] + '.tradin'
		arch=open (rutaAmbiente,'a')
		valor=self.f2s_ChOrden.GetSelection()
		guardar='#orden de salida\r\n#0=Original al principio\r\n#1=Original al final\r\n'
		guardar+='orden<|>%i\r\n'%(valor)
		valor=self.f2s_ChControl.GetSelection()
		guardar+='#Si por dentro del archivo se controla la copia se activa esta opcion\r\n'
		guardar+='Control<|>%i\r\n' %(valor)
		arch.write(guardar)
		arch.close()	
			
	def GuardarItem(self,texto):
		if texto =="[Texto para Original]": 
			guardar='#relacion formato original\r\noriginal<|>%s__Trafico_Original\r\n' %(self.G_formato)
		else:
			guardar='#relacion formato copia\r\ncopia<|>%s__Trafico_Copia\r\n' %(self.G_formato)
		rutaAmbiente=self.G_ruta + os.sep + self.G_ambiente[0:-4] + '.tradin'
		arch=open (rutaAmbiente,'a')
		arch.write(guardar)
		arch.close()
		
			
		print guardar
		
	def VerfAmbiente(self):
		print "VerfAmbiente"
		if not self.GeneraArcAmbiente('.tradin'):return False
		print '----------------------'
		print "alimentador de campos"
		print '----------------------'
		if not self.GeneraArcAmbiente('.tradin.py'):return False
		print '----------------------'
		return True
	
	def GeneraArcAmbiente(self,nombre):
		print 'GeneraArcAmbiente\n----------------------'
		print self.G_ambiente
		rutaAmbiente=self.G_ruta + os.sep + self.G_ambiente[0:-4]  + nombre
		print "Ambiente final:", rutaAmbiente
		if	not os.path.isfile(rutaAmbiente):return True
		if	not self.MoverArchivo(rutaAmbiente):
			mensaje="No es posible renombar archivo:[%s]"%(rutaAmbiente)
			wx.MessageBox(mensaje,'Error',wx.ICON_ERROR)
			return False
		return True
	
	def CrearAmbTrafico(self):
		rutaAmbiente=self.G_ruta + os.sep + self.G_ambiente[0:-4] + '.tradin'
		try:
			archivo=open(rutaAmbiente,'w')
			texto='#El trafico dinamico: utilizado cuando se tiene el mismo formato pero se necesita que el trafico en texto tenga varias posiciones.\r\n'
			archivo.write(texto)
			archivo.close()
			return rutaAmbiente

		except:
			mensaje="Error en la creacion de ambiente [%s]" %(rutaAmbiente)
			wx.MessageBox(mensaje,'Error',wx.ICON_ERROR)
			return None
		
	def VerfFormatos(self):
		print "VerfFormatos"
		print '----------------------'
		print self.G_ambiente
		print self.G_formato
		rutaformato=self.G_ruta[0:-9] + 'Formatos' + os.sep
		print rutaformato		
		print '----------------------'
		if  not os.path.isdir(rutaformato):
			wx.MessageBox("Error: No existe la ruta para los formatos",'Error',wx.ICON_ERROR)
			return False
		
	
		lista=['_original.frm','_copia.frm','_original.eps','_copia.eps']
		rutaformato+= self.G_formato
		for nombre in lista:
			if not os.path.isdir (rutaformato+self.G_formato + nombre): continue
			if not self.MoverArchivo(rutaformato+nombre):
				mensaje="No es posible renombar archivo:[%s]"%(rutaformato+self.G_formato)
				wx.MessageBox(mensaje,'Error',wx.ICON_ERROR)
				return False
		
		return True
		
		

	def MoverArchivo(self,ruta):
		print "Mover Archivo"
		#Si no exite formatos sale
		if not os.path.isfile(ruta): return True
		
		temp=ruta
		contador=1
		while os.path.isfile(temp):
			temp=ruta + '.%i'%(contador)
			print temp
			contador+=1
		try:
			os.rename(ruta, temp)
			return True
		except:
			return False

			
if __name__ == '__main__':
	aplicacion=wx.PySimpleApp()
	frame_usuario = IncioInterface()			
	frame_usuario.Show()
	aplicacion.MainLoop()
