'''
2023.05.09
신승훈

#문제정의
    1~100까지의 입력받은 숫자의 배수의 합계
#문제분석
    변수-정수(num) 합계(sum) 반복변수(i)
#알고리즘
    1.변수 초기화
        num 변수에 정수입력
        sum=0
        i=0
    2.논리(반복 안에 선택 포함-while,if)
        while i<=100:
            i=i+1
            if i 가 num의 배수가 아니면
                continue
            sum=num+i      
'''

num=int(input("배수 숫자 입력:"))
sum=0
i=0

while i<=100: #선택조건
    i=i+1
    if i%num 1=0 #선택조건 (1가 num의 배수가 아니면)
        continue
    sum