#include <stdio.h>

const int N = 2256; //Cambie este numero, dependiendo de su temario

int i = 0;
long suma = 0;

int main(void){
	while(i<N){
		if ((i%5==0) || (i%7==0)){ //Si es divisible ente 7 o 5
			suma += i;
		}
		i++;
	}
	printf("\n%ld\n\n", suma);
	return 0;
}