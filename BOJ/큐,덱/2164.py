# 큐 카드2

import collections 
import sys

myqueue = collections.deque([])

N = int(sys.stdin.readline())

for i in range(N):
    myqueue.appendleft(i+1)


while len(myqueue) >= 1:
    if len(myqueue) == 1:
        print(myqueue[0])
        break
    myqueue.pop()
    myqueue.appendleft(myqueue.pop())
    