class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s_arr = [char for char in s]
        stack = []
        for i, char in enumerate(s):
            if char == '(':
                stack.append(('(', i))
            elif char == ')':
                if len(stack) > 0 and stack[-1][0] == '(':
                    stack.pop()
                else:
                    stack.append((')', i))
        for tuple in stack:
            index = tuple[1]
            s_arr[index] = ''
        return ''.join(s_arr)
