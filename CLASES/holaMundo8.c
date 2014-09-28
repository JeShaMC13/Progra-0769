//Operador MOD
//Operador ternario

#include<stdio.h>

/*

	if(a>=5){
		b=1;
	}else{
		b=0;
	}

	Version simple:	
	b = (a>=5?1:2);

*/

unsigned int a; //Numero a evaluar
unsigned int b; //Resultado. Si es par: 1; si es impar: 0

int main(void){
	printf("\nNumero mayor a 0: ");
	scanf("%d", &a);
		
	if(a%2==0){
		b=1;
	}else{
		b=0;
	}
	
	//b = ((a%2==0)?1:0);
	
	printf("0: impar, 1: par ====>  %d\n\n", b);
	
	return 0;
}

