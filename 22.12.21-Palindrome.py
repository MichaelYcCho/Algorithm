# 문자열 조작
# 팰린드롬, 회문


STR1 = "A man, a plan, a canal: Panama"
STR2 = "race a car"

"""
List를 활용한 방법 빅오는 O(n^2) 
304 밀리초
"""


def isPalindrome(s: str) -> bool:

    strs = []
    for char in s:
        if char.isalnum():  # is alphabet or Num
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.pop(0) != strs.pop():  # List의 Pop(0) 는 O(n)
            return False

    return True


answer1 = isPalindrome(STR1)
answer2 = isPalindrome(STR2)

print(answer1)
print(answer2)


"""
DeQue를 활용 (O(n))
64 밀리초
앞, 뒤 양쪽 방향에서 엘리먼트(element)를 추가하거나 제거할 수 있다.
데크는 양 끝 엘리먼트의 append와 pop이 훨씬 빠르다.
컨테이너(container)의 양끝 엘리먼트(element)에 접근하여 삽입 또는 제거를 할 경우, 일반적인 리스트(list)가 이러한 연산에 O(n)이 소요되는 데 반해, 
데크(deque)는 O(1)로 접근 가능하다.
"""
from collections import deque
import re
from typing import Deque


def isPalindrome2(s: str) -> bool:
    # 자료형 선언
    strs: Deque = deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():  # poplift = O(1)
            return False

    return True


print()
print(isPalindrome2(STR1))
print(isPalindrome2(STR2))


"""
술라이싱 사용
36밀리초
"""


def isPalindrome3(s: str) -> bool:
    s = s.lower()
    s = re.sub("[^a-z0-9]", "", s)
    return s == s[::-1]  # 역순부터 조회


print()
print(isPalindrome3(STR1))
print(isPalindrome3(STR2))


# 정규표현식없이
def is_palindrome(s):
    # 문자열의 알파벳 문자만 추출하여 모두 소문자로 변경
    s = "".join(filter(str.isalpha, s)).lower()
    # 문자열을 뒤집은 결과와 원본 문자열이 같은지 검사(역순조회)
    return s == s[::-1]


# 팰린드롬 검사 예시
print(is_palindrome("A man, a plan, a canal, Panama"))  # True
print(is_palindrome("Hello, world!"))  # False
