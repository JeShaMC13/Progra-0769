//Matrices y ciclos: ya se va poniendo interesante...
//Las matrices son vectores de más de 1 dimensión

#include <stdio.h>

#define ALUMNOS 3
#define CURSOS 5

//Aqui almacenaremos cada una de las notas de todos los alumnos
unsigned int notas[ALUMNOS][CURSOS]; //Cada alumno esta llevando 5 cursos


int main(void){
	unsigned int i, j; //Contadores para nuestros ciclos
	
	for(i=0; i<ALUMNOS; i++){ //Recorreremos las filas
		printf("\n----------Alumno %d----------\n", i+1);
		for(j=0; j<CURSOS; j++){ //Y ahora, cada una de las columnas de cada fila
			printf("Ingrese nota de curso %d: ", j+1);
			scanf("%d", &notas[i][j]);
		}
	}
	
	printf("\n");
	
	for(i=0; i<ALUMNOS; i++){ //Cada uno de los alumnos es una fila
		printf("\nAlumno %d: ", i+1);
		for(j=0; j<CURSOS; j++){ //Y cada curso es una columna
			printf("%d ", notas[i][j]); 
		}
	}
	
	printf("\n\n");
	
	return 0;
}
