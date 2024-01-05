# 백트래킹 N과 M (4)

import sys
input = sys.stdin.readline

N,M = map(int,input().split())

rs=[0]

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
        if i >= rs[len(rs)-1]:
            rs.append(i)
            recur(num+1)
            rs.pop()

recur(0)