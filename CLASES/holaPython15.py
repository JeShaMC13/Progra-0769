#Puerto serial
#Antes de explicar el codigo, conceptos de puerto serial y UART

import serial #pySerial debe estar instalado para utilizar este modulo
import time

class temperaturaSerial(object):
    def __init__(self, puerto, baudrate, grafica=False, tOut = 1):
        self.uart = serial.Serial(puerto,baudrate,timeout = tOut)
        self.uart.flushInput()
        self.uart.flushOutput()
        self.grafica = grafica
        self.configuraTemp()
        self.leerTemperaturas()

    def configuraTemp(self):
        """
        Configuracion inicial de parametros de lectura de temperatura
        """
        self.muestras = int(raw_input('Cuantas muestras desea tomar?              --> '))
        self.periodo  = float(raw_input('Cada cuanto (segundos) quiere tomar las muestras? --> '))
        self.data = []

    def leerMuestra(self, index):
        """
        Lee una muestra individual de temperatura
        """
        print 'Leyendo muestra #'+str(index+1)
        self.uart.write('a') #Notificar al microcontrolador para que envie temp. actual
        self.data.append(float(self.uart.readline())) #Leer temperatura del microcontrolador

    def closeUART(self):
        """
        Cierra la conexion activa del puerto serial
        """
        self.uart.close()

    def leerTemperaturas(self):
        """
        Lee todas las muestras requeridas por el usuario
        """
        for i in range(self.muestras):
            self.leerMuestra(i)
            time.sleep(self.periodo)
        self.uart.write('b') #Notificar al microcontrolador que ha finalizado el muestreo
        self.closeUART() #SIEMPRE se debe cerrar el puerto serial al salir

    def plotData(self):
        """
        Crea una grafica de las temperaturas en funcion del tiempo.
        Esta funcion no es necesario entenderala aun.
        """
        import pylab
        x = range(len(self.data))
        a = pylab.plot(x,self.data)
        #pylab.show()
        pylab.savefig('miGrafica.png')

    def getTemp(self):
        """
        Devuelve todas las temperaturas registradas
        """
        if self.grafica:
            self.plotData()
        return self.data

    def __str__(self):
        return """Lee la temperatura proveniente de un Launchpad \n\
                  conectado a traves de un puerto serial emulado.\n\
                  Si el atributo 'grafica' es "True", se genera una\n\
                  grafica temporal de las temperaturas leidas"""
        

PORT = 'COM54'
BAUD = 115200

temperaturas = temperaturaSerial(PORT,BAUD,True)
try:
    print temperaturas.getTemp()
except:
    temperaturas.closeUART()
