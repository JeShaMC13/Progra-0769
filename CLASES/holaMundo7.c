#include <stdio.h>

//Utilizando la sentencia "Switch-Case"

int n1, n2;
char op;


int main(void){
	
	printf("\n\n\nCalculadora v2.1 (ahora con Switch-Case)\n\n");
	printf("1) Suma\n2) Resta\n3) Producto\n4) Cociente\n\n");
	printf("Seleccione una opcion (entre 1 y 4): ");
	scanf("%c", &op); //Leyendo un caracter
	
	if((op=='1') || (op=='2') || (op=='3') || (op=='4')){
		printf("Ingrese n1: ");
		scanf("%d", &n1);
		printf("Ingrese n2: ");
		scanf("%d", &n2);
		
		switch(op){
			case '1':
				printf("La suma es: %d", (n1 + n2));
				break;
			case '2':
				printf("La resta es: %d", (n1 - n2));
				break;
			case '3':
				printf("El producto es: %d", (n1 * n2));
				break;
			default:
				if(n2 != 0){
					printf("El cociente es: %d", (n1 / n2));
				}else{
					printf("Indefinido: division sobre 0");
				}
		}

	}else{
		printf("Le dijimos que era entre 1 y 4");
	}

	printf("\n\n\n");

	return 0;
}
