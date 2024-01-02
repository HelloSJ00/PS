import sys

N,K = map(int,sys.stdin.readline().split()) # N: 숫자의 개수, K: 지울 숫자의 개수
num = list(sys.stdin.readline()) # 숫자 입력받기

stack = []
for i in range(len(num)):
    while K > 0 and stack and stack[-1] < num[i]: # 지울 숫자가 남아있는 경우
        stack.pop()
        K-=1

    stack.append(num[i])



print(''.join(stack[:N-K]))

