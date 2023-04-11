'''
2023.04.05
신승훈
5과목 점수 입력받아서 출력
p117 14번 문제 풀기
'''
#변수선언
sub1=int(input('과목1:'))
sub2=int(input('과목2:'))
sub3=int(input('과목3:'))
sub4=int(input('과목4:'))
sub5=int(input('과목5:'))

total=sub1+sub2+sub3+sub4+sub5
avg=total/5

print('5과목의 합계는{}이고, 평균은 {}이다'.format(total,avg))



