//Vectores y ciclos "for"

/*TAREA:
1) Calcular el FACTORIAL de un numero ingresado por el usuario
2) Calcular la potencia de un numero. El usuario ingresa base y exponente (positivo).
*/

#include<stdio.h>

//Vector CONSTANTE con los digitos del sistema decimal
//Este vector NO puede ser modificado: es constante
const unsigned int digitos[10] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};

//Esta es otra forma de definir constantes
#define N 5 //Almacenaremos la edad de 5 personas. 


//Vector que almacenara la edad de N personas
unsigned int edades[N]; //Seran almacenados en bloques de memoria individuales

int main(void){

	/*Componentes de un ciclo:
		Inicio
		Fin
		Incremento
	*/

	unsigned int i; //Este va a ser nuestro contador del ciclo
	//Un ciclo SIEMPRE debe tener un contador

	//Codigo del ejemplo anterior
	/*
		printf("\n\n-------Edades-------\n\n");
		printf("Ingrese la edad de la persona 1: ");
		scanf("%d", &edades[0]); //Note que el indice de los vectores SIEMPRE inicia en 0
		printf("Ingrese la edad de la persona 2: ");
		scanf("%d", &edades[1]);
		printf("Ingrese la edad de la persona 3: ");
		scanf("%d", &edades[2]);
		printf("Ingrese la edad de la persona 4: ");
		scanf("%d", &edades[3]);
		printf("Ingrese la edad de la persona 5: ");
		scanf("%d", &edades[4]); //El ultimo indice del vector es N-1. 4=5-1
	*/
	
	//Version eficiente, utilizando un ciclo
	printf("\n\n-------Edades-------\n\n");
	for(i=0; i<N; i=i+1){ //Recordemos que N=5, segun se definio al inicio
		printf("Ingrese la edad de la persona %d: ", (i+1)); //Solo para que inicie desde 1 (i+1)
		scanf("%d", &edades[i]); //Leemos y almacenamos lo que ingrese el usuario por el teclado
	}
	
	
	
	
	
	
	//Codigo del ejemplo anterior
	/*
	printf("\n\nLas edades ingresadas fueron: ");
	printf("%d", edades[0]);
	printf(", %d", edades[1]);
	printf(", %d", edades[2]);
	printf(", %d", edades[3]);
	printf(", %d", edades[4]);
	*/
	
	//Version eficiente, utilizando un ciclo
	printf("\n\nLas edades ingresadas fueron: ");
	for(i=0; i<N; i=i+1){ //Es posible reutilizar la variable "i"
		printf("%d ", edades[i]);
	}
	
	
	//Codigo del ejemplo anterior
	/*	
	printf("\nLos digitos el sistema decimal son: ");
	printf("%d", digitos[0]);
	printf(", %d", digitos[1]);
	printf(", %d", digitos[2]);
	printf(", %d", digitos[3]);
	printf(", %d", digitos[4]);
	printf(", %d", digitos[5]);
	printf(", %d", digitos[6]);
	printf(", %d", digitos[7]);
	printf(", %d", digitos[8]);
	printf(", %d", digitos[9]);
	*/
	
	//Version eficiente, utilizando un ciclo
	printf("\nLos digitos el sistema decimal son: ");
	for(i=0; i<10; i++){ // "i++" es equivalente a decir "i=i+1"
		printf("%d ", digitos[i]);
	}

	printf("\n\n");

	return 0;
}
