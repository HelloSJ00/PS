# 알파벳 개수

import sys
input = sys.stdin.readline

EngS = {'a':0,
       'b':0,
       'c':0,
       'd':0,
       'e':0,
       'f':0,
       'g':0,
       'h':0,
       'i':0,
       'j':0,
       'k':0,
       'l':0,
       'm':0,
       'n':0,
       'o':0,
       'p':0,
       'q':0,
       'r':0,
       's':0,
       't':0,
       'u':0,
       'v':0,
       'w':0,
       'x':0,
       'y':0,
       'z':0
       }

_string = list(input().rstrip())

for i in _string :
    if i in Eng:
        Eng[i] +=1

result = list(Eng.values())
print(*result)

