# https://leetcode.com/problems/valid-parentheses/

s1 = "()"
s2 = "()[]{}"
s3 = "(]"


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for p in s:
            if p == "(":
                stack.append(")")
            elif p == "{":
                stack.append("}")
            elif p == "[":
                stack.append("]")

            # stack이 비어있거나, stack의 마지막 원소와 p가 다르면 False
            elif not stack or stack.pop() != p:
                return False

        result = False if stack else True
        return result


if __name__ == "__main__":
    solution = Solution()
    print(solution.isValid(s1))
    print(solution.isValid(s2))
    print(solution.isValid(s3))
