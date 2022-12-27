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








STRING = "babad"
solution = Solution()
#print(solution.longest_palindrome1(STRING))  # bab
print(solution.longest_palindrome2(STRING))  # aba