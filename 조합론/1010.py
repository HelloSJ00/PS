# 조합론 다리 놓기

def factorial(N):
    if N == 0:
        return 1
    if N>0 :
        return N*factorial(N-1)
    
def findAnwser(N,M):
    anwser = int(factorial(M)/(factorial(N)*factorial(M-N)))
    return anwser
    
K = int(input()) # 테스트 케이스

for _ in range(K):
    N,M = map(int,input().split())
    print(findAnwser(N,M))




