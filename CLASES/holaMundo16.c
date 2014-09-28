/*

Hoy les presentamos:
- Prototipos
- Punteros

*/

#include<stdio.h>

int suma(int *data);  //Prototipo de funcion SUMA
int resta(int *data); //Prototipo de funcion RESTA

int main(void){
	int sumandos[2];
	int *dir; //Declaracion del puntero a un entero
	int resultado;
	
	dir = &sumandos[0]; //Apuntamos a la direccion de memoria del primer elemento
	
	printf("\n\nIngrese n1: ");
	scanf("%d", &sumandos[0]);
	
	printf("Ingrese n2: ");
	scanf("%d", &sumandos[1]);
	
	resultado = suma(dir); //"dir" es la DIRECCION de memoria de "sumandos[0]"
	printf("\n\nLa suma es: %d ", resultado);
	
	resultado = resta(dir);
	printf("\n\nLa resta es: %d ", resultado);
	
	return 0;
}


int suma(int *data){ //"data" almacenara la DIRECCION de memoria recibida
	return data[0]+data[1];	
}

int resta(int *data){
	return data[0]+data[1];
}
