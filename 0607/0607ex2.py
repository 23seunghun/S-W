'''
2023.06.07
신승훈
#문제정의
    로또 만들기
#문제분석
    변수-LOTTO
#알고리즘
    1.랜덤모듈 추가
    2.lotto(set변수) 생성
    3.반복(무한반복)
        while True:
            lotto=랜덤 수 6개 추가
            li len(lotto)==6
                break
    4.생성된 로또번호
'''

import random #난수 발생을 위한 random 모듈 포함

lotto = set    #비어있는 세트 lotto 선언
i=0
while True :    #무한 반복
    lotto.add(random.randint(1,45)) 


    i=i+1 #난수 발생 횟수 저장
    if len(lotto)==6: #난수가 6개가 되는 경우 반복 종료
        break
print("이번주 로또 넘버:",sorted(lotto)) #sorted() 함수를 이용하여 오름차순으로 정렬된 숫자 출력

print("중복된 난수의 발생 횟수:",i-6) #중복 횟수 출력