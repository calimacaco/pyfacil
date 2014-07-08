#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 12/10/2013

@author: marco
'''


# error =1   No existe archivo de configuracion

import os
from librerias.ctrlog import ObLog



class ObCtrlArchivo():
	'''
	classdocs
	'''


	def __init__(self,nivelLog):
		'''
		Constructor
		'''
		self.log=ObLog('ObCtrlArchivo')
		self.log.nivel=nivelLog
		self.error=0
	
	def dirRecusivo(self,ruta):
		
		if not ruta[-1]==os.sep:    ruta+=os.sep
		print ruta
		
		
	def abrirConfig(self):
		self.log.logger.info('ctrlarchivo.abrirConfig')
		ruta = self.buscarConfig()
		if self.log==1:return ''
		else: return ruta


		
	def buscarConfig(self):
		self.log.logger.info('ctrlarchivo.buscarConfig')
		try:
			salida = os.environ['pyfacil']
			self.log.logger.info ('ruta configuracion:%s'%(salida))
			return salida

		except:
			self.log.logger.warning('No existe variable de entorno pyfacil')
			if os.name ==  'posix': #Linux
				if os.path.isfile('/ect/pyfacil.conf'):
					self.log.logger.info ('ruta configuracion:/ect/pyfacil.conf')
					return '/ect/pyfacil.conf'
				else:
					self.log.logger.warning('no existe archivo de configuracion')
					return None
				
			elif os.name ==  'nt' : #Windows
				if os.path.isfile ('c:\\pyfacil\\pyfacil.conf'):
					self.log.logger.info ('ruta configuracion:c:\pyfacil\pyfacil.conf')
					return 'c:\\pyfacil\\pyfacil.conf'
				else:
					self.log.logger.warning('no existe archivo de configuracion')
					return None				
			else: #faltan:, 'os2', 'ce', 'java', 'riscos'.
				self.log.logger.error('Sistema operativo desconocido')
				self.error=1
				return None
			
			
		
		
if __name__ == '__main__':
	ob=ObCtrlArchivo()
	ob.dirRecusivo('/home/marco/borrar/sumadre/estuvo/aqui')
	
	
	