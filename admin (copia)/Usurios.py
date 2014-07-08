'''
Created on 14/04/2013

@author: marco
'''
from FormMapic import F_Grilla

class MyClass(object):
	'''
	classdocs
	'''


	def __init__(selfparams):
		'''
		Constructor
		'''
		self.ObjGrilla=F_Grilla()
		
	def Grilla(self):
		tabla="tbl_cliente"
		campos="id, busqueda, dircorreo,CASE WHEN (imprimir=1) THEN 'X' ELSE '' END AS imp_x ,CASE WHEN (pdf=1) THEN 'X' ELSE '' END AS pdf_x, CASE WHEN (correo=1) THEN 'X' ELSE '' END AS correo_x"
		condicion=""
		limite=20
		orden ="id DESC"
		self.ObGrilla(self,u"Lista de Usuarios registrados")
		self.ObGrilla.InfoBase(self.ObaseD, tabla, campos, condicion, orden, limite)
		titulo=['Id','Identificador','Dirección Correo','imprimir',"pdf","correo"]
		ancho=[40,200,300,90,50,80]
		self.ObGrilla.Titulos_columna(titulo, ancho)
		self.ObGrilla.Listar()
		self.ObjGrilla.f2s_TxtLimite.SetValue('20')
	