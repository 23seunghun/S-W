#include<stdio.h>

int main(void)
{
	int a,b,c;
	int num1;
	
	printf("�� ���� ������ �Է�:");
	scanf("%d %d %d", &a ,&b ,&c);
	
	num1 = a<b ? a: b;
	num1 = c < num1 ? c : num1;
	printf("���� ���� �� : %d",num1);
	return 0;
}
