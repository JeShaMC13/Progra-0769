//Ciclos WHILE
//Siempre se requiere de una variable de control/contador

#include <stdio.h>

int i; //La famosa variable de control "i"

int main(void){
	
	//Vamos a sumar "n" numeros, donde "n" lo define el usuario
	int n; //Variable local. Veremos esto a mas detalle en programacion modular.
	int suma; //Necesitamos almacenar en algun lado el resultado de la suma
	int temp; //Tambien una variable temporal donde almacenar el sumando actual
	
	printf("\nCuantos numeros desea sumar?: ");
	scanf("%d", &n);
	
	
	i=0; //A diferencia de "for", hay que inicializar el contador
		 //antes de ingresar al ciclo "while". Este es el inicio
	suma=0; //La suma inicia con 0
	
	while(i<n){ //La condicion de finalizacion
		printf("Numero %d: ", i+1);
		scanf("%d", &temp);
		suma+=temp; // "suma+=temp" es equivalente a "suma=suma+temp"
		i++; //Siempre hay que modificar el contador dentro del ciclo
			 //de lo contrario, nos quedamos en un ciclo infinito.
			 //Este es el incremento del ciclo
	}
	
	printf("\nLa suma es %d\n\n", suma);
	
	return 0;
}
