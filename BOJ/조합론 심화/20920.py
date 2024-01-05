# 조합론 심화 영단어 암기는 괴로워

import sys

N, M = map(int,sys.stdin.readline().split())
vocadic = {}
# 딕셔너리 추가
for _ in range(N):
    voca = sys.stdin.readline().rstrip()
    if len(voca) >= M:
        if voca in vocadic:
            vocadic[voca] +=1
        else :
            vocadic[voca] = 1

# 정렬
result = sorted(vocadic.items(),key= lambda x : (-x[1],-len(x[0]),x[0]))

for i in result:
    print(i[0])
