'''
2023.05.16
신승훈
파일 입출력 seek(0)
'''

f=open("C:/data/text.txt","r")

print(f.read(10),end='')
print(f.read(10),end='')
print(f.read(10))

f.seek(0)

print(f.read(10),end='')
print(f.read(10),end='')
print(f.read(10),end='')

f.close