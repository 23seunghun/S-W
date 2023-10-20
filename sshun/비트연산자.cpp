#include <stdio.h>

int main(void)

{
	int n1,n2;
	
	printf("두 수 입력(단 한자리 수로)");
	scanf("%d %d",&n1,&n2);
	
	printf("%d & %d = %d\n", n1,n2, n1&n2);
	printf("%d | %d = %d\n", n1,n2, n1|n2);
	printf("%d ^ %d = %d\n", n1,n2, n1^n2);
	
	return 0;
	
	
}
