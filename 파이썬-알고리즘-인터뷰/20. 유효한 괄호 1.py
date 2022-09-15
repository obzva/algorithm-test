"""
스택 일치 여부 판별
"""


class Solution:
    def isValid(self, s: str) -> bool:
        # exception
        if len(s) < 2:
            return False

        stack = []
        table = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        for pth in s:
            if pth not in table:
                stack.append(pth)
            elif not stack or table[pth] != stack.pop():
                return False

        # 유효한 괄호라면, loop 이후 stack이 비어 있어야 함
        return len(stack) == 0
