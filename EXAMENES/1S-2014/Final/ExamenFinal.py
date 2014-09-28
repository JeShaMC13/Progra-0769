'''
Examen final - Intro a la Progra 0769
Facultad de Ingenieria
Universidad de San Carlos de Guatemala

1er Semestre 2014 - Seccion "N"
Ing. Ivan Rene Morales
'''

import socket, time

global IP #SOLO PARA DEPURACION
global PUERTO #SOLO PARA DEPURACION

IP = '127.0.0.1' #SOLO PARA DEPURACION
PUERTO = 5829 #SOLO PARA DEPURACION

class juego(object):
    def __init__(self, IP, PUERTO, servidor=True, SIZE_X = 12, SIZE_Y = 12, MAX_BARCOS = 3, MAX_ESPACIOS = 10):
        self.SIZE_X = SIZE_X
        self.SIZE_Y = SIZE_Y
        self.IP = IP
        self.PUERTO = PUERTO
        self.servidor = servidor #Esta computadora sera el servidor, o sera cliente?
        self.MAX_BARCOS = 4 #Maxima cantidad de barcos a importar
        self.MAX_ESPACIOS = MAX_ESPACIOS #Cantidad maxima de espcios a ocupar por todos los barcos
        self.BUFFER_SIZE = 4096
        self.DUMMY_CHAR  = '*' #Solo para DEPURACION
        self.barcos = {} #Diccionario de barcos a importar desde el archivo de texto
        self.iniciar()

    def iniciar(self):
        if self.servidor:
            self.iniciarServidorLAN()
            self.jugarServidor()
        else:
            self.buscarServidorLAN()
            self.jugarCliente()
        

    def iniciarServidorLAN(self):
        self.tcp = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.tcp.bind((self.IP, self.PUERTO))
        print 'Esperando conexion de jugador remoto...'
        self.tcp.listen(2)
        self.tcp.setblocking(1)
        self.tcpConn, self.tcpAddr = self.tcp.accept()
        print '\n\nConexion satisfactoria con',str(self.tcpAddr)


    def buscarServidorLAN(self):
        self.tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp.connect((self.IP, self.PUERTO))
        self.tcp.setblocking(1)
        print '\n\nConexion satisfactoria con el servidor en',str((self.IP, self.PUERTO))

    def closeLAN(self):
        self.tcp.close()

    def leerNumero(self,rqst,limits=(0,1000)):
        ok = False
        while not ok:
            a = raw_input(rqst)
            if a.isdigit():
                if int(a) in range(limits[0],limits[1]+1):
                    ok = True
        return int(a)

    def pedirObjetivo(self):
        print 'Nuevo blanco: '
        X_MAX = self.SIZE_X - 2
        Y_MAX = self.SIZE_Y - 2
        x = self.leerNumero('x (1-'+str(X_MAX)+')  -> ',(1,X_MAX))
        y = self.leerNumero('y (1-'+str(Y_MAX)+')  -> ',(1,Y_MAX))
        return x,y

    def formatOut(self, data):
        return data

    def formatIn(self, data):
        return data
        
    def reimprimirMapas(self):
        self.mapa1.verificaHundimiento()
        self.mapa1.popularMapa()
        self.mapa1.imprimirMapa()
        self.mapa1.imprimirDescripcionBarcos()
        
        self.mapa2.popularMapa()
        self.mapa2.imprimirMapa(False)

    def agregaObjetosRemotos(self,data): #Agrega objetos provenientes del jugador remoto.
        #print data #Solo para DEPURACION
        data = data.strip('(')
        data = data.strip(')')
        data = data.split(',')
        x = int(data[0])
        y = int(data[1])
        self.mapa1.agregarObjetos([objeto(1,1,x,y)]) #Agrega en el MAPA1 el disparo que fue enviado por el jugador remoto
        if len(data)>2: #Si trae informacion del ultimo disparo que se envio localmente y el jugador remoto responde
            acertoAlla = int(data[2]) #Indica si el disparo que enviamos de ultimo acerto o no algun objetivo remoto
            i,j = self.lastSentShot
            self.mapa2.agregarObjetos([objeto(acertoAlla,1,i,j)])
        return x,y
        

    def imprimirMsjEspera(self):
        print '\n\nDebe esperar el movimiento del otro jugador...\n'

    def imprimirMsjGanar(self):
        print '\n\nGanaste!\n\n'

    def imprimirMsjPerder(self):
        print '\n\nPerdiste :(\n\n'

    def jugarServidor(self): #Server funciona bien MAPA2
        ganador = False
        self.inicializarTablero()
        self.imprimirMsjEspera()
        rxData = self.serverRx()
        self.lastRecvShot = self.agregaObjetosRemotos(rxData) #Ultima posicion del disparo recibido y agregar a mapa2 disparo enviado localmente en turno anterior
        self.reimprimirMapas()
        
        while not self.verificaPerdedor() and not ganador:
            acertoAqui = self.acertoDisparo(self.lastRecvShot)
            self.lastSentShot = self.pedirObjetivo()
            outData = str(self.lastSentShot[0])+','+str(self.lastSentShot[1])+','+str(acertoAqui)
            self.serverTx(outData)

            if self.verificaPerdedor():
                break

            self.imprimirMsjEspera()
            rxData = self.serverRx()
            tmp = rxData.split(',')
            if int(tmp[0])==0 and int(tmp[0])==0:
                ganador = True
                break
            #self.lastSentShot = self.agregaObjetosRemotos(rxData)
            self.lastRecvShot = self.agregaObjetosRemotos(rxData)
            self.reimprimirMapas()

        if ganador:
            self.imprimirMsjGanar()
        else:
            self.imprimirMsjPerder()
            self.serverTx('0,0') #Indica al servidor que el cliente perdio el juego

    def jugarCliente(self):
        ganador = False
        self.inicializarTablero()
        #self.clientTx(self.DUMMY_CHAR) #Solo para DEPURACION
        self.lastSentShot = self.pedirObjetivo()
        outData = str(self.lastSentShot[0])+','+str(self.lastSentShot[1])
        self.clientTx(outData)
        while not self.verificaPerdedor() and not ganador:
            self.imprimirMsjEspera()
            rxData = self.clientRx()
            tmp = rxData.split(',')
            if int(tmp[0])==0 and int(tmp[0])==0:
                ganador = True
                break
            self.lastRecvShot = self.agregaObjetosRemotos(rxData)
            self.reimprimirMapas()

            if self.verificaPerdedor():
                break

            acertoAqui = self.acertoDisparo(self.lastRecvShot)
            self.lastSentShot = self.pedirObjetivo()
            outData = str(self.lastSentShot[0])+','+str(self.lastSentShot[1])+','+str(acertoAqui)
            self.clientTx(outData)

        if ganador:
            self.imprimirMsjGanar()
        else:
            self.imprimirMsjPerder()
            self.clientTx('0,0') #Indica al servidor que el cliente perdio el juego

        

            
            
    def acertoDisparo(self,pos):
        for i in self.mapa1.ocupados:
            if i == pos:
                return 1 #Este caracter indica 'Disparo acertado'
        return 2 #Este es el indice del caracter que indica 'Disparo fallido'
                  

    def clientTx(self, data):
        a = self.tcp.sendall(data)

    def clientRx2(self, bufferSize = 1024):
        a = self.tcp.recv(bufferSize)
        while not len(a):
            a = self.tcp.recv(bufferSize)
        return a

    def clientRx(self, bufferSize = 1024):
        a = self.tcp.recv(bufferSize)
        return a

    def serverTx(self, data):
        a = self.tcpConn.sendall(data)

    def serverRx2(self, bufferSize = 4096):
        a = self.tcpConn.recv(bufferSize)
        while not len(a):
            a = self.tcpConn.recv(bufferSize)
            #time.sleep(0.1)
        return a

    def serverRx(self, bufferSize = 4096):
        a = self.tcpConn.recv(bufferSize)
        return a
        

    def inicializarTablero(self):
        self.instanciarMapas()
        self.leeArchivoBarcos()
        self.listaBarcos()
        self.mapa1.crearMapa()
        self.mapa1.popularMapa()
        self.mapa1.imprimirMapa()
        self.mapa1.imprimirDescripcionBarcos()

        self.mapa2.crearMapa()
        self.mapa2.popularMapa()
        self.mapa2.imprimirMapa(False)
  
        
    
    def instanciarMapas(self):
        self.mapa1 = mapa(self.SIZE_X, self.SIZE_Y)
        self.mapa2 = mapa(self.SIZE_X, self.SIZE_Y)

    def leeArchivoBarcosDeprecated(self,archivo = 'ExamenFinal.txt'): #Este metodo ya no se usa
        """
        Devuelve diccionario con {'Nombre de Barco':Tamanio,}
        """
        try:
            archivo = open(archivo,'r')
        except IOError:
            print 'Error al leer el archivo de base de datos de barcos :('
            return None
        data = []
        self.barcos = {} #Diccionario con barcos
        for linea in archivo:
            data.append(linea)
        for barco in data:
            self.barcos[barco.split(',')[0]] = int(barco.split(',')[1])

    def leeArchivoBarcos(self, archivo = 'ExamenFinal.txt'):
        """
        Devuelve diccionario con formato {(posX,posY):tamanio}
        """
        try:
            archivo = open(archivo,'r')
        except IOError:
            print 'Error al leer el archivo de base de datos de barcos :('
            return None
        data = []
        self.barcos = {}
        for linea in archivo:
            data.append(linea)
        for barco in data:
            tmp = barco.split(',')
            x = int(tmp[0])
            y = int(tmp[1])
            sz = int(tmp[2])
            self.barcos[(x,y)] = sz
            
    def listaBarcosDeprecated(self): #Solo para DEPURACION. No utilizar este metodo
        temp = self.barcos.keys()
        data = []
        for i in range(len(self.barcos)):
            data.append(objeto(temp[i],self.barcos[temp[i]],random.randrange(1,self.SIZE_X-2),random.randrange(1,self.SIZE_Y-1)))
        self.mapa1.agregarObjetos(data)

    def listaBarcos(self):
        '''
        Agrega los barcos leidos (previamente) del archivo de texto
        al mapa actual.
        '''
        temp = self.barcos.keys()
        data = []
        if len(self.barcos) > self.MAX_BARCOS:
            print 'Solo pueden haber '+str(self.MAX_BARCOS)+' barcos en el juego.'
            print 'Barcos ignorados: '+str(len(self.barcos)-self.MAX_BARCOS)+'\n'

        i = 0
        cant = 0
        while((i<self.MAX_BARCOS)and i<len(self.barcos)): #Solo se pueden agregar MAX_BARCOS al juego y ocupar MAX_ESPACIOS en total
            if (cant+self.barcos[temp[i]]<=self.MAX_ESPACIOS):
                data.append(objeto(0,self.barcos[temp[i]],temp[i][0],temp[i][1]))
                cant += self.barcos[temp[i]]
            else:
                print 'Solo puede haber '+str(self.MAX_ESPACIOS)+' espacios ocupados por barcos.'
                print str(len(self.barcos)-i)+' barcos seran ignorados.\n'
                i = self.MAX_BARCOS
            i += 1
        self.mapa1.agregarObjetos(data)

    def verificaPerdedor(self): #Verifica si el usuario ha perdido la partida (todos los barcos hundidos)
        if self.mapa1.verificaBarcos():
            return False
        else:
            return True

    def cleanMaps(self):
        self.mapa1.limpiarObjetos()
        #self.mapa2.limpiaObjetos()
            

class mapa(object):
    """
    Muestra al usuario (mediante sentencias 'print') los mapas
    del juego

    Como se deben desplegar dos tableros (principal y secundario),
    son dos instancias de esta clase las que hay que crear.

    En el mapa principal se muestra:
    - Flota del usuario local con el record de disparos provenientes
    del jugador contrario.

    En el mapa secundario se muestra:
    - Disparos que el jugador local ha enviado hacia el jugador contrario.
    Debe poder distinguirse entre disparos acertados y fallidos (esta informacion
    la provee la computadora remota automaticamente luego de cada jugada).
    """
    def __init__(self,tamX,tamY):
        #(ancho, alto, objetos iniciales del mapa)
        self.tamX = tamX
        self.tamY = tamY
        self.SIMBOLO_ESPACIO = ' '
        self.SIMBOLO_BORDE = '+'
        self.ocupados = [] #Espacios ocupados por barcos
        self.matriz = []
        self.objetos = []
        self.crearMapa()
        self.popularMapa()
        

    def crearMapa(self):
        '''
        Crea la matriz vacia que representara al mapa.
        Esta sera luego ocupada por los bordes y los
        simbolos que representan los objetos.
        '''
        self.matriz = []
        for x in range(self.tamY):
            self.matriz.append([])
            for y in range(self.tamX):
                self.matriz[x].append(self.SIMBOLO_ESPACIO)

    def agregarObjetos(self,extraObjetos):
        '''
        Agrega objeto(s) al mapa y refresca
        las posiciones ocupadas por cada uno
        de estos
        '''
        for i in extraObjetos:
            if i.getTipo() != 1:
                if self.posicionValida(i.getX(), i.getY(), i.getTam()):
                    self.objetos.append(i)
                    self.popularMapa()
                else:
                    print "Advertencia: Ya hay un objeto ocupando la posicion",str((i.getX(),i.getY()))+':'+str(i.getTam())+". Este barco ha sido ignorado."
            else:
                self.objetos.append(i)
                self.popularMapa()

    def disparoSobreBarco(self,objBarco,objDisparo): #Verifica si un disparo se encuentra en el rango de un barco
        k = objBarco
        l = objDisparo
        if l.getY()==k.getY() and l.getX() in range(k.getX(),k.getX()+k.getTam()):
            return True
        return False


    def verificaHundimiento(self): #Busca y clasifica todos los disparos que hayan caidos sobre todos los barcos
        for i in self.objetos:
            if i.getTipo()==0: #Si es un barco
                disparos = [] #Disparos que le han acertado a este barco
                for j in self.objetos:
                    if j.getTipo()==1: #Si es un disparo
                        if self.disparoSobreBarco(i,j):
                            if (j.getX(),j.getY()) not in disparos:
                                disparos.append((j.getX(),j.getY()))
                if len(disparos)>=i.getTam():
                    print '\n'+str(i), 'ha sido HUNDIDO por el enemigo' #Solo para DEPURACION
                    self.eliminarObjeto(i.getX(),i.getY())
    
    def verificaBarcos(self): #Cuenta la cantidad de barcos vivos aun
        cnt = 0
        for i in self.objetos:
            if i.getTipo() == 0: #Se contaran solamente los barcos
                cnt += 1
        return cnt
                        
                

    def eliminarObjeto(self,x,y):
        '''
        Eliminar un objeto especifico del mapa. Se requiere
        su ubicacion (x,y) para ser identificado individualmente
        '''
        i = 0
        while i<len(self.objetos):
            if self.objetos[i].getX()==x and self.objetos[i].getY()==y:
                del self.objetos[i]
                break
            i += 1

    def limpiarObjetos(self):
        '''
        Eliminar los objetos del mapa
        y dejar solamente los bordes
        '''
        self.objetos = []
        self.ocupados = []
        for y in range(1,self.tamY-1):
            for x in range(1,self.tamX-1):
                self.matriz[y][x] = self.SIMBOLO_ESPACIO

    def posicionValida(self,x,y,tam):
        """
        Devuelve True o False, dependiendo si la posicion es valida.
        Se evalua traslape con otros objetos y con el borde del mapa.
        """
        #print '' #DEPURACION
        #print 'Propuesta (x,y,tam):   '+str((x,y,tam)) #DEPURACION
        #print self.ocupados
        if x==0 or x>=self.tamX-1:
            return False
        if y==0 or y>=self.tamY-1:
            return False
        if x in range(self.tamX-tam,self.tamX):
            return False
        for i in self.ocupados:
            if y == i[1]:
                #print i, #DEPURACION
                if i[0] in range(x,x+tam) or i[0] == x:
                    return False
        return True

    def popularMapa(self):
        '''
        Actualiza la matriz con los datos (simbolos)
        de los objetos alojados en 'self.objetos'
        '''
        for x in range(self.tamX): #Bordes horizontales
            self.matriz[0][x] = self.SIMBOLO_BORDE
            self.matriz[self.tamY-1][x] = self.SIMBOLO_BORDE                  

        for y in range(1,self.tamY-1): #Bordes verticales
            self.matriz[y][0] = self.SIMBOLO_BORDE
            self.matriz[y][self.tamX-1] = self.SIMBOLO_BORDE
       
        for objeto in self.objetos: #Objetos especiales en el mapa
            if objeto.getStatus(): #Si el barco sigue vivo
                for y in range(self.tamY):
                    faltanImprimir = 0
                    for x in range(self.tamX):
                        if (objeto.getX()==x and objeto.getY()==y):
                            imprimeObjeto = objeto.getSimbolo()
                            faltanImprimir = objeto.getTam()
                            self.matriz[y][x] = imprimeObjeto
                            if objeto.getTipo() == 0: #Solo los barcos 'ocupan' espacio
                                self.ocupados.append((x,y))
                            faltanImprimir -= 1
                        elif (objeto.getY()==y and faltanImprimir > 0):
                            self.matriz[y][x] = imprimeObjeto
                            self.ocupados.append((x,y))
                            faltanImprimir -= 1
                        

    def imprimirMapa(self,principal=True):
        print     '\n----------------'
        if principal:
            print ' Mapa principal'
        else:
            print 'Mapa  secundario'
        print     '----------------'
        i = 0
        for line in self.matriz:
            if i != 0 and i != self.tamY-1:
                if i<10:
                    print ' '+str(i),
                else:
                    print str(i),
            else:
                print '  ',
            i += 1
            for item in line:
                print item+'  ',
            if i<self.tamY:
                print '\n'
        print '\n      ',
        for i in range(1,self.tamX-1):
            if i<10:
                print str(i)+' '*2,
            else:
                print str(i)+' '*1,
        print '\n'

    def imprimirDescripcionBarcos(self):
        print 'Barcos en juego:'
        for i in self.objetos:
            if i.getTipo()==0:
                print i,
        print ''

        

class objeto(object):
    """
    Cualquier objeto que se coloque dentro de los mapas
    Existen distintos tipos:
    * Barcos (Tipo 0)
    * Marcas de disparo del jugador contrario (Tipo 1)
    * Marcas de disparo fallido del jugador contrario (Tipo 2)

    Los objetos relacionados con barcos son leidos
    del archivo de texto a traves del metodo 'leeArchivoBarcos'
    de la clase 'juego'

    No se utiliza herencia, ya que no es parte del contenido del curso
    """

    def __init__(self,tipo,tam,posX,posY):
        self.tipo = tipo
        self.tam  = tam
        self.posX = posX
        self.posY = posY
        self.vivo = True #Sigue vivo el objeto? Por defecto se crea 'vivo'
        self.SIMBOLO_BARCO   = '0'
        self.SIMBOLO_DISPARO = 'X'
        self.SIMBOLO_FALLO   = '-'
        self.SIMBOLOS = [self.SIMBOLO_BARCO, self.SIMBOLO_DISPARO, self.SIMBOLO_FALLO]

    def getX(self):
        return self.posX

    def getY(self):
        return self.posY

    def setX(self,x):
        self.posX = x

    def setY(self,y):
        self.posY = y


    def getTam(self):
        return self.tam

    def setTam(self,tam):
        self.tam = tam


    def getTipo(self):
        return self.tipo

    def setTipo(self,tipo):
        self.tipo = tipo

    def kill(self):
        self.vivo = False

    def respawn(self):
        self.vivo = True

    def getStatus(self):
        return self.vivo

    def getSimbolo(self):
        return self.SIMBOLOS[self.getTipo()] #Tipo puede ser 0 o 1.
            

    def __str__(self):
        return '('+str(self.getX())+','+str(self.getY())+')'

"""

global j #Solo para DEPURACION.

def test1(): #Solo para DEPURACION. Crear objetos en mapa1
    global j
    for i in range(3):
        j = juego(IP,PUERTO)
        j.instanciarMapas()
        j.leeArchivoBarcos()
        j.listaBarcos()
        j.mapa1.crearMapa()
        j.mapa1.popularMapa()
        j.mapa1.imprimirMapa()
        print 'Ocupados:',j.mapa1.ocupados
        j.cleanMaps()

def test2(): #Solo para DEPURACION. Crear y eliminar objetos en mapa1
    global j
    j = juego(IP,PUERTO)
    j.instanciarMapas()
    j.leeArchivoBarcos()
    j.listaBarcos()
    j.mapa1.crearMapa()
    j.mapa1.popularMapa()
    j.mapa1.imprimirMapa()
    for i in j.mapa1.objetos:
        print i
    
    j.mapa1.eliminarObjeto(3,9)
    j.mapa1.crearMapa()
    j.mapa1.popularMapa()
    j.mapa1.imprimirMapa()
    for i in j.mapa1.objetos:
        print i

    j.mapa1.eliminarObjeto(2,4)
    j.mapa1.crearMapa()
    j.mapa1.popularMapa()
    j.mapa1.imprimirMapa()
    for i in j.mapa1.objetos:
        print i

    j.mapa1.eliminarObjeto(7,8)
    j.mapa1.crearMapa()
    j.mapa1.popularMapa()
    j.mapa1.imprimirMapa()
    for i in j.mapa1.objetos:
        print i

    j.leeArchivoBarcos()
    j.listaBarcos()
    j.mapa1.crearMapa()
    j.mapa1.popularMapa()
    j.mapa1.imprimirMapa()
    for i in j.mapa1.objetos:
        print i

def test3(): #Solo para DEPURACION. Verificar el metodo 'posicionValida' de la clase 'mapa'
    global j
    j = juego(IP,PUERTO)
    j.instanciarMapas()
    j.leeArchivoBarcos()
    j.listaBarcos()
    j.mapa1.crearMapa()
    j.mapa1.popularMapa()
    j.mapa1.imprimirMapa()
    print '\nBarcos en juego:'
    for i in j.mapa1.objetos:
        if i.getTipo()==0:
            print i,

def test4(): #Solo para DEPURACION. Verifica funcionamiento de 'hudir barcos' y perder el juego
    test3()
    j.mapa1.agregarObjetos([objeto(1,1,6,9)])
    j.mapa1.agregarObjetos([objeto(1,1,5,9)])
    j.mapa1.agregarObjetos([objeto(1,1,4,9)])
    j.mapa1.verificaHundimiento()
    j.mapa1.popularMapa()
    j.mapa1.imprimirMapa()

    print '\nBarcos en juego:'
    for i in j.mapa1.objetos:
        if i.getTipo()==0:
            print i,
    print '\nPartida perdida: ',
    print j.verificaPerdedor()


    j.mapa1.agregarObjetos([objeto(1,1,5,11)])
    j.mapa1.agregarObjetos([objeto(1,1,6,11)])
    j.mapa1.agregarObjetos([objeto(1,1,7,11)])
    j.mapa1.agregarObjetos([objeto(1,1,8,11)])
    j.mapa1.verificaHundimiento()
    j.mapa1.popularMapa()
    j.mapa1.imprimirMapa()
    
    print '\nBarcos en juego:'
    for i in j.mapa1.objetos:
        if i.getTipo()==0:
            print i,
    print '\nPartida perdida: ',
    print j.verificaPerdedor()

    j.mapa1.agregarObjetos([objeto(1,1,5,7)]) #Posiciones aleatorias
    j.mapa1.agregarObjetos([objeto(1,1,4,4)]) #No caen sobre ningun barco
    j.mapa1.agregarObjetos([objeto(1,1,7,6)])
    j.mapa1.verificaHundimiento()
    j.mapa1.popularMapa()
    j.mapa1.imprimirMapa()
    
    print '\nBarcos en juego:'
    for i in j.mapa1.objetos:
        if i.getTipo()==0:
            print i,
    print '\nPartida perdida: ',
    print j.verificaPerdedor()

    j.mapa1.agregarObjetos([objeto(1,1,2,2)])
    j.mapa1.agregarObjetos([objeto(1,1,3,2)])
    j.mapa1.agregarObjetos([objeto(1,1,4,2)])
    j.mapa1.agregarObjetos([objeto(1,1,5,2)])
    j.mapa1.verificaHundimiento()
    j.mapa1.popularMapa()
    j.mapa1.imprimirMapa()
    
    print '\nBarcos en juego:'
    for i in j.mapa1.objetos:
        if i.getTipo()==0:
            print i,
    print '\nPartida perdida: ',
    print j.verificaPerdedor()


    j.mapa1.agregarObjetos([objeto(1,1,2,4)])
    j.mapa1.agregarObjetos([objeto(1,1,3,4)])
    j.mapa1.verificaHundimiento()
    j.mapa1.popularMapa()
    j.mapa1.imprimirMapa()
    
    print '\nBarcos en juego:'
    for i in j.mapa1.objetos:
        if i.getTipo()==0:
            print i,
    print '\nPartida perdida: ',
    print j.verificaPerdedor()

def test5(): #DEPURACION. Verifica funcionalidad de mapa secundario (juego.mapa2)
    test3()
    j.mapa2.agregarObjetos([objeto(1,1,2,4)])
    j.mapa2.agregarObjetos([objeto(1,1,3,1)])
    j.mapa2.agregarObjetos([objeto(1,1,7,6)])
    j.mapa2.agregarObjetos([objeto(1,1,11,9)])
    j.mapa2.agregarObjetos([objeto(1,1,5,12)])
    j.mapa2.agregarObjetos([objeto(1,1,10,8)])
    j.mapa2.agregarObjetos([objeto(2,1,4,9)])
    j.mapa2.agregarObjetos([objeto(2,1,11,7)])
    print ' '
    j.mapa2.imprimirMapa(False)



def test6(): #DEPURACION. Verifica conectividad LAN y jugabilidad
    global j
    s = raw_input('(s)ervidor o (c)liente? -->  ')
    if s=='s':
        j = juego(IP, PUERTO, True)
        j.closeLAN()
    else:
        j = juego(IP, PUERTO, False)
        j.closeLAN()

"""

def jugar():
    s = None
    print '\n\n'
    while s not in ('s','c'):
        s = raw_input('Que rol desea tomar? (s)ervidor/(c)liente  -> ')
    if s == 's':
        ip = raw_input('IP local para levantar servidor:           ')
        while True:
            port = raw_input('Puerto donde desea levantar el servicio:   ')
            if port.isdigit():
                port = int(port)
                if port>0 and port<65536:
                    break
        j = juego(ip, port, True)
        j.closeLAN()
    else:
        ip = raw_input('IP del servidor al que desea conectarse:  ')
        while True:
            port = raw_input('Puerto del servidor al que se conectara:  ')
            if port.isdigit():
                port = int(port)
                if port>0 and port<65536:
                    break
        j = juego(ip, port, False)
        j.closeLAN()

jugar()
'''
http://en.wikipedia.org/wiki/Battleship_(game)
'''

'''
ToDo
        * (DONE) Agregar sprites de ataques recibidos
        * (DONE) Crear MAPA2
        * (DONE) Punteo
        * (DONE) Limitar cantidad total de espacios ocupados por barcos
        * (DONE) Interaccion LAN
        * (DONE) Interfaz amigable
        * (DONE) Arreglar bugs en MAPA2
'''
