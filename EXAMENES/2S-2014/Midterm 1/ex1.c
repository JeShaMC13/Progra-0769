#include <stdio.h>

unsigned const N = 3241; //Reemplace este numero por el que le corresponde a su carnet

unsigned int i = 3; //Es ilogico iniciar desde cero
unsigned int suma = 0;

int main(void){
	while(i < N){
		if((i%3==0)||(i%5==0)){ //Es divisible entre 3 o 5?
			suma += i; //Sumarlo!
		}
		i++; //Vamos a verificar el siguiente nuemro
	}
	printf("\nResultado: %u\n\n", suma);
	return 0;
}
