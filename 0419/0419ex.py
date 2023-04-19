'''
2023.04.19
신승훈
p141 4번
조건문을 사용하여 입력된 수가 양수, 0, 음수인지 판별하는 프로그램을 두 가지 형태인 단순 if문 형태와 이중 if문 형태로 작성하시오.


#문제분석
    변수: 정수 (num)    
    수식: 
        num>0 양수
        num<0 음수

#알고리즘 (단순if)
    1.변수 선언
        num에 정수 입력
    2.논리(선택):
        if num>0:
            "양수"
        if num<0:
            "음수"
        if num==0
            "0"
#알고리즘(다중 if)
    1.변수 선언
        num에 정수 입력
    2.논리(선택):
        if num>0:
            "양수"
        elif num<0:
            "음수"
        else:
            "0"

'''

#단순if
num=int(input("숫자 입력:"))
if num>0:
    print("입력값 {}은 양수 입니다.".format(num))
if num<0:
    print("입력값 {}은 음수 입니다.".format(num))
if num==0:
    print("입력값 {}은 0 입니다.".format(num))

#다중if
num=int(input("숫자 입력:"))
if num>0:
    print("입력값 {}은 양수 입니다.".format(num))