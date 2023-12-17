# 체스판 다시 칠하기 

import sys
input = sys.stdin.readline

M,N = map(int,input().split())

startPosition=[[0]*N-7 for i in range(M-7)]

for _ in range(M):
    chessRow = list(input())
    for i in range(M-7):
        for j in range(i,i+8):
            if chessRow[j] == 'B':
                



# for _ in range(N):
#     tmpList = list(input())
#     for i in range(M):
#         if tmpList[i] == 'B':
#             bNum +=1
#         else:
#             wNum +=1

# if 32-bNum > 0:
#     needBlack = 32-bNum
# else:
#     needBlack = 0

# if 32-wNum >0:
#     needWhite = 32 -wNum
# else:
#     needWhite = 0

# print(needWhite + needBlack)