#include<stdio.h>

int main(void)
{
	int num;
	printf("�����ϴ� ��(��)�� ������ : \n");
	scanf("%d", &num);
	
	switch (num)
	
	{
		case 12: case 1: case 2:
			printf("�Է��Ͻ� ��(��)�� �ܿ��Դϴ�.");
			break;
		case 3: case 4: case 5:
			printf("�Է��Ͻ� ��(��)�� �� �Դϴ�.");
			break;
		case 6: case 7: case 8:
			printf("�Է��Ͻ� ��(��)�� �����Դϴ�.");
			break;
		case 9: case 10: case 11:
			printf("�Է��Ͻ� ��(��)�� �����Դϴ�.");
			break;
		default;
			printf("��(��)�� �߸� �Է��ϼ̽��ϴ�.")
			break;
	}
	
}
