'''
신승훈
2023.04.12
두 수 중 큰 수를 출력받는 프로그램
#문제분석
    변수-숫자1(num1),숫자2(num2)
#알고리즘
    1.변수선언
        num1,num2에 정수입력
    2.논리(선택)
        if num1>num2:
            (참)큰 수는:num1 , 작은 수는:num2
        else
            (거짓)큰 수는:num2, 작은 수는:num1
'''

num1=int(input('첫 번째 숫자 입력:'))#숫자1 변수정수로 입력받기
num2=int(input('두 번쨰 숫자 입력:'))#숫자2 변수정수로 압력받기
if num1>num2:
    print("두 수 중에 큰 수는 {}, 작은 수는 {} 이다. ".format(num1,num2)) #조건 참
else:
    print("두 수 중에 큰 수는 {}, 작은 수는 {} 이다. ".format(num2,num1)) #조건 거짓