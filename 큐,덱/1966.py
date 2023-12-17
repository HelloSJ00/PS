# 큐 프린터 큐 
import sys
import collections
import copy

T = int(sys.stdin.readline()) # test case
for _ in range(T):
    N,M =map(int,sys.stdin.readline().split()) # 자료의 개수와 찾고자하는 값의 위치 입력받기
    importanceValue = list(map(int,sys.stdin.readline().split())) # 중요도 입력받기
    _list = collections.deque([[] for _ in range(N)])
    anwser=[] # 출력순서 저장

    for i in range(N):
        _list[i] = [i,importanceValue[i]]


    while copy.deepcopy(_list):
        for j in copy.deepcopy(_list):
            if j[1] != max(importanceValue):
                _list.rotate(-1)
                continue
            anwser.append(_list.popleft())
            importanceValue.remove(j[1])
            continue

    for k in anwser:
        if k[0] == M:
            print(anwser.index(k)+1)
                   
    