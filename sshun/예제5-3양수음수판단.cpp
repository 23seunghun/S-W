#include<stdio.h>

int main(void)
{
	int num;
	
	printf("����? ");
	scnaf("%d", &num);
	
	
	if(num<0)
		printf("�����Դϴ�.\n");
	else if(num > 0)
		printf("����Դϴ�.\n");
	 else
	 	printf("0�Դϴ�.\n");
}
