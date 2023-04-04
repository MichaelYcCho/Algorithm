def find_duplicates(arr: list):
    """
    배열에서 중복 원소를 찾아서 리스트로 반환하는 함수.

    :param arr: 중복 원소를 찾을 배열
    :return: 중복 원소 리스트
    """
    # 중복 원소를 저장할 집합을 초기화합니다.
    duplicates = set()

    # 배열의 원소들을 저장할 집합을 초기화합니다.
    elements = set()

    # 배열의 원소들을 순회합니다.
    for elem in arr:
        # 원소가 이미 elements 집합에 있다면, duplicates 집합에 추가합니다.
        if elem in elements:
            duplicates.add(elem)
        # 그렇지 않으면, 원소를 elements 집합에 추가합니다.
        else:
            elements.add(elem)

    # 중복 원소 리스트를 반환합니다.
    return list(duplicates)


# 예제 배열
question_list = [1, 2, 3, 4, 5, 6, 3, 2, 1]

# 중복 원소를 찾아 출력합니다.
print(find_duplicates(question_list))  # 출력: [1, 2, 3]
