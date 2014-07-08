#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

import os
import shutil

try:  
	import cPickle as pickle  
except ImportError:  
	import pickle


class Obj_Spool:
	def __init__(self,nombre,cortarspool,r_programa,r_trabajo):

		ambiente=r_trabajo + '\\ambientes\\' + cortarspool + ".py"
		print "ambiente:[%s]" %(ambiente)
		if not os.path.isfile(ambiente):
			arc=open(ambiente,'w')
			comandos={"ruta":"\\\\SERVERUNO\PedidoControl","buscar":"PEDIDO DEL CLIENTE","Fila":2,"Columna":60}  
			pickle.dump(comandos, arc, 2)
			seleccion={"campocontrol":"1","Fila":4,"Columna":123,"Columnas":136}  
			pickle.dump(seleccion, arc, 2)
			arc.close()
			##return
		
		
		
		nombre=self.copiar(r_programa,nombre)
		arc = open(ambiente, "r")  
		comandos=pickle.load(arc)
		control=pickle.load(arc)
		arc.close()
		print comandos
#		print control
		
		if self.BuscarTipo(comandos,nombre):
			self.Procesar(control,nombre,comandos["ruta"]+"\\")
		
		
		
	def copiar(self,rutasalida,fuente):
		rutasalida+="\\splcopia"
		if not os.path.isdir(rutasalida):
			os.mkdir(rutasalida)
		destino,nombre=os.path.split(fuente)
		destino=rutasalida + "\\" + nombre
		shutil.copy(fuente, destino)
		return destino
	def BuscarTipo(self,comando,nombre):
		arc=open(nombre,"r")
		contarlinea=1
		encontro=False
		
		comando["Columna"]=comando["Columna"]-1
		if comando["Columna"]<0:
			comando["Columna"]=0
		
		while True:
			linea = arc.readline()
			if not linea: break
			if contarlinea==comando["Fila"]:
				##print "encontro %s %i"%(comando["buscar"],linea.find(comando["buscar"]))
				if linea.find(comando["buscar"]) == comando["Columna"]:
					#print linea
					encontro=True
				break
			contarlinea+=1
		arc.close()
		return encontro
	def Procesar(self,control,nombre,rutasalida):
		##print "nombre",nombre
		##print "rutasalida",rutasalida
		arc=open(nombre,"r")
		
		finarchivo=False
		indicador=""
		
		control["Fila"]=control["Fila"]-1
		if control["Fila"]<0:
			control["Fila"]=0
		sobra=""
		while not finarchivo:
			pagina,sobra,finarchivo=self.LeerPagina(arc,sobra)
			if len(pagina)>=control["Fila"]:
				fila=pagina[control["Fila"]]
				indicador_1=fila[control["Columna"]:control["Columnas"]]
				
				if len(indicador)==0:
					print "indicador =0"
					if len(indicador_1)==0:
						indicador="sicodigo.spl"
					else:
						indicador=indicador_1
				else:
					if len(indicador_1)>0:
						print "indicado4 1>0"
						indicador=indicador_1
						
			self.GuardarFinal(rutasalida,indicador,pagina)
		
		
		
		arc.close()

	def LeerPagina(self,arc,sobra):
		
		pag=[]
		if len(sobra)>0:
			pag.append(sobra)
		
		finarchivo=False
		salir=False
		while not salir:
			linea = arc.readline()
			if not linea: 
				finarchivo=True
				salir=True
				break
			salto=linea.find('\f')
			##print salto
			if salto>0:
				##print "salto"
				if salto<len(linea):
					##print "Sobra"
					sobra=linea[salto+1:]
					linea=linea[0:salto+1]
				salir=True
					
			pag.append(linea)
		return pag,sobra,finarchivo

	def GuardarFinal(self,rutasalida,indicador,pagina):
		rutasalida+=indicador + ".spl"
		arc=open(rutasalida,"a")
		for linea in pagina:
			arc.write(linea)
		arc.close()

##		f=open("c:/borrar/coco.txt","w")
##		for x in pagina:
##			f.write(x)
##		f.write ("**Sobra***")
##		f.write(sobra)
##		f.close()
