# 스택 균형잡힌 세상
import sys

while(1):
    newString = list(sys.stdin.readline().rstrip())
    if newString[0] == '.' and len(newString) == 1 : # 종료조건
        break

    balance_value = [] #균형인수

    while(1):
        cnt = 0
        stringIndex =0
        if len(balance_value) == 0: # balance_value 길이가 0일때
            if newString[stringIndex] == '(' :
                balance_value.append([1,0]) 
                balance_value.append([0,0])
                cnt +=1

            elif newString[stringIndex] == '[':
                balance_value.append([0,1])
                balance_value.append([0,0])
                cnt+=1

            elif newString[stringIndex] == ')':
                print('no')
                break
            elif newString[stringIndex] == ']':
                print('no')
                break

        else: # balanceValue 의 길이가 0보다 클때
            if newString[stringIndex] == '(':
                balance_value[cnt][0]+=1
                balance_value.append([0,0])
                cnt+=1
                
            elif newString[stringIndex] == '[':
                balance_value[cnt][1]+=1
                balance_value.append([0,0])
                cnt+=1

            elif newString[stringIndex] == ')':
                if balance_value[cnt] != [0,0]: # 안쪽 부분이 균형이 아닐때 
                    print('no')
                    break
                elif balance_value[cnt] == [0,0]: # 안쪽 부분이 균형이라면
                    balance_value.pop()

                    cnt-=1 
                    balance_value[cnt][0]-=1  
            
                    if balance_value[cnt][0] < 0:
                        print('no')
                        break

            elif newString[cnt] == ']':
                if balance_value[cnt] != [0,0]: # 안쪽 부분이 균형이 아닐때 
                    print('no')
                    break
                elif balance_value[cnt] == [0,0]: # 안쪽 부분이 균형이라면
                    balance_value.pop()

                    cnt-=1 
                    balance_value[cnt][1]-=1  
                    
                    if balance_value[cnt][1] < 0:
                        print('no')
                        break
            
        if balance_value == [[0,0]]:
            print('yes')
        else:
            print('no')

    
    
    


