#Manejo de excepciones

import serial, time


global uart #Objeto para acceder al puerto serial

def abrirSerial(baud = 115200):
    global uart
    MAX_UART_RANGE = 60
    i = 1
    while i <= MAX_UART_RANGE:
        time.sleep(0.1)
        try:
            print 'Intentando conectar en COM'+str(i)+'...'
            uart = serial.Serial(str('COM'+str(i)),baud)
            
        except serial.SerialException:
            i += 1
        else:
            print 'Conectado a COM'+str(i)+'!'
            i = MAX_UART_RANGE+1
    uart.close()

def abrirArchivo(fName = 'MiTexto.txt'):
    try:
        archivo = open(fName,'r')
    except IOError:
        print 'Error: El archivo no existe!'
    else:
        data = []
        for line in archivo:
            data.append(line)
        return data


def division(n1, n2):
    try:
        return float(n1)/n2
    except ZeroDivisionError:
        print 'Error: El divisor no puede ser 0'
    except ValueError:
        print 'Error: Ambos caracteres deben ser numericos'
    except:
        print 'Error desconocido'
