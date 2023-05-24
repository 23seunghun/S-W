'''
2023.05.24
신승훈
#문제정의
    score1.txt 파일을 읽어와서 각 학생의 등급을 결정하고
    결과를 report1.txt.파일에 저장하기
'''
score=[] #빈 리스트 변수 생성
f=open("C:/data/score1.txt","r") #읽기 객체 생성

for i in range(10): #10명의 학생 점수 읽어 오기
    score.append(f.readline().split()) #한 줄씩 읽어서 공백을 기준으로 나누고 score 리스트에 추가

for j in range(10): #10명의 점수에 대한 등급 계산을 반복하는것
    score[j][i]=float(score[j][i]) #문자열을 실수로 변환

    if score[j][i]>=90: #90이상이면
        score[j].append("A")
    elif score[j][i]>=80: #80에서 89사이면
        score[j].append("B")
    elif score[j][i]>=70: #70에서 79사이면
        score[j].append("C")
    else:
        score[j][i].append("D") #70미만이면

for i in range(10): #10명 등급 화면에 출력
    print("{:<5}{:<5}".format(score[i][0],score[i][2]))
f.close()