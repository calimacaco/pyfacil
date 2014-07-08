# -*- coding: iso-8859-1 -*-
import smtplib
import os
from email.Utils import COMMASPACE, formatdate

from email import Encoders

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText 
from email.MIMEBase import MIMEBase

from email.Header import Header

 
class Envio_Correo ():
	def __init__(self):
		self.error=""
		self.smtp_server = None




	def VerificarAjuntos(self,adjuntos):
		print "Envio_Correo->VerificarAjuntos"
		print adjuntos
		
		
		if type (adjuntos)==str or type(adjuntos)==unicode:
			adjuntos=adjuntos.strip()
			if len(adjuntos)<1:
				return None
			else:
				return adjuntos.split(',')

		elif type(adjuntos)==list:
			return adjuntos
		
		else:
			return None
			
			
	# Carbon Copy) fields and the ability to add attachments. 
	def send_email(self, subject="", text="", texthtml="", send_from="", dest_to=None, attachments=None,send_cc=None, send_bcc=None, 
		server="localhost", port=25,user="", passwd="",tls=0):
		"""Send a email with(out) attachment(s) enabling CC and BCC fields.
		Arguments:
			(str) subject -- the mail's subject
			(str) text -- the message's text
			(str) send_from -- a sender's email address (default "")
			(list) dest_to -- a list of receivers' email addresses ("")
			(list) attachments -- a list of attachments files (default None)
			(list) send_cc -- a list of carbon copy's email addresses (def. None)
			(list) send_bcc -- a list of blind carbon copy's email addresses (None)
			(str) server -- the smtp server (default "localhost")
			(int) port -- the smtp server port (default 25)
			(str) user -- the smtp server user (default "")
			(str) passwd --the smtp server password (default "")
		If "send_from" or "dest_to" are empty or None, then script user's mailbox 
		is assumed instead. Useful for logging scripts
		"""
		#print type( dest_to)
	
		unicodigo = 'latin-1'
	
		if type( dest_to)==str or type(dest_to)==unicode:	dest_to=dest_to.split(',')
		if type (send_cc)==str or type(send_cc)==unicode:	send_cc=send_cc.split(',')
		if type (send_bcc)==str or type(send_bcc)==unicode:	send_bcc=send_bcc.split(',')
	
	
		lst_enviar=[]
	
		
		print "destino:"
		dest_to_addrs=[]
		for dest in dest_to:
			dest_to_addrs.append (dest.strip()) # receivers mails including to, cc and bcc fields
		
		
		lst_enviar.append(dest_to_addrs)
		
		
		
		attachments=self.VerificarAjuntos(attachments)
		print "************************"
		print attachments
		print "************************"
		
		
		if attachments !=None:
			for archivo in attachments:
				if not os.path.isfile(archivo):
					self.error="Archivo Ajunto No existe [%s]"%(archivo)
					return -1
	
		
				
				
		message = MIMEMultipart('alternative')
		###subject=unicode(subject,'latin-1')
		##print "tipo %s" % (type(subject))
		message["Subject"] = Header(subject,'latin-1')
		message["From"] = send_from
		message["To"] = COMMASPACE.join(dest_to)
		if send_cc:# or send_bcc:
			message["Cc"] = COMMASPACE.join(send_cc)
			dest_to_addrs += send_cc
			
		if send_bcc:
			dest_to_addrs += send_bcc
		
		
		
		
				
		message["Date"] = formatdate(localtime=True)
		message.preamble = "You'll not see this in a MIME-aware mail reader.\n"

		#msgAlternative = MIMEMultipart('alternative')
		#message.attach(msgAlternative)
		
			#msgAlternative.attach(MIMEText(texthtml, 'html'))
		# For all type of attachments
		
		if attachments!=None:
			for att_file in attachments:
				print "for ",att_file 
				with open(att_file, "rb") as attmnt:
					att = MIMEBase("application", "octet-stream")
					att.set_payload(attmnt.read())
				Encoders.encode_base64(att)
				att.add_header("content-disposition", "attachment",
							   filename=os.path.basename(att_file))
				message.attach(att)
		# initialize the mail server




		if text !=None:
			message.attach(MIMEText(text))
		if texthtml!=None:
			message.attach(MIMEText(texthtml, 'html'))
			


	
		print "Abrir Servidor"
		smtp_server = smtplib.SMTP()
		# Connect to mail server
		try:
			print "concecta Servidor:" + server + ":"+str(port) 
			smtp_server.connect(server, port)
		
		except smtplib.SMTPConnectError:
			print ("Error occurred during establishment of a connection with the server.")
			self.error="Mail Error connection with the server."
			return 1
		except:
			print("mail error", "Error en conexion?")
			self.error="mail Error  en conexion"
			return 2    
		# EHLO	
		try:
			print "ehlo"
			smtp_server.ehlo()
		except smtplib.SMTPHeloError:
			print ("The server refused our HELO message.")
			self.error="mail error The server refused our HELO message."
			return 3				
		except:
			print("mail error", "Error en ehlo?")
			self.error="mail error Error en ehlo"
			return 4
		#TLS
		try:
			#print "tls:"+tls
			if int(tls)==1:
				print "tls: Activado.."
				smtp_server.starttls()
				smtp_server.ehlo	
		except smtplib.SMTPException:
			print("mail error", "No suitable authentication method")
			self.error="mail error No suitable authentication method"
			return 5
		except:
			print("mail error", "tls error")
			self.error="mail error Error en tls"
			return 6
		
		try:
			if len(user.strip())>0:
				print "Login"
				smtp_server.login(user, passwd)
			# Send mail
		except:
			print "Error usuario [%s] o clave [%s] erronea" % (user,passwd)
			return 7
		
		try:
			print "De:"+send_from
		
		
			smtp_server.sendmail(send_from, dest_to_addrs, message.as_string())
			
			#smtp_server.sendmail(send_from, lst_enviar, message.as_string())
			# Disconnect from server
			smtp_server.quit()
			print "enviado"
			
			
			
		except smtplib.SMTPAuthenticationError:
			print("mail error", "Authentication error")
			self.error="mail error Authentication. Usuario:["+user+"]"
			return 7			
		except smtplib.SMTPRecipientsRefused:
			print("mail error:", "Usuarios desconocido.","Nobody got the mail.")
			self.error="mail error Usuarios desconocido."
			return 8
		except smtplib.SMTPSenderRefused:
			print("mail error", "The server didn't accept the from_addr")
			self.error="mail error The server didn't accept the from_addr"
			return 9 
		except smtplib.SMTPDataError:
			print("mail error", "An unexpected error code, Data refused")
			self.error="mail error The SMTP server refused to accept the message data."
			return 10
		except smtplib.SMTPResponseException:
			print("mail error", "SMTPResponseException")
			self.error="mail error SMTPResponseException"
			return 11	
		except smtplib.SMTPException:
			print("mail error", "Base exception class for all exceptions raised by this module.")
			self.error="mail error smtp module."
			return 12
		except:
			print("mail error", "Desconcido")
			self.error="mail error Desconcido"
			return 13
		#Todo fue ok
		return 0


	def pruebaConectar(self,server,port=25, tls=False,user='',clave='',send_from=''):
		print "Prueba de Correo."
		print "server [%s]\nPuerto[%i]\nTls[%s]\nuser[%s]\nClave[%s]\nenviado[%s]" %(server,port, tls,user,clave,send_from)
		dest_to="soportesimplesoft@gmail.com"
		status = "Abrir Servidor\n"
		self.smtp_server = smtplib.SMTP()
		# Connect to mail server
		try:
			status += "concecta Servidor-> %s:%i\n" % (server,port) 
			self.smtp_server.connect(server, port)
		
		except smtplib.SMTPConnectError:
			status += 'Error occurred during establishment of a connection with the server.\n'
			return status
			
		except:
			status +='mail error", "Error en conexion?\n'
			return status
		try:
			status += 'ehlo\n'
			self.smtp_server.ehlo()
		except smtplib.SMTPHeloError:
			status +"The server refused our HELO message.\n"
			return status			
		except:
			status +="mail error", "Error en ehlo?\n"
			return status
		#TLS
		try:
			if tls:
				self.smtp_server.starttls()
				self.smtp_server.ehlo	
		except smtplib.SMTPException:
			status +="mail error", "No suitable authentication method\n"	
			return status
		except:
			status +="mail error", "tls error\n"
			return status

		try:
			status += "Login\n Usuario:[%s]  Clave:[%s]\n" % (user, clave)
			if len(user.strip())>0:
				self.smtp_server.login(user, clave)
		except:
			status +="Error, Usuario o Clave errada"
			return status
		try:
			status +="De: %s \nPara: %s" %(send_from,dest_to)
			message = MIMEMultipart()
			message["Subject"] = "Prueba de Coneccion"
			message["From"] = send_from
			message["To"] = COMMASPACE.join(dest_to)
			message["Date"] = formatdate(localtime=True)
			message.preamble = "You'll not see this in a MIME-aware mail reader.\n"
			message.attach(MIMEText("Texto Normal"))
			message.attach(MIMEText("<b>Texto,/b> con Html", 'html'))
			self.smtp_server.sendmail(send_from, [dest_to], message.as_string())
			self.smtp_server.quit()
			status+="******\nPrueba realizada con exito."
			return status

		except smtplib.SMTPAuthenticationError:
			status+="mail error Authentication. Usuario:["+user+"]"
			return status			
		except smtplib.SMTPRecipientsRefused:
			status+="mail error:Usuarios desconocido.","Nobody got the mail."
			return status
		
		except smtplib.SMTPSenderRefused:
			status +="mail error:The server didnot accept the from_addr"
			return status
		except smtplib.SMTPDataError:
			status +="mail error The SMTP server refused to accept the message data."
			return status
		except smtplib.SMTPResponseException:
			print("mail error", "SMTPResponseException")
			status +="mail error SMTPResponseException"
			return status	
		except smtplib.SMTPException:
			print("mail error", "Base exception class for all exceptions raised by this module.")
			status +="mail error Base exception class for all exceptions raised by this module.."
			return status
		except:
			print("mail error", "Desconcido")
			status +="mail error Desconcido"
			return status
		#Todo fue ok
		print "ok"
		return status + '\nOK'
		



if __name__ == "__main__":
	print "inicio"
	#prueba
    #send_email("estoy probando", "cuerpo del texto", 
			#"soportesimplesoft@gmail.com",
			#["calimacaco@hotmail.com","calimacaco@yahoo.com"],
			#["/home/marco/Imágenes/visual-illusion09.jpg"],
			#["calimacaco@gmail.com"], 
			#["calimacaco@hotmail.com"],
			#"smtp.gmail.com",587,"soportesimplesoft@gmail.com", "ComoVos2011")
