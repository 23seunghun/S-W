'''
2023.05.09
신승훈

#문제정의
    -두 개의 숫자를 입력받아 두 수 사이의 모든 정수값을 더하여 출력하는 프로그램을 작성하시오.

#문제분석
    변수-정수1(num1) 정수2(num2) 합계(sum) 임시변수(temp) 반복횟수(i)

#알고리즘    
    1.변수 선언(변수 초기화)
        num1,num2는 정수를 입력받는다.
        temp=0,temp=0
    2.프로그램 논리(선택,반복)
        2-1.(선택조건), 항상num1<=num2
            if num1>=num2:
                num1, num2
        2-2.(반복) - num1-num2까지 1씩 증가하면서 더하기
            i=num1
            while i<=num1:
                sum = sum +i
                i=i+1
'''

num1=int(input("첫 번째 숫자:"))
num2=int(input("두 번쨰 숫자:"))
sum=0
temp=0

if num1>num2: #선택조건
    temp=num1 #num1값을 temp에 저장해라
    num1=num2 #temp값을 num1 에 저장해라
    num2=temp #tpmp값을 num2에 저장해라

i=num1 #i num1로 초기화
while i<=num2: #반복조건
    sum=sum+i #합계구하기
    i=i+1 #i 1씩 증가

print("{}~{}까지의 합계는 {}".format(num1,num2,sum))
