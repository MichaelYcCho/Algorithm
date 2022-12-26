class Solution:
    def longestPalindrome(self, s: str) -> str :

        def isPalin(s1):
            """ 팰린드롬인지 확인하는 함수 """
            if s1[::-1] == s1:
                return True
            return False
