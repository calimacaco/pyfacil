import sys, getopt

class objPrincipal():
	def __init__(self):
		self.archentrada = ''
		self.archsalida = ''
		self.escala=-1
		self.brillo=-1
		
	def uso(self):
		print 'convert  -e <Nombre archivo de imagen> -s <Nombre archivo de salida LGO>'
		print 'Parmetros adicionales'
		print '-t #              -->Escalar a un porcentaje ###% '
		print '-b #.#            -->Brillo  1=blanco'

		print ''
		sys.exit(2)
		
		
		
	def procesar(self):
		argv = sys.argv[1:]
		if len(argv)==0:
			self.uso()

		try:
			opts, args = getopt.getopt(argv,"he:s:t:b:",["entrada=","salida=","tam","brillo"])
		
		except getopt.GetoptError:
			self.uso()
			
		for opt, arg in opts:
			if opt == '-h':
				self.uso()
			elif opt in ("-e", "--entrada"):
				self.archentrada = arg
			elif opt in ("-s", "--sailda"):
				self.archsalida = arg + '.lgo'
			elif opt in ("-b", "--brillo"):
				self.brillo = arg
			elif opt in ("-t", "--tam"):
				self.escala= arg
		
		if len(self.archsalida)==0:
			self.archsalida='salida.lgo' 


if __name__ == "__main__":
	ob=objPrincipal()
	ob.procesar()
	print 'Entrada: ', ob.archentrada
	print 'Salida : ', ob.archsalida
	print 'Escala : ', ob.escala
	print 'Brillo : ', ob.brillo
