#!/usr/bin/env python
# -*- coding: utf-8 -*- 

'''
Created on 9/10/2013
@author: marco
'''

import sys
import os


class obArg():
	def __init__(self):

		self.jobid=sys.argv[1]  	#argv[1]    The job ID
		self.user=sys.argv[2]  		#argv[2]    The user printing the job
		self.jobname=sys.argv[3] 	#argv[3]    The job name/title
		self.copias=sys.argv[4]		#argv[4]    The number of copies to print
		self.opciones=sys.argv[5]	#argv[5]    The options that were provided when the job was submitted
		self.nombrespool=sys.argv[6]#argv[6]    The options that were provided when the job was submitted

def argumentos():	
	contador=0
	a=open('/tmp/marco.prn','a')
	for arg  in sys.argv:
		a.write ( 'Argumento[%i]=%s \n' %(contador, arg))
		contador +=1
	try:
		a.write ( 'Argumento=%s \n' %(os.environ['HOME']))
	except:
		pass
	
	a.close()





if __name__ == '__main__':
	argumentos()
	arc=open (sys.argv[6],'r')
	datos=arc.read()
	arc.close()
	esc=chr(27)
	datos= '%s%%-12345X@PJL JOB NAME ="Simplesoft"\n@PJL COMMENT ** Facil - SimpleSoft **\n@PJL ENTER LANGUAGE=PCL\n%s\f%s%%-12345X' %(esc,datos,esc) 
	a=open('/tmp/marco.prn','a')
	a.write(datos)
	a.close()
	
	
	
	sys.stderr.write('INFO:Envio datos')
		
	sys.stdout.write (datos)
	sys.stdout.flush()	
	sys.exit(0)