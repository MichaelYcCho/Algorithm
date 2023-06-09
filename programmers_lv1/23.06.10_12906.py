def solution(arr):
    # 결과를 저장할 리스트 초기화
    result = []

    # 리스트의 첫 번째 요소를 결과에 추가
    result.append(arr[0])

    # 리스트의 두 번째 요소부터 마지막 요소까지 반복
    for i in range(1, len(arr)):
        # 현재 요소가 이전 요소와 다르면 결과에 추가
        if arr[i] != arr[i-1]:
            result.append(arr[i])

    return result
