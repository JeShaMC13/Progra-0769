#include <stdio.h>

const unsigned int magicNumber = 3;

unsigned int n;

int main(void){
	
	printf("Adivine el numero magico. Es entre 0 y 9: ");
	scanf("%d", &n);
	
	if(n < magicNumber){
		printf("\n\nEl numero ingresado es menor al magico");
	}else if(n > magicNumber){
		printf("\n\nEl numero ingresado es mayor al magico");
	}else{
		printf("\n\nAdivinaste. %d es el numero magico", n);
	}

	return 0;
}
