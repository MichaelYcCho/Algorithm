def solution(numbers):
    num=[1,2,3,4,5,6,7,8,9]
    a = list(set(num) - set(numbers)) # 차집합
    return sum(a)


def solution(numbers):
    return 45 - sum(numbers)


def solution(numbers):
    answer=0
    for i in range(1,10):
        if i not in numbers:
            answer += i
    return answer



def rm_small(mylist):
    # 함수를 완성하세요
    return [i for i in mylist if i > min(mylist)]


# 아래는 테스트로 출력해 보기 위한 코드입니다.
my_list = [4, 3, 2, 1]
print("결과 {} ".format(rm_small(my_list)))