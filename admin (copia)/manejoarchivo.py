'''
Created on 18/12/2013

@author: marco
'''
from ObjGrilla import ObGrilla

class ObjRelArchivo():
	def __init__(self,padre,base):	
		print "ObjRelArchivo"
		self.ObaseD=base
		self.padre=padre
		tabla="tbl_Adjuntos"
		campos="id, archivo, accion, descripcion"
		condicion=""
		limite=20
		orden ="id DESC"
		#Vista
		self.formato=ObGrilla(self.padre,u"Lista de Relacion archivo -> proceso")
		self.formato.InfoBase(self.ObaseD, tabla, campos, condicion, orden, limite,'nombre')
		titulo=['Id','nombrearchivo','accion','descripcion']
		ancho=[40,200,200,420]
		self.formato.Titulos_columna(titulo, ancho)
		self.formato.Listar()
