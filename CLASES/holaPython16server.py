import socket

TCP_IP = '192.168.43.170'
TCP_PORT = 5005
BUFFER_SIZE = 20

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Abrir socket
s.bind((TCP_IP, TCP_PORT)) #Levantar el servidor
s.listen(1) #Esperar 1 conexion. Accion bloqueadora

print 'Esperando conexion...\n\n'

conn, addr = s.accept() #Aceptar la conexion solicitada

print 'Conectado con: ', addr

try:
	while 1:
		data = conn.recv(BUFFER_SIZE) #Recibir datos a traves del socket
		print "Recibido: ", data
except KeyboardInterrupt:
	conn.close()
