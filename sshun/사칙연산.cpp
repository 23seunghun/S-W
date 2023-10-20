#include <stdio.h>

int main()
{
	int num1, num2;
	printf("두 개의 수 입력:");
	scanf("%d %d", &num1,&num2); 
	
	printf("%d + %d = %d\n",num1 , num2, num1+num2);
	printf("%d - %d = %d\n",num1 , num2, num1-num2);
	printf("%d * %d = %d\n",num1 , num2, num1*num2);
	printf("%d / %d = %.3f\n",num1 , num2, (float)num1/num2);aa
	printf("%d %% %d = %d\n",num1 , num2, num1%num2);
	return 0;
}
