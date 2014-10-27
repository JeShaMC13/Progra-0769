import thread
import time

global data

def contar(limite, delay):
    global data
    for i in range(limite):
        print str(i)
        time.sleep(delay)
        if data == 'Silva':
            thread.exit()

def recibeTCP(ip='127.0.0.1', port=666):
    import socket
    global data
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp.bind((ip,port))
    tcp.listen(1)

    print 'Esperando conexion...\n'
    
    conn, addr = tcp.accept()
    try:
        while True:
            data = conn.recv(100)
            print data
    except KeyboardInterrupt:
        conn.close()
        tcp.close()
        print 'Adios!'

data = None
thread.start_new_thread(contar, (500,0.5))
recibeTCP()

