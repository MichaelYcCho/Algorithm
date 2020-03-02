def rule(n):
    num_l = max([int(i) for i in n])
    count_num = [str(i) + str(str(n).count(str(i))) for i in range(1, num_l +1)]
    return ''.join(count_num)

def solution(count):
    answer = '1'
    if count == 1:
        return answer
    for i in range(1, count):
        answer = rule(answer)
        print(answer)
    return answer

print(solution(6))





'''
1 ~ 10000까지 8의 개수를 세는 문제

a = str(list(range(1, 10000))).count('8')

print(a)


# 순서 1

def rule(n):
    num_l = max([int(i) for i in n])
    return num_l
rule('345')


# 순서 2

def rule(n):
    num_l = max([int(i) for i in n])
    count_num = [str(i) + str(str(n).count(str(i)) for i in range(1, num_l +1)]
rule('3353')


'''