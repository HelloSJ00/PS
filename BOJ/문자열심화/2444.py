#문자열 심화 별찍기 - 7

import sys
input = sys.stdin.readline

N = int(input())
P = 1
K = 1
while P != 0:
    for i in range(N-P):
        print(' ',end='')
    
    for j in range(2*P-1):
        if j != 2*(P-1):
            print('*',end='')
        else:
            print('*')
    

    #증감 조절
    if P == N:
        K= -1

    if K == 1:
        P +=1
    else : 
        P -=1