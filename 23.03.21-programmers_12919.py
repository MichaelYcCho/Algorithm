# https://school.programmers.co.kr/learn/courses/30/lessons/12919


test_cases = ["Jane", "Kim", "Merry", "Mark", "Ki"]


def solution_01(seoul):
    result = None
    for index, value in enumerate(seoul):
        if value == "Kim":
            result = index
            break

    answer = f"김서방은 {result}에 있다"
    return answer


def solution_02(seoul):
    answer = f"김서방은 {seoul.index('Kim')}에 있다"
    return answer


print(solution_01(test_cases))
print(solution_02(test_cases))
