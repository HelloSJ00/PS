# 8진수 2진수
'''
import sys
from collections import deque
input = sys.stdin.readline


eight = input()
two = ''
for i in eight:
    if int(i) >= 4:
        two += '1'
    else:
        two += '0'
        
    if  (3 >= int(i) >= 2) or ( 7>= int(i) >= 6):
        two += '1'
    else:
        two += '0'

    if (int(i)%2 == 1) :
        two += '1'
    else:
        two += '0'



two = deque(list(two))
while two[0] != '1':
    two.popleft()
    if len(two) == 0:
        break

if two :
    for i in range(len(two)):
        if i != len(two) -1:
            print(two[i],end='')
        else:
            print(two[i])
else:
    print(0)
    '''
    
import sys

# 입력을 8진수로 변환
n = int(sys.stdin.readline().rstrip(), 8)

# 8진수를 2진수로 변환한 뒤, 맨 앞의 '0b'를 제외한 나머지 출력
print(bin(n)[2:])
                