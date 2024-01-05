# -2진법

import sys
input = sys.stdin.readline
'''
N = input()
result = '1'

if N[0] == '-': # 음수일때
    i = 1
    sum = 0
    while True:
        sum += 2**(2*i-1)
        if int(N[1:]) <= sum:
            break
        i+=1

    exponent = 2*i-1
    num = (-2)**exponent
    exponent -=1
    while exponent != -1:
        if num < int(N) and exponent%2 == 0:
            result+='1'
            num += (-2)**exponent
            
        elif num <= int(N) and exponent%2 == 1:
            result+='0'

        elif num >= int(N) and exponent%2 == 0:
            result+='0'

        elif num > int(N) and exponent%2 == 1:
            result+='1'
            num += (-2)**exponent

        exponent-=1
    print(result)

elif N == '0':
    print(0)

else: # 양수일때
    i = 1
    sum = 0
    while True:
        sum += 2**(2*i-2)
        if int(N) <= sum:
            break
        i+=1

    exponent = 2*i-2
    num = (-2)**exponent
    exponent -=1
    while exponent != -1:
        if num < int(N) and exponent%2 == 0:
            result+='1'
            num += (-2)**exponent
            
        elif num <= int(N) and exponent%2 == 1:
            result+='0'

        elif num >= int(N) and exponent%2 == 0:
            result+='0'

        elif num > int(N) and exponent%2 == 1:
            result+='1'
            num += (-2)**exponent

        exponent-=1
    print(result)



'''

N = int(input())
answer = []

while True :
    if N != 0:
        if N > 0:
            answer.append(N % -2)
            N //= -2
        else:
            answer.append(abs(N % -2))
            N = (N-1)//-2

    if N == 0:
        print(answer)
        break
