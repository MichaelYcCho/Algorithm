def is_permutation(str1: str, str2: str):
    """
    두 문자열이 순열 관계인지 확인하는 함수입니다.

    :param str1: 첫 번째 문자열
    :param str2: 두 번째 문자열
    :return: 두 문자열이 순열 관계이면 True, 그렇지 않으면 False
    """
    # 두 문자열의 길이가 다르면 순열 관계가 아닙니다.
    if len(str1) != len(str2):
        return False

    # 두 문자열의 문자 개수를 저장할 딕셔너리를 생성합니다.
    char_count = {}

    # 첫 번째 문자열의 문자를 세어서 딕셔너리에 저장합니다.
    for char in str1:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # 두 번째 문자열의 문자를 세어서 딕셔너리에서 빼줍니다.
    for char in str2:
        if char in char_count:
            char_count[char] -= 1
        else:
            return False

    # 모든 문자의 개수가 0이면 두 문자열은 순열 관계입니다.
    return all(count == 0 for count in char_count.values())


# 예제 문자열 - 두 문자가 가지고있는 문자가 같으면 순열
q_1 = "listen"
q_2 = "silent"

# 두 문자열이 순열 관계인지 확인하고 출력합니다.
print(is_permutation(q_1, q_2))  # 출력: True
