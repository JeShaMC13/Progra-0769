#Rangos de billar

#Esta es una variable
#Nomenclatura de camello

miVariableNumero1 = 1
miVariableNumero2 = 2

#Constantes siempre en MAYUSCULAS
#Palabras separadas por guion bajo

B_INICIAN  = 1
B_TERMINAN = 5
M_INICIAN  = 6
M_TERMINAN = 10
A_INICIAN  = 11
A_TERMINAN = 15

print "\n\n\n\nRangos de billar\n\n"
n = raw_input("Numero de bola: ")
if n.isdigit():
    n = int(n)

if ((n>=B_INICIAN) and (n<=B_TERMINAN)):
    print "Baja"
elif ((n>=M_INICIAN) and (n<=M_TERMINAN)):
    print "Media"
elif ((n>=A_INICIAN) and (n<=A_TERMINAN)):
    print "Altas"
else:
    print "Usted metio la bola blanca. Esta no tiene numero!"
