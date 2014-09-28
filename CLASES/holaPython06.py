#Ciclos "for" y listas

carros = ['Lamborghini', 'Ferrari', 'Porsche', 'Bugatti']

for x in carros:
    print x
    print type(x)

print '\n\n'

for x in range(len(carros)):
    print carros[x]
    print type(x)

print '\n\n'

for x in range(0,101,10):
    print x
