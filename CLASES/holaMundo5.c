#include <stdio.h>

/*
Continuamos con sentencias condicionales

Operadores de comparacion:

==    Igual
!=    Distinto
<=    Menor o igual que
>=    Mayor o igual que
<     Menor que
>     Mayor que

*/

int n1, n2;
char operacion;


int main(void){

	printf("Calculadora v2.0\n\n");
	printf("1) Suma\n2) Resta\n3) Producto\n4) Cociente\n\n");
	printf("Seleccione una opcion (entre 1 y 4): ");
	scanf("%c", &operacion); //Leyendo un caracter

	printf("Ingrese n1: ");
	scanf("%d", &n1);
	printf("Ingrese n2: ");
	scanf("%d", &n2);

	if(operacion == '1'){
		printf("La suma es: %d", (n1+n2));
	}else if(operacion == '2'){
		printf("La resta es: %d", (n1-n2));
	}else if(operacion == '3'){
		printf("El producto es: %d", (n1*n2));
	}else if(operacion == '4'){
		if(n2 != 0){
			printf("El cociente es: %d", (n1/n2));
		}else{
			printf("Indefinido: division entre 0");
		}
	}else{
		printf("Le dijimos que era entre 1 y 4");
	}

	printf("\n\n\n");

	return 0;
}

