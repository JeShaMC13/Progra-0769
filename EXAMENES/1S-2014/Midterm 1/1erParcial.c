#include <stdio.h>

const int entrada[8][3] = {  //Tabla con los datos iniciales (A, B, C)
							{0,0,0},
							{0,0,1},
							{0,1,0},
							{0,1,1},
							{1,0,0},
							{1,0,1},
							{1,1,0},
							{1,1,1}
						};
int resulta[8]; //Aqui se almacenara resultado de la operacion

int and(int a, int b){ //Compuerta AND
	if(a==1 && b==1){
		return 1;
	}else{
		return 0;
	}
}

int or(int a, int b){ //Compuerta OR
	if(a==0 && b==0){
		return 0;
	}else{
		return 1;
	}
}

int not(int a){ //Compuerta NOT
	return a==1?0:1; //Operador ternario :)
	
	/*
	La linea de arriba es equivalente a:
	if(a==1){
		return 0;
	}else{
		return 1;
	}
	*/
}

void despliegaTablaInicial(void){ //Mostrar elegantemente la tabla inicial de datos
	int x, y;
	
	printf("\n\n");

	printf("Ivan Rene Morales - 200815521");
	
	printf("\n|A|B|C|\n=======");
	for(x=0; x<8; x++){
		printf("\n|");
		for(y=0; y<3; y++){
			printf("%d|", entrada[x][y]);
		}
	}
	printf("\n\n");
	
}

void miFuncion(void){ //Ejecutar mi funcion asignada. Mi carnet termina en "1"
	int x;
	for(x=0; x<8; x++){ //Cada una de las combinaciones de la tabla inicial
		resulta[x] = and(not(and(entrada[x][0],entrada[x][1])),or(entrada[x][1],entrada[x][2]));  
		// La funcion logica a ejecutarse es: (~(A*B))*(B+C)
		// ~: NOT
		// *: AND
		// +: OR
	}
}

void despliegaResultado(){
	int x;
	printf("|x|\n==="); //Encabezado
	for(x=0; x<8; x++){
		printf("\n|%d|",resulta[x]); //Mostrar c/u de los elementos del resultado
	}
	printf("\n***");
	printf("\n");
}

int main(void){
	despliegaTablaInicial(); //Mostrar mi carnet y la tabla inicial
	miFuncion(); //Ejecutar la funcion booleana asignada
	despliegaResultado(); //Mostrar el resultado de la funcion, luego
						  //de haber sido aplicada a todas las combinaciones
						  //de la tabla inicial
	return 0;
}
