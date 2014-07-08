# -*- coding: utf-8 -*- 
## celular *#06#
import sqlite3
import os,sys
try:  
	import cPickle as pickle  
except ImportError:  
	import pickle


class campos_Envio():
	def __init__(self):
		self.fecha=''
		self.enviar=''
		self.adjuntos=''
		self.asunto=''
		self.bandera=''
		self.bscopia=''
		self.copia=''
		self.idtrabajo=0
		self.estado=0


	def Estructura(self):
		estructura = {'fecha':'TEXT',
				'enviar':'TEXT',
				'adjuntos':'TEXT',
				'asunto':'TEXT',
				'bandera':'TEXT',
				'estado':'NUMERIC',
				'bscopia':'TEXT',
				'copia':'TEXT',
				'idtrabajo':'NUMERIC'
				}
		return estructura

	def Campos(self):
		salida = {'fecha':self.fecha,
				'enviar':self.enviar,
				'adjuntos':self.adjuntos,
				'asunto':self.asunto,
				'bandera':self.bandera,
				'estado':self.estado,
				'bscopia':self.bscopia,
				'copia':self.copia,
				'idtrabajo':self.idtrabajo
				}

		return salida

		


class ObjBase():
	'''
	classdocs
	'''
	def __init__(self,nombre,crear=True):
		print "ObjBase->"
		'''
		Constructor
		'''
#		self.separador='/'
#		if not os.name=='posix':
#			self.separador="\\"	
#		self.rutabase=self.AbrirConfig()



		
		nombre=os.path.split(nombre)
		nombre=nombre[0] +os.sep + nombre[1]
		self.rutabase=nombre #ruta + os.sep + "config.db"
		print "Base de datos [%s]" % (self.rutabase)
		
		#Conectar Base de datos	   
		try:
			if os.path.isfile(self.rutabase):
				self.conector=sqlite3.connect(self.rutabase)
				
			else:
				if crear==False:
					print "error: no existe base"
					sys.exit(2)
									
				self.conector=sqlite3.connect(self.rutabase)
				self.Crear()
	
			self.verifTablas()
			self.conector.text_factory = lambda x: unicode(x, "utf-8", "ignore")
			self.conector.row_factory = sqlite3.Row
		
		except:
			print "error apertura BaseDatos"	
			self.rutabase=None
			
								
	def verifTablas(self):
		print "ObjBase->verifTablas"
		tablas=['tbl_Estado',
				'tbl_cliente',
				'tbl_usuarios',
				'tbl_Adjuntos',
				'tbl_impresoras',
				'tbl_correo',
				'tbl_logerror',
				'tbl_logimpr',
				'tbl_logenvio',
				'tbl_envioarch',
				'tbl_patrones',
				'tbl_spool'
				
				]
		sql = "SELECT name FROM sqlite_master WHERE type='table';"
		cursor=self.conector.cursor()
		cursor.execute(sql)
		registro=cursor.fetchall()
		cursor.close()
		busqueda =[]
		for campos in registro:
			busqueda.append(campos[0])
		for tabla in tablas:
			if not tabla in busqueda:
				print "no existe [%s]"% (tabla)
				if tabla =='tbl_Estado'			:self.CrearEstados()
				elif tabla =='tbl_cliente'		:self.CrearClientes()
				elif tabla =='tbl_usuarios'		:self.CrearUsuarios()
				elif tabla =='tbl_Adjuntos'		:self.CrearAjuntos()
				elif tabla =='tbl_impresoras'	:self.CrearImpr()
				elif tabla =='tbl_correo'    	:self.CrearCorreo()
				elif tabla =='tbl_logerror'		:self.CrearLogError()
				elif tabla =='tbl_logimpr'		:self.CrearLogImpresion()
				elif tabla =='tbl_logenvio'		:self.CrearLogEnvio() 
				elif tabla =='tbl_envioarch'	:self.CrearEnvioArch()
				elif tabla =='tbl_patrones'		:self.CrearPatrones()
				elif tabla =='tbl_spool'		:self.CrearSpool()
			else:
				print "existe [%s]"% (tabla)

	def CrearSpool(self):
		print "CrearSpool"
		campos='''
				idstado 	NUMERIC NOT NULL ,
				idimpresora	NUMERIC NOT NULL ,
				usuario 	TEXT NOT NULL,
				nombrejob 	TEXT NOT NULL,
				jobid 		NUMERIC NOT NULL, 
				copias		NUMERIC NOT NULL, 
				fecha 		TEXT NOT NULL
			'''
		self.CreaTabla("tbl_spool", campos)
					
	def CreaTabla(self,tabla,campos):
		print "->CreaTabla"
		if type(campos)==list:
			sql = 'CREATE TABLE IF NOT EXISTS %s (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,' % (tabla)
			primer=True
			for campo in campos:
				if primer:
					primer =False
				else:
					sql +=','
				sql += campo
		
			sql += ');'
		if type (campos)==dict:
			sql = 'CREATE TABLE IF NOT EXISTS %s (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,' % (tabla)
			primer=True
			
#			print campos
			for campo in campos.keys():
				if primer:
					primer =False
				else:
					sql +=','
#				print campos
#				print campos[campo]

				sql += "%s %s" %(campo,campos[campo]) 
		
			sql += ');'
				
		
		else:
			campos ='id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,' + campos
			sql = 'CREATE TABLE IF NOT EXISTS %s (%s);' % (tabla,campos)
		print sql
		cursor=self.conector.cursor()
		cursor.execute(sql)
		cursor.close()
		return True

	def CrearTablaTempProc(self):
		campos='''
				fecha,
				rutapdf,
				rutapcl ,
				estado NUMERIC
				'''
		self.CreaTabla('tbl_temp1', campos)

	def BorrarTablaTempProc(self):
		cursor=self.conector.cursor()
		cursor.execute("DELETE FROM tbl_temp1;")
		self.conector.commit()
		cursor.close()

	def BorrarReg(self,tabla='',condicion=''):
		print 'BorrarReg'
		if len(tabla)==0:
			return False
		sql='DELETE FROM %s' %(tabla)
		if len(condicion)>0:
			sql +=' WHERE %s' %(condicion)
		sql +=';'
		print sql
		cursor=self.conector.cursor()
		cursor.execute(sql)
		self.conector.commit()
		cursor.close()
		return True

	def CrearCorreo(self):
		print "Crea Tabla Correo"
		campos=''' 
				htmlcontenido,
				txtcontenido ,
				puerto NUMERIC, 
				usuario TEXT, 
				clave TEXT, 
				servidor TEXT, 
				tls varchar(1), 
				bandera TEXT, 
				enviado TEXT, 
				rutafinal TEXT,
				rutaanexo TEXT,
				archivoanexo TEXT,
				confirmar TEXT,
				estado NUMERIC
			'''
		self.CreaTabla('tbl_correo', campos)

	def CrearLogEnvio(self):
		#campos=campos_Envio().Estructura()		
		#self.CreaTabla('tbl_logenvio', campos)
		campos=''' 
			fecha TEXT,
			enviar TEXT,
			adjuntos TEXT,
			asunto TEXT,
			bandera TEXT,
			estado NUMERIC,
			bscopia TEXT,
			copia TEXT,
			rutafinal TEXT,
			idtrabajo NUMERIC 
			'''
		self.CreaTabla('tbl_logenvio', campos)
		
	def CrearLogError(self):	
		print "Tabla log"
		campos=''' 
				fecha TEXT,
				descripcion TEXT ,
				estado NUMERIC 
			'''
		self.CreaTabla('tbl_logerror', campos)

	def CrearLogImpresion(self):	
		campos=''' 
				fecha TEXT,
				archivo TEXT ,
				usuario TEXT,
				equipo TEXT,
				nropag NUMERIC,
				estado NUMERIC 
			'''
		self.CreaTabla('tbl_logimpr', campos)

	def CrearImpr(self):
		campos='''
		nombre TEXT NOT NULL ,
		tipo INTEGER NOT NULL  REFERENCES tbl_Estado (pertenecia),
		UNIQUE (nombre)
		'''
		self.CreaTabla('tbl_impresoras', campos)

	def CrearEstados(self):
		print "CrearEstados"
		campos='''
				pertenecia 	NUMERIC NOT NULL ,
				valor		NUMERIC NOT NULL ,
				texto 		TEXT NOT NULL 
			'''
		self.CreaTabla("tbl_Estado", campos)
	
	def CrearClientes(self):
		print "Crea Tabla cliente"
		campos='''
				busqueda  TEXT NOT NULL ,
				dircorreo TEXT NOT NULL ,
				imprimir  INTEGER(1) NOT NULL  DEFAULT 1,
				pdf       INTEGER(1) NOT NULL  DEFAULT 0,
				correo    INTEGER(1) NOT NULL  DEFAULT 0,
				estado    NUMERIC NOT NULL  REFERENCES tbl_Estado (id),
				UNIQUE (busqueda)
				'''		
		self.CreaTabla('tbl_cliente', campos)

	def CrearUsuarios(self):
		campos='''
				windows TEXT NOT NULL ,
				impresora TEXT NOT NULL ,
				estado NUMERIC NOT NULL  REFERENCES tbl_Estado (id),
				UNIQUE (windows)
				'''
		self.CreaTabla("tbl_usuarios", campos)

	def CrearAjuntos(self):
		print "Crea Tabla relacion archivopcl ->adjunto ->pdf"
		campos='''
				nombre TEXT NOT NULL ,
				dirPdf TEXT NOT NULL ,
				dirpcl TEXT NOT NULL ,
				estado NUMERIC NOT NULL  REFERENCES tbl_Estado (id),
				UNIQUE (nombre)
				'''
		self.CreaTabla('tbl_Adjuntos', campos)

	def CrearEnvioArch(self):
		print "CrearEnvioArch"
		campos='''
				proceso	TEXT NOT NULL,
				impresora TEXT NOT NULL,
				fecha   TEXT NOT NULL,
				ruta	TEXT NOT NULL,
				usuario TEXT NOT NULL,
				idambiente INTEGER,
				estado	INTEGER
			'''
		self.CreaTabla("tbl_envioarch", campos)

	def CrearPatrones(self):

		print "CrearAccion"
		campos='''
				patron		TEXT NOT NULL,
				descrip 	TEXT NOT NULL,
				ambiente	TEXT NOT NULL,
				idproceso	INTEGER NOT NULL  
			'''
		self.CreaTabla("tbl_patrones", campos)
	

	def Crear(self):
		print "Crear Base de datos"
		self.CrearEstados()
		self.CrearCorreo()
		self.CrearClientes()
		self.CrearUsuarios()
		self.CrearAjuntos()
		self.CrearImpr()
		self.CrearCorreo()
		self.CrearLogEnvio()
		self.CrearLogError()
		self.CrearLogImpresion()
		self.CrearTablaTempProc()
		self.CrearEnvioArch()
		self.CrearPatrones()
		#self.CrearAmbientes()
		self.listaestadosdef()
		
	def Contar(self,tabla,condicion=''):
		print "ObjBase.Contar"
		if len(tabla)==0:
			return 0
		sql='SELECT COUNT (id) FROM '+tabla
		if len(condicion.strip())>3:
			sql+=' WHERE '+ condicion
		sql +=';'
		cursor=self.conector.cursor()
		print sql
		cursor.execute(sql)		
		campo=cursor.fetchone()
		if campo==None:
			return 0
		salida = campo[0]
		cursor.close()
		return salida
	
		
	#Se puede actulaizar de dos maneras:
	#registro={'campo1':valor1,'campon':valor}
	#registro='campo1='valor1',campon='valorn'
	
	def ActualizarCampos(self,tabla,registro,condicion):
		print "actualiza registro"
		sql=""
		coma=""
		print type (registro)
		if type(registro) is dict:
			print "dict"
			for campo in registro:
				sql += coma + campo + "='" + registro[campo]+"'"	
				if coma=="":coma=','
			sql="UPDATE %s SET %s WHERE %s" %(tabla,sql,condicion)
		else:
			sql="UPDATE %s SET %s WHERE %s" %(tabla,registro,condicion)
		
		print sql
		try:
			cursor=self.conector.cursor()
			cursor.execute(sql)
			self.conector.commit()
			cursor.close()
			return True
		except:	
			return False
					
	def InsertarVarios(self,tabla="",campos=[],valores=[]):
		
		cursor=self.conector.cursor()
		mascara='?,' * len(campos)
		mascara=mascara[:-1] 
		comando="INSERT INTO %s (" % (tabla)
		for campo in campos:
			comando+=campo +","
		comando=comando[:-1] + ") "
		comando+="VALUES (%s)" % mascara
		print comando
		print valores
		try:
			cursor.executemany(comando,valores)
			#cursor.executemany("INSERT INTO config (grupo,desc1,desc2) VALUES (?,?,?)",valores)
			self.conector.commit()
			print "ok"
			return True
		except:
			print "err"
			return False

	def SelectUno(self,campos="*",tabla="",condicion=""):
		print "ObjBase->SelectUno"
		cursor=self.conector.cursor()
		#salida=[]
		if len(tabla)==0:
			return None
		sql="SELECT %s FROM %s " % (campos,tabla)
		if len(condicion)>0:
			sql+=" WHERE %s" %(condicion)
		print sql		
		cursor.execute(sql + ';')
		salida=cursor.fetchone()
		print salida
		cursor.close()
		return salida
	
	def LeerCampos(self,campos="*",tabla="",condicion="",Ordenar="", Limite=""):
		if len(tabla)==0:
			return None
#		salida=[]		
		self.conector.row_factory = sqlite3.Row 
		cursor=self.conector.cursor()
		
		if type(campos)==list:
			sql="SELECT "
			primer=True
			for campo in campos:
				if primer:
					primer=False
				else:
					sql += ','
				sql += campo
			
		else:
			sql="SELECT %s " % (campos)
		
		sql +=  " FROM %s" % (tabla)
		
		if len(condicion)>0: sql+=" WHERE %s" %(condicion)
		if len(Ordenar)>0:
			sql+=" ORDER BY %s" %(Ordenar)
		if len(Limite)>0:
			sql+=" LIMIT %s" %(Limite)
		
		print sql
		cursor.execute(sql)
		registro=cursor.fetchall()
		return registro
	
		
#		col_name_list = [tuple[0] for tuple in cursor.description]
#		print col_name_list
#		
#		for fila in cursor:
#			salida.append(fila)
#		cursor.close()
#		return salida
	
	def Insertar(self,tabla="",campos="",valores=""):
		#try:
		if type(campos)==dict:
			temp=campos
			campos=''
			valores=''
			primer =True
			for campo in temp.keys():
				if primer:
					primer =False
				else:
					campos +=','
					valores +=','
				campos +=campo
#				if temp[campo]=='str':
#					temp[campo]=unicode(temp[campo], 'utf-8', 'replace')
#					valores+= "'" +  temp[campo] + "'"
#				else:	
				valores+= "'%s'" %(temp[campo])
			


		sql="INSERT INTO %s (%s) VALUES (%s);" % (tabla,campos,valores)
		
		print sql
		try:
			cursor=self.conector.cursor()
			cursor.execute(sql)
			self.conector.commit()
			salida = cursor.lastrowid
			cursor.close()
			return salida
		except sqlite3.Error as e:
			print "!!!!!!!!!!!!!!!"
			print "Error ocurrido:", e.args[0]
		#	return -1

	def adlistaestado(self,vista,pertenece):
		print "adlistaestado"
		valores=[(pertenece,0,'Desactivado'),(pertenece,1,'Activado'),]
		self.InsertarVarios("tbl_Estado", ["pertenecia","valor","texto"], valores)	
		cursor=self.conector.cursor()
		sql="CREATE VIEW IF NOT EXISTS %s AS SELECT id, valor,texto FROM tbl_Estado WHERE pertenecia=%i;" % (vista,pertenece)
		print sql
		cursor.execute(sql)
	def listaestadosdef(self):
		print "listaestadosdef"
		self.adlistaestado('v_estadocorreo',1)
		self.adlistaestado('v_estadousr',2)
		self.adlistaestado('v_estadoadj',3)

	def ejecutarSQL(self,sql=""):
		print "ObjBase->ejecutarSQL"
		cursor=self.conector.cursor()
		print sql
		cursor.execute(sql)
		self.conector.commit()
		cursor.close()
	
#valores Generales	
	
	def Gen_rutaModelos(self):
		return self.SelectUno("texto", "tbl_Estado", "pertenecia=5 and valor=1")

	def Gen_rutaPrgEnvioArchivo(self):
		return self.SelectUno("texto", "tbl_Estado", "pertenecia=5 and valor=2")

	def Gen_rutaPrgEnvioCorreo(self):
		return self.SelectUno("texto", "tbl_Estado", "pertenecia=5 and valor=3")

		
if __name__ == '__main__':
	print "Obj Base datos"
	G_ruta=sys.argv[0]
	G_ruta='.'#os.path.split(G_ruta)
	G_ruta=G_ruta[0]
	OBase=ObjBase("config.db")
