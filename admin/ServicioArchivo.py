#!/usr/bin/env python
# -*- coding: utf-8 -*- 
'''
Created on 27/03/2014

@author: marco
'''

import wx
import sys,os
import subprocess


from FormMapic import  D_AdminServArchivo
from basedatos import ObjBase


if os.name =='nt':
	from serviciowin import WService
	from librerias.registro import RegistroWindows

class ObjServArchivo():
	'''
	classdocs
	'''

	def __init__(self,padre,base):	
		print "ObjRelArchivo"
		self.ObaseD=base
		self.padre=padre
		self.listaAcciones=[]
		
		self.formato=D_AdminServArchivo(padre)
		self.formato.Bind(wx.EVT_BUTTON,self.onCrearServicio,self.formato.f2s_BtnCrear)
		self.formato.Bind(wx.EVT_BUTTON, self.onSalir, self.formato.f2s_btnCancelar)
		self.formato.Bind(wx.EVT_BUTTON,self.onStartSRV,self.formato.f2s_BtnIniciar)
		self.formato.Bind(wx.EVT_BUTTON,self.onRefrescar,self.formato.f2s_btnRefrescar)
		self.formato.Bind(wx.EVT_BUTTON,self.onStopSRV,self.formato.f2s_btnDetener)
		self.formato.Bind(wx.EVT_LIST_ITEM_SELECTED,self.onActivarSeleccion,self.formato.f2s_lstServicios)
		self.formato.Bind(wx.EVT_LIST_ITEM_DESELECTED,self.onDesSeleccion,self.formato.f2s_lstServicios)

		
		
		self.leerTabla()
		
		self.SwicheBotones(False)
		self.formato.f2s_BtnCrear.Enable(False)
		self.formato.ShowModal()
		
	def onRefrescar(self,event):
		self.leerTabla()
		
	def onStopSRV(self,event):
		print "onStopSRV"
		if os.name =='nt':
			puntero= self.formato.f2s_lstServicios.GetFirstSelected()
			registro = self.listaAcciones[puntero]
			print registro
			if registro[2]==3 or registro[2]==4:
				nombre="FacilArchivo_id%i" %(registro[0])
				servicio = WService(nombre)
				servicio.stop()
				self.leerTabla()
	
	def onStartSRV(self,event):
		print "onStartSRV"
		if os.name =='nt':
			puntero= self.formato.f2s_lstServicios.GetFirstSelected()
			registro = self.listaAcciones[puntero]
			print registro
			if registro[2]==1 or registro[2]==2:
				nombre="FacilArchivo_id%i" %(registro[0])
				servicio = WService(nombre)
				servicio.start()
				self.leerTabla()
		
		
		
	def onDesSeleccion(self,event):
		self.SwicheBotones(False)
		self.formato.f2s_BtnCrear.Enable(False)
		
	def onActivarSeleccion(self,event):
		puntero= self.formato.f2s_lstServicios.GetFirstSelected()
		if self.listaAcciones[puntero][2]==0:
			self.SwicheBotones(False)
		else:
			self.SwicheBotones(True)
		
		
		
	def onCrearServicio(self,event):
		print "onCrearServicio"
		puntero= self.formato.f2s_lstServicios.GetFirstSelected()
		registro = self.listaAcciones[puntero]
		rutaprg = self.ObaseD.Gen_rutaPrgEnvioArchivo()
		rutaprg = rutaprg[0] + os.sep + "srvany.exe" 
		if not os.path.isfile(rutaprg):
			wx.MessageBox("No esta el programa:\n%s" %(rutaprg),"Error",wx.ICON_ERROR)
			return
		
		if os.name =='nt':
			ejecutar ='sc create "FacilArchivo_id%i" binPath= "%s" DisplayName= "%s"' %(registro[0],rutaprg,registro[1])
			a=subprocess.call(ejecutar)
			wReg=RegistroWindows()
			llave="System\\CurrentControlSet\\services\\FacilArchivo_id%i\\Parameters"%(registro[0])
			lugar='Application'
			valor=rutaprg.replace('srvany.exe', 'envioarchivo.exe') + ' -b "%s" ' %(self.ObaseD.rutabase) + "-i %i" %(registro[0])
			wReg.GuardarReg(llave,lugar,valor)
			self.leerTabla()

		
	def onSalir(self,event):
		self.formato.Destroy()

	def SwicheBotones(self,valor):
		self.formato.f2s_BtnIniciar.Enable(valor)
		self.formato.f2s_btnDetener.Enable(valor)
		self.formato.f2s_BtnCrear.Enable(not(valor))

	def InicioGrilla(self):
		self.formato.f2s_lstServicios.ClearAll()
		self.formato.f2s_lstServicios.InsertColumn(0,"Id",width=20)
		self.formato.f2s_lstServicios.InsertColumn(1,"Servicio",width=150)
		self.formato.f2s_lstServicios.InsertColumn(2,"Estado",width=150)


#

	def leerTabla(self):
		campos="id,proceso"
		self.InicioGrilla()
		listaAcciones=self.ObaseD.LeerCampos(campos,"tbl_envioarch")
		print listaAcciones
		self.listaAcciones=[]
		for registro in listaAcciones:
			puntero = self.formato.f2s_lstServicios.InsertStringItem(sys.maxint,str(registro[0]))
			self.formato.f2s_lstServicios.SetStringItem(puntero,1,registro[1])
			idservicio="FacilArchivo_id%i" %(registro[0])
			if os.name =='nt':
				sw=WService(idservicio)
				if sw.errores:
					self.formato.f2s_lstServicios.SetStringItem(puntero,2,"No Creado")
					self.listaAcciones.append([registro[0],registro[1],0])
					self.formato.f2s_lstServicios.SetItemBackgroundColour(puntero,(244,170,170))

				else:
					print "estado:" , sw.status()

					if sw.status()=='STOPPED':
						self.formato.f2s_lstServicios.SetStringItem(puntero,2,"Detenido")
						self.formato.f2s_lstServicios.SetItemBackgroundColour(puntero,(255,153,85))

						self.listaAcciones.append([registro[0],registro[1],1])
					if sw.status()=='STOPPING':
						self.formato.f2s_lstServicios.SetStringItem(puntero,2,"Deteniendose")
						self.listaAcciones.append([registro[0],registro[1],2])
						self.formato.f2s_lstServicios.SetItemBackgroundColour(puntero,(255,221,85))

					if sw.status()=='STARTING':
						self.formato.f2s_lstServicios.SetStringItem(puntero,2,"Iniciando")
						self.listaAcciones.append([registro[0],registro[1],3])
						self.formato.f2s_lstServicios.SetItemBackgroundColour(puntero,(188,221,95))

					if sw.status()=='RUNNING':
						self.formato.f2s_lstServicios.SetStringItem(puntero,2,"En Ejecucion")
						self.listaAcciones.append([registro[0],registro[1],4])
						self.formato.f2s_lstServicios.SetItemBackgroundColour(puntero,(127,255,42))
