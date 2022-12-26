class Solution:
    def longestPalindrome1(self, s: str) -> str :

        def isPalin(s1):
            """ 팰린드롬인지 확인하는 함수 """
            if s1[::-1] == s1:
                return True
            return False

        """ 첫글자를 기준으로 한칸씩 포인터가 뒤로가면서 모두 순회하면서 팰린드롬이면 answer에 저장하는 형태 """
        answer = ""
        n = len(s)
        for i in range(n):
            for j in range(i, n):
                subStr = s[i : j+1]
                if isPalin(subStr) and len(subStr) > len(answer):
                    answer = s[i : j+1]
        return answer


solution = Solution()
print(solution.longestPalindrome1("babad")) # bab