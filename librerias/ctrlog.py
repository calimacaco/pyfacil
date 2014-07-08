#!/usr/bin/env python
# -*- coding: utf-8 -*- 
'''
Created on 12/10/2013

@author: marco
'''

import logging 
import logging.handlers 

class ObLog(object):
	'''
	classdocs
	'''
	def __init__(self,nombrelog='facil.log',nivel=0):
		'''
		Constructor
		'''
		self.logger=logging.getLogger(nombrelog) 
		# Indicamos el nivel máximo de seguridad para los mensajes que queremos que se 
		# guarden en el archivo de logs 
		# Los niveles son: 
		# DEBUG - El nivel mas alto 
		# INFO 
		# WARNING 
		# ERROR 
		# CRITIAL - El nivel mas bajo logger.setLevel(logging.DEBUG) 
		# Creamos una instancia de logging.handlers, en la cual vamos a definir el nombre
		# de los archivos, la rotación que va a tener, y el formato del mismo 
		# Si maxBytes=0, no rotara el archivo por tamaño 
		# Si backupCount=0, no eliminara ningún fichero rotado 
		
		handler = logging.handlers.RotatingFileHandler(filename='facil.log', mode='a', maxBytes=1024, backupCount=15) 
		# Definimos el formato del contenido del archivo de logs 
		formatter = logging.Formatter(fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s',datefmt='%y-%m-%d %H:%M:%S') 
		# Añadimos el formato al manejador 
		handler.setFormatter(formatter) 
		# Añadimos el manejador a nuestro logging 
		self.logger.addHandler(handler) 
		# Añadimos mensajes al fichero de log 
		self.nivel=nivel
		self.setNivel(self.nivel)
		
	def setNivel(self,nivel):
		if self.nivel==0:self.logger.setLevel(logging.DEBUG)
		elif self.nivel==1:self.logger.setLevel(logging.INFO)
		elif self.nivel==2:self.logger.setLevel(logging.WARNING)
		elif self.nivel==3:self.logger.setLevel(logging.ERROR)
		elif self.nivel==4:self.logger.setLevel(logging.CRITICAL)
		elif self.nivel > 4:
			self.nivel=3
			self.logger.setLevel(logging.ERROR)
		
		print nivel
		
		
	def getNivel(self):
		return self.nivel
		
if __name__ == "__main__":
		oblog=ObLog('prueba')
		oblog.logger.setLevel=5
		oblog.logger.debug('message debug') 
		oblog.logger.info('message info') 
		oblog.logger.warning('message warning') 
		oblog.logger.error('message error') 
		oblog.logger.critical('message critical')
		