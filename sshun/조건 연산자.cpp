#include<stdio.h>

int main(void)
{
	int a,b,c;
	int num1;
	
	printf("세 개의 정수를 입력:");
	scanf("%d %d %d", &a ,&b ,&c);
	
	num1 = a<b ? a: b;
	num1 = c < num1 ? c : num1;
	printf("가장 작은 수 : %d",num1);
	return 0;
}
