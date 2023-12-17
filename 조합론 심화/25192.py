# 조합론 심화 인사성 밝은 곰곰이

import sys
from collections import deque

N = int(sys.stdin.readline())
chat = deque([])
gomgom = 0
name={}

for _ in range(N):
    chat.append(sys.stdin.readline().rstrip())

for i in chat:
    if i == 'ENTER':
        name.clear()

    elif i not in name:
        gomgom+=1
        name[i] =True

print(gomgom)


