#!c:\python27\python.exe
# -*- coding: utf-8 -*- 

'''
Lee la base de datos y archivos para compatibilidad con FacilRecardo.
'''



#from datetime import *
import datetime
from  time import sleep
import signal
import sys, os, shutil
from librerias.EnvioCorreo import Envio_Correo
import sqlite3
import glob
from basedatos import ObjBase,campos_Envio
import getopt
import shutil

def Segimiento(ruta):
	if not os.path.isdir(ruta):
		os.makedirs(ruta)

def Uso():
	print "Version 3.40"
	print "Argumentos"
	print '-b <ruta base de datos>, --basedatos=<ruta base de datos>'
	print '   Definir ruta de la base de datos'
	print '-a, --archivo'
	print '   Activar compatiblidad FacilRecargado, lectura directorio enviar'
	print '-n, --nomover'
	print '   No mueve el archivo fuente PDF'

def signal_handler(signal, frame):
	print 'Fin de la ejecucion se pulso  Ctrl+C !'
	sys.exit(0)

def Log(ruta,datos,estado=True):
	j= datetime.datetime.now()
	fecha=j.strftime('%Y-%m')
		
	ruta+='logs/'
	if not os.path.isdir(ruta):
		os.makedirs(ruta)
	
	if estado:
		ruta+='estado %s.log' %(fecha)
		if not os.path.isfile(ruta):
			f = open(ruta,'w')
			f.write('fecha|Enviado|asunto|adjuntos|enviar')
			datos+='\n'
			f.write(datos)
		else:
			f = open(ruta,'a')
			datos+='\n'
			f.write(datos)

	else:
		ruta+='error %s.log' %(fecha)
		if not os.path.isfile(ruta):
			f = open(ruta,'w')
			f.write('fecha|error|Enviado|asunto|adjuntos|enviar')
			datos+='\n'
			f.write(datos)
		else:
			f = open(ruta,'a')
			datos+='\n'
			f.write(datos)
	f.close()


def extraervirtual(ruta):
	print '*********'
	print "extraervirtual=[%s]"%(ruta)
	#Se define $usuarios$  --->Usuarios o Users
	#se define $Escritorio$ -->Escritorio o Desktop
	
	lenguaje=[('usuarios','escritorio','mis documentos'),('users', 'desktop', 'documents')]
	
	
	for leng in lenguaje:
		rutatemp,archivo=os.path.split(ruta)
		print 'rutatemp %s -- %s'%(rutatemp,archivo)
		
		rutatemp=rutatemp.replace('$usuarios$', leng[0])
		rutatemp=rutatemp.replace('$escritorio$', leng[1])
		rutatemp=rutatemp.replace('$documentos$', leng[2])
		print rutatemp
		print '**************'
		if os.path.isdir(rutatemp):
			print type(os.sep)
			rutatemp +=  os.sep + archivo 
			return rutatemp
	
	print 'Error no hay sitio de llegada'
	rutatemp='c:\\simplesoft\\facil\\modelos\\pdf\\enviados\\'
	return rutatemp
	
		
def LeerCampos(nombre):
	print "LeerCampos"
	arch = open(nombre,'r')
	contenido=arch.readlines()
	arch.close
	print contenido
	resultado={'estado':1,'bscopia':'','adjuntos':'','copia':'','asunto':'','enviar':'','bandera':'','rutafinal':''}
	campos=[]
	#resultado.append(len(contenido))#Nro de lineas
	for linea in contenido:
		linea=linea.replace("\r","")
		linea=linea.replace("\n","")
		campos=(linea.split('<|>'))
		for campo in campos:

			clave=campo.split("::")
			print clave
			
			
			if len(clave)>1:
#				print clave[0],"---->",clave[1]
				if clave[0].lower()=='enviar':
					clave[1]=clave[1].replace(";",",")
					resultado['enviar']=clave[1]#.split(',')
				elif clave[0].lower()=='copia':
					clave[1]=clave[1].replace(";",",")
					resultado['copia']=clave[1]#.split(',')
				elif clave[0].lower()=='bscopia':
					clave[1]=clave[1].replace(";",",")
					resultado['bscopia']=clave[1]#.split(',')
				elif clave[0].lower()=='pdf':
				#	resultado['pdf'].append(clave[1])
					resultado['adjuntos']=clave[1]#.split(',')
				elif clave[0].lower()=='asunto':
					resultado['asunto']=clave[1]
				elif clave[0].lower()=='bandera':
					resultado['bandera']=clave[1]
				elif clave[0].lower()=='rutavirtual':
					#print "ruta final"
					if len(resultado['rutafinal'])==0:
						resultado['rutafinal']=extraervirtual(clave[1])
					else:
						resultado['rutafinal']=resultado['rutafinal'] + ',' + extraervirtual(clave[1])
						
	#if resultado['enviar']=='':
	#	return None
	#if resultado['bandera']=='':
	#	resultado['bandera']=='F2S_Defecto'
	print "resultado",resultado
	
	
	return resultado	
def BuscarBD(campo,ruta):

	nombre='correo.db'
	argv=sys.argv[1:]
	try:                                
		opts, args = getopt.getopt(argv, "hb:d", ["help", "base="])
		
	except getopt.GetoptError:
		print getopt.GetoptError.msg
		Uso()						 
		sys.exit(2)					 
	for opt, arg in opts:
		if opt in ("-h", "--help"):
			#Uso()					 
			sys.exit()				  
		elif opt == '-d':
			global _debug			   
			_debug = 1				  
		elif opt in ('-b','--base'):
			ruta=arg
			nombre=''
			
	resultado={}
	
	
	print "Base de datos:"+ruta + nombre
	print "--------------------------------"
	#sys.exit(0)
	
	try:
		baseconn=sqlite3.connect(ruta + nombre )
	
	except sqlite3.OperationalError: # Can't locate database file
		log(ruta,"No Existe la base de datos")
		exit(1)
		
		
##	sql="SELECT puerto,usuario,clave,servidor,tls,enviado,rutafinal,txtcontenido,htmlcontenido,addruta FROM config WHERE bandera='" +campo+"' LIMIT 1"
	sql="SELECT puerto,usuario,clave,servidor,tls,enviado,rutafinal,txtcontenido,htmlcontenido FROM tbl_correo WHERE bandera='" +campo+"' LIMIT 1"

	cursor = baseconn.cursor()
	cursor.execute (sql)
	
	
	for fila in cursor:
		resultado={'puerto':int(fila[0]),'usuario':str(fila[1]),'clave':str(fila[2]),'servidor':str(fila[3]),
					'tls':str(fila[4]),'de':str(fila[5]),
##					'rutafinal':str(fila[6]),'txtcontenido':str(fila[7]),'htmlcontenido':str(fila[8]),'addruta':str(fila[9])}
					'rutafinal':str(fila[6]),'txtcontenido':str(fila[7]),'htmlcontenido':str(fila[8])}



	if len(resultado)==0:
		print "no hubo...."
#aqui este el error bandera enviado#		sql="SELECT puerto,usuario,clave,servidor,tls,enviado,rutafinal,txtcontenido,htmlcontenido FROM config WHERE idcod=1"
		sql="SELECT puerto,usuario,clave,servidor,tls,bandera,rutafinal,txtcontenido,htmlcontenido FROM tbl_correo WHERE id=1"
		cursor.execute (sql)
		for fila in cursor:
			resultado={'puerto':fila[0],'usuario':str(fila[1]),'clave':str(fila[2]),'servidor':str(fila[3]),
						'tls':str(fila[4]),'de':str(fila[5]),
						'rutafinal':str(fila[6]),'txtcontenido':str(fila[7]),'htmlcontenido':str(fila[8])}

	cursor.close()
	baseconn.close()	
	return resultado


def MoverPDF(ruta_Entrada,ruta_Salida):
	print "Mover PDF's [%s] a [%s]" % (ruta_Entrada,ruta_Salida)

	for Entrada in ruta_Entrada.split(','):
		if not os.path.isfile(Entrada): return 4
		print "Moviendo de entrada:",Entrada
		
		dir_Entrada,archivo= os.path.split(Entrada)

		#Crear directorio de salida si no existe
		#try:
		#	dir_Salida,archivo= os.path.split(ruta_Salida)
		#	if not os.path.isdir(dir_Salida): 
		#		os.makedirs(dir_Salida)
		#except:
		#	return 1		
		
		#Si existe archivo en directorio destino lo borramos
		
		try:
			
			if os.path.isfile(ruta_Salida):
				print "borrar destino:",ruta_Salida
				os.remove (ruta_Salida)
		except:
			return 2
	
		#Mueve a destino
		print "**************************\nMover"
		print "Archivo_destino:",ruta_Salida
		print "Archivo_entrada:",ruta_Entrada
		print "**************************"
		try:
			shutil.move( ruta_Entrada, ruta_Salida ) # mover el archivo
		except:
			return 3
		
	return 0
		
def Repositorio(ruta,final):
	#Crear directorio de salida si no existe
	if not os.path.isdir(ruta + final):
		os.makedirs(ruta + final)
	else:
		return (ruta + final)
		
	#Comprobar si se creo
	#De lo contrario los deja en el raiz
	
	if not os.path.isdir(ruta + final):
		return ruta
	else:
		return (ruta + final)

def BuscarNombre(Nombre,repositorio):
	salir=False
	contador=1
	x, Nombre =os.path.split(Nombre)
	Nombre=repositorio + str(Nombre)
	temp_nombre=Nombre
	
	while not salir:
		if os.path.isfile(temp_nombre):
			temp_nombre=Nombre +str(contador)
			contador+=1
		else:
			salir=True
	print "tempo nombre:" + temp_nombre
	return temp_nombre


#***************************************************

def Argumentos():
	print "pycorreo->Argumentos"
	salida={"base":'config.db',"archivos":False,"mover":True}
	print sys.argv[0]
	salida["Ruta"],temp=os.path.split(sys.argv[0])
	if len(salida['Ruta'])==0:
		salida['Ruta']='.' + os.sep
	else:
		salida["Ruta"]=salida["Ruta"]+os.sep
	print salida	
	argv=sys.argv[1:]
	try:                                
		opts, args = getopt.getopt(argv, "hb:an:d", ["help","base","archivos","nomover"])# "ha:s:b:d", ["help", "ambiente=","salida=","base"])
		
	except getopt.GetoptError:
		print "except"
		print getopt.GetoptError.msg
		Uso()						 
		sys.exit(2)					 
	for opt, arg in opts:
		if opt in ("-h", "--help"):
			Uso()					 
			sys.exit()				  
		elif opt == '-d':
			global _debug			   
			_debug = 1				  
		elif opt in ('-b','--base'):
			"base datos"
			salida["base"]=arg
		elif opt in ('-a','--archivo'):
			print "archivos"
			salida["archivos"]=True
		elif opt in ('-n','--nomover'):
			print "no mover"
			salida["mover"]=False

	print salida
	return salida

def LeerArchivo(ruta):
	print "LeerArchivo"
	correoarch=None
	ruta += 'enviar'
	print "leer ruta :[%s]" % (ruta)
	
	if not os.path.isdir(ruta):
		print "No existe Directorio para la lectura"
		return None
	ruta += os.sep + '*.mail'
	archivos=glob.glob(ruta)
	for nombre in archivos:
		print "Nombre Archivo a procesar:",nombre
		correoarch=LeerCampos(nombre)
		return nombre, correoarch
	#si no hay
	print "No hay datos"
	return None, None




if __name__ == "__main__":
	
	print "Version 3.40"
	print "------------------------------------------------"
	signal.signal(signal.SIGINT, signal_handler)

	salida=Argumentos()
	print salida
	print "Base de datos:", salida["base"]
	bd=ObjBase(salida['base'])
	campos=campos_Envio()
	while True:
		
		
		tabla='tbl_logenvio'
		condicion='estado=1 or estado =2 '# enviar, reenviado
		ordenar='estado'
		campos=['id','enviar','adjuntos','asunto','bandera','copia','bscopia','rutafinal']
		if salida["archivos"]:
			nombarch,datosarch=LeerArchivo(salida['Ruta'])
			
			print "********************   nombarch,datos" ,nombarch,datosarch

			
			
			if nombarch !=None and datosarch !=None:
				subirdb=bd.Insertar(tabla, datosarch)
				if subirdb>0:
					os.remove(nombarch)
					
					
		
		datos_envio=bd.LeerCampos(campos, tabla, condicion, ordenar)
		print "datos de envio:" , datos_envio
		for campo_envio in datos_envio:
			condicion="bandera='%s'" %(campo_envio['bandera'])
			servercorreo = bd.SelectUno('*', 'tbl_correo', condicion)
			if servercorreo==None : continue
			
			print 'servercorreo:[%s]'%(servercorreo)
			print 'campo_envio:[%s]'%(campo_envio)
			correo=Envio_Correo()
			
			resultado=correo.send_email(campo_envio['asunto'],servercorreo['txtcontenido'],servercorreo['htmlcontenido'],
				servercorreo['enviado'],campo_envio['enviar'],campo_envio['adjuntos'],campo_envio['copia'],campo_envio['bscopia'],
				servercorreo['servidor'],servercorreo['puerto'],servercorreo['usuario'],servercorreo['clave'],servercorreo['tls'])



			j= datetime.datetime.now()
			fecha=j.strftime('%Y-%m-%d %H:%M:%S')
			
			
			print 'resultado [%s]'  %(resultado)
			
				
			if resultado==0:
				#mover archivos	
				if len (campo_envio['rutafinal'].strip())>0:
					MoverPDF(campo_envio['adjuntos'], campo_envio['rutafinal'])
					
				
				#cambia estado a 0 =enviado satisfactorio
				condicion='id=%i' %(campo_envio['id'])
				registro='estado=0' 
				bd.ActualizarCampos(tabla, registro, condicion)
				
				
				#si exite un repositorio de confirmacion de envio es realizado este 
				condicion="bandera='LOG_ENVIO' AND estado=1"		
				servercorreo = bd.SelectUno('*', 'tbl_correo', condicion)
				contenido='%s|%s|%s|%s|%s' %(fecha,'Enviado',campo_envio['asunto'],campo_envio['adjuntos'],campo_envio['enviar'])
				
				
				if servercorreo !=None:
					print "enviar log."
					resultado=correo.send_email('LOG_ENVIO',contenido,'',
							servercorreo['enviado'],servercorreo['rutafinal'],'','','',
							servercorreo['servidor'],servercorreo['puerto'],servercorreo['usuario'],servercorreo['clave'],servercorreo['tls'])
					
				##Log(salida["Ruta"],contenido)			
			
			else:
				condicion='id=%i' %(campo_envio['id'])
				registro='estado=3' 
				bd.ActualizarCampos(tabla, registro, condicion)
				condicion="bandera='LOG_ERROR' AND estado=1"
				servercorreo = bd.SelectUno('*', 'tbl_correo', condicion)
				contenido='%s|%s|%s|%s|%s' %(fecha,correo.error,campo_envio['asunto'],campo_envio['adjuntos'],campo_envio['enviar'])
				if servercorreo !=None:
					resultado=correo.send_email('error de envio',contenido,'',
							servercorreo['enviado'],servercorreo['rutafinal'],'','','',
							servercorreo['servidor'],servercorreo['puerto'],servercorreo['usuario'],servercorreo['clave'],servercorreo['tls'])
				
				##Log(salida["Ruta"],contenido,False)			
		
				
		sleep(2)
		
		print "*",
	print "final"
	
#===============================================================================
#	Ruta_Errores=""
#	print "Version 3.20"
#	G_ruta=sys.argv[0]
#	G_ruta,temp=os.path.split(G_ruta)	
#	if len(G_ruta)<1:G_ruta='.'
#	print "--------------- GENERALES  ---------------------"
#	temp=G_ruta  +os.sep + "enviar" + os.sep + "*.mail"
#	print "Ruta captura de archivos:", temp
#	
#	print "------------------------------------------------"
#	signal.signal(signal.SIGINT, signal_handler)
#	
# 
#	if not os.path.isdir(G_ruta +os.sep+"enviar"):
#		print "Creando carpeta:" + G_ruta+os.sep+'enviar'
#		os.mkdir(G_ruta+os.sep+'enviar')
#===============================================================================
	
#===============================================================================
#	sys.exit()
#	
#	while True:
#		archivos=glob.glob(temp)
#		for nombre in archivos:
#			print "Nombre Archivo a procesar:",nombre
#			correoarch=LeerCampos(nombre)
#					
#			if correoarch==None:
#				print "error:Campos datos errados"
#				Log(G_ruta,"Campos datos errados ["+ nombre + ']')
#				CambiarA=BuscarNombre(nombre+".error.[Campos datos Incorrectos]",Ruta_Errores)
#				os.rename(nombre,CambiarA)
#				continue
#			print "Contenido Archivo:",correoarch
#			basedatos={}
#			basedatos=BuscarBD(correoarch['bandera'],G_ruta)
#			print "-------------------------------------------"
#			print "Consulta BaseDatos:",basedatos
#			if len(basedatos)<9:
#				print "error:Campos de la base de datos"
#				Log(G_ruta,"Campos en la base  incorrectos["+ nombre + ']')
#				CambiarA=BuscarNombre(nombre+".error.[Campos Base datos Incorrectos]",Ruta_Errores)
#				os.rename(nombre,CambiarA)
#				continue
#			print "-------------------------------------------"
#			correo=Envio_Correo()
# 
#			resultado=correo.send_email(correoarch['asunto'],basedatos['txtcontenido'],basedatos['htmlcontenido'],
#				basedatos['de'],correoarch['enviar'],correoarch['pdf'],correoarch['copia'],correoarch['bscopia'],
#				basedatos['servidor'],basedatos['puerto'],basedatos['usuario'],basedatos['clave'],basedatos['tls'])
#					
#			
#			if resultado>=1 and resultado <=7:
#				##Error conexion server
#				Log(G_ruta,str(correo.error) + '['+ nombre + ']')
#				continue
#					
#			if resultado==-1:
#				Log(G_ruta,str(correo.error) + '['+ nombre + ']')
#				print "Error Enviado Correo !!!!"
#				#CambiarA=BuscarNombre(nombre+"["+correo.error+"]",Ruta_Errores)
#				#os.rename(nombre,CambiarA)
#				continue
#			else:
#				#copiar en otra ruta
# ##				CopiarPDF (str(correoarch['pdf']),str(basedatos["addruta"]),G_Separador)
#				#Mover al destino
#				if len(basedatos["rutafinal"].strip())>0:
#					resultado = MoverPDF (str(correoarch['pdf']),str(basedatos["rutafinal"]))
#					if resultado==1:
#						print "imposible crear ruta destino PDF:",str(basedatos["rutafinal"])
#						print "----------------------------------------------"
#						Log("ruta destino","Imposible Crear Ruta Destino_PDF")
#						#CambiarA=BuscarNombre(nombre+".error.Ruta Destino_PDF",Ruta_Errores)
#						#os.rename(nombre,CambiarA)
#						continue
#					if resultado ==2:
#						print "No es posible borrar destino:",str(basedatos["rutafinal"])
#						Log("Destino","Imposible Borrar Archivo_PDF")
#						#CambiarA=BuscarNombre(nombre+".error.Borrar Archivo Destino_PDF",Ruta_Errores)
#						#os.rename(nombre,CambiarA)
#						print "----------------------------------------------"
#						continue
#					if resultado==3:
#						print "No es posible Mover archivo destino"
#						Log("Destino","Imposible Mover Archivo_PDF")
#						#CambiarA=BuscarNombre(nombre+".Error_Mover Archivo Destino_PDF",Ruta_Errores)
#						#os.rename(nombre,CambiarA)
#						print "----------------------------------------------"
#						continue
#					if resultado==4:
#						print "Archivo Fuente de entrada no existe:" ,str(correoarch['pdf'])
#						Log("entrada","Fuent de entrada no existe Archivo_PDF")
#						#CambiarA=BuscarNombre(nombre+".Error.Fuente PDF no existe",	Ruta_Errores)
#						#os.rename(nombre,CambiarA)
#						print "----------------------------------------------"
#						continue
#					
#					os.remove(nombre)
#				#Cambiar ok
#				#CambiarA=BuscarNombre(nombre+".ok",Ruta_Enviados)				
#				#try:
#				#	os.rename(nombre,CambiarA)
#				#except:
#				#	print "aqui"
#					#Log("No es posible Mover archivo[",nombre + "] a [" + CambiarA )
#					#os.rename (nombre,nombre+".ok")
#		print "*",
#		sleep(4)
#		archivos=[]
#===============================================================================
#===============================================================================
# def CopiarPDF(ruta_Entrada,dir_Salida,G_Separador):
# 	print "Copiar PDF"
# 	
# 	Buscar = dir_Salida.strip(' \t\n\r')
# 	if len(Buscar)==0:
# 		return 0
# 	
# 	if dir_Salida=='None':
# 		return 0
# 
# 	
# 	
# 	
# 	ruta_Entrada=ruta_Entrada[2:-2]
# 	if not os.path.isfile(ruta_Entrada):
# 		return 4
# 
# 	dir_Entrada,archivo= os.path.split(ruta_Entrada)
# 	
# #	dir_Salida="C:\\borrar\\xpdf"
# 	print "Ruta de entrada:",ruta_Entrada
# 	print "Ruta de salida:",dir_Salida
# 	print "Archivo PDF:",archivo
# 	print '------------------------------------------'
# 	
# 	#Crear directorio de salida si no existe
# 	try:
# 		if not os.path.isdir(dir_Salida): 
# 			os.makedirs(dir_Salida)
# 	except:
# 		return 1
# 	#Si existe archivo en directorio destino lo borra
# 	try:
# 		Archivo_destino=dir_Salida#+G_Separador+archivo
# 		if os.path.isfile(Archivo_destino):
# 			print "borrar destino:",Archivo_destino
# 			os.remove (Archivo_destino)
# 	except:
# 		return 2
# 	#Mueve a destino
# 	print "Archivo_destino:",Archivo_destino
# 	print "Archivo_entrada:",ruta_Entrada
# 	try:
# 		shutil.copyfile( ruta_Entrada, Archivo_destino ) # mover el archivo
# 	except:
# 		return 3
#===============================================================================
