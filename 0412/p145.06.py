'''
2023.04.12
신승훈



#문제분석
    
    변수-숫자1(num),숫자2(num2)
    수식-num1%2==0 (num1은 짝수)/ num1%2|=0 (num1은 홀수) 
'''

num1=int(input("첫 번째 숫자 입력:"))
num2=int(input("두 번째 숫자 입력:"))
if num1%2==0 and num2%2==0:
    print(num1+num2)
elif num1%2==1 and num2%2==0:
    print("첫번째 숫자를 짝수로 입력하세요.")
elif num1%2==0 and num2%2==1:
    print("두번째 숫자를 짝수로 입력하세요.")
else:
    print("두 숫자 모두를 짝수로 입력하세요")