# 큐 덱 구현하기

import collections
import sys, copy

class deque():
    def __init__(self) -> None:
        self._deque = collections.deque([])
    
    def push_front(self,data):
        self._deque.appendleft(data)

    def push_back(self,data):
        self._deque.append(data)

    def pop_front(self):
        if len(self._deque) != 0: 
            return self._deque.popleft()
        else:
            return -1
    
    def pop_back(self):
        if len(self._deque) != 0: 
            return self._deque.pop()
        else:
            return -1
    
    def size(self):
        return len(self._deque)
    
    def empty(self):
        if len(self._deque) == 0:
            return 1
        else:
            return 0

    def front(self):
        if len(self._deque) != 0:
            return self._deque[0]
        else:
            return -1
    
    def back(self):    
        if len(self._deque) != 0:
            return self._deque[len(self._deque)-1]
        else:
            return -1
T = int(sys.stdin.readline())
q = deque()
while T>0:
    command = sys.stdin.readline().split()
    if command[0] == 'push_back':
        q.push_back(command[1])
    if command[0] == 'push_front':
        q.push_front(command[1])
    if command[0] == 'pop_front':
        print(q.pop_front())
    if command[0] == 'pop_back':
        print(q.pop_back())
    if command[0] == 'size':
        print(q.size())
    if command[0] == 'empty':
        print(q.empty())
    if command[0] == 'front':
        print(q.front())
    if command[0] == 'back':
        print(q.back())
    T -=1