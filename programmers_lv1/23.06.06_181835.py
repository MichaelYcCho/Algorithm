def solution(arr, k):
    result = []
    for num in arr:
        if k % 2 == 1:  # k가 홀수인 경우
            result.append(num * k)
        else:  # k가 짝수인 경우
            result.append(num + k)
    return result



# 다른 풀이
def solution(arr, k):
    if k % 2 != 0:
        return list(map(lambda x: x * k, arr))

    return list(map(lambda x: x + k, arr))