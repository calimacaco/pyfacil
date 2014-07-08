#!/usr/bin/env python
# -*- coding: utf-8 -*- 
'''
Created on 13/03/2014

@author: marco
'''
import os,sys
import ctypes 

from registro import  RegistroWindows


class Revision(ctypes.Structure):
	_fields_ = [
        ("producto", ctypes.c_char),
        ("copyright", ctypes.c_char),
        ("revision", ctypes.c_long),
        ("revisiondate", ctypes.c_long)
        ]

class GhostscriptError(RuntimeError):
	def __init__(self, ecode):
		# :todo:
		RuntimeError.__init__(self, error2name(ecode))



class ObjGS():
	def __init__(self,ArchivoEntrada="",ArchivoSalida=""):
		self.nombre=ArchivoEntrada
		self.salida=ArchivoSalida
		self.gs=None

	def delete_instance(self,instance):
		"""
	    Destroy an instance of Ghostscript
	    
	    Before you call this, Ghostscript must have finished.
	    If Ghostscript has been initialised, you must call exit()
	    before delete_instance()
	    """
		return self.gs.gsapi_delete_instance(instance)


	def Instanciar(self):
		Registro=RegistroWindows()
		gsEjecutar = Registro.BuscarGS()
		gsEjecutar = gsEjecutar.lower()
		self.gs=ctypes.windll.LoadLibrary (gsEjecutar)
		gs_main_instance = ctypes.c_void_p
		instance = gs_main_instance()
		display_callback=None		
		rc = self.gs.gsapi_new_instance(ctypes.pointer(instance), display_callback)
		
		if rc != 0:
			raise GhostscriptError(rc)

		return instance



	def init_with_args(self,instance, argv):
		"""
	    Initialise the interpreter.
	
	    1. If quit or EOF occur during init_with_args(), the return value
	       will be e_Quit. This is not an error. You must call exit() and
	       must not call any other functions.
	       
	    2. If usage info should be displayed, the return value will be
	       e_Info which is not an error. Do not call exit().
	       
	    3. Under normal conditions this returns 0. You would then call one
	       or more run_*() functions and then finish with exit()
	    """
		ArgArray = ctypes.c_char_p * len(argv)
		c_argv = ArgArray(*argv) 
		rc = self.gs.gsapi_init_with_args(instance, len(argv), c_argv)
		if not rc==0:# not in (0, e_Quit, e_Info):
			raise GhostscriptError(rc)
		return rc
	
	def ProcesarPCL(self):
		Orientacion = self.Orientacion()
		instancia = self.Instanciar()
		print instancia
		args = [
		    "ps2pdf",	# actual value doesn't matter
		    "-sFONTPATH=c:/windows/fonts",
		    "-dNOPAUSE",
		    "-dBATCH",
		    "-dSAFER",
		    "-sDEFAULTPAPERSIZE=letter",
		    "-sDEVICE=ljet4",
		    "-sOutputFile=%s" %(self.salida),
		    "-f",
		    self.nombre
	    ]

		if Orientacion: #LandScape
			args.append('-c "<</Orientation 3>> setpagedevice"')
	
		print args
		code = self.init_with_args(instancia, args)
		#code1 = self.gs.exit(instance)
		self.delete_instance(instancia)	
		#editar pcl y tranformar
		arcpcl=open(self.salida ,'rb')
		datos=arcpcl.read()
		arcpcl.close()
		if Orientacion:
			datos1= "%s*r1F%s*p6000x0Y" % (chr(27) ,chr(27))
		else:
			datos1=chr(27) + "*p20x360Y"
		datos=datos1 + datos[75:-1]
		arcpcl=open(self.salida,'wb')
		arcpcl.write(datos)
		arcpcl.close()
		
		
		
#		gsEjecutar = "gs.exe"#gsEjecutar.replace('.dll', '.exe')
#		ejecutar = '"%s" -sFONTPATH=c:/windows/fonts -dNOPAUSE  -dBATCH -sDEVICE=ljet4 -sOutputFile="%s.frm" ' % (gsEjecutar, self.salida)
		
#		if Orientacion: #LandScape
#			ejecutar +='-c "<</Orientation 3>> setpagedevice" -f "%s.frm"' % (self.nombre)
#		else:			#Verical
#			ejecutar +='-f "%s"' % (self.nombre)		
#		print ejecutar
		
	def Orientacion(self):
		archivo=open (self.nombre,'rb')
		datos=archivo.read(384)
		#print datos
		archivo.close()
		datos = datos.upper()
		landscape=False
		if  datos.find('LANDSCAPE')>-1:
			landscape=True
		return landscape
		
		#clipk Andico 3415993 3312779199 nit 900.618620-5 avd. jimenez 7-25 of 603 henrry faux

	def ProcesarPNG(self):
		print "procesar png"
		instancia = self.Instanciar()
		print self.salida
		if self.salida[-3:].lower()=='frm':
			salida=self.salida[:-3]+'png'
		else:
			salida=self.salida+'.png'
			
		args = [
		    "ps2png",	# actual value doesn't matter
		    "-sFONTPATH=c:/windows/fonts",
		    "-dNOPAUSE",
		    "-dBATCH",
		    "-dSAFER",
		    "-sDEVICE=png16",#png16m,pngalpha
		    "-sOutputFile=%s" %(salida),
		    "-f",
		    self.nombre
	    ]
		print args
		code = self.init_with_args(instancia, args)
		#code1 = self.gs.exit(instance)
		self.delete_instance(instancia)	
		
if __name__ == '__main__':
	prueba=ObjGS('prueba2.ps','formato.frm')
	prueba.Procesar()
	