#Bluetooth
#Importante: es necesario emparejar el dispositivo antes de cualquier conexion
#Modulo bluetooth para Python: pyBluez

import bluetooth

def conectarBT(dr):
    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    print dr
    sock.connect((dr,1))
    return sock

def leerComando():
    print 'Sintaxis: <C>'
    print 'Ejemplos: \nR012\nG055\nB255'
    c = raw_input('Ingrese comando:     ')
    return c

#Buscaremos conectarnos con mi dispositivo Bluetooth
miBT = 'IvanBT'
print 'Buscando dispositivos Bluetooth...'
dispositivosCercanos = bluetooth.discover_devices()

for btAddr in dispositivosCercanos:
    if miBT == bluetooth.lookup_name(btAddr):
        miAddr = btAddr
        break

if miAddr is not None:
    print 'Conectando a '+miBT+'...'
    bt = conectarBT(miAddr)
    print 'Conectado!\n\n'
    try:
        while True:
            bt.send(leerComando())
    except KeyboardInterrupt:
        bt.close()
        print 'Adios!'
else:
    print 'Dispositivo no encontrado :('
