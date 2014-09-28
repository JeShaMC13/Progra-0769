class automovil(object):
    def __init__(self, color, peso):
        self.color = color
        self.peso  = peso
        self.combustible = 0.0  #Combustible inicial
        self.rendimiento = 45.0 #45km/gal

    def setRendimiento(self, valor): #Si se desea cambiar el rendimiento
        self.rendimiento = valor

    def agregarCombustible(self, cant): #Agregar combustible
        self.combustible += cant

    def convierteCombustible(self): #Convertir combustible a distancia
        return self.combustible*self.rendimiento

    def convierteDistancia(self, distancia): #Convertir distancia a combustible
        return float(distancia) / self.rendimiento

    def mover(self, distancia):
        if distancia <= self.convierteCombustible():
            self.combustible -= self.convierteDistancia(distancia)
            print 'Se movio ' + str(distancia) + ' kilometros'
        else:
            print 'No hay combustible suficiente'

class bus(automovil):
    def __init__(self, pasajeros, color, peso):
        self.pasajeros = pasajeros
        self.rendimiento = 30.0
        self.MAX_PASAJEROS = 60
        self.combustible = 0
        automovil.__init__(self, color, peso)

    def convierteCombustible(self):
        return self.combustible*self.rendimiento*((self.MAX_PASAJEROS - self.pasajeros))*.2

    def convierteDistancia(self, distancia):
        return float(distancia) / (self.rendimiento*((self.MAX_PASAJEROS - self.pasajeros))*.2)

