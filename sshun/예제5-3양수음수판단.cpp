#include<stdio.h>

int main(void)
{
	int num;
	
	printf("정수? ");
	scnaf("%d", &num);
	
	
	if(num<0)
		printf("음수입니다.\n");
	else if(num > 0)
		printf("양수입니다.\n");
	 else
	 	printf("0입니다.\n");
}
