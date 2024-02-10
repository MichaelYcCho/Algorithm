def solution(arr, k):
    result = []
    unique_nums = set()  # 이미 나온 수를 저장하는 집합

    for num in arr:
        if num not in unique_nums:  # 새로운 수가 나타났을 때
            result.append(num)  # 배열에 추가
            unique_nums.add(num)  # 나온 수를 집합에 저장
            if len(result) == k:  # 배열 길이가 k와 같으면 종료
                break

    # 배열의 길이가 k보다 작으면 나머지를 -1로 채움
    while len(result) < k:
        result.append(-1)

    return result