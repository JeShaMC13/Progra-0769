def validaNumero(promptText):
    try:
        x = int(float(raw_input(promptText)))
        return x
    except ValueError:
        return None

def leerNumero(promptText):
    x = validaNumero(promptText)
    while(x == None):
        x = validaNumero(promptText)
    return x
    

try:
	num = leerNumero('Ingrese numerador: ')
	den = leerNumero('Ingrese denominador: ')
	a = num / den
except ZeroDivisionError:
	while(den == 0):
		den = leerNumero('Tonto, ingrese un denominador valido: ')
	a = num / den
print a
k
