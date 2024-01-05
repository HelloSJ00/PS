import sys
input = sys.stdin.readline

def generate_combinations(characters, length):
    if length == 0:
        return [""]
    smaller_combinations = generate_combinations(characters, length - 1)
    return [s + char for s in smaller_combinations for char in characters]

TC = int(input())
for _ in range(TC):
    n,m,k = map(int,input().split())
    string = list(input()) # 문자열
    # n = 테스트 케이스 길이
    # m = 검색 상자에 입력할 수 있는 최대 허용 단어 길이
    # k = 검색 상자가 처음 k문자만 허용하도록 지정  

    dic = {} # 문자열에 있는 알파벳
    alpha = []
    cnt = k
    for i in string:
        if i not in dic:
            dic[i] = True
            alpha.append(i) # 딕셔너리에 담긴 알파벳들 , ex) ['a','b']
            cnt -=1
            if cnt == 0:
                break
    
    compare_dic = {} # 원본 문자열에서 나오는 경우의 수
    compare_list = [] # 가능한 경우의 수

    if k > 1: 
        for i in range(2,m+1): # 나올 수 있는 경우의 수 찾기
            compare_list += generate_combinations(alpha,i)
        
        for i in range(2,m+1): # 원본 문자열에서 나오는 경우의 수 찾기
            for j in range(len(string)-i+1):
                compare_string =''
                for k in range(j,j+i):
                    compare_string += string[k]
                if compare_string not in compare_dic:
                    compare_dic[compare_string] = True
        # print(compare_list)
        # print(compare_dic)
    
    anwser = []
    for i in compare_list:
        if i not in compare_dic:
            anwser.append(i)
    # print(compare_list)

    print(anwser[0])
        
    