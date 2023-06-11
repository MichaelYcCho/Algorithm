from itertools import combinations

def solution(numbers):
    # 모든 세 수의 조합을 찾음
    combinations_of_three = list(combinations(numbers, 3))

    # 조합 중에서 합이 0인 것을 카운트
    count = 0
    for combination in combinations_of_three:
        if sum(combination) == 0:
            count += 1

    return count


def solution(number):
    answer = 0
    l = len(number)
    for i in range(l-2):
        for j in range(i+1, l-1):
            for k in range(j+1, l):
                # print(number[i],number[j],number[k])
                if number[i]+number[j]+number[k] == 0:
                    answer += 1           
    return answer