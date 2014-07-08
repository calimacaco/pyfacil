'''
Created on 26/03/2014

@author: marco
'''
#pertenecia=5   -Generales
#valor =1 ruta de ambiente

import wx
import glob, os, sys


from FormMapic import  D_Generales
from basedatos import ObjBase

class objGeneral():

	def __init__(self,padre,base):
		self.ObaseD=base
		self.padre=padre
		self.salida=None
		
		self.formato=D_Generales(padre)
		
		self.formato.Bind(wx.EVT_BUTTON, self.onSalir, self.formato.f2s_btnCancelar)
		self.formato.Bind(wx.EVT_BUTTON, self.onGuardar,self.formato.f2s_BtnGuadar)
		self.formato.Bind(wx.EVT_DIRPICKER_CHANGED,self.onLeer,self.formato.f2s_dirModelos)
		
		self.Abrir()		
		self.formato.ShowModal()

	def onSalir(self,event):
		event.Skip()
		self.formato.Destroy()

	def GuardarRutaModelo(self):
		#Ruta Modelos
		ruta=''
		ruta=self.formato.f2s_dirModelos.GetPath()
		if len(ruta.strip())==0: 
			return False
		rutaDBase=self.ObaseD.Gen_rutaModelos()
		if not self.guardar(ruta,rutaDBase,1):	
			return False
		return True
	def GuardarRutaArchivo(self):	#ruta Envio Archivo
		print "GuardarRutaArchivo"
		ruta=self.formato.f2s_DirArchivo.GetPath()
		if len(ruta.strip())==0: 
			return False
		rutaDBase=self.ObaseD.Gen_rutaPrgEnvioArchivo()
		if not self.guardar(ruta,rutaDBase,2):
			return False
		return True
	def GuardarEnvioCorreo(self):
			#ruta Envio Correo
		ruta=self.formato.f2s_dirCorreo.GetPath()
		if len(ruta.strip())==0: 
			return False
		rutaDBase=self.ObaseD.Gen_rutaPrgEnvioCorreo()
		if not self.guardar(ruta,rutaDBase,3):
			return False
		return True

	def onGuardar(self,event):
		self.GuardarRutaModelo()
		self.GuardarRutaArchivo()
		self.GuardarEnvioCorreo()

		event.Skip()
	def guardar(self,ruta,rutaDBase,posicion):
		if not os.path.isdir(ruta):
			wx.MessageBox("No existe directorio:%s" %(ruta),"Error",wx.ICON_ERROR)
			return False
		if rutaDBase ==None:
			self.insertar(posicion,ruta)
		elif ruta != rutaDBase :
			self.actualizar(posicion,ruta)
		return True
	
	def insertar(self,valor,ruta):
		tabla="tbl_Estado"
		campos="texto,pertenecia,valor"
		valores="'%s',%i,%i" %(ruta,5,valor)
		self.indice=self.ObaseD.Insertar(tabla, campos, valores)
		wx.MessageBox("Guadardo","Estado",wx.ICON_ASTERISK)

	def actualizar(self,valor,ruta):
		tabla="tbl_Estado"
		campos={"texto":ruta}
		self.ObaseD.ActualizarCampos(tabla,campos,"pertenecia=5 and valor=%i" %(valor))
		wx.MessageBox("Actualizado","Estado",wx.ICON_ASTERISK)
				
	def inicioLista(self):
		self.formato.f2s_LstAmbientes.ClearAll()
		self.formato.f2s_LstAmbientes.InsertColumn(0,"Ambientes",width=240)

	def leerRutaArchivo(self):
		'''Leer la ruta donde se encuentra el programa RutaArchivo'''
		##############
		#Ruta Envio Archivo		
		print "obj.Generales.leerRutaArchivo"
		ruta=self.ObaseD.Gen_rutaPrgEnvioArchivo()
		if not ruta==None:
			ruta=ruta[0]
			if not self.verifRuta(ruta):
				return
			self.formato.f2s_DirArchivo.SetPath(ruta)
			self.formato.f2s_DirArchivo.Refresh()
		

	def leerRutaModelos(self):
		'''Leer la ruta donde se encuentra La carpeta modelos'''
		##############
		#Ruta Modelos
		print "obj.Generales.leerRutaModelos"
		ruta=self.ObaseD.Gen_rutaModelos() # .SelectUno("texto", "tbl_Estado", "pertenecia=5 and valor=1")
		if not ruta==None:
			ruta=ruta[0]
			if not self.verifRuta(ruta):
				return
			self.formato.f2s_dirModelos.SetPath(ruta)  #.f2s_txtRutaParametros.SetValue(ruta)
			self.formato.f2s_dirModelos.Refresh()
			self.llenar(ruta)

	def leerRutaCorreo(self):
		'''Leer la ruta donde se encuentra el programa pyCorreo'''		
		##############
		#Ruta Envio Correo		
		ruta=self.ObaseD.Gen_rutaPrgEnvioCorreo()
		if not ruta==None:
			ruta=ruta[0]
			if not self.verifRuta(ruta):
				return
			self.formato.f2s_dirCorreo.SetPath(ruta)
			self.formato.f2s_dirCorreo.Refresh()
		

	def Abrir(self):
		self.inicioLista()
		self.leerRutaModelos()
		self.leerRutaArchivo()
		self.leerRutaCorreo()
		
			
			
	def verifRuta(self,ruta):
		print ruta
		if not os.path.isdir(ruta):
			wx.MessageBox("No existe directorio:\n%s"%(ruta),"Error",wx.ICON_ERROR)
			return False
		return True

	def onLeer(self,event):
		print "onLeer"
		self.inicioLista()
		#self.formato.f2s_txtRutaParametros.SetValue(self.formato.f2s_dirPicker.GetPath())
		ruta=self.formato.f2s_dirPicker.GetPath() #.f2s_txtRutaParametros.GetValue()
		self.llenar(ruta)
		event.Skip()

		
	def llenar(self,ruta):
		print "llenar:", ruta
		ruta +=os.sep + "Ambientes"

		if not os.path.isdir(ruta):
			wx.MessageBox("No existe directorio:[%s]"%ruta,"Error grave",wx.ICON_ERROR)
			return
		
		for extension in ["*.dim","*.amb"]:
			for lista in glob.glob(ruta + os.sep + extension):
				self.formato.f2s_LstAmbientes.InsertStringItem(sys.maxint,lista.replace(ruta + os.sep, ''))
		
