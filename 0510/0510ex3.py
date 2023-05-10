'''
2023.05.10
신승훈

#문제정의
    사용자로부터 하나의 숫자를 입력받아 다음과같이 *을 출력하는 프로그램을 작성
#문제분석
    변수-숫자(num)
#알고리즘
    1.변수 초기화
        num에 변수 입력
    2.논리(중첩,반복)
        (반복)for i in range(1,num+1): #줄바꿈
            (반복) for j in range(1,i+1): #별 찍기 반복
                별 찍기

'''

num=int(input('숫자 입력:'))

for i in range(1,num+1):
    for j in range(1,i+1):
        print("*",end="")
    print() #줄바꿈


#거꾸로 출력

num1=int(input("숫자입력:"))
print("\n 거꾸로 출력")
for i in range(1,num1+1):
    for j in range(i,num1+1):
        print("*",end=" ")
    print() #줄바꿈
    

