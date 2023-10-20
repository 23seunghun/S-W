#include <stdio.h>
#include <stdlib.h>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char *argv[]) {
	int num10;
	char s[10];

	
	printf("please the number:");
	scanf("%d",&num10);
	
	char numC=num10+'0';
	
	itoa(num10,s,2);
	printf("%d's binary is 0%s\n",num10,s);
	printf("%d's octal is %#o\n",num10,num10);
	printf("%d's hexadecimal is %#x\n",num10,num10);
	printf("%d's character value is %c",num10,numC);
	
	return 0;
}
