# 조합론 이항계수 1

A ,B = map(int,input().split())

def factorial(N):
    if N == 0:
        return 1
    if N>0 :
        return N*factorial(N-1)
    
anwser = factorial(A)/(factorial(B)*factorial(A-B))
print(int(anwser))