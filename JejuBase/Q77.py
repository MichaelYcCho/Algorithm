# 두 열에 공통으로 나열되어있는 요소로 만들 수 있는 가장 긴 부분열 

def sol(s):
    result = []
    for i in range(1, len(s) + 1):
        for j in range(i):
            result.append(s[j:j+len(s)-i+1])
    return result

user_input = input().split(' ')
user_input_split_set_one = set(sol(user_input[0])) 
user_input_split_set_two = set(sol(user_input[1]))


answer = user_input_split_set_one.intersection(user_input_split_set_two)
answer = max(answer, key=len)
print(len(answer))


'''
만약 
ABCDEFGHIJ라면 len(s) = 10



'''