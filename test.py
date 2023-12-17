# 1,2,3 더하기 5

import sys
input = sys.stdin.readline



dp = [[0]*4 for _ in range(5)]

dp[1][1] = 1 # dp[1] = [0,1,0,0]
dp[2][2] = 1 # dp[2] = [0,0,1,0]
dp[3][1] = 1 # dp[3] = [0,1,1,1]
dp[3][2] = 1
dp[3][3] = 1 
print(dp[1])
print(dp[2])
print(dp[3])


dp[4][1] = dp[3][2]+dp[3][3]
dp[4][2] = dp[2][1] + dp[2][3]
        
dp[4][3] = dp[1][1]+dp[1][2]
        

# print(dp[4][1],dp[4][2],dp[4][3])