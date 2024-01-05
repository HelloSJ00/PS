import sys
input = sys.stdin.readline
N = int(input()) 
string = list(input())
anwser = 0
for i in range(N):
    anwser += ((ord(string[i])-96)*(31**i))

print(anwser%1234567891)