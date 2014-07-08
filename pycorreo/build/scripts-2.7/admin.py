# -*- coding: utf-8 -*-
import sys
import sqlite3

from PyQt4 import QtCore, QtGui
from manejocampos import Ui_MainWindow

class form_pal(QtGui.QWidget):
	def __init__(self, parent=None):
		#Formato
		super(form_pal, self).__init__(parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		#varibles
		self.baseconn=sqlite3.connect('correo.db')
		self.posreg=0
		self.indices=self.LeerIndices()
		self.ui.BtnAnterior.setEnabled(False)
		if len(self.indices)<1:
			self.ui.BtnProximo.setEnabled(False)
			self.ui.BtnModificar.setEnabled(False)
			self.ui.BtnBorrar.setEnabled(False)
		else :
			self.posreg=1
			self.BuscarItem()
			
		#Eventos
		QtCore.QObject.connect(self.ui.BtnProximo,QtCore.SIGNAL("clicked()"), self.Reg_Siguiente)
		QtCore.QObject.connect(self.ui.BtnPrincipio,QtCore.SIGNAL("clicked()"), self.Reg_Primero)
		QtCore.QObject.connect(self.ui.BtnFinal,QtCore.SIGNAL("clicked()"), self.Reg_Ultimo)
		QtCore.QObject.connect(self.ui.BtnAnterior,QtCore.SIGNAL("clicked()"), self.Reg_Anterior)
		QtCore.QObject.connect(self.ui.BtnAdicionar,QtCore.SIGNAL("clicked()"), self.Reg_Adicionar)
		QtCore.QObject.connect(self.ui.BtnBorrar,QtCore.SIGNAL("clicked()"), self.Reg_Borrar)
		QtCore.QObject.connect(self.ui.BtnModificar,QtCore.SIGNAL("clicked()"), self.Reg_Modificar)
		
			
#		QtCore.QMetaObject.connectSlotsByName(self)

#Movimiento de campos
	def Reg_Primero(self):
		self.posreg=1
		self.ui.BtnAnterior.setEnabled(False)
		#if self.cantreg > 1:
		if len(self.indices)>1:
			self.ui.BtnProximo.setEnabled(True)
		else:
			self.ui.BtnProximo.setEnabled(False)
		self.BuscarItem()

	def Reg_Ultimo(self):
		#self.posreg=self.cantreg
		self.posreg=len(self.indices)
		self.ui.BtnProximo.setEnabled(False)
		#if self.cantreg == 1:
		if len(self.indices)==1:
			self.ui.BtnAnterior.setEnabled(False)
		else:
			self.ui.BtnAnterior.setEnabled(True)
		self.BuscarItem()

	def Reg_Siguiente(self):
		print "siguiente"
		self.posreg+=1
		self.ui.BtnAnterior.setEnabled(True)
		#if self.posreg > self.cantreg:
		if self.posreg > len(self.indices):
			#self.posreg = self.cantreg
			self.posreg = len(self.indices)
			self.ui.BtnProximo.setEnabled(False)
		#elif self.posreg == self.cantreg:
		elif self.posreg == len(self.indices):
			self.BuscarItem()
			self.ui.BtnProximo.setEnabled(False)
		else:
			self.BuscarItem()
			
	def Reg_Anterior(self):
		print "Anterior"
		self.posreg-=1
		self.ui.BtnProximo.setEnabled(True)
		if self.posreg < 1:
			self.posreg = 1
			self.ui.BtnAnterior.setEnabled(False)
		elif self.posreg == 1:
			self.BuscarItem()
			self.ui.BtnAnterior.setEnabled(False)
		else:
			self.BuscarItem()

	def BuscarItem(self):
		if self.posreg==0:
			return
		cursor =self.baseconn.cursor()
		valor=str(self.indices[self.posreg-1])
		cursor.execute ('SELECT * FROM config WHERE idcod=' + valor )
		for campo in cursor:
			self.ui.LblRegistro.setText(QtGui.QApplication.translate("MainWindow", str(self.posreg) + "/" + str(len(self.indices))  , None, QtGui.QApplication.UnicodeUTF8))
			self.ui.TxtHost.setPlainText(QtGui.QApplication.translate("MainWindow", campo[4], None, QtGui.QApplication.UnicodeUTF8))
			self.ui.TxtUsuario.setPlainText(QtGui.QApplication.translate("MainWindow", campo[2], None, QtGui.QApplication.UnicodeUTF8))
			self.ui.TxtClave.setPlainText(QtGui.QApplication.translate("MainWindow", campo[3], None, QtGui.QApplication.UnicodeUTF8))
			self.ui.TxtEnviado.setPlainText(QtGui.QApplication.translate("MainWindow", campo[7], None, QtGui.QApplication.UnicodeUTF8))
			self.ui.TxtBandera.setPlainText(QtGui.QApplication.translate("MainWindow", campo[6], None, QtGui.QApplication.UnicodeUTF8))
			self.ui.TxtRuta.setPlainText(QtGui.QApplication.translate("MainWindow", campo[8], None, QtGui.QApplication.UnicodeUTF8))
			self.ui.TxtPuerto.setPlainText(QtGui.QApplication.translate("MainWindow", str(campo[0]), None, QtGui.QApplication.UnicodeUTF8))
			
			if campo[5]=="S" or campo[5]=="s":
				self.ui.CmbTls.setCurrentIndex(0)
		cursor.close()

	def LeerIndices(self):
		cursor =self.baseconn.cursor()
		cursor.execute ('SELECT idcod FROM config')
		datos=[]
		for fila in cursor:
			datos.append(fila[0])
		cursor.close()
		return datos
	
	def Reg_Adicionar(self):
		datos =[]
		datos.append (str(self.ui.TxtUsuario.toPlainText()))
		datos.append (str(self.ui.TxtClave.toPlainText()))
		datos.append (str(self.ui.TxtHost.toPlainText()))
		datos.append (int(self.ui.TxtPuerto.toPlainText()))
		datos.append (str(self.ui.TxtEnviado.toPlainText()))
		datos.append (str(self.ui.TxtBandera.toPlainText()))
		datos.append (str(self.ui.TxtRuta.toPlainText()))
		if  self.ui.CmbTls.currentIndex() ==0:
			datos.append ('S')
		else:
			datos.append ('N')
		cursor =self.baseconn.cursor()
		cursor.execute ('INSERT INTO config (usuario,clave,servidor,puerto,enviado,bandera,rutafinal,tls) VALUES (?,?,?,?,?,?,?,?)' ,datos)
		self.baseconn.commit()
		self.indices=self.LeerIndices()
		self.Reg_Ultimo()
		cursor.close()
		
	def Reg_Borrar(self):
		answer = QtGui.QMessageBox.warning(self, self.tr("Borrar"),
                    self.tr("El registro sera borrado definitivamente,\n Esta Seguro de hacerlo"),
                    QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
		if answer == QtGui.QMessageBox.No:
			return

		idcod=str(self.indices[self.posreg-1])
		print self.indices
		print self.posreg
		print idcod
		cursor =self.baseconn.cursor()
		cursor.execute ('DELETE FROM config  WHERE idcod =?' ,idcod)
		self.baseconn.commit()
		self.indices=self.LeerIndices()
		
		self.Reg_Ultimo()
		cursor.close()
		
	def Reg_Modificar(self):
		#print "modificar"
		
		answer = QtGui.QMessageBox.warning(self, self.tr("Modificacion"),
                    self.tr("Se guardaran los cambios realizados a este registro,\n Esta Seguro de hacerlo"),
                    QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
		if answer == QtGui.QMessageBox.No:
			return


		print answer
		datos =[]
		datos.append (str(self.ui.TxtUsuario.toPlainText()))
		datos.append (str(self.ui.TxtClave.toPlainText()))
		datos.append (str(self.ui.TxtHost.toPlainText()))
		datos.append (int(self.ui.TxtPuerto.toPlainText()))
		datos.append (str(self.ui.TxtEnviado.toPlainText()))
		datos.append (str(self.ui.TxtBandera.toPlainText()))
		datos.append (str(self.ui.TxtRuta.toPlainText()))
		if  self.ui.CmbTls.currentIndex() ==0:
			datos.append ('S')
		else:
			datos.append ('N')
		datos.append (str(self.indices[self.posreg-1]))
		print datos
		cursor =self.baseconn.cursor()
		cursor.execute ('UPDATE config SET usuario=?,clave=?,servidor=?,puerto=?,enviado=?,bandera=?,rutafinal=?,tls=? WHERE idcod=?' ,datos)
		self.baseconn.commit()
		self.indices=self.LeerIndices()
		self.Reg_Ultimo()
		cursor.close()


if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	myapp = form_pal()
	myapp.show()
	sys.exit(app.exec_())



