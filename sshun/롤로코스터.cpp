#include <stdio.h>

int main(void)
{
	int age, ki;
	printf("���̸� �Է��� �ּ���:");
	scanf("%d" , &age);
	printf("Ű�� �Է��� �ּ���:");
	scanf("%d" , &ki);
	
	if (age >= 9){
		if(ki >= 130)
			printf("��ӷѷ��ڽ��� ���� ����");
		else
			printf("���� �ѷ��ڽ��� ���� ����");
	}
	else
		printf("����Ұ�");
}
