#!c:\python27\python.exe
# -*- coding: utf-8 -*- 
from librerias.ctrlog import  ObLog
from PIL import Image
import ImageEnhance
import os
from argumentos import objPrincipal



class convert_img():
	def __init__(self,nivelLog):
		self.imagen=None
		self.log=ObLog('ConvertLogo')
		self.log.nivel=nivelLog
		self.archsalida=None
	
	def setImagen(self,rutaimagen):
		self.log.logger.info ('setImagen (%s)'%(rutaimagen))
		if os.path.isfile(rutaimagen):
			self.imagen=Image.open(rutaimagen)
			return True
		else:
			self.log.logger.error ('no existe archivo de imagen')
			return False
		
	def setArchivoSalida(self,ruta):
		self.log.logger.info ('setArchivoSalida (%s)'%(ruta))
		self.archsalida=ruta
		
	def procesar(self):
		self.log.logger.info (' procesar')
		self.log.logger.info ('Entrada: %s' % (obarg.archentrada))
		self.log.logger.info ('Entrada: %s' % (obarg.archentrada))
		self.log.logger.info ('Escala : %i' % (obarg.escala))
		self.log.logger.info ('Brillo : %i' % (obarg.brillo))	

		if self.imagen==None: return
		if self.archsalida==None: return
		ancho,alto = self.imagen.size
		img_neg=self.imagen.convert('1')
		img_neg.show()
		pixels = img_neg.load() 
		all_pixels = []
		for y in range(alto):
			for x in range(ancho):
				cpixel = pixels[x, y]
				if cpixel==255:
					all_pixels.append('0')
				else:
					all_pixels.append('1')
		pos=0
		lineas=[]
		for y in range(alto):
			#print ''
			salida=[]
			letra=''
			for x in range(ancho):
				letra +=all_pixels[pos]
				if len(letra)==8:
					salida.append(int(letra, 2))
					letra =''
				#print '%s' %(all_pixels[pos]),
				pos +=1
			if ancho%8 != 0:
				letra += '0' * (8 - (ancho%8)) 
				salida.append(int(letra, 2))
			lineas.append(salida)
		all_pixels=[]
		esc=chr(27)
		try:
			arcsalida = open (self.archsalida,'w')
			#este no va
			##arcsalida.write('%s&u600D%s*p1000x1000Y' % (esc,esc))  					#unidad de medida, pos x,y
			arcsalida.write('%s*r1A' %(esc)) 										#Inicio Raster por current posicion cursor
			arcsalida.write('%s*t1200R%s*r0F%s*r%is%iT' % ( esc,esc,esc,ancho,alto))	#resolucion, presentacion, ancho, alto
			
			if ancho % 8 !=0:
				nrobytes= (ancho + (8 - (ancho % 8)))/8
			else:
				nrobytes= ancho / 8
				
			arcsalida.write('%s*b0M' %(esc))
			
			for salida in lineas:
				arcsalida.write('%s*b%iW' %(esc,nrobytes))
				letra=''
				for valor in salida:
					letra+=chr(valor)
				arcsalida.write('%s' %(letra))
				
			arcsalida.write('%s*rC' % (esc))  								#Fin raster
			arcsalida.close()
			return True
		except:
			self.log.logger.error ('no es posible guardar archivo de salida')
			return False
	
	
	def escalar (self, porcentaje):
		self.log.logger.info ('escalar')
		porcentaje = porcentaje /100.0
		ancho,alto = self.imagen.size
		ancho = int(ancho * porcentaje)
		alto= int(alto * porcentaje)
		self.imagen = self.imagen.resize((ancho, alto), Image.ANTIALIAS)
	

	def modify_img (self,opacity = 0.6):
		self.log.logger.info ('modify_img')
		"""The modifications consist on changing the mode to 
		Grayscale and to add a white layer with the specified opacity
		"""
		if self.imagen.mode != "L":
		        self.imagen = self.imagen.convert ("L")
		#Create a white image 
		white_img = Image.new ("RGB", self.imagen.size, (255, 255, 255))
		white_img = white_img.convert('RGBA')
		alpha = white_img.split()[3]
		alpha = ImageEnhance.Brightness(alpha).enhance(opacity)
		white_img.putalpha(alpha)
		#Create a layer with the white image
		layer = Image.new('RGBA', self.imagen.size, (0,0,0,0))
		layer.paste(white_img, layer.getbbox())
		#Create the final image
		self.imagen = Image.composite(layer, self.imagen, layer)
		#self.imagen.show()
		self.log.logger.info ('Fin')
		
class x():
	def __init__(self):
		self.archentrada='EHR_1100.png'
		self.archsalida='salida.lgo'
		self.escala=-1
		self.brillo=-1
		
		
if __name__ == '__main__':
	obarg=objPrincipal()
	obarg.procesar()	
	#obarg=x()

	objconv=convert_img(3)
	objconv.setImagen(obarg.archentrada)
	objconv.setArchivoSalida(obarg.archsalida)
	if obarg.escala!=-1:objconv.escalar(obarg.escala) 
	if obarg.brillo!=-1:objconv.modify_img(obarg.brillo)
	objconv.procesar()
	print "finalizo"
