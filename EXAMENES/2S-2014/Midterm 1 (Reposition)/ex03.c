#include <stdio.h>

const unsigned int N = 5491; //Cambie este numero, dependiendo de su temario

unsigned int primo(unsigned int n){
	unsigned int i;
	i = n / 2;
	while(i > 1){
		if(n%i == 0){ //Si hay un divisor entero
			return 0; //No es primo
		}
		i--;
	}
	return 1; //Si no encuentra divisor entero, es primo
}

int main(void){ //Buscar el n-esimo primo

	unsigned int cant = 0;
	unsigned int i = 1;

	while(cant < N){
		i++;
		if(primo(i)){ //Si el numero actual es primo
			cant++; //Tomarlo en cuenta para la cantidad total
		}
	}

	printf("\n\n%u\n\n", i);

	return 0;
}