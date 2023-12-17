# 단어 뒤집기

import sys
input=sys.stdin.readline

TC = int(input())
for _ in range(TC):
    sentence = input().rstrip().split()
    for i in sentence:
        for j in range(len(i)):
            print(i[len(i)-(j+1)],end='')
        print(end=' ')
    print()



