def solution(N):
    answer = 0
    for digit in str(N):
        answer += int(digit)
    return answer
