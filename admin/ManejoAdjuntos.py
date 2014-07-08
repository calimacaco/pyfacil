#!/usr/bin/env python
# -*- coding: utf-8 -*- 

'''
Created on 15/04/2013

@author: marco
'''

from ObjGrilla import ObGrilla

class ObjAdjunto():
	def __init__(self,padre,base):	
		print "ObjAdjunto"
		self.ObaseD=base
		self.padre=padre
		tabla="tbl_Adjuntos"
		campos="id, nombre, dirPdf, dirpcl, estado"
		condicion=""
		limite=20
		orden ="id DESC"
		#Vista
		self.formato=ObGrilla(self.padre,u"Lista de Relacion PDF -> PCL")
		self.formato.InfoBase(self.ObaseD, tabla, campos, condicion, orden, limite,'nombre')
		titulo=['Id','Identificador','Ruta PDF','Ruta PCL.',"estado"]
		ancho=[40,80,440,420,45]
		self.formato.Titulos_columna(titulo, ancho)
		self.formato.Listar()
