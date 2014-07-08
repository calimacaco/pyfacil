'''
Created on 28/07/2013

@author: marco
'''

class objCampos():
	'''
	Manejo de campos, estructurado de la siguiente manera:
	idcampo-> tipo caracter
	columna ->Inicio toma de caracteres, si es 0 se toma todo el campo
	columnas ->Nro de caracteres a tomar, si es 0 se toma desde el inicio.columna hasta final
	'''
	def __init__(self):
		'''
		Constructor
		'''
		self.tipo=0
		self.idcampo=''
		self.columna=0
		self.columnas=0
		
	def __tipo__(self):
		return 'campos'
	
class objFilas():
	'''
	classdocs
	'''
	def __init__(self):
		'''
		Constructor
		'''
		self.tipo=1
		self.fila=0
		self.filas=0
		self.columna=0
		self.columnas=0
		
class obCaracteres():
	def __init__(self):
		self.tipo=2
		self.bloques=0