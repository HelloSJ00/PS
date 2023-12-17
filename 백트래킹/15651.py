#  백트래킹 N과M(3)

import sys
input= sys.stdin.readline

N,M = map(int,input().split())

rs= []
def recur(num):
    if num == M:
        for i in range(M):
            if i != M-1:
                print(rs[i],end=' ')
            else:
                print(rs[i])
        return
    
    for i in range(1,N+1):
        rs.append(i)
        recur(num+1)
        rs.pop()

recur(0)