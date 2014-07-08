#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

import os, sys
import win32print

class Impresora:
	def __init__(self):
		self.nombreimpresora="Formatos"
	####
	"""Determina el nombre de la impresora"""
	def Nombre(self,nomimpr):
		self.nombreimpresora=nomimpr
	####
	"""Envio de la impresion"""
	def Imprimir(self,datos):
		hPrinter = win32print.OpenPrinter (self.nombreimpresora)
		try:
			hJob = win32print.StartDocPrinter (hPrinter, 1, ("Simplesoft-Envio Archivo", None, "RAW"))
			try:
				win32print.StartPagePrinter (hPrinter)
				win32print.WritePrinter (hPrinter, datos)
				win32print.EndPagePrinter (hPrinter)
			finally:
				win32print.EndDocPrinter (hPrinter)
		finally:
			win32print.ClosePrinter (hPrinter)
######

if __name__=="__main__":
	prueba=Impresora()
	prueba.Nombre ("Formatos")
	prueba.Imprimir("Prueba de objeto Simplesoft\n")
	
