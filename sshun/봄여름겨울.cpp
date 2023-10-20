#include<stdio.h>

int main(void)
{
	int num;
	printf("좋아하는 달(월)을 쓰세요 : \n");
	scanf("%d", &num);
	
	switch (num)
	
	{
		case 12: case 1: case 2:
			printf("입력하신 달(월)은 겨울입니다.");
			break;
		case 3: case 4: case 5:
			printf("입력하신 달(월)은 봄 입니다.");
			break;
		case 6: case 7: case 8:
			printf("입력하신 달(월)은 여름입니다.");
			break;
		case 9: case 10: case 11:
			printf("입력하신 달(월)은 가을입니다.");
			break;
		default;
			printf("달(월)을 잘못 입력하셨습니다.")
			break;
	}
	
}
