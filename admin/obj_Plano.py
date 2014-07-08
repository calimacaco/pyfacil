'''
Created on 12/03/2013

@author: marco
'''

class ObPlano():
	'''
	classdocs
	'''


	def __init__(self):
		'''
		Constructor
		'''
		self.nombre=""
		self.basedatos=None
		
		
	def Fun_Formato(self,padre):
		print "Formato"
		
	
	def AbrirPlano(self):
		abrir=open (self.nombre,"r")
		
		for linea in abrir.readlines():
			datos=linea.split(',')