#include<stdio.h>

int main(void)
{
	int kor, eng, math, avg;
	printf("�� ������ ���� �Է�(����, ����, ����) : ");
	scanf("%d %d %d", &kor, &eng, &math);
	
	avg=(kor+eng+math)/3;
	printf("�� ������ ��� : %d\n\n", avg);
	// 
	if(kor>=40 && eng >=40 && math>= 40 && avg>=60)
		printf("�հ�");
	else
		printf("���հ�"); 
	
		
}
