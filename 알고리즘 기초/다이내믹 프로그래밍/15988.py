# 1,2,3 더하기 3

import sys
input = sys.stdin.readline

TC = int(input())

for _ in range(TC):
    N = int(input())
    dp = [0] * 5
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    dp[4] = 7

    for i in range(5,N+1):
        dp.append((dp[i-3] + dp[i-2] + dp[i-1])%1000000009)
    print(dp[N])

import sys
input = sys.stdin.readline

dp = [1,2,4,7]
for i in range(int(input())):
    n = int(input())
    for j in range(len(dp), n):
        dp.append((dp[-3]+dp[-2]+dp[-1])%1000000009)
    print(dp[n-1])
