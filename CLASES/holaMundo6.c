#include <stdio.h>

//Rangos de billar

int main(void){
	const unsigned int bInician = 1;
	const unsigned int bTerminan = 5;
	const unsigned int mInician = 6;
	const unsigned int mTerminan = 10;
	const unsigned int aInician = 11;
	const unsigned int aTerminan = 15;

	unsigned int bola;

	printf("Que numero de bola ingreso?:  ");
	scanf("%d", &bola);

	// &: ampersand. Sirve para "scanf"
	// &&: AND
	// ||: OR

	if((bola >= bInician) && (bola <= bTerminan)){
		printf("Bajas");
	}else if((bola >= mInician)&&(bola <= mTerminan)){
		printf("Medias");
	}else if((bola >= aInician) && (bola <= aTerminan)){
		printf("Altas");
	}else{
		printf("Usted no sabe jugar billar. Esa es la bola blanca!");
	}

	printf("\n\n"); 

	return 0;
}

