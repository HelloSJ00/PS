# 문자열심화 팰린드롬인지 확인하기

import sys
input = sys.stdin.readline

_string = list(input().rstrip())
isTrue = 0
for i in range(len(_string)//2):
    if _string[i] != _string[len(_string)-(i+1)]:
        print(0)
        isTrue = 1
        break
if isTrue == 0: 
    print(1)

