import collections
import re


paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

def most_common_word(paragraph: str, banned: list[str]) -> str:
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]
    
    counts = collections.Counter(words)
    print(counts.most_common(1)[0][0])
    

most_common_word(paragraph, banned)