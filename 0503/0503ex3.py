'''
2023.05.03 
신승훈

#문제정의
    1-입력받은 숫자의 합계 구하기

#문제분석
    1.변수-숫자(num),합계(total)
    2.수식  for i in range()
        score=score+i   
        i=i+1
#알고리즘
    1.변수선언
        num에 정수입력
        total=0
    2.논리
        (조건) for i in range(1,num+1):


        
    
    
'''

num=int(input("숫자 입력:"))
total=0

for i in range(1,num+1):
    total=total+i #합계

print('1~{}까지의 합계는 {}'.format(num,total))
