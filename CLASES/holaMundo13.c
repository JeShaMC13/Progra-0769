//Mas sobre ciclos WHILE
/*TAREA: Programar este juego de tal forma que el numero elegido
siempre sea aleatorio.*/


#include <stdio.h>

/*
Vamos tratar de adivinar un numero que la computadora
tiene almacenado de forma secreta (SECRETO=7). Pero ahora
el juego sera un poco mas dinamico. Le pediremos al usuario
que ingrese un numero, y le indicaremos si este es mayor o menor
al numero secreto. Si el usuario acerta, concluye el juego.
Tambien hay otro agregado, contaremos el numero de intentos
para ver que tan rapido se adivina. El que tenga el menor numero
de intentos es el ganador.

Ahora pensemos. Que tal si en vez de definir SECRETO como una constante,
lograramos que la computadora realmente creara un numero aleatorio?
Esto les queda de tarea a ustedes.
*/

#define SECRETO 7  //El famoso numero secreto

int temp; //El numero que ingrese el usuario
int intentos; //Vamos a contar los intentos que necesito el usuario para adivinar

int main(void){

	temp = -1; //Inicializamos temp para poder ejecutar el ciclo WHILE
	intentos = 1; //Iniciaremos con el intento #1

	printf("\n\nLet's play a game. Att, Jigsaw\n");
	printf("Ingrese un numero entre 1 y 20: ");
	scanf("%d", &temp);

	while(temp!=SECRETO){ //Ahora la condicion no es que un contador llegue a un limite
		intentos++;
		if(temp<SECRETO){
			printf("El numero que ingresaste es muy BAJO.\nIntento #%d: ", intentos);
		}else{
			printf("El numero que ingresaste es muy ALTO.\nIntento #%d: ", intentos);
		}
		scanf("%d", &temp);
		printf("\n");
	}
	printf("\nAcertaste en %d intentos! El numero secreto es %d\n\n", intentos, SECRETO);


	return 0;
}
