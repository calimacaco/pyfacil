#!/usr/bin/env python
# -*- coding: utf-8 -*- 
'''
Created on 14/08/2013

@author: marco

Converso de encabezados de facil -> python
'''



import struct
from estructura import obEstructura

class obEncabezado():
	'''
	classdocs
	'''

	def __init__(self):
		'''
		Constructor
		'''
		self.campos={}
		

	def extraerCampo(self,clave):
		if self.campos.has_key(clave):
			return self.campos[clave]
		else:
			return None
		
		
		
		
	def convertir(self,nombreamb):
		es=obEstructura()
		es.AddTexto('Modo As Integer')
		es.AddTexto('SepCampo     As String * 1')
		es.AddTexto('SaltoPag     As Byte')# String * 1')
		es.AddTexto('UniMedida    As Integer')
		es.AddTexto('FormFrente   As Integer')
		es.AddTexto('Orientacion  As Byte')
		es.AddTexto('Segmento     As Byte')
		es.AddTexto('duplex       As Integer')
		es.AddTexto('Tamaño       As Integer')
		es.AddTexto('formAtras    As Integer')
		es.AddTexto('Transito     As Boolean')
		es.AddTexto('Copias       As Integer')
		es.AddTexto('Resolucion   As Integer')
		es.AddTexto('Compaginado  As Boolean')
		es.AddTexto('TipoBandeja  As Byte')
		es.AddTexto('OffsetPag    As Integer')
		es.AddTexto('OffsetDoc    As Integer')
		es.AddTexto('FormFijo     As Integer')
		es.AddTexto('UP           As Integer')
		es.AddTexto('Nrolineas    As Integer')
		es.AddTexto('BandSalida   As Integer')
		es.AddTexto('BandEntrada  As Integer')
		es.AddTexto('ActDetalle   As Boolean')
		es.AddTexto('DetDuplex    As Integer')
		es.AddTexto('DetBandEn    As Integer')
		es.AddTexto('DetFormat    As Integer')
		es.AddTexto('SalidaImagen As Integer')
		es.AddTexto('DetNomBandeja As Byte')
		es.AddTexto('Libre4       As String * 1')
		es.AddTexto('DetLinea1    As Integer')
		es.AddTexto('DetLinMax    As Integer')
		es.AddTexto('MargenGeneral As Integer')
		es.AddTexto('MargenGrapa  As Integer')
		es.AddTexto('UpModo       As Integer')
		es.AddTexto('SaltoLinea As String * 1')
		es.AddTexto('VerticalIndex As Single')
		es.AddTexto('OffsetLinea As Boolean')
		es.AddTexto('FontListado As Integer')
		es.AddTexto('FontTamaño As Single')
		es.AddTexto('RompACT As Boolean')
		es.AddTexto('RompTexto As String * 18')
		es.AddTexto('RompLinea As Integer')
		es.AddTexto('RompColumna As Integer')
		es.AddTexto('NumPag As Boolean')
		es.AddTexto('TextNro As String * 15')
		es.AddTexto('ZebraGris As Integer')
		es.AddTexto('ZebraBlanco As Integer')
		es.AddTexto('Marco As Integer')
		es.AddTexto('IntenZebra As Integer')
		es.AddTexto('LisInicioRayado As Integer')
		es.AddTexto('DelEspacio As Boolean')
		es.AddTexto('Version As String * 3')
		es.AddTexto('UpPosx As Long')
		es.AddTexto('UpPosY As Long')
		es.AddTexto('Totales As Boolean')
		es.AddTexto('AnchoControl As Integer')
		es.AddTexto('TraficoPosX As Long')
		es.AddTexto('TraficoPosY As Long')
		es.AddTexto('NumActivo           As Boolean')
		es.AddTexto('ClaveAncho          As Integer')
		es.AddTexto('ClaveAcceso         As String * 28')
		es.AddTexto('NombreFormFrente    As String * 40')
		es.AddTexto('NombreFormAtras     As String * 40')
		es.AddTexto('NombreFormDetalle   As String * 40')

		
		

		es.procesar()
		tipo=''
		largo=0
		print nombreamb
		arch=file(nombreamb,'rb')
		actBool=False
		
		for dato in es.campo:
			nombre = dato.keys()
			tipo= dato[nombre[0]][1]
			largo= dato[nombre[0]][0]
			leer=arch.read(largo)
			
			if tipo=='B': 
				tipo='h'
				actBool=True
			
			valor=struct.unpack(tipo,leer)
			valor=valor[0]
			if tipo[-1]=='s':	valor=valor.strip()	
			
			if actBool:
				actBool=False
				if valor==0	: valor=False
				else		: valor=True
			self.campos[nombre[0]]=valor


		#for lista in self.campos:
		#	print lista ,'=',self.campos[lista]
		
		