# -*- coding: utf-8 -*-
import smtplib
import os
from email.Utils import COMMASPACE, formatdate
from email import Encoders

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText 
from email.MIMEBase import MIMEBase
 
class Envio_Correo ():
	def __init__(self):
		self.error=""
	  
	# Carbon Copy) fields and the ability to add attachments. 
	def send_email(self, subject="", text="", texthtml="", send_from="", dest_to=None, attachments=None,send_cc=None, send_bcc=None, 
		server="localhost", port=25,user="", passwd="",tls="N"):
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
		
		print "Atta:", attachments
		
		for archivo in attachments:
			if not os.path.isfile(archivo):
				self.error="Archivo Ajunto No existe: [",archivo,"]"
				return 
		print "no debe llegar"
		print "*****************"		
		dest_to_addrs = dest_to # receivers mails including to, cc and bcc fields
		message = MIMEMultipart()
		message["Subject"] = subject
		message["From"] = send_from
		message["To"] = COMMASPACE.join(dest_to)
		if send_cc:
			message["Cc"] = COMMASPACE.join(send_cc)
			dest_to_addrs += send_cc
		if send_bcc:
			dest_to_addrs += COMMASPACE.join(send_bcc)
		message["Date"] = formatdate(localtime=True)
		message.preamble = "You'll not see this in a MIME-aware mail reader.\n"
		message.attach(MIMEText(text))
		message.attach(MIMEText(texthtml, 'html'))




		# For all type of attachments
		print attachments
		if attachments:
			for att_file in attachments:
				with open(att_file, "rb") as attmnt:
					att = MIMEBase("application", "octet-stream")
					att.set_payload(attmnt.read())
				Encoders.encode_base64(att)
				att.add_header("content-disposition", "attachment",
							   filename=os.path.basename(att_file))
				message.attach(att)

		# initialize the mail server
		smtp_server = smtplib.SMTP()
		# Connect to mail server
		
		try:
			smtp_server.connect(server, port)
		except:
			print("mail error", "Wrong server, are you sure is correct?")
			self.error="mail error: Wrong server, are you sure is correct?"
			return -1
		#except socket.gaierror:
			#print("mail error", "Wrong server, are you sure is correct?")
			#self.error="mail error: Wrong server, are you sure is correct?"
		#except socket.error:
			#print("mail error", "Server unavailable or connection refused")
			#self.error="mail error: Server unavailable or connection refused"
			
			
			
			
		# Login in mail server	
		smtp_server.ehlo()
		print "************"
		print "tls:"+tls.upper()
		if tls.upper()=="S":
			smtp_server.starttls()
			smtp_server.ehlo	
		try:
			smtp_server.login(user, passwd)
		except smtplib.SMTPAuthenticationError:
			print("mail error", "Authentication error")
			self.error="mail error:mail error Authentication error. Usuario:["+user+"]"
			return -1
		except smtplib.SMTPException:
			print("mail error", "No suitable authentication method")
			self.error="mail error: No suitable authentication method"
			return -1
	# Send mail
		try:
			smtp_server.sendmail(send_from, dest_to_addrs, message.as_string())
		except smtplib.SMTPRecipientsRefused:
			print("mail error", "All recipients were refused.","Nobody got the mail.")
			self.error="mail error: All recipients were refused. Nobody got the mail."
			return -1
		except smtplib.SMTPSenderRefused:
			print("mail error", "The server didn’t accept the from_addr")
			self.error="mail error: The server didn’t accept the from_addr"
			return -1
		except smtplib.SMTPDataError:
			print("mail error", "An unexpected error code, Data refused")
			self.error="mail error: An unexpected error code, Data refused"
			return -1
		# Disconnect from server
		smtp_server.quit()
    

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
