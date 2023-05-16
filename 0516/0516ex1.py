'''
2023.05.16
신승훈
파일 입출력
'''

ft=open("C:/data/text.txt","w") #파일 객체 생성/ft 모드 (읽기 모드)

for i in range(1,11): #10번 반복
    ft.write("%d번째 줄 입니다.\n"%i) #ft에 i 출력

ft.close() #파일종료