#!c:\python27\python.exe
# Echo server program
import socket
import sys

HOST = "localhost"               # Symbolic name meaning all available interfaces
PORT = 14000  #40001              # Arbitrary non-privileged port
s = None
for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC,socket.SOCK_STREAM, 0, socket.AI_PASSIVE):
	af, socktype, proto, canonname, sa = res
	try:
		s = socket.socket(af, socktype, proto)
	except socket.error, msg:
		s = None
		continue
	try:
		s.bind(sa)
		s.listen(1)
	except socket.error, msg:
		s.close()
		s = None
		continue
	break
if s is None:
	print 'No puede abrir socket'
	sys.exit(1)

print "Abriendo puerto...."
contador =0

while 1:
	conn, addr = s.accept()
	f = open('formatos.pcl'+str(contador), 'w')
	print 'Archivo       :formatos.pcl%s'%(contador)
	print 'Conectador por:', addr
	#f = open('/mnt/simplesoft/2s/virtual/Clientes/Medellin/daimler/Modelos/Repositorio/formatos.prn', 'w')

	print "Recibe impresion.------------------------------>>>"
	while 1:
		data = conn.recv(1024)
		f.write(data)
		if not data: break
		#conn.send(data)
	print "--------------------------------<<<< Fin Impresion"
	f.close()
	contador=contador+1
	conn.close()

