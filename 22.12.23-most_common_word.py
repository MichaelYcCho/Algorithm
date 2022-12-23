import collections
import re


paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

def most_common_word(paragraph: str, banned: list[str]) -> str:
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]

    # Counter 생성자는 여러 형태의 데이터를 인자로 받는다
    # 먼저 중복된 데이터가 저장된 배열을 인자로 넘기면 각 원소가 몇 번씩 나오는지가 키은트가 많은 순으로 출력해준다
    # cf) 문자열만 넘기면 넘긴 문자순으로 카운트 하여 출력한다.
    counts = collections.Counter(words)
    print(counts.most_common(1)[0][0])
    

most_common_word(paragraph, banned)