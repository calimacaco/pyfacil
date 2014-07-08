#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

import getopt
import signal
import os
import sys
import glob
import leerregistro
import datetime
import time
import random
import shutil
import subprocess

from subprocess import call

def RutaFacil():
	registro=leerregistro.RegistroWindows()
	ruta=registro.LeerReg("programa")
	return ruta

def Ejecutar(logact=False):
	ruta =RutaFacil()
	ruta+='\\facilrecargado.exe'
	if logact==True:
		Log ("Ruta FacilRecargado= " + ruta)
	return ruta

def Log(datos):
	print datos
	ruta=RutaFacil()	
	ruta+='\\envioarchivo\\logs.log'
	f = open(ruta,'a')
	datos+='\n'
	f.write(datos)
	f.close()

def LeerConf(config="",logact=False):
	print "leer config"
	ruta=RutaFacil()
	if len(config)==0:
		ruta+='\\envioarchivo\\config.cfg'
	else:
		ruta+='\\envioarchivo\\'+ config +'.cfg'
#	if !isfile(ruta):
	
	if logact==True:
		Log ("Ruta configuracion= " + ruta)

	print "Archivo [%s]" % ruta
	f = open(ruta,'r')
	buscar=[]
	impr=[]
	for linea in f:
		partir= linea.split("<|>")
		if partir[0]!='\n':
			buscar.append(partir[0])
			impr.append(partir[1])
	f.close()
	Log (ruta + '\n')
	print "buscar :", buscar
	print "impr :",    impr
	return buscar,impr

#def LeerArchivo(nombre):
#	f=open(nombre,'r')
#	datos=f.read()
#	f.close()
#	return datos

def main(argv):

	while 1:
		time.sleep(10)
		print "ola"
	


	verificar =0
	archivo=""
	ruta=""
	Config=""
	logact=False
	for opt in argv:
		comando,valor = opt.split("=")
		print comando
		if comando.lower()=="--config" or comando.lower()=="-c":
			Config=valor
			if logact==True:
				Log ( "Configuracion= " + valor)
		if comando.lower()=="--ruta" or comando.lower()=="-r":
			
			ruta=valor
			if os.path.isdir(ruta):
				verificar+=1
				if logact==True:
					Log ( "Ruta= " + valor)
		if comando.lower()=="--impresora" or comando.lower()=="-i":
			print "impresora"
			if logact==True:
				Log ("Impresora= " + valor)
			impresora=valor
			verificar+=2
		if comando.lower()=="--log" or comando.lower()=="-l":
			Log ("argumentos")
			logact=True
#			finally:
#				print verificar
#	finally:
	print "Valor Verificar[%i]" % verificar
	if verificar<3 :
		print "no estan los parametros basicos\n --ruta=<Directorio archivos> --impresora=<impresora de salida> [--config=<nombre configuracion>]\n"
		sys.exit(2)

	#leer ruta con filtro
	
	filtro,imp=LeerConf(Config,logact)
	if len(filtro)>0:
		salir=0
		ejecutar=Ejecutar()
		while salir==0:
			ciclo=0
			if logact==True:
					Log ("leer filtro")
			for item in filtro:
				archivos=ruta + "\\" + item
				if logact==True:
					Log (archivos)
				lista=glob.glob(archivos)
				for arch in lista:
					
					if os.path.getsize(arch)>0:
						tamarchivo=os.path.getsize(arch)
						time.sleep(1)
						if tamarchivo != os.path.getsize(arch):
							continue
							

						# ## datos=LeerArchivo(arch)
						fecha= datetime.datetime.now()
						temp1,temp2=os.path.split(arch)
						

						# ## temp2=temp1.split("\\")
						# ##temp1=temp2[-1]
						
						
						archsalida =RutaFacil() + "\\proceso\\" + impresora 
						if not os.path.exists(archsalida):
							os.makedirs(archsalida)


						# ##archsalida+= "\\" + temp1 + fecha.strftime("%d%m%Y_%H%M%S")+ str(random.randint(1, 1000))+".spl"
						archsalida+= "\\" + temp2 + "_" + str(random.randint(1, 1000))+".spl" 
						shutil.move( arch , archsalida ) # mover el archivo
						
						activarfacil=ejecutar + " --JOB="+archsalida+" --IMP="+impresora + " --MOD=" + imp[ciclo] + " --PRO=" + impresora + " --FUN=Facil --USR=Facil"
						
						#salprint=impresora + "_" + imp[ciclo]
						if logact==True:
							Log ("Archivo :" + arch)
							Log ("Proceso de salida:" + archsalida)
							activarfacil+=" --log"
							Log ("ejecutar:" + activarfacil)
							
						try:
							
							#os.system(activarfacil)
							subprocess.Popen(activarfacil, shell=True)
							if logact==True:
								Log ("Fin ejecucion")
						except e:
							if logact==True:
								Log ("Fin ejecucion:" + e)
				ciclo+=1
			time.sleep(2)


if __name__ == "__main__":
	main(sys.argv[1:])

