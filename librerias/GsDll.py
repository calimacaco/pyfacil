# -*- coding: cp1252 -*-

'''
Created on 05/01/2013

@author: marco
'''
from ctypes import windll,c_char_p,c_long, pointer, sizeof, Structure,c_void_p
from registro import RegistroWindows

 
class gsapi_revision_t(Structure):
	_fields_ = [('product', c_char_p),
            ('copyright', c_char_p),
            ('revision', c_long),
            ('revisiondate', c_long)]


class ObjGS_dll():
	'''
	Objecto Manejador de gsdll32.dll
	'''

	def __init__(self):
		self.Gsdll=None
		self.ruta=''


	def BuscarGS(self):		
		ubicar=RegistroWindows()
		llave="Software\\GPL Ghostscript"
		if ubicar.defKey(llave):
			ultima=ubicar.ListaKey()
			llave+= '\\%s'%(ultima[-1])
			print llave
			ubicar.defKey(llave)	
			print ubicar.ListarValor()
			self.ruta,tipo = ubicar.LeerReg ("GS_DLL")
			#self.Gsdll=windll.LoadLibrary(ruta)
			
			print self.ruta
			print tipo
			return True
		else:
			print "error 1"
			return False
		
		
		
		

	
	def Revision(self):
		r =gsapi_revision_t()
		j=self.Gsdll.gsapi_revision (pointer(r), sizeof(r))
		print "Producto :",r.product,"\nRev      :", r.revision, "\nfecha    :",r.revisiondate,"\nCopyRight:", r.copyright
	
	
	##Private Declare Function gsapi_new_instance Lib "gsdll32.dll" (ByRef lngGSInstance As Long, ByVal lngCallerHandle As Long) As Long
	def gsapi_new_instance(self):
		minst = c_void_p()
		if self.Gsdll.gsapi_new_instance(pointer(minst), None) != 0:
			raise GhostscriptException('Error: Creacion de instancia de Ghostscript, Solo soporta 1 al la vez')
		return minst

	#int GSDLLAPI gsdll_init(GSDLL_CALLBACK callback, HWND hwnd, int argc, char *argv[]);
	def gsapi_init_with_args(self,instance, argv):
		argc = len(argv)
		argv_t = c_char_p * argc
		c_argv = argv_t(*argv)
		if self.Gsdll.gsapi_init_with_args(instance, argc, c_argv) != 0:
			raise GhostScriptException('Error: Inicio de la instacia a fallado!!')
		
	def procesar(self,argumentos):
		self.Gsdll= windll.LoadLibrary(self.ruta) 
		objgs = self.gsapi_new_instance()		
		print objgs
		print(self.gsapi_init_with_args(objgs,argumentos))
		print(self.Gsdll.gsapi_exit(objgs))
		print self.Gsdll.gsapi_delete_instance(objgs)

	def GenPCL(self,entrada,salida):
		if not self.BuscarGS():return False		
		salida="-sOutputFile=%s" %(salida)
		arg=['q','-sDEVICE=ljet4',"-dNOPAUSE", "-dBATCH", "-dSAFER",salida,entrada]
		print arg
		self.procesar(arg)


	def GenPDF(self,entrada,salida):
		#if not self.BuscarGS():return False
		
		entrada='-sOutputFile=' + entrada
		arg=['-dNOPAUSE','-dBATCH','-sDEVICE=pswrite',entrada,salida]
		objgs = self.gsapi_new_instance()		
		print objgs
		print(self.gsapi_init_with_args(objgs,arg))
		print(self.Gsdll.gsapi_exit(objgs))
		self.Gsdll.gsapi_delete_instance(objgs)
		return True
	

	
if __name__ == '__main__':
	Prueba=ObjGS_dll()
	Prueba.GenPCL("entrada 233-Ñoño.pdf", 'salida.pcl')
        #Prueba.BuscarGS()            
	#Prueba.Revision()
	#arg=['-dNOPAUSE','-dBATCH','-sDEVICE=pswrite','-sOutputFile=out2.ps','out1.ps','-c "<</Orientation 1 >> setpagedevice"']	
	#Prueba.procesar(arg)
