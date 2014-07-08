#!/usr/bin/env python
# -*- coding: utf-8 -*-
#import win32api
#import win32con
import random
import sys
import os
import datetime
import leerregistro
import msvcrt



def enviarStout(rutaarchivo):
	ruta,nombre=os.path.split(rutaarchivo)
	ruta,temp=os.path.split(registro.LeerReg("Trabajo"))
	ruta+="\\"+temp+"\\stdout\\"
	
#	sys.stdout.write(nombre + "\n" + ruta + "\n\n")
	

	if not os.path.isfile(os.path.join(ruta,nombre)):
		sys.stdout.write("Error No existe archivo:"+nombre)
		GuardarLog ("Error No exite stdout")
		sys.exit(0)
		return 0
	try:
		msvcrt.setmode(sys.stdout.fileno(), os.O_BINARY)
		arch=open(os.path.join(ruta,nombre),"rb",0)
		sys.stdout.write(arch.read())
		#print(datos)
		#datos=arch.read(1))
		#while len(datos)>0:
		#	sys.stdout.write(datos)
		#	datos=arch.read(1)
	except:
		sys.stdout.write("error")
		GuardarLog ("Error: lecutra:" + ruta+nombre)
	finally:
		arch.close()

	
	


def GuardarLog(datos):
	try:
		ruta ='c:\\captura.log'
		if os.path.isfile(ruta):
			f=file(ruta,'a')
		else:
			f=file(ruta,'w')
		datos+="\n"
		f.write (datos)
		f.close()
	except:
		print "no Se puede Crear Log"
		
def BuscarArgumentos():
	""" 
		Busca los argumentos ingresado desde la linea de comando
		Devuelve la impresora,ambiente,ruta, proceso,log, donde log=0 no, log=1 si
	"""
##	print "Buscar Argumentos"
	if (len(sys.argv) <5):
		return 0,0,0,0,0
	valor=0
	impresora=""
	ambiente=""
	proceso=""
	programa=""
	cortaspool=""
	log=0
	for pos  in range (1,len(sys.argv)):
		datos=sys.argv[pos]
		if (datos[2:5].upper()=="IMP"):
			temp=datos.split("=")
			if (len(temp)>=2):
				impresora=temp[1]
				valor+=1;
		elif (datos[2:5].upper()=="MOD"):
			temp=datos.split("=")
			if (len(temp)>=2):
				ambiente=temp[1]
				valor+=2;
		elif (datos[2:5].upper()=="PRO"):
			temp=datos.split("=")
			if (len(temp)>=2):
				proceso=temp[1].strip()
				valor+=3;
		elif (datos[2:5].upper()=="LOG"):
				log=1
		##Mod nov 2012

##Guarda una copia del spool, en una ruta.
		##Corta por pagina segun indicador
		elif (datos[2:5].upper()=="SPL"):
			temp=datos.split("=")
			if (len(temp)>=2):
				cortaspool=temp[1].strip()
		########
		elif (datos[2:5].upper()=="PRU"):
			temp=datos.split("=")
			if (len(temp)>=2):
				programa=temp[1]
				
	return valor,impresora,ambiente,proceso,log,programa,cortaspool
########################## Incio del programa ###########################
if __name__ == "__main__":
	(estado,impresora,ambiente,proceso,log,programa,cortaspool)=BuscarArgumentos()
	if estado<6:
		sys.exit (2)
	ruta=""
	registro=leerregistro.RegistroWindows()
	ruta=registro.LeerReg("programa")
	if (log==1):
		GuardarLog ("Impresora:"+impresora)
		GuardarLog ("Ambinte  :"+ambiente)
		GuardarLog ("Ruta     :"+ruta)
		GuardarLog ("Proceso  :"+proceso)
		guardarLog ("SpoolSrv :"+cortaspool)

	hora=datetime.datetime.now()
	
	nrospool=random.randint(1,100000)
	nombre=ruta + '\\proceso\\' + proceso 
	if not os.path.exists(nombre):
		os.makedirs(nombre)
	nombre+= '\\'+ 'spl'+hora.strftime("%Y%m%d-%H%M%S-")+str(nrospool)+'.slp'
	if os.path.isfile(nombre):
		nrospool=random.randint(1,100000)
		nombre+= str(nrospool)
	archivo=file(nombre,'w')
	data =sys.stdin.readlines()
	archivo.writelines (data)
	archivo.close()
	

	if len(data)==0:
		sys.exit (0)
	cuenta=0
	for linea in data:
		if linea=='\n' or linea=='\r\n':
			cuenta+=1
		else:
			break
		if cuenta==66:
			sys.exit (0)
	if (log==1):
		GuardarLog ("Archivo de salida:"+nombre)

	if len(cortaspool)>0:
		from guardarspool import Obj_Spool
		r_programa=registro.LeerReg("programa")
		r_trabajo=registro.LeerReg("Trabajo")
		ObjCopiarSpool=Obj_Spool(nombre,cortaspool,r_programa,r_trabajo)

	if len(programa)==0:
		programa='FacilRecargado.exe'
	ejecutar= ruta + "\\"+programa+" --JOB=" + nombre + " --IMP=" + impresora + " --MOD=" + ambiente + " --PRO=" + proceso + " --StdOut "

	try:
		ejecutar+=' --FUN=' + os.environ['REDMON_PRINTER'] + ' --USR=' + os.environ['REDMON_USER']
	except:
		ejecutar+=' --FUN=No establecido --USR=No establecido'
	try:
		if (log==1):
			GuardarLog ("Ejecutar:"+ejecutar)
		os.system(ejecutar)
	except:
		if (log==1):
			GuardarLog ("Error Ejecutar!")
	enviarStout(nombre)


