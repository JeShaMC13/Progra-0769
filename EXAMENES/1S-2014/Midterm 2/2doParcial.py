import random, time

#Juego: encontrar el tesoro

class mundo(object):
    def __init__(self,tamX,tamY,objetos=[]): #Enviar como objetos: [tesoro,jugador,...]
        self.tamX = tamX #Tamanho inicial del mapa (columnas)
        self.tamY = tamY #Tamanho inicial del mapa (filas)
        self.objetos = objetos #Objetos a colocar en el mapa inicial
        self.BORDE    = '+' #Constante: Caracter que simboliza BORDE
        self.ESPACIO  = ' ' #Constante: Caracter que simboliza ESPACIO
        self.TESORO   = 0 #Constante: Correlativo de TESORO = 0
        self.JUGADOR  = 1 #Constante: Correlativo de JUGADOR = 1

    def agregaObjetos(self,objetos): #Agregar mas objetos al mapa
        self.objetos.extend(objetos) #Extender la lista de objetos del mundo

    def buscaObjetos(self): #Buscar objetos en el mundo
        listaPos = []
        for item in self.objetos:
            listaPos.append([item.tipo,(item.posX,item.posY)])
        return listaPos #Devolver la posicion de cada objeto

    def imprimeMundo(self,delay = 0): #Imprimir la abstraccion del mundo en pantalla
        print '\n\n'
        for y in range(self.tamY): #Recorrer cada una de las filas
            line = [] #Se imprimira linea por linea
            for i in range(self.tamX):
                line.append('')
            if y==0 or y==(self.tamY-1): #Las filas inicial y final son bordes
                for x in range(self.tamX):
                    line[x]=(self.BORDE) #Llenar de bordes todas las columnas
            else: #Si son las filas correspondientes al area de juego
                line = []
                for i in range(self.tamX): #Vaciar cada una de las columnas
                    line.append('')
                line[0] = self.BORDE #La primer columna es un borde
                x = 1
                while x < (self.tamX-1): #Si las columnas pertenecen al area de juego
                    time.sleep(delay) #Un efecto visual (puede eliminarse)
                    cnt = 0 #Cantidad de "objetos" en la posicion (x,y)
                    ocupado = 0 #Existe mas de un objeto en el mismo (x,y)?
                    for obj in self.objetos: #Cada uno de los objetos
                        if (y==obj.getY() and x==obj.getX()): #Verificar si estan ubicados en (x,y) actual
                            ocupado += 1 #Indicar que se ocupa un espacio
                            line[x] = obj.getSimbolo() #Imprimir el caracter correspondiente al objeto ('0' o 'x')
                            cnt += 1 #Se agrego un objeto a esta posicion
                            temp = x
                            while ocupado > 1: #Agrega un espacio a la derecha por cada posicion repetida
                                line[temp+1] = self.ESPACIO
                                temp += 1
                                ocupado -= 1
                    x += cnt #Verificar la siguiente columna
                    if x<self.tamX-1 and not cnt:
                        line[x] = self.ESPACIO
                        x += 1
                line[x] = self.BORDE #La ultima columna es un borde
            l = '' #Convertir la lista "line" a una cadena de caracteres
            for i in line:
                l += i
            print l #Imprimir la linea correspondiente a la fila 'y'

    def posValida(self,val,limite): #Es una posicion valida?
        return (val>0 and val<limite-1)

    def mueveObjeto(self,x,y,index): #Mover "x" o "y" posiciones respecto a la actual
        ob = self.objetos[index] #Que objeto se quiere mover?
        x += ob.getX() #Movimiento relativo en X
        y += ob.getY() #Movimiento relativo en Y
        if self.posValida(x,self.tamX): #Antes de moverse, verificar que
            ob.setX(x) #La posicion de destino sea valida en X
        else:
            ob.setX(self.objetos[index].getX())
            #print 'X invalida'
        if self.posValida(y,self.tamY):
            ob.setY(y)
        else:
            ob.setY(self.objetos[index].getY())
            #print 'Y invalida'

    def mueveJugador(self,x,y):
        self.mueveObjeto(x,y,self.JUGADOR) #Mover al jugador

    def mueveTesoro(self,x,y):
        self.mueveObjeto(x,y,self.TESORO) #Mover al tesoro
        
    def getPosObjeto(self,index): #Leer la posicion de cualquier objeto
        return (self.objetos[index].getX(),self.objetos[index].getY())

    def getPosJugador(self): #Leer la posicion del jugador
        return self.getPosObjeto(self.JUGADOR)

    def getPosTesoro(self): #Leer la posicion del tesoro
        return self.getPosObjeto(self.TESORO)
        

class objeto(object): #Un objeto puede ser el jugador, el tesoro o una traza
    def __init__(self,tipo,posX,posY):
        self.tipo = tipo #Tipo: Objeto, jugador, traza
        self.posX = posX #Posicion inicial en X
        self.posY = posY #Posicion inicial en Y
        self.TESORO  = 'x' #CONSTANTE: Caracter para mostrar TESORO en pantalla
        self.JUGADOR = '0' #CONSTANTE: Caracter para mostrar JUGADOR en pantalla
        self.TRAZA   = '*' #CONSTANTE: Caracter para mostrar TRAZA en pantalla

    def getX(self): #Devolver la posicion actual (X) del objeto
        return self.posX

    def getY(self): #Devolver la posicion actual (Y) del objeto
        return self.posY

    def setX(self,x): #Establecer posicion absoluta (X) del objeto
        self.posX = x
        #Depuracion:
##        print 'Tipo: '+self.asociaSimbolo(self.getTipo())+':',
##        print '('+str(x)+',',

    def setY(self,y): #Establecer posicion absoluta (Y) del objeto
        self.posY = y
        #Depuracion:
##        print str(y)+')'

    def asociaSimbolo(self,tp): #Que caracter corresponde a cada tipo de objeto?
        if tp==0:
            return self.TESORO
        elif tp==1:
            return self.JUGADOR
        elif tp==2:
            return self.TRAZA
        
    def getTipo(self): #Que tipo de objeto soy (TESORO,JUGADOR,TRAZA)?
        return self.tipo

    def getSimbolo(self): #Devuelve el caracter que corresponde al tipo de objeto
        return self.asociaSimbolo(self.tipo)

def imprimeInstrucciones(): #Creo que no es necesario explicar esto...
    print "El tesoro (marcado con 'x') aparecera en una ubicacion aleatoria. \n\
De la misma manera, usted (el jugador marcado con '0')\n\
comenzara el juego en una posicion al azar.\n\n  \
El objetivo es capturar el tesoro utilizando el menor \n\
numero de intentos. El unico problema es que Minimi\n\
tiene en su poder el objeto, por lo que usted debera\n\
perseguirlo hacia donde este se mueva; aunque debido a su\n\
corta estatura, el malevolo villano solamente puede\n\
moverse un cuadro a la vez. En cambio, usted es capaz\n\
de saltar uno o dos cuadros en cada turno.\n\n\
Le deseamos suerte en esta mision, Agente Powers!"

def inicializarJuego(SIZE_X = 30, SIZE_Y = 15): #Condiciones iniciales del juego
    global juego #Esta sera la instancia global del juego
    imprimeInstrucciones() 
    ocupados = [] #Posiciones ocupadas dentro del mapa
    tesoro =  objeto(0,0,0) #Inicializar objetos
    jugador = objeto(1,0,0) #Sin posicion
    agregar = [tesoro,jugador] #Coloque aqui los objetos que desee agregar
    nuevosObj = [] #Lista auxiliar. No cambiar.
    for item in agregar: #Colocar cada objeto en una posicion aleatoria
        itemX = random.randrange(1,SIZE_X - 1)
        itemY = random.randrange(1,SIZE_Y - 1)
        while (itemX,itemY) in ocupados: #No utilizar un espacio ocupado
            itemX = random.randrange(1,SIZE_X - 1)
            itemY = random.randrange(1,SIZE_Y - 1)
        item.setX = itemX
        item.setY = itemY
        nuevosObj.append(objeto(item.getTipo(),itemX,itemY))
        ocupados.append((itemX,itemY))
    juego = mundo(SIZE_X,SIZE_Y) #Crear la instancia del mundo
    juego.agregaObjetos(nuevosObj) #Agregar los objetos creados previamente en posiciones aleatorias

    #Depurando...
##    juego.objetos[0].setX(3)
##    juego.objetos[0].setY(1)
##    juego.objetos[1].setX(4)
##    juego.objetos[1].setY(1)
    #Quitar luego de terminar depuracion


    juego.imprimeMundo(0.001) #Imprimir la pantalla inicial. 1 milisegundo por fila

def mover(): #Pedir al usuario la direccion y saltos en cada turno
    pasos = None
    direc = None
    while (pasos not in ('1','2')):
        pasos = raw_input('Pasos a saltar (1,2)        --> ')
    while (direc not in ('U','D','L','R')):
        direc = raw_input("Direccion ('U','D','L','R') --> ")
    if direc=='U': #Arriba
        return (0,-1*int(pasos))
    if direc=='D': #Abajo
        return (0,int(pasos))
    if direc=='L': #Izquierda
        return (-1*int(pasos),0)
    else:         #Derecha
        return (int(pasos),0)

def jugar(): #Jugar
    global juego #Utilizar la instancia que se creo en 'inicializarJuego()'

    #Mover al jugador    
    (x,y) = mover()
    juego.mueveJugador(x,y)

    #Mover el tesoro aleatoriamente
    x = [-1,0,1]
    random.shuffle(x)
    x = x[0]
    if not x:
        y = [-1,1]
    else: #Evitar saltos en diagonal
        y = [0,0]
    random.shuffle(y)
    y = y[0]
    juego.mueveTesoro(x,y)

    #Reimprimir mapa del mundo
    juego.imprimeMundo(0.0005) #Imprimir una linea cada 500 microsegundos

def ganar():
    global intentos #Intentos utilizados para capturar el tesoro
    print "\n\nFelicitaciones, atrapaste a Minimi junto con el paquete"
    print 'Utilizaste '+str(intentos)+' turnos'


juego = None #Crear el objeto que sera utilizado como instancia del juego
intentos = 0

inicializarJuego()
while(juego.getPosJugador()!=juego.getPosTesoro()): #Mientras no coincidan posiciones
    jugar()
    intentos += 1
ganar() #Ganar
