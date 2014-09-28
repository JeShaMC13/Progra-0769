#Funcion split. Aplica solamente a objetos tipo STRING

def splitSpace(a):
    #Split de elementos separados por espacios
    b = a.split()
    return b

def splitComma(a):
    #Split de elementos separados por comas
    b = a.split(',')
    return b

def splitAmpersand(a):
    #Split de elementos separados por... &?
    b = a.split('&')
    return b


txt1 = 'Hola Mundo Este es Python'
txt2 = '01,200815521,Progra 0769,Notas,61,61,61,60,58'
txt3 = '01&25&37&Jacinto Javier&Maria Jose&Tamarindo y Rosa Jamaica'

print "\n\n"
print txt1
print splitSpace(txt1)
print "\n\n"
print txt2
print splitComma(txt2)
print "\n\n"
print txt3
print splitAmpersand(txt3)
