'''
2023.05.30
신승훈

#문제정의
    2차원 리스트의 각 줄의 합계를 구하고 리스트에서 가장 작은 값 찾기


'''

listl=[[11,33,22,7],[77,22,90],[3,66,44,9,8]]

minvlaue=min(listl(0)) #minvlaue에 리스트의 최솟값 초기화

for i in range(len(listl)): #listl의 길이만큼 반복
    print(i+"번째 줄의 합계:",sum(listl[i])) #각 줄의 합계

    if minvlaue>min(list[i]): #minvlaue와 리스트요소 비교
        minvlaue=min(listl[i] )

    print("리스트에서 가장 작은값:",minvlaue)


