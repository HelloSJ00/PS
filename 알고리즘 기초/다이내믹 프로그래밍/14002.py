# 가장 긴 증가하는 부분 수열 4

import sys
input = sys.stdin.readline

N = int(input())
numList = list(map(int,input().split()))
answerList = []
dp = [1]*(N+1)

for i in range(1,N):
    tmpList = [] 
    for j in range(0,i):
        if numList[j] < numList[i]:
            if dp[i] < dp[j]+1:
                tmpList.append(numList[j])
                dp[i] = dp[j]+1
                
            if j == i-1:
                tmpList.append(numList[i])

    if dp[i] != max(dp):
        answerList = tmpList 

    
            
print(max(dp))
print(*answerList)
