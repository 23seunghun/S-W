'''
2023.05.16
신승훈 
파일 입출력-writelines
'''
L1=['충청남도','충청북도\n','전라북도\n','경상남도','경상북도']

L2=[1,2,3,4,5]

with open("C:/datatest.txt","w")as f:
    
    f.writelines(L1)
