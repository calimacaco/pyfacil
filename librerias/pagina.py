'''
Created on 15/01/2014

@author: marco

objPagina(
			nombrearch=Nombre del archivo que contiene la pagina 
			Saltolinea=el final de linea es por defecto LineFeed.
			lectura, Normal = Filaxcoluma,
		)
       




Control Seleccion
'''
from ctrlog import ObLog
from twisted.protocols.ftp import EXCEEDED_STORAGE_ALLOC

class objPagina():
	def __init__(self):
		self.lineas=None
		self.separador=''
		self.log=False
		self.manlog=ObLog(nivel=5)
		self.error=False
		
	def leerPagina(self,nombrearch,saltolinea='\n',normal=True):
		if self.log:self.manlog.logger.debug("objPagina.leerPagina ->>")
		try:
			archpagina=open(nombrearch,'rb')
			if normal:
				self.lineas=archpagina.read()
				self.lineas=self.lineas.split(saltolinea)
			else:
				self.lineas=archpagina.read()
			archpagina.close()
		except:
			if self.log:self.manlog.logger.error("objPagina.leerPagina:Leer %s" % (nombrearch))
			self.error=True
			return
		if self.log:self.manlog.logger.debug("objPagina.leerPagina <<-")

	def Seleccionar(self,prefijo='',lineaInicial=0,nroLineas=0,nroCampo=1,columna=0,nroColumnas=0,separador=''):
		'''
		Seleccion por Campos
		prefijo            	=  Texto selecion por perfijo
		lineaInicial		=  Nro de linea inicial de lectura si es 0, inicia desde la primera
		nroLineas			= Nro linea a tomar despues del marcador de la lineaInicial, si es 0 Son todas las siguientes.
		columna				= inicio columna, si es 0 e toma toda la la linea
		nroColumnas			= selecciona la cantidad de caracteres despues del marcardor de columna
		'''
		if self.log:self.manlog.logger.debug("objPagina.Seleccionar ->>")
		if self.lineas==None:return
		contadorlineas=0
		datos=[]		
		if len(separador)==0 and len(self.separador)>0:
			separador=self.separador		

		for linea in self.lineas:			
			if len(prefijo)>0:
				#print "campos"
				if linea[0:len(prefijo)]==prefijo:
					contadorlineas +=1
					linea=linea[len(prefijo):]
					#print contadorlineas,lineaInicial
					if lineaInicial <=contadorlineas:
						if len(separador)>=1:
							campo=linea.split(separador)
							linea=campo[nroCampo-1]
							linea=self.selcol(columna, nroColumnas, linea)
						datos.append(linea)
			else:
				#print "lineas"
				contadorlineas +=1
				if lineaInicial <= contadorlineas:
					linea=self.selcol(columna, nroColumnas, linea)
					datos.append(linea)
					
			if nroLineas == 0: continue		
			if len(datos)==nroLineas:break

		if self.log:self.manlog.logger.debug("objPagina.Seleccionar <<-")
		return datos
				
			
	#Seleccion de columnas
	def selcol(self,columna,nroColumnas,linea):
		if self.log:self.manlog.logger.debug("objPagina.selcol ->> %i %i %s" %(columna,nroColumnas,linea))
		if columna >=0:
			if nroColumnas==0:
				linea=linea
			elif nroColumnas>0:
				nroColumnas += (columna -1)
				linea=linea[columna-1:nroColumnas]
			elif columna<0:
				linea=linea[columna:]
		if self.log:self.manlog.logger.debug("objPagina.selcol <<-")
		return linea
	
if __name__ == '__main__':
	pag=objPagina()
	
	pag.leerPagina("pagina1.txt")
	print pag.Seleccionar(lineaInicial=8, nroLineas=5,  columna=1, nroColumnas=20)
	print "----------Campos---------------"
	print pag.Seleccionar(prefijo='a',lineaInicial=0, nroLineas=0,nroCampo=1,  columna=0, nroColumnas=0)
	print "-------------------------"
	print pag.Seleccionar(prefijo='a',lineaInicial=0, nroLineas=0, nroCampo=1,  columna=0, nroColumnas=0,separador=':')
	print "-------------------------"
	pag.log=True
	pag.separador=':'
	print pag.Seleccionar(prefijo='a',lineaInicial=0, nroLineas=0, nroCampo=1,  columna=0, nroColumnas=0)
	print "-------------------------"
	print pag.Seleccionar(prefijo='a',lineaInicial=2, nroLineas=2, nroCampo=1,  columna=0, nroColumnas=0)
	print "-------------------------"
	print pag.Seleccionar(prefijo='a',lineaInicial=2, nroLineas=2, nroCampo=1,  columna=3, nroColumnas=7)
	print "-------------------------"
	print pag.Seleccionar(prefijo='a',lineaInicial=4, nroLineas=2, nroCampo=1,  columna=3, nroColumnas=7)
	