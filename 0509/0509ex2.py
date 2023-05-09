'''
2023.05.09
신승훈

#문제정의
    -1부터 100까지의 정수 중에서 사용자가 입력한 숫자의 배수만을 더하여 출력하는
    프로그램 for문을 작성하시오.

#문제분석
    변수-정수(num),합계(total)
#알고리즘
    1.변수 초기화
        num변수에 정수 입력
        total=0
    2.프로그램 논리(반복for)
        for i in range(num,1001,num):
            sum=sum+i
'''

num=int(input("합을 원하는 배수 입력"))
total=0 #합계

for i in range(num,1001,num): #반복조건
    total=total+i
    print("1~100까지의{}의 배수의 합계:{}".format(num,total))