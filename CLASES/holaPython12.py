#Diccionarios

Guatemala = {'Capital':'Guatemala','Habitantes':15.08e6,'Extension':108889}
Eslovenia = {'Capital':'Liublijana','Habitantes':2.047e6,'Extension':20253}
Italia = {'Capital':'Roma','Habitantes':59.4e6,'Extension':301338}
Cuba = {'Capital':'La Habana','Habitantes':11.24e6,'Extension':110860}

print Guatemala['Capital']
Guatemala['Capital'] = 'Cd. Guatemala'
print Guatemala['Capital']
print ""
print 'Habitantes en Eslovenia'
print Eslovenia['Habitantes']
Eslovenia['Habitantes'] = 2e6 #Notacion cientifica!

print ""
print "Existe la clave 'capital' en Guatemala?"
print (Guatemala.has_key('capital'))

print ""
print "Existe la clave 'Capital' en Guatemala?"
print (Guatemala.has_key('Capital'))

print ""
print "Que valor tiene asociada la clave 'Extension' en Cuba?"
print Cuba['Extension']

print ""
print "Cuantos elementos tiene Italia?"
print str(len(Italia))

print ""
print "Que claves tiene Italia?"
print Italia.keys()

print ""
print "Que valores tienen las claves de Italia?"
print Italia.values()

print ""
print "Que elementos contiene Italia?"
print Italia.items()

print ""
print "Eliminaremos la clave 'Extension' de Italia"
del Italia['Extension']

print ""
print 'Si juntamos todos los paises en una lista: '

paises = [Guatemala, Eslovenia, Italia, Cuba]
for i in paises:
    print i
print "Notese que Italia ya no tiene 'Extension'..."
