#문자열 문자와 문자열

import sys

input = sys.stdin.readline

_string = input().rstrip()
N = int(input())

print(_string[N-1])