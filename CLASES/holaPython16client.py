import socket

TCP_IP = '192.168.10.16'
TCP_PORT = 5005

BUFFER_SIZE = 20
msg = 'Hola Mundo!'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
cnt = 1
try:
	while True:
	    s.send(raw_input('Ingrese texto a enviar: ')) #Enviar el mensaje
	    print str(cnt)
	    cnt += 1
except KeyboardInterrupt:
	s.close()
