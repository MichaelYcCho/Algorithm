def solution(num_list):
    count = 0  # 나누기 연산의 횟수를 저장하는 변수

    for num in num_list:
        while num != 1:  # 숫자가 1이 될 때까지 반복
            if num % 2 == 0:  # 짝수인 경우
                num //= 2
            else:  # 홀수인 경우
                num -= 1
                num //= 2
            count += 1

    return count