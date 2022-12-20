# 문자열 조작
# 팰린드롬, 회문


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



answer1 = isPalindrome("A man, a plan, a canal: Panama")
print(answer1)

answer2 = isPalindrome("race a car")
print(answer2)