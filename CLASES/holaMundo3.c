#include <stdio.h>

/*
Este programa pide datos al usuario y luego hace operaciones
matematicas basicas.
*/

int n1, n2;

int main(void){
	printf("Bienvenid@ a la calculadora basica de 0769\n");

	printf("\n\nIngrese N1: ");
	scanf("%d", &n1);

	printf("Ingrese N2: ");
	scanf("%d", &n2);

	printf("\n\nLa suma es: %d\n", (n1+n2));
	printf("La resta es: %d\n", (n1-n2));
	printf("El producto es: %d\n", (n1*n2));

	if(n2==0){
		printf("No se puede dividir dentro de 0\n\n");	
	}else{
		printf("La division es: %1.4f\n", (n1/(float)n2));
	}


	return 0;
}
