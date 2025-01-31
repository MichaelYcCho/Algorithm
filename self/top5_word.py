import string
from collections import Counter

"""
텍스트 파일을 읽고
구두점을 제거한 후 소문자로 변환
어별 등장 횟수를 계산
가장 많이 등장한 5개 단어를 출력
"""


def most_common_words(file_path, top_n=5):
    # 파일 읽기
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()

    # 구두점 제거 및 소문자 변환
    text = text.translate(str.maketrans("", "", string.punctuation)).lower()

    # 단어 분리
    words = text.split()

    # 단어 빈도수 계산
    word_counts = Counter(words)

    # 상위 N개 단어 출력
    top_words = word_counts.most_common(top_n)

    return top_words


# 사용 예시
file_path = "sample.txt"  # 분석할 텍스트 파일 경로
top_words = most_common_words(file_path)

print("가장 많이 등장한 단어:")
for word, count in top_words:
    print(f"{word}: {count}번")
