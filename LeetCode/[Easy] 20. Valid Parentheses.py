class Solution:
    def isValid(self, s: str) -> bool:
        # MY SOLUTION
        #
        # if len(s) < 2:
        #     return False
        # stack = []
        # for p in s:
        #     if p == '(' or p == '{' or p == '[':
        #         stack.append(p)
        #     else:
        #         if stack:
        #             pop = stack.pop()
        #             if p == ')' and pop != '(':
        #                 return False
        #             if p == '}' and pop != '{':
        #                 return False
        #             if p == ']' and pop != '[':
        #                 return False
        #         else:
        #             return False
        # return len(stack) == 0

        # BETTER SOLUTION

        dic = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for p in s:
            if p in dic:
                stack.append(p)
            elif len(stack) == 0 or dic[stack.pop()] != p:
                return False
        return len(stack) == 0