'''
2023.05.10
신승훈

#문제정의
    정수를 반복적으로 입력받아 정수의 합이 1000이상이 되었을 때의 결과값과 평균을 구하여 다음과 같이 출력하는 프로그램을 작성.
#문제분석
    변수-합계(sum),입력횟수(cnt),평균(avg)

#알고리즘
    1.변수 초기화
        num 키보드로 입력
        sum=0,cnt=0,avg=0
    2.논리(반복안에 선택 포함)
        (반복)while True: #무한반복
            num 키보드로 입력:
            cnt 1증가
            sum에 더하기
            (선택) if sum>=1000:
                        break

    3.합계,평균 출력
'''

sum=0
cnt=0
avg=0

while True: #무한반복
    num=int(input("숫자 입력:"))
    cnt+=1  #cnt 1출력
    sum += num  #합계
    if sum>=1000: #선택조건
        break  #반복종료

avg=sum/cnt #평균계산

print("1000을 넘은수:%d"%sum, end=" ")
print("평균:%.2f"%avg)
