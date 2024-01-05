#문자열 문자열

import sys
input = sys.stdin.readline

TC = int(input())

for _ in range(TC):
    string = input().rstrip()
    print(string[0]+string[len(string)-1])