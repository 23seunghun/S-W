#while 반복문

i=1             #반복 횟수 초기화
sum=0           #합계
while i<=10:    #반복조건
    sum=sum+i   #합계저장
    i=i+1       #i 1증가
print('1~10까지의 합계:',sum)


print() #줄 띄우기  

#for 반복문

i=1
sum1=0
for j in range(1,56):
    sum1=sum1+1
    #j=j+1 안해도됨
print('1~10까지의 합계:',sum1)
    