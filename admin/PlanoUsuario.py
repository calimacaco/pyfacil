# -*- coding: utf-8 -*- 

'''
Created on 21/03/2013

@author: marco
'''

import wx,sys
from basedatos import ObjBase
from FormMapic import D_SubirPlano



class ObjSubirArch():
	'''
	classdocs
	'''

	def __init__(self,padre,base=ObjBase,f_usuario=wx.Frame):
		
		self.f_usuario=f_usuario
		self.f_Subir=D_SubirPlano(padre)
		print "Subir plano usuarios"
		self.f_Subir.SetTitle("Generar Plano")
		self.f_Subir.Center()
		self.f_Subir.Show()
		self.BD=base
		print self.BD.rutabase
		
		self.f_Subir.Dir_Plano.Bind(wx.EVT_FILEPICKER_CHANGED, self.OnProcesar)


	def OnProcesar(self,event):
		texto="Procesando:" + self.f_Subir.Dir_Plano.GetPath()+ '\n'
		self.f_Subir.Lb_Status.SetLabel(texto)
		arch=open(self.f_Subir.Dir_Plano.GetPath(),'r')
		lineas=arch.readlines()
		contador=0
		for linea in lineas:
			contador+=1
			self.f_Subir.Medidor.SetValue(int((contador/len(lineas))*100))
			
			if len (self.f_Subir.Lb_Status.GetLabel())>1000:
				self.f_Subir.Lb_Status.SetLabel('')
			linea=linea[:-1]
			texto=self.f_Subir.Lb_Status.GetLabel() + linea
			campos=linea.split(',')
			campos.append('1')
			if len(campos)!=6:
				texto +=' <- Error de estructura\n'
				self.f_Subir.Lb_Status.SetLabel(texto)
				continue
			else:
				T_campos=['busqueda','dircorreo','imprimir','pdf','correo','estado']
				valores=[campos]
				if self.BD.InsertarVarios('tbl_cliente', T_campos, valores):
					texto+="<-Adicionado \n"
				else:
					texto+="<- Error Campo ya existe\n"
					
			self.f_Subir.Lb_Status.SetLabel(texto)
		self.llenarGrilla()
		wx.MessageBox("Usuarios adicionado","Fin Proceso",wx.ICON_EXCLAMATION)

	def llenarGrilla(self):
		print "Llenar Grilla"
		self.f_usuario.SetTitle(u'Usuarios registrados')
		self.f_usuario.Lst_Usuarios.ClearAll()
		self.f_usuario.Lst_Usuarios.InsertColumn(0,'Id',width=40)		
		self.f_usuario.Lst_Usuarios.InsertColumn(1,'Identificador',width=200)
		self.f_usuario.Lst_Usuarios.InsertColumn(2,'Directorio Correo',width=300)
		self.f_usuario.Lst_Usuarios.InsertColumn(3,'Opciones',width=400)
		
		campos="id, busqueda, dircorreo, imprimir, pdf, correo"
		condicion=""
		tablas="tbl_cliente"
		limite="0,20"
		
		registros=self.ObaseD.LeerCampos(campos,tablas, condicion , "id DESC",limite)
		#print registros
		fila = 0
		if len(registros)<1:
			wx.MessageBox("No hay registro de clientes en este momento","Busqueda",wx.ICON_INFORMATION)
			return
		
		for registro in registros:
			index = self.f_usuario.Lst_Usuarios.InsertStringItem(sys.maxint, str(fila + 1))
			self.f_usuario.Lst_Usuarios.SetStringItem(index,0,str(registro[0]))
			self.f_usuario.Lst_Usuarios.SetStringItem(index,1,registro[1])
			self.f_usuario.Lst_Usuarios.SetStringItem(index,2,registro[2])
			texto=""
			print registro
			
			if registro[3]==1:
				texto="Impresión,"
			if  registro[4]==1:
				texto+="Gen. Pdf,"
			if registro[5]==1:
				texto+="Envio Correo"
			self.f_usuario.Lst_Usuarios.SetStringItem(index,3,texto)
