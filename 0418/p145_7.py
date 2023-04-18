'''
2023.04.18
신승훈
3장 연습문제 7번
두 정수 입력 x>y->x//y,  x<y->x+y,  x==y-> x*y
단, 나눗셈 몫 계산할 때 y는 0안됨
#문제분석
    변수:x=x y=y
    수식:x>y->x//y,  x<y->x+y,  x==y-> x*y
#알고리즘
    1.변수선언:x,y
    2.논리:
    if x>y:
        if y!=0:
            
        else: ("y는 0이 안됩니다.")
        
    elif x<y: 
        x+y

    else: x*y
    
'''

x=int(input("x값 입력:"))
y=int(input("y값 입력:"))

if x>y:
    if y!=0: 
        print("{}//{}={}".format(x,y,x//y))
    else:
        print("y의 값이 0입니다.")
elif x<y:
    print("{}+{}={}".format(x,y,x+y))
else:
    print("{}*{}={}".format(x,y,x*y))






