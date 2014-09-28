#Mas sobre funciones

def sumaVectores(vec1, vec2):
    n = len(vec1)
    suma = []
    for i in range(n):
        suma.append(vec1[i]+vec2[i])
    return suma
