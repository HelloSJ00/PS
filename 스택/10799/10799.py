import sys

text = list(sys.stdin.readline())

stack = []

fragment = 0
state = -1 # '(' == 0, ')' == 1
for i in text :
    if i == '(':
        stack.append(i)
        state = 0
    
    if i == ')':
        if state == 0:
            stack.pop()
            fragment+= len(stack)
        else:
            stack.pop()
            fragment+=1
        state = 1

print(fragment)


    
    