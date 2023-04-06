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


class Solution2:
    @staticmethod
    def is_valid_parentheses(s):
        """
        문자열이 올바른 괄호 쌍을 가지고 있는지 확인하는 함수

        :param s: 검사할 문자열
        :return: 올바른 괄호 쌍이면 True, 그렇지 않으면 False
        """
        # 괄호 쌍을 저장할 딕셔너리를 생성
        brackets = {")": "(", "}": "{", "]": "["}

        # 스택을 초기화합니다.
        stack = []

        # 문자열을 순회하며 괄호를 검사
        for char in s:
            # 닫는 괄호가 나오면 스택에서 짝이 되는 여는 괄호를 찾음
            if char in brackets:
                # 스택이 비어있으면 괄호 쌍이 올바르지 않은 것
                if not stack:
                    return False

                # 스택의 마지막 요소를 꺼내와서 여는 괄호와 비교
                top = stack.pop()
                if brackets[char] != top:
                    return False
            # 여는 괄호가 나오면 스택에 추가
            else:
                stack.append(char)

        # 스택이 비어있다면 괄호 쌍이 일치하는것으로보면 됨
        return not stack


# 예제 문자열
s1 = "{[()()]}"
s2 = "{[()]}"

print(Solution2().is_valid_parentheses(s1))  # 출력: True
print(Solution2().is_valid_parentheses(s2))  # 출력: False
