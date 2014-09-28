/*
Programacion Modular:
	-Funciones/Procedimientos
	-Parametros de una funcion/procedimiento
*/

#include<stdio.h>

void miProc1(void){
	printf("\nEstoy ejecutando el Procedimiento 1");
}

void miProc2(int parametro){
	printf("\nSoy el procedimiento 2 y recibi un parametro: %d", parametro);
}

void miProc3(int param1, int param2){
	printf("\nSoy el procedimiento 3 y recibi dos parametros: %d, %d", param1, param2);
}

int sumar(int n1, int n2){ //Notese que ahora no inicia con "void"
	return (n1 + n2); //Una funcion SIEMPRE devuelve un valor
}

int parImpar(int n){
	if(n%2 == 0){ //Si es par
		return 1; //devuelve 1
	}else{ 		  //de lo contrario
		return 0; //devuelve 0
	}
}

int main(void){
	int temp; //Variable temporal
	
	miProc1();
	miProc2(5);
	miProc3(1,2);
	
	temp = sumar(3, 4);
	
	printf("\nLa suma de 3 y 4 es %d", temp);
	
	printf("\nEs 4 un numero par? (1=SI, 0=NO): %d", parImpar(4));
	printf("\nEs 7 un numero par? (1=SI, 0=NO): %d", parImpar(7));
	
	printf("\n\n");

	
	return 0;
}
