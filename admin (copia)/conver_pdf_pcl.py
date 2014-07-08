#!/usr/bin/env python
# -*- coding: utf-8 -*- 

'''
Created on 05/03/2013

@author: marco
'''
import glob
import os
#import threading
import time
import wx
if os.name!="posix":
	from librerias.GsDll import ObjGS_dll


from basedatos import ObjBase

#
#class GenpclThread ( threading.Thread ):
#	
#	def __init__(self, num,archpdf,rutags,rutapcl,rutabd,archxdir=10):
#		threading.Thread.__init__(self)
#		self.num = num 
#		self.arch_pdf=archpdf
#		self.rutaGS=rutags
#		self.rutapcl=rutapcl
#		self.archxdir=archxdir
#		self.BuscarRuta()
#		self.archprocesados=0
#		print "guardar en:",self.rutapcl
#		self.bd=rutabd
#		if os.name!="posix":
#			self.GS=ObjGS_dll()
#
#	def BuscarRuta(self):
#		
#		inicio=True
#		cuenta=1
#		for raiz ,directorio, archivos in os.walk(self.rutapcl):
#			if inicio:
#				inicio=False
#			else:
#				cuenta +=1
#				print "cantidad de archivos:",len (archivos),archivos
#				if len (archivos)<self.archxdir:
#					self.rutapcl=raiz
#					return True
#		self.rutapcl=self.rutapcl + os.sep + str(cuenta)
#		os.mkdir(self.rutapcl)
#		
#			
#
#	def run ( self ):
#		ruta,nombre=os.path.split(self.arch_pdf)		
#		id,ext=nombre.split(".")
#		nombre=self.rutapcl + os.sep + nombre + ".pcl"
#		print 'Soy el hilo=%i archivo [%s] nombre[%s]'%(self.num,self.arch_pdf,nombre)		
#		print id,self.num,self.arch_pdf,nombre
#		print "guarda en base:",self.bd
#		valores="'%s','%s','%s','1'" % (id,self.arch_pdf,nombre)
#		bd=ObjBase(self.bd)
#		bd.CrearTablaTempProc()
#		#adiciona a la base de datos el nombre y archivo pdf archivo pcl
#		#inserto=bd.Insertar('tbl_Adjuntos', 'nombre,dirpdf,dirpcl,estado', valores)		
#		buscar=bd.SelectUno('nombre','tbl_Adjuntos',"nombre='"+ id +"'")
#	
#		if not buscar==None:
#			print "ya Existe"
#			return		
#		print "procesado ;",self.num
#		if os.name=="posix":
#			argumento='gs -dNOPAUSE -dBATCH -dQUIET -sDEVICE=ljet4 -sOutputFile="%s" "%s"' %(nombre,self.arch_pdf)
#			print argumento		
#			os.system(argumento)
#		else:
#			print "Generar PCL"
#			self.GS.GenPCL(self.arch_pdf,nombre)
#			self.archprocesados +=1
#
#		print "@nombre salida:",nombre
#		if  os.path.isfile(nombre):
#			print "@Generado"
#			inserto=bd.Insertar('tbl_Adjuntos', 'nombre,dirpdf,dirpcl,estado', valores)
#			if inserto:
#				valores="'%s','%s','1'" % (self.arch_pdf,nombre)
#				bd.Insertar("tbl_temp1",'rutapdf, rutapcl ,estado',valores)
#				print "@guardado en base"
#		else:
#			valores="'%s','%s','0'" % (self.arch_pdf,nombre)
#			bd.Insertar("tbl_temp1",'rutapdf, rutapcl ,estado',valores)
#			
#
#
#
#		print "@procesados" , self.archprocesados


class ObConversor():
	'''
	classdocs
	'''


	def __init__(self):
		'''
		Constructor
		'''
		self.VerificarTablas=False
		self.rutaEntrada=""
		self.rutaSalida=""
		self.rutaGS=""
		self.nroarch=5
		self.bd=None
		self.mensaje=None
		

		
	def Procesar(self,lista):
		#genera la carpetas contenedoras
		archprocesados=0
		cantidad=len(lista)
	
		for i in lista:		
			self.mensaje.SetValue(self.mensaje.GetValue()+'\n'+ i)
			self.proceso1(1,i,self.rutaGS,self.rutaSalida,self.bd,self.nroarch)
			self.proceso2()
			
		
		
		#	
	def TotalPDF(self):
		total=0
		for root,dir,file in os.walk(self.rutaEntrada):
			print root
			lista = glob.glob(root+"/*.pdf")
			total +=len(lista)
		return total
	
	def PDFaPCL(self):
		print "PDFaPCL"
		
		
		if not os.path.isdir(self.rutaSalida):
			os.mkdir(self.rutaSalida)

		
		
		#lista = glob.glob(self.rutaEntrada+"*.pdf")
		#print lista

		#self.TotalPDF()
		
		for root,dir,file in os.walk(self.rutaEntrada):
			print root
			lista = glob.glob(root+"/*.pdf")
			print lista
			if len(lista)>0:
				self.Procesar(lista)



		
			print "------------------------------------------------------"
			#print dir
			#file
		wx.MessageBox("Proceso Terminado")
		
	def oMensaje(self,texto):
		
		self.mensaje=texto
		#.SetValue("Aqui estoy en esto")


	def proceso1(self, num,archpdf,rutags,rutapcl,rutabd,archxdir=10):
		self.num = num 
		self.arch_pdf=archpdf
		self.rutaGS=rutags
		self.rutapcl=rutapcl
		self.archxdir=archxdir
		self.BuscarRuta()
		self.archprocesados=0
		print "guardar en:",self.rutapcl
		self.bd=rutabd
		if os.name!="posix":
			self.GS=ObjGS_dll()

	def BuscarRuta(self):
		
		inicio=True
		cuenta=1
		for raiz ,directorio, archivos in os.walk(self.rutapcl):
			if inicio:
				inicio=False
			else:
				cuenta +=1
				print "cantidad de archivos:",len (archivos),archivos
				if len (archivos)<self.archxdir:
					self.rutapcl=raiz
					return True
		self.rutapcl=self.rutapcl + os.sep + str(cuenta)
		os.mkdir(self.rutapcl)
		
			

	def proceso2 ( self ):
		ruta,nombre=os.path.split(self.arch_pdf)		
		id=nombre[0:-4]
		print "***********************************************"
		nombre=self.rutapcl + os.sep + nombre + ".pcl"
		print 'Soy el hilo=%i archivo [%s] nombre[%s]'%(self.num,self.arch_pdf,nombre)		
		print id,self.num,self.arch_pdf,nombre
		print "guarda en base:",self.bd
		valores="'%s','%s','%s','1'" % (id,self.arch_pdf,nombre)
		bd=ObjBase(self.bd)
		archtemporal=file("temporal.log",'a')
		if self.VerificarTablas==False:
			bd.CrearTablaTempProc()
			self.VerificarTablas=True
		#adiciona a la base de datos el nombre y archivo pdf archivo pcl
		#inserto=bd.Insertar('tbl_Adjuntos', 'nombre,dirpdf,dirpcl,estado', valores)		
		buscar=bd.SelectUno('nombre','tbl_Adjuntos',"nombre='"+ id +"'")
	
		if not buscar==None:
			print "ya Existe"
			archtemporal.write (id + ',ya exite,' + nombre + '\n')
			return		
		archtemporal.write (id + ',nuevo,' + nombre)

		print "procesado ;",self.num
		if os.name=="posix":
			argumento='gs -dNOPAUSE -dBATCH -dQUIET -sDEVICE=ljet4 -sOutputFile="%s" "%s"' %(nombre,self.arch_pdf)
			print argumento		
			os.system(argumento)
		else:
			print "Generar PCL"
			self.GS.GenPCL(self.arch_pdf,nombre)
			self.archprocesados +=1

		print "@nombre salida:",nombre
		if  os.path.isfile(nombre):
			print "@Generado"
			print valores
			inserto=bd.Insertar('tbl_Adjuntos', 'nombre,dirpdf,dirpcl,estado', valores)
			if inserto:
				valores="'%s','%s','1'" % (self.arch_pdf,nombre)
				bd.Insertar("tbl_temp1",'rutapdf, rutapcl ,estado',valores)
				print "@guardado en base"
				archtemporal.write (',gardado bd\n')

		else:
			valores="'%s','%s','0'" % (self.arch_pdf,nombre)
			bd.Insertar("tbl_temp1",'rutapdf, rutapcl ,estado',valores)
			archtemporal.write (',no gardado bd\n')

		print "@procesados" , self.archprocesados
		
		
if __name__ == '__main__':
	# Lanzamos aplicación.
	j=ObConversor()
	j.rutaEntrada="/home/marco/clientes/XEROX/sanofi"
	j.rutaSalida="/home/marco/borrar/pcl1"
	j.rutaGS="c:/Program Files/gs/gs9.07/bin/gswin32.exe"
	j.bd="config.db"
	
	
	
	j.PDFaPCL()
		