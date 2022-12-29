class Solution:

    @staticmethod
    def is_palin(s1):
        """ 팰린드롬인지 확인하는 함수 """
        if s1[::-1] == s1:
            return True
        return False

    def longest_palindrome1(self, s: str) -> str:
        """ 
        첫글자를 기준으로 한칸씩 포인터가 뒤로가면서 모두 순회하면서 팰린드롬이면 answer에 저장하는 형태 
        O(n^3)의 시간복잡도를 가짐
        """

        answer = ""
        n = len(s)
        for i in range(n):
            for j in range(i, n):
                subStr = s[i: j+1]
                if self.is_palin(subStr) and len(subStr) > len(answer):
                    answer = s[i: j+1]
        return answer

    def longest_palindrome2(self, s: str) -> str:
        """ 
        큰 문자열을 기준으로 작은 문자열로 작아짐 처음에 걸리는 팰린드롬이 가장 큰 팰린드롬이므로 1보다 개선됨
        다만 뒤에서 부터 잡다보니 aba가 나와서 원하는 output인 bab가 나오지 않음
        O(n^2)의 시간복잡도를 가짐
        """

        answer = ""
        n = len(s)
        while n > 0:
            for i in range(len(s) - n+1):    # -> (5 - 5- + 1 = 1), (5 - 4 + 1 = 2), (5 - 3 + 1 = 3), (5 - 2 + 1 = 4), (5 - 1 + 1 = 5)
                if self.is_palin(s[i: i+n]):
                    return s[i:i+n]
                n -= 1
        return answer


    def longest_palindrome3(self, s: str) -> str:
        
        answer = ""
        n = len(s)
        for i in range(n):
            left, right = i, i
            while left >= 0 and right < n and s[left] == s[right]:
                if right - left + 1 > len(answer):
                    answer = s[left: right+1]
                left -= 1
                right += 1
            
            left, right = i, i+1
            while left >= 0 and right < n and s[left] == s[right]:
                if right - left + 1 > len(answer):
                    answer = s[left: right+1] # 새로운 answer가 기존의 answer보다 크면 answer에 저장
        
        return answer

    
    def longest_palindrome4(self, s: str) -> str:

        # 홀수 글자, 짝수 글자를 모두 고려해야함
        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1: right]

        if len(s) < 2 or s == s[::-1]:
            return s

        result = ''
        # 슬라이딩 윈도우 우측으로 이동
        for i in range(len(s)-1):
            # max 함수를 이용하여 가장 긴 팰린드롬을 result에 저장 (max에 들어온 인자들 중 가장 큰 값을 반환)
            result = max(result, expand(i, i+1), expand(i, i+2), key=len)

        return result




STRING = "babad"
solution = Solution()
#print(solution.longest_palindrome1(STRING))  # bab
#print(solution.longest_palindrome2(STRING))  # aba
print(solution.longest_palindrome4(STRING))  # bab