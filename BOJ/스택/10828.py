# 스택 스택구현

'''
class Stack():
    def __init__(self) -> None:
        self.list = []

    def empty(self):
        if len(self.list) == 0: # 비어있으면 1
            return 1
        else:
            return 0

    def push(self,data):
        self.list.append(data)

    def _pop(self):
        if len(self.list) != 0: # 비어있지 않으면
            return self.list.pop()
        
        else :
            return -1
    
    def size(self):
        return len(self.list)
    
    def top(self):
        if len(self.list) != 0 : # 비어있지 않으면
            return self.list[len(self.list)-1]
        else:
            return -1
        
N = int(input()) # test case
mystack = Stack()

while(N>0):
    command_list = input().split( )
    if command_list[0] =='push':
        mystack.push(int(command_list[1]))
    elif command_list[0] =='pop':
        print(mystack._pop())
    elif command_list[0] =='size':
        print(mystack.size())
    elif command_list[0] =='empty':
        print(mystack.empty())
    elif command_list[0] =='top':
        print(mystack.top())
    N-=1

'''
import sys

N = int(sys.stdin.readline()) # test case
stack = []

while ( N>0):
    command = sys.stdin.readline().split()

    if command[0] == 'push':
        stack.append(int(command[1]))

    elif command[0] == 'pop':
        if len(stack) != 0:
            print(stack.pop())
        else :
            print(-1)

    elif command[0] == 'size':
        print(len(stack))

    elif command[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    elif command[0] == 'top':
        if len(stack) != 0:
            print(stack[len(stack)-1])
        else:
            print(-1)

    N -=1