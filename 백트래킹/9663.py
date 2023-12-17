# 백트래킹 N-Queen 
'''
1. 아이디어 
- 2차원 배열로 check 배열 
2. 시간복잡도
3. 자료구조 
'''
import sys
input = sys.stdin.readline

'''
N = int(input())

check = [[0]*N]*N 
Queen = [[False]*N]*N
cnt = 0

def 

def recur(num):
    if num == N:
        global cnt
        cnt +=1
        return 
    
    for i in range(N):
        for j in range(N): # 퀸 놓기
            if check[i][j] == 0:
                check[i][j] = 1 # 퀸의 위치

                for k in range(N): # 퀸의 양옆 , 위아래 check
                    check[i][k] = 1
                    check[k][j] = 1
                p = 0
                while p+i < 9 or j-p >= 0: # 대각선 
                    check[p+i][j-p] = 1
                q = 0
                while q+i < 9 or q+j < 9: # 대각선
                    check[q+i][q+j] = 1
                recur(num+1)
                check[i][j] = 0
                for k in range(N): # 퀸의 양옆 , 위아래 check
                    check[i][k] = 0
                    check[k][j] = 0
                while p+i < 9 or j-p >= 0: # 대각선 
                    check[p+i][j-p] = 0
                q = 0
                while q+i < 9 or q+j < 9: # 대각선
                    check[q+i][q+j] = 0
'''

N = int(input())
col = [0]*(N+1)
cnt = 0
def promising(i,col):
    k =1
    flag = True
    while( k < i and flag):
        if col[i] == col[k] or abs(col[i]-col[k]) == (i-k) :
            flag = False
        k +=1
    return flag

def n_queens(i,col): 
    n = len(col) - 1
    if promising(i,col) :
        if i == n:
            global cnt
            cnt+=1
        else:
            for j in range(1,n+1):
                col[i+1] = j
                n_queens(i+1,col)

n_queens(0,col)
print(cnt)


                
                
            

