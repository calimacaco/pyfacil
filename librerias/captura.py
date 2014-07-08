'''
Created on 12/10/2013

@author: marco
'''

import os,sys
import random
import datetime

if not os.name=='nt':
	import msvcrt

class ObCaptura():
	'''
	classdocs
	'''


	def __init__(self):
		self.nombreSpool=""
		
		
	def GenNombre(self,ruta):
		hora=str(datetime.datetime.now())
		hora=hora[0:10]
		nrospool=str(random.randint(1,100000))
		if len(ruta)>0:
			ruta + os.sep
			
		self.nombreSpool= ruta +'proceso' +os.sep  +str(nrospool) + "-" + hora + ".spl"
		while os.path.isfile(self.nombreSpool):
			self.nombreSpool=str(random.randint(1,10000))
		
	
	def Stdin(self,ruta):
		self.GenNombre(ruta)
		archivo=file(self.nombreSpool,'wb')
		if  not os.name=='posix':
			msvcrt.setmode (sys.stdin.fileno(), os.O_BINARY)
		archivo.write(sys.stdin.read())
		archivo.close()

