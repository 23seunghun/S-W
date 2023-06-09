'''
2023.05.23
신승훈

#문제 정의
    stu,txt 파일을 읽어서 각 학생의 평균 성적 계산해서 출력하기
#문제 분석
    변수-한줄씩 읽어서 저장 (score),
         리스트 자료로 변환하기 위해서 (scorelist)
         리스트에서 이름 항목을 저장하기 위해서(name)
         세 과목의 합계를 구하기 위해서(sum)

#알고리즘
    1.파일열기 (쓰기모드)
    2.파일 처리
        2-1(반복)while True:
            한 줄 읽어서score저장
            읽어온 내용을 리스트로 변환해서scorelist 저장
            scorelist에서 첫 번쨰 항목(이름)을 name에 저장
            (반복) for i in range(1,4)
                    socrelist의 1,2,3항목의 값을 sum에 더하기
    3.파일닫기

'''

f=open("c:/data/stu.txt",'r') #읽기모드 파일 객체 생성
while True: #무한반복
    score=f.readline() #한 줄씩 읽어 오기
    if score=='': #더 이상 읽어 올 내용이 없다면
        break #반복 종료

    scorelist=score.split()#리스트 자료로 변환
    name=scorelist[0] #리스트 천번째 항목은 이름


    sum=0 #합계

    for i in range(1,4): #1,2,3 을 더함
        sum=sum+scorelist[i]

    print(name,"의 평균 성적은:",sum/3)
    f.close() #파일 닫기


