# 스택 제로
import sys

N = int(sys.stdin.readline()) # test case
stack = []

for _ in range(N):
    command_number = int(sys.stdin.readline())
    if command_number != 0:
        stack.append(command_number)

    elif command_number ==0:
        stack.pop()
sum = 0
for i in stack:
    sum += i

print(sum)
