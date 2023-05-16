'''
2023.05.16
신승훈
파일 입출력-읽기(read)
'''

f=open("C:/data/text.txt","r") #파일 객체 생성/ft 모드 (읽기)

txts=f.read()

print(txts)

f.close