#include <stdio.h>
#include <stdlib.h>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */
int num[5];

int main(int argc, char *argv[]) {
	printf("please tape the numer:");
	for(int i=0;i<5,i++) scanf("%d",&num[i]);
	
	
	printnumbers();
	printf("the max number is %d\n",findmax(num,5));
	printf("the max number is %d\n",findmin(num,5));
	printf("the max number is %d\n",total(num,5));
	
	
	return 0;
}

void printnumbers(int *arr,int size){
	printf("the number you tape is ");
	for(int i=0;i<size;i++)printf("%d",arr[i]);
	printf("/n");
}

int findmax(int *arr,int size){
	int max=arr[0];
	for (int i=1;i<size;i++) if (arr[i]>max) max=arr[i];
	return max;
}

int findmin(int *arr,int size){
	int min=arr[0];
	for (int i=1;i<size;i++) if (arr[i]<min) min=arr[i];
	return min;
}

int total(int *arr,int size){
	int total;
	for(int i=0;i<size;i++)total+=arr[i];
	return total;
}

