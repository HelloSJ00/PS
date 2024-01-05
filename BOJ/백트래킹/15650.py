# 백트래킹 N과 M(2)

import sys
input = sys.stdin.readline

N,M = map(int,input().split())
rs = [0] 
check = [False] * (N+1)

def recur(num):
    if num == M:
        #print
        for i in range(1,M+1):
            if i != M:
                print(rs[i],end=' ')
            else:
                print(rs[i])
        return
    for i in range(1,N+1):
        if check[i] == False and rs[len(rs)-1] < i:
            check[i] = True
            rs.append(i)
            recur(num+1)
            check[i] = False
            rs.pop()

recur(0)
            
