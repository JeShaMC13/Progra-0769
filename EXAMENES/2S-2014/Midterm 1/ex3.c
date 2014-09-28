#include <stdio.h>

const unsigned int N = 467690; //Este numero depende de su carnet

unsigned int i = 2; //Collatz para 1 no tiene sentido. Iniciamos en 2
unsigned int maxCollatz = 0; //Maxima cantidad de iteraciones de la actual secuencia?
unsigned int mayor; //A quien pertenece la mayor secuencia?
unsigned int x; //Variable auxiliar para generar una secuencia Collatz
unsigned int cant; //Cuantas iteraciones tiene la actual secuencia?

int main(void){
	mayor = i; //Inicializar el maximo valor
	while(i <= N){
		x = i; //La secuencia comienza con este valor inicial
		cant = 1; //Todas las secuenicas tienen como minimo una iteracion.
		while(x > 1){ //Aqui se implementa cada una de las secuencias
			if (x % 2 == 0){ //Si el numero actual es par
				x /= 2; //El proximo numero es x/2
			}else{ //Si es impar
				x = 3*x + 1; //El proximo numero es 3x+1
			}
			cant++; //Agregar uno al contador de iteraciones de la actual seucencia
		}
		if (cant > maxCollatz){ //Si la actual secuencia tiene mas elementos que la maxima secuencia anterior
			maxCollatz = cant; //Cantidad de iteraciones de la nueva maxima secuencia
			mayor = i; //El nuevo numero inicial con mayor cantidad de iteraciones
		}
		i++; 
	}

	printf("El numero que genera la mayor secuencia Collatz es: %u \n\n", mayor);

	return 0;
}
