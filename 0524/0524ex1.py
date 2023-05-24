'''
2023.05.24
신승훈

#문제정의
    p247 1번문제
'''
import random #난무 모듈 추가
with open("C:/data/num.txt","w") as f:#파일 객체
    for i in range(5): #줄 반복
        for j in range(5): #랜덤수 찍기반복
                f.write(str(random.randint(1,100))) #랜덤 수 파일에 쓰기
                f.write(' ') #숫자 다음 공백 찍기
        f.write('\n') #줄 바꿈

with open("c:/data/num.txt",'r') as f1: #읽기 파일 객체
    with open("c:/data/avg.txt","w") as f2: #쓰기 파일 객체
        
        j=0
        while True: #무한반복
            j=j+1 #번 앞에 숫자 추가
            score=f1.readline() #num.txt 한 줄 읽어 오기
            if score=='':#내용이 없으면
                break
            scorelist=score.split() #읽어 온 한 줄을 공백 기준 리스트로

            sum=0 #합계
            for i in range(5): #한 학생당 5과목 점수 더하기
                sum=sum+int(scorelist[i]) #리스트 항목 더 하기
            print(j,"번 학생의 평균",sum/5,file=f2) #결과 파일에 작성
                    
                     


