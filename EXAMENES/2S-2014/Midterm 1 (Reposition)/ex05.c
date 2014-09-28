#include <stdio.h>

const unsigned int N = 97; //Cambie este numero, dependiendo de su temario

long long triangular(unsigned int x){
	long long suma = 0;
	unsigned int i;

	for(i=0; i<=x; i++){
		suma += i; //Ir sumando cada uno de los numeros anteriores al numero triangular
	}

	return suma;
}

unsigned int divisoresTriangular(unsigned int x){ //Cant. de divisores de cada numero triangular
	long long n;
	long long i;
	unsigned int cant = 0; //Cantidad de divisores del numero triangular
	n = triangular(x);
	i = n;
	while (i > 0){
		if (n%i == 0){
			cant++;
		}
		i--;
	}
	return cant;
}

int main(void){ 
	
	unsigned int i = 0;
	unsigned int cant = 0;

	while(cant <= N){ //Buscar hasta encontrar un triangular con MAS de N divisores
		i++;
		cant = divisoresTriangular(i);
	}

	printf("\n\n%u\n\n", i);

	return 0;
}