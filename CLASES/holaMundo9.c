//Vectores

#include<stdio.h>

//Vector CONSTANTE con los digitos del sistema decimal
//Este vector NO puede ser modificado: es constante
const unsigned int digitos[10] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};

//Esta es otra forma de definir constantes
#define N 5 //Almacenaremos la edad de 5 personas. 


//Vector que almacenara la edad de N personas
unsigned int edades[N]; //Seran almacenados en bloques de memoria individuales

int main(void){

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
	
	printf("\n\nLas edades ingresadas fueron: ");
	printf("%d", edades[0]);
	printf(", %d", edades[1]);
	printf(", %d", edades[2]);
	printf(", %d", edades[3]);
	printf(", %d", edades[4]);
	
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
	
	printf("\n\n");

	return 0;
}
