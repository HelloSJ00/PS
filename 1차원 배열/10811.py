# 1차원 배열 바구니 뒤집기

import sys
input = sys.stdin.readline

N,M = map(int,input().split())

basket=[i+1 for i in range(N)]
for _ in range(M):
    i,j = map(int,input().split())
    # 뒤집는 알고리즘
    temp = basket[i-1:j]
    temp.reverse()
    basket = basket[:i-1] + temp + basket[j:]
    
print(*basket)

    