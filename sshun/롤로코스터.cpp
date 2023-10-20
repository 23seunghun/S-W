#include <stdio.h>

int main(void)
{
	int age, ki;
	printf("나이를 입력해 주세요:");
	scanf("%d" , &age);
	printf("키를 입력해 주세요:");
	scanf("%d" , &ki);
	
	if (age >= 9){
		if(ki >= 130)
			printf("고속롤러코스터 입장 가능");
		else
			printf("저속 롤러코스터 입장 가능");
	}
	else
		printf("입장불가");
}
