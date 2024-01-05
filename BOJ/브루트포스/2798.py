# 브루트 포스 블랙잭
import sys

N , M = map(int,sys.stdin.readline().split())
num_list = list(map(int,sys.stdin.readline().split()))

idx = [0,1,2]

sum= 0
while sum != M:
    # 브루트 포스
    temp =num_list[idx[0]] +num_list[idx[1]] + num_list[idx[2]] # 더한값 저장
    if temp <= M and sum < temp:
        sum = temp  
    # idx 변화
    if idx[2] <= N-2:
        idx[2]+=1
    elif idx[2] == N-1 :
        if idx[1] <= N-3:
            idx[1]+=1
            idx[2] = idx[1]+1
        elif idx[1] == N-2:
            if idx[0] <= N-4:
                idx[0] +=1
                idx[1] = idx[0]+1
                idx[2] = idx[1]+1
            elif idx[0] == N-3:
                break

    if sum == M:
        break
print(sum)




