def solution(s):
    # 문자열을 공백으로 나누어 각 단어를 원소로 갖는 리스트 생성
    words = s.split(' ')

    # 결과를 저장할 리스트 초기화
    result = []

    # 각 단어에 대해 반복
    for word in words:
        # 단어의 각 문자에 대해 반복하며 대문자와 소문자를 변경
        new_word = ''
        for i in range(len(word)):
            # 인덱스가 짝수이면 대문자로, 홀수이면 소문자로 변환
            if i % 2 == 0:
                new_word += word[i].upper()
            else:
                new_word += word[i].lower()

        # 결과 리스트에 새 단어 추가
        result.append(new_word)

    # 결과 리스트의 원소들을 공백으로 결합하여 최종 결과 문자열 생성
    answer = ' '.join(result)

    return answer

print(solution("try hello world"))  # "TrY HeLlO WoRlD"


def solution(s):
    return ' '.join([''.join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(word)]) for word in s.split(' ')])

print(solution("try hello world"))  # "TrY HeLlO WoRlD"