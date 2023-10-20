#include<stdio.h>

int main(void)
{
	int kor, eng, math, avg;
	printf("세 과목의 점수 입력(국어, 영어, 수학) : ");
	scanf("%d %d %d", &kor, &eng, &math);
	
	avg=(kor+eng+math)/3;
	printf("세 과목의 평균 : %d\n\n", avg);
	// 
	if(kor>=40 && eng >=40 && math>= 40 && avg>=60)
		printf("합격");
	else
		printf("불합격"); 
	
		
}
