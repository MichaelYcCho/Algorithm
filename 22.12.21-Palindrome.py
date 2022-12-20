# 문자열 조작
# 팰린드롬, 회문


STR1 = "A man, a plan, a canal: Panama"
STR2 = "race a car"

"""
List를 활용한 방법 빅오는 O(n^2)
"""

def isPalindrome(s: str) -> bool:

    strs = []
    for char in s:
        if char.isalnum(): # is alphabet or Num
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False
    
    return True



answer1 = isPalindrome(STR1)
answer2 = isPalindrome(STR2)

print(answer1)
print(answer2)


"""
DeQue를 활용
앞, 뒤 양쪽 방향에서 엘리먼트(element)를 추가하거나 제거할 수 있다.
데크는 양 끝 엘리먼트의 append와 pop이 훨씬 빠르다.
컨테이너(container)의 양끝 엘리먼트(element)에 접근하여 삽입 또는 제거를 할 경우, 일반적인 리스트(list)가 이러한 연산에 O(n)이 소요되는 데 반해, 
데크(deque)는 O(1)로 접근 가능하다.
"""
from collections import deque
from typing import Deque


def isPalindrome2(s: str) -> bool:
    # 자료형 선언
    strs : Deque = deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False

    return True


print(isPalindrome2(STR1))
print(isPalindrome2(STR2))

    
