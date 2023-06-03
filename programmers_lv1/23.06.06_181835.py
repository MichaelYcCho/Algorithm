def solution(arr, k):
    result = []
    for num in arr:
        if k % 2 == 1:  # k가 홀수인 경우
            result.append(num * k)
        else:  # k가 짝수인 경우
            result.append(num + k)
    return result