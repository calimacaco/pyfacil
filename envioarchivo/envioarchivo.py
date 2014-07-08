#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-


import os
import sys
import glob


import time
import shutil



import subprocess
from librerias.basedatos import ObjBase
from optparse import OptionParser
from datetime import datetime


if os.name =='nt':
	from librerias.registro import RegistroWindows
	import leerregistro


def ArgOpciones():
	uso = "uso: %prog [opciones] \n Opciones:\n -b o --base= <base de datos>\n -i o --id= <id proceso>\n -l o --log     ->activar log\n -g o --guardar	 ->Dejar arhcivo"
	parser = OptionParser(uso)
	parser.add_option("-b", "--base=", dest="basedatos",
					  help="Ruta y nombre de la base de datos")
	
	parser.add_option("-i", "--id=", dest="id",
					  help="Id del proceso")

	parser.add_option("-l", "--log",
					  action="store_true", dest="logs")

	parser.add_option("-g", "--guardar",
					  action="store_false", dest="guardar")


	(opciones, args) = parser.parse_args()
	if not opciones.basedatos and not opciones.id:
		print "Error no hay opciones\n"
		print uso
		sys.exit()
		
	if not os.path.isfile(opciones.basedatos):
		print "Error: no exite Base de datos"
		sys.exit()
	
	return opciones	

def Ejecutar():
	print "Ejecutar:"
	salida ={}
	if os.name =='nt':
		wReg=RegistroWindows()
		llave="Software\\simplesoft\\facil"
		if wReg.defKey(llave):
			ruta,tipo = wReg.LeerReg ("programa")
			print ruta
			print tipo
			if not os.path.isdir(ruta):
				print "error no existe Directorio de Facil"
				sys.exit()
			facil = ruta + os.sep + "FacilRecargado.exe"
			if not os.path.isfile(facil):
				print "Error: no esta el programa FacilRecargado"
				sys.exit()
			
			print "facil:", facil
			
			salida ["rutaFacil"]=ruta
			salida ["ejecutarFacil"]=facil

		
			return salida 
		else:
			print "error No existe FACIL"
			sys.exit()
		

if __name__ == "__main__":

	opciones=ArgOpciones()
	baseDatos=ObjBase(opciones.basedatos,False)
	patrones = baseDatos.LeerCampos("ambiente,patron", "tbl_patrones", "idproceso=%s" % opciones.id)
	proceso =baseDatos.SelectUno("proceso,impresora,ruta", "tbl_envioarch", "id=%s" % opciones.id)
	ejecutar=Ejecutar()
	
	
	
	impresora=proceso[1]
	
	print "patrones",patrones
	print "proceso",proceso
	print "ejecutar",ejecutar
	
	
	rutaBusqueda=proceso[2] + os.sep
	print 'rutaBusqueda',rutaBusqueda
	
	
	
	for patron in patrones:
		ruta = rutaBusqueda + patron[1]
		ambiente=patron[0]
		print ruta,'-->',ambiente
		listaArch=glob.glob(ruta)
		print listaArch
		for arch in listaArch:
			if os.path.getsize(arch)>0:
				tamarchivo=os.path.getsize(arch)
				time.sleep(1)
				if tamarchivo != os.path.getsize(arch):
					print "Esta llegando"
					continue
				archSalida =ejecutar["rutaFacil"] + os.sep +  "proceso" + os.sep + impresora


				nombre=os.path.split(arch)
				print 'final:', nombre
				fecha =str(datetime.now())
				
				campos={"idstado":1,
						"idimpresora":1,
						"usuario":"EnvioArchivo",
						"nombrejob":arch,
						"jobid":"%s" % (opciones.id),
						"copias":1,
						"fecha":fecha}
				idjob=baseDatos.Insertar('tbl_spool', campos)
								
				if not os.path.exists(archSalida):
					os.makedirs(archSalida)
				
				archSalida += os.sep + nombre[1] + "_" + str(idjob)
				print archSalida
				
				
				if opciones.guardar:
					shutil.copy(arch, archSalida)
				else: #mover
					shutil.move( arch , archSalida)

				correr = ejecutar["ejecutarFacil"] + ' --JOB=%s --IMP=%s --MOD=%s --PRO=%s --FUN=%s --ID=%i ' %(archSalida,impresora,ambiente,impresora,impresora,idjob)
 				subprocess.call(correr)