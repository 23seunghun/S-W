'''2023.04.11
신승훈
선택문-elif~else
성적이 90이상이면 'A',80이상 90미만 이면 'B'
70이상 80미만이면 'C' 70미만이면 'F'

'''
score=int(input("점수 입력:"))
if score>=90: #조건1
    print("A학점") #조건이1이 참인 경우 출력
elif score>80: #조건2
    print("B학점") #조건2가 참인 경우 출력
elif score>=70:
    print("C학점") #조건3이 참인 경우 출력
else:
    print("F학점") #조건1,2,3 이 모두 거짓일 경우 출력
    