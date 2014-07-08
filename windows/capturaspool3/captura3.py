'''
Created on 22/02/2014

@author: marco

redmon de ghostscript tiene tres maneras de entregrar el archivo de impresion y 4 salida posible.
Ademas vamos a incorporar funciones de guarda spools, con plugin de preproceso. y preprocesos al spool de 
entrega a Facil

Formas de procesar:
1.)  El spool llega stdin y el envio a la impresora es por el programa. FACIL
2.)  El spool es entregado desde un archivo y el envio a la impresora es por el programa. FACIL
3.)  El spool llega Stdin, se procesa por FACIL y retorna Stdout a la impresora
4.)  el spool llega Stdin y se entrega una ruta para escribir la salida
5.)emprendetonica udistrital


'''

class MyClass(object):
	'''
	classdocs
	'''


	def __init__(selfparams):
		'''
		Constructor
		'''
		