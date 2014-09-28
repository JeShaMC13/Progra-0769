/*Mas sobre procedimientos y funciones
	- Alcance de variables (LOCALES, GLOBALES)
*/

//Calculadora con menu

#include<stdio.h>

//Las funciones y procedimientos SIEMPRE
//se declaran antes de ser invocadas(os).


//Estas son variables de alcance GLOBAL
//Todas las funciones y procedimientos
//pueden leerlas y modificarlas
float data[2]; //Aqui se almacenaran los numeros que ingrese el usuario

long factorial(unsigned int n){ //Las funciones SIEMPRE devuelven algun tipo (int, char, float, etc.)
	unsigned int cont;
	long i;
	i = 1;
	for(cont=1; cont<=n; cont++){
		i*=cont;
	}
	return i; //Las funciones SIEMPRE deben retornar algo
}

long potencia(unsigned int base, unsigned int exp){
	unsigned int cont;
	long i;
	i=1;
	for(cont=0; cont<exp; cont++){
		i*=base;
	}
	return i;
}

void leerNumeros(unsigned int cant){ //Este es un procedimiento. Inicia con "void". No devuelve nada.
	//Vamos a acceder desde aqui a la variable (vector) global "data".
	int i;
	printf("\n");
	for(i=0; i<cant; i++){
		printf("Ingrese n%d: ", i+1);
		scanf("%f", &data[i]); //Aqui escribimos en la variable global "data"
	}
} //Es importante resltar que aqui no se debe colocar "return" al final, por ser un procedimiento

char menu(void){ //Si no uso ningun parametro, coloco "void"
	char op; //Es la opcion que elija el usuario
				 //"op" tambien es una variable LOCAL, ya que fue declarada
				 //dentro de la funcion "menu". Nadie mas puede acceder a ella
	op = ' ';
	printf("\n=================Calculadora v3.0=================\n\n");
	printf("1. Suma\n2. Resta\n3. Producto\n4. Cociente\n5. Factorial\n6. Potencia\n7. Salir");
	printf("\n\nSeleccione una opcion: ");
	scanf("%c", &op);
	return op;
}

void pausa(void){
	printf("\n\nPresione ENTER para continuar...");
	getchar(); //Vaciar el buffer
	getchar(); //Ejecutar getchar()
}

int main(void){
	char operacion;
	operacion = '0'; //Inicializamos en un valor, de tal forma que entre al ciclo WHILE
	while(operacion!='7'){
		operacion = menu();
		switch (operacion){
			case '1': //Si el usuario pide sumar
				leerNumeros(2); //Almacenamos 2 numeros en "data[0] y data[1]"
				printf("La suma es: %f", data[0]+data[1]); //Y los sumamos
				pausa();
				break;
			case '2': //Resta
				leerNumeros(2); //Se pide al usuario el minuendo y el sustraendo
				printf("La diferencia es: %f", data[0]-data[1]);
				pausa();
				break;
			case '3': //Producto
				leerNumeros(2); //Se pide al usuario ambos productos
				printf("El producto es: %f", data[0]*data[1]); //Y se multiplican
				pausa();
				break;
			case '4': //Cociente
				leerNumeros(2); //Se pide al usuario el dividendo y el divisor
				printf("El cociente es: %f", data[0]/data[1]);
				pausa();
				break;
			case '5': //Factorial
				leerNumeros(1); //Solamente se pide que ingrese un numero
				printf("El factorial es: %ld", factorial(data[0]));
				pausa();
				break;
			case '6': //Potencia
				leerNumeros(2); //Se pide la base y el exponente
				printf("La potencia es: %ld", potencia(data[0], data[1]));
				pausa();
				break;
			case '7': //Al salir...
				printf("\nAdios!\n\n");
				break;
			default: //Si la opcion elegida no es la correcta
				printf("\nSeleccione una opcion valida de la lista...");
		}
	}

	return 0;
}
