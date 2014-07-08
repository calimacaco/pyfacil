'''
Created on 12/04/2013

@author: marco
'''
import wx
from FormMapic import F_GenerarPDF


class Pdf2Pcl():
	'''
	classdocs
	'''


	def __init__(self,padre):
		'''
		Constructor
		'''
		GenPcl=F_GenerarPDF(padre)
		self.f_GenPcl.SetTitle("Generador PCL")
		self.f_GenPcl.Center()
		self.f_GenPcl.Show()
		#self.f_GenPcl.Btn_GenerarPCL.Bind(wx.EVT_BUTTON,self.OnProcesarPDF)
		#self.f_GenPcl.Btn_BorrarResultado.Bind(wx.EVT_BUTTON,self.OnBorrarResultado)
		#self.f_GenPcl.Btn_Resultado.Bind(wx.EVT_BUTTON,self.OnMuestraResultado)
		