'''
2023.05.31
신승훈
#문제정의
    튜플안에 있는 숫자들의 종류와 반복 갯수 분석하기
#문제분석
    변수-    

'''

num=(1,4,6,5,4,3,2,0,1,2,4,6,7,9,4,0)
print("생성된 튜플:",num)

a_list=[] #중복 출력 하지 않기 위한 빈 리스트 생성

for i in range(len(num)): #튜플 길이 만큼 반복

    if num[i] not in a_list: #리스트에 없는 경우만 출력
        print(num[i],"개수:",num.count(num[i])) #개수 출력
        a_list.append(num[i])   #리스트에 추가