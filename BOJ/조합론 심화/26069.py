# 조합론 심화 붙임성 좋은 총총이

import sys

dancedic = {'ChongChong':True}

N = int(sys.stdin.readline())

for _ in range(N):
    A ,B = sys.stdin.readline().split()
    if A in dancedic:
        dancedic[B] = True
    elif B in dancedic:
        dancedic[A] = True

print(len(dancedic))