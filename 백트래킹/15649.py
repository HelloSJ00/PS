#   백트래킹 N 과 M
'''
1.  아이디어 
- 백트래킹 재귀함수 안에서, for 돌면서 숫자 선택( 이때 방문여부 확인)
- 재귀함수에서 m개를 선택할 경우 print
2. 시간복잡도
중복 아니니 N!
3. 자료구조
- 결과값 저장 배열 
- 방문여부 확인 배열
'''

import sys
input = sys.stdin.readline

N,M = map(int,input().split())
rs = [] 
check = [False] * (N+1)

def recur(num):
    if num == M:
        for i in range(M):
            if i == M-1:
                print(rs[i])
            else:
                print(rs[i],end=' ') # print(' '.join(map(str,rs)))
        return
    for i in range(1,N+1):
        if check[i] == False:
            check[i] = True
            rs.append(i)
            recur(num+1)
            check[i] = False
            rs.pop()
recur(0)