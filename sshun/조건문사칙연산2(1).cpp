#include<stdio.h>

int main(void)

{
	int opt;
	double num1, num2;
	double result;
	
	printf("1.���� 2.���� 3.���� 4.������ \n");
	printf("����?");
	scanf("%d", &opt);
	printf("ù ��° ���� �Է�:");
	scanf("%lf", &num1);
	printf("�� ���� ���� �Է�:");
	scanf("%lf", &num2);
	if (opt==1)
		result = num1 + num2 ;
	else if (opt==2)
		result = num1 - num2 ;
	else if (opt==3)
		result = num1 * num2 ;
	else 
		result = num1 / num2 ;
		
	printf("���: %g \n",result);
	return 0;
}
