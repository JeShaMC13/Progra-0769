#include <stdio.h>

const int N = 789442; //Cambie este numero, dependiendo de su temario

unsigned int previous[2] = {0, 1};
unsigned int fib = 0;
long suma = 0;

int main(void){

	while(fib < N){
		if(fib%2!=0){ //Si es impar
			suma += fib; //Sumarlo
		}
		fib = previous[0] + previous[1]; //Fibonacci suma los dos digitos anteriores
		previous[0] = previous[1];
		previous[1] = fib;
	}
	printf("\n%ld\n", suma);

	return 0;
}