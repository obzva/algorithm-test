class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        res = 0
        for char in s:
            if char == '(':
                stack.append(char)
            elif char == ')':
                res = max(res, len(stack))
                stack.pop()
        return res