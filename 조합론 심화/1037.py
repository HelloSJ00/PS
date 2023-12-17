# 조합론 심화 약수

import sys

cnt = int(sys.stdin.readline()) # 약수의 개수
nums = list(map(int,sys.stdin.readline().split())) # 약수들
nums.sort() #오름차순 정렬

anwser = nums[0] * nums[len(nums)-1]
print(anwser)


