import random

#Mas sobre ciclos while
#Numero magico

def generaAleatorio(rango):
    x = random.randrange(rango[0], rango[1], 1)
    #print x #Imprimir el numero secreto: SOLO PARA DEPURACION
    return x

def verifica(x, n):
    """
    x: Ingresado por el usuario
    n : Generado aleatoriamente al inicio del juego
    """
    if(n < x):
        print 'El numero secreto es menor a',str(x)
        return 0
    elif(n > x):
        print 'El numero secreto es mayor a',str(x)
        return 0
    else:
        print '\n\nAcertaste!'
        return 1

def leeNumero(data):
    if data.isdigit():
        return int(data)
    else:
        print "Error"
        return 0

def jugar(rango = [0, 20]):
    n = generaAleatorio(rango)
    cnt = 1 #Conteo de intentos
    ok = 0 #Bandera para verificar si se acerto o no
    while(not ok):
        print '\nIntento:',str(cnt)
        print 'Ingrese un numero entre',str(rango[0]),'y',str(rango[1]),':',
        x = leeNumero(raw_input())
        ok = verifica(x, n)
        cnt += 1
    print 'Utilizaste',str(cnt-1),'intentos para encontrar al secreto:' ,str(n)
        

jugar()        
