def solution(numbers):
    answer = []
    for i in numbers:
        answer.append(i * 2)
    return answer

# 리스트 컴프리헨션을 사용할 경우
def solution(numbers):
    return [i * 2 for i in numbers]