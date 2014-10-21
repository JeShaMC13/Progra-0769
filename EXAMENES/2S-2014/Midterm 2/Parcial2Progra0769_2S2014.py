class interfaz(object):

    '''
    Interfaz para el usuario    
    '''

    #Metodos especiales
    def __init__(self, N):
        self.cmplxOp = operacionesComplejas() #Instanciar operaciones complejas
        self.N = N
        if self.N == 3: #Si son 3 bits, hacer las operaciones
            self.id = int(raw_input('Ingrese el ultimo digito de su carnet: '))%10
            self.runOp()
        else: #De lo contrario, solo mostrar la tabla de verdad
            self.showTruthTable()

    def __str__(self):
        return self.showTruthTable()

    def __repr__(self):
        return self.__str__()


    #Metodos publicos
    def runOp(self):
        tmpAns = self.cmplxOp.computeAnswer(self.id) #Calcular respuestas
        tempMat = [] #Matriz temporal donde se almacenara la tabla de verdad para N=3
        tempMat.extend(self.cmplxOp.truthTbl(self.N))
        tempMat.append([]) #Agregar la ultima fila para colocar alli las respuestas
        for i in range(len(tempMat[0])):
            tempMat[-1].append(tmpAns[i]) #Agregar las respuestas de cada combinacion
        tempMat = self.cmplxOp.matrixTranspose(tempMat) #Transponer la matriz para que se vea bonito
        
        tAns = [[]] #Esta matriz sera la que se despliegua
        tAns[0].extend(self.cmplxOp.letterList(self.N)) #Insertar los caracteres al inicio
        tAns[0].append('OUT') #La ultima columna se llama "OUT"
        tAns.extend(tempMat) #Agregar los valores de la tabla de verdad y resultado

        for i in tAns: #Desplegar la matriz, fila por fila
            print i
        
    def showTruthTable(self): #Mostrar la tabla de verdad para un N arbitrario
        tTable = []
        tTable.append([])
        tTable[0].extend(self.cmplxOp.letterList(self.N))
        tTable.extend(self.cmplxOp.matrixTranspose(self.cmplxOp.truthTbl(self.N)))

        for i in tTable:
            print i



class operacionesComplejas(object):

    '''
    Funciones logicas a implementar para cada temario
    Todas las entradas son de 3 bits y 1 bit de salida

    Aqui tambien se genera la matriz de N bits para mostrar
    la tabla de verdad
    '''


    #Metodos especiales
    def __init__(self):
        self.op = opBasicas()

    def __str__(self):
        return self.matrixTranspose(self.truthTbl(3))

    def __repr__(self):
        return self.__str__()

    
    #Metodos publicos
    def truthTbl(self, N): #Genera una tabla de verdad de N bits
        M = 2**N #Numero de filas
        cntMax = M/2
        truthTable = []
        for i in range(N):
            currentValue = 1
            truthTable.append([])              
            for j in range(M):
                if (j % cntMax == 0): #Cambiar a 1 o 0 cada M/2 elementos
                    currentValue = int(not currentValue)
                truthTable[i].append(currentValue)
            cntMax /= 2
        return truthTable

    def matrixTranspose(self, mat): #Devuelve la traspuesta de una matrix N*M
        N = len(mat)
        M = len(mat[0])
        newMatrix = []
        for i in range(M):
            newMatrix.append([])
            for j in range(N):
                newMatrix[i].append(mat[j][i])
        return newMatrix
    
    def letterList(self, N): #Devuelve una lista del abecedario en mayusculas
        capitalLetters = []
        for i in range(65, 65 + N):
            capitalLetters.append(chr(i))
        return capitalLetters

    def computeAnswer(self, carnet): #Calcular respuesta para cada rango de carnet
        data = self.matrixTranspose(self.truthTbl(3)) #Generar tabla para N=3 bits
        
        if carnet < 2:
            fun = self.__op01
        elif carnet < 4:
            fun = self.__op23
        elif carnet < 6:
            fun = self.__op45
        elif carnet < 8:
            fun = self.__op67
        else:
            fun = self.__op89

        ans = []
            
        for i in data:
            self.a = i[0]
            self.b = i[1]
            self.c = i[2]
            ans.append(fun())

        return ans


    #Metodos privados
    def __op01(self): #Carnet con terminacion 0 o 1
        return self.op.AND(self.op.NOT(self.op.AND(self.a, self.b)), self.op.OR(self.b, self.c))

    def __op23(self): #Carnet con terminacion 2 o 3
        return self.op.OR(self.op.AND(self.op.NOT(self.a), self.b), self.op.NOT(self.c))

    def __op45(self): #Carnet con terminacion 4 o 5
        return self.op.NOT(self.op.NOT(self.op.AND(self.op.OR(self.a, self.b), self.c)))

    def __op67(self): #Carnet con terminacion 6 o 7
        return self.op.OR(self.op.OR(self.a, self.b), self.op.NOT(self.op.AND(self.c, self.c)))

    def __op89(self): #Carnet con terminacion 8 o 9
        return self.op.AND(self.op.NOT(self.a), self.op.OR(self.op.NOT(self.b), self.c))
   

class opBasicas(object):

    '''
    Operaciones basicas de logica digital
    Se implementa tambien la conversion a entero
    de una lista de datos (independiente de su tamanio)
    '''
    
    #Metodos especiales
    def __init__(self):
        pass

    #Metodos publicos
    def NOT(self, x):
        x,  = self.__toInt((x,))
        if x == 0:
            return 1
        else:
            return 0
        
    def AND(self, x, y):
        x, y = self.__toInt((x, y))
        if x == 1:
            if y == 1:
                return 1
            else:
                return 0
        else:
            return 0

    def OR(self, x, y):
        x, y = self.__toInt((x, y))
        if x == 0:
            if y == 0:
                return 0
            else:
                return 1
        else:
            return 1

    #Metodos privados
    def __toInt(self, data):
        '''
        Conversion de una lista de datos
        a numero entero
        '''
        z = []
        for i in data:
            z.append(int(i))
        return z

interfaz(3) #Ejecutar con N=3 bits
