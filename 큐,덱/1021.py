# 큐 회전하는 큐
import collections
import sys, copy

def rightR(list):
    list.rotate(-1)

def leftR(list):
    list.rotate(1)


N,M = map(int,sys.stdin.readline().split())
index_list =  sys.stdin.readline().split() #찾고자하는 주소값
_list = collections.deque([i+1 for i in range(N)])

cnt = 0 # 연산의 개수
while(len(index_list)) != 0:
    if _list[0] == int(index_list[0]):
        _list.popleft()
        index_list.remove(index_list[0])
        continue
    
    if _list.index(int(index_list[0])) > len(_list)//2:
        leftR(_list)
        cnt+=1
    elif _list.index(int(index_list[0])) <= len(_list)//2:
        rightR(_list)
        cnt+=1
print(cnt)



