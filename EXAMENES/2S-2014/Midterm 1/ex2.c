#include <stdio.h>

const unsigned int N = 661043; //Este numero depende de su carnet
unsigned int x, i;
int factorPrimo, primo;

int main(void){
	x = N/2; //Como se busca a el mayor factor primo
			 //se inicia desde arriba, y no desde 1
	factorPrimo = 0; //0 = Falso, 1 = Verdadero
	while(!factorPrimo){ //Es equivalente a "while(factorPrimo==0)"
		if (N%x == 0){ //Verificando si el numero es un factor
			i = x/2;
			primo = 1; //0 = Falso, 1 = Verdadero
			while (i > 1){
				if (x % i == 0){ //Verificando si el factor es primo
					primo = 0; //Si es divisible, no es primo
				}
				i--;
			}
			if (primo){ //Equivalente a "if (primo != 0)"
				factorPrimo = 1; //Encontramos el mayor factor primo
			}
		}
		x--;
	}
	x++;
	printf("\n\nEl mayor factor primo es: %d\n", x);
	return 0;
}
