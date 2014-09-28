#include <stdio.h>

const unsigned int N = 105340; //Cambie este numero, dependiendo de su temario

long long triangular(unsigned int n){
	long long suma = 0;
	unsigned int i;

	for(i=0; i<=N; i++){
		suma += i; //Ir sumando cada uno de los numeros anteriores al numero triangular
	}

	return suma;
}

int main(void){ 
	
	printf("\n\n%lld\n\n", triangular(N));

	return 0;
}