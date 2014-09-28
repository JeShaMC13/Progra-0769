# Este es un comentario
# No se requiere importar libreria estandar

print 'Hola Python'   #printf("Hola Python");
print "Hola Python"   #printf("Hola Python");

"""
Este es un comentario
de multiples lineas

En C un 'if' se escribe asi:

int a;
a=8;
if(a==1){
    printf("A es 1");
}else{
    printf("A no es 1, A es %d", a);
}
"""

#Para hacer lo mismo en Python:
#No se declaran variables

a=8 #No fue necesario predeclarar la variable
if a==1:
    print 'A es 1'
else:
    print 'A no es 1, A es', str(a) #Type casting: str(a). Conversion a "STRING"

"""
Ahora, para leer las entradas de texto del usuario
a traves del teclado (algo similar a 'scanf' en C)
se utiliza 'raw_input'
"""

b = raw_input("Ingrese el valor de b: ")
if b.isdigit(): #Si el texto ingresado es un numero
    b = int(b)  #Se hace type casting de forma segura

print 'b es de tipo',str(type(b)) #'type' devuelve el tipo de la variable/objeto
