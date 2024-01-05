# 문자열 심화 너의 평점은

import sys
input = sys.stdin.readline
_list = []
sum = 0
total_credit = 0

def Grade(record) -> float:
    if record == 'A+':
        return  4.5
    elif record == 'A0':
        return 4.0
    elif record == 'B+':
        return 3.5
    elif record == 'B0':
        return 3.0
    elif record == 'C+':
        return 2.5
    elif record == 'C0':
        return 2.0
    elif record == 'D+':
        return 1.5
    elif record == 'D0':
        return 0
    elif record == 'F':
        return 0
    elif record == 'P':
        return -1

for _ in range(20):
    _list.append(input().rstrip().split())

for i in range(20):
    total_credit += int(float(_list[i][1]))
    if Grade(_list[i][2] ) > 0:
        sum += int(float(_list[i][1]))* Grade(_list[i][2])

print(sum/total_credit)