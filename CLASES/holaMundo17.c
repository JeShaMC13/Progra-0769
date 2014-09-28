/*
Mas sobre punteros
*/

#include<stdio.h>

int main(void){

	int var; //Una variable cualquiera
	int *pntr1; //Puntero 1
	int *pntr2; //Puntero 2
	
	var = 777; //Un numero cualquiera para variable
	
	pntr1 = &var; //& es el operador "de direccion"
				  //pntr1 almacena LA DIRECCION de memoria
				  //donde se encuentra "variable"

	pntr2 = &var; //pntr2 tambien apunta a la misma direccion
				  //de memoria a la que esta dirigida "pntr1"
					   
	
	printf("\nDesplegando la variable \"var\": %d", var);
	printf("\nDesplegando el valor del puntero \"pntr1\": %p", pntr1);
	printf("\nDesplegando el valor del puntero \"pntr2\": %p", pntr2);
	printf("\nDesplegando el valor a donde apunta \"pntr1\": %d", *pntr1);
	printf("\nDesplegando el valor a donde apunta \"pntr2\": %d", *pntr2);
	printf("\n\n\n");
	
	printf("Si modifico el valor de \"pntr1\" o \"pntr2\" habra un CRASH");
	
	printf("\nEn vez de eso, mejor modifico lo que esta almacenado en la direccion a la que estan dirigidos los punteros\n\n");
	
	printf("Ahora modificare \"var\" indirectamente a traves de uno de los punteros");
	
	
	
	printf("\n\n\nVamos a hacer \"*pntr1 = 555;\"");
	
	*pntr1 = 555;
	
	printf("\nVerificamos entonces el valor almacenado en \"var\": %d \n\n", var);
	
	return 0;
}
