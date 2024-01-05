# 스택 괄호
import sys

N = int(sys.stdin.readline())

for _ in range(N):
    string_list = list(sys.stdin.readline())
    cnt = 0
    for i in string_list:
        if i == '(':
            cnt+=1
        elif i == ')':
            cnt -=1

        if cnt < 0:
            break

    if cnt ==0 :
        print('YES')
    else:
        print('NO')