def solution(d, budget):
    answer = 0  # 가능한 부서의 수
    for i in sorted(d):
        budget -= i
        if budget < 0:
            break
        answer += 1
    return answer


def solution(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)
