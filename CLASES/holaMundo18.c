//Manejo de cadenas de caracteres (Strings)

#include<stdio.h>
#include<string.h>

#define TXT_LEN 50

char texto0[TXT_LEN]; //Una cadena de caracteres forma un string
char texto1[TXT_LEN]; 
char texto2[TXT_LEN];
char texto3[2*TXT_LEN]; //Aqui se concatenara el texto 1 y el texto 2
char texto4[2*TXT_LEN]; //Aqui se concatenara parte del texto 1 y el texto 2
unsigned int cant;

int main(void){

	printf("\nIngrese texto 1: ");
	scanf("%s", texto1); //Note que el scanf no requiere derreferenciacion(&)
	printf("Texto1 ingresado: %s\n", texto1);
	
	printf("\nIngrese texto 2: ");
	scanf("%s", texto2);
	printf("Texto2 ingresado: %s\n\n", texto2);

	printf("No se puede igualar directamente un string con otro. Por ejemplo:\n");
	printf("texto0 = texto1  es una operacion invalida, porque son vectores.\n\n");

	printf("En vez de eso, se utiliza la funcion \"strcpy\":\n");
	printf("strcpy(texto0, texto1);\n\n");
	strcpy(texto0, texto1);

	printf("Ahora \"texto0\" vale: %s", texto0);


	//Concatenar significa unir dos o mas textos
	strcat(texto3, texto1); //Agregar (concatenar) al texto3 el valor de texto1
	strcat(texto3, texto2); //Agregar al texto3 el valor de texto2

	printf("\n\n\n\n\nAl utilizar la sentencia \"strcat\":\n");
	printf("\nTexto concatenado: %s\n\n", texto3);	

	printf("\nSi se desea concatenar solo una parte de un texto");
	printf("\nse utiliza la instruccion \"strncat\".\n\n");

	printf("Cuantos caracteres de \"texto2\" desea agregar al final de \"texto1\"?:  ");
	scanf("%u", &cant);

	strcat(texto4, texto1);
	strncat(texto4, texto2, cant);

	printf("\nResultado: %s\n\n", texto4);

	return 0;
}