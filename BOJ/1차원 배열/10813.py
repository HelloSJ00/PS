# 1차원 배열 공바꾸기

import sys
input = sys.stdin.readline

N,M = map(int,input().split())

blanket=[i for i in range(N+1)]

for _ in range(M):
    i,j = map(int,input().split())
    temp = blanket[i]
    blanket[i]=blanket[j]
    blanket[j]=temp

for i in range(1,N+1):
    print(blanket[i],end=' ')