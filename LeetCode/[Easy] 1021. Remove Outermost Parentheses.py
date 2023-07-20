class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ''
        # index to divide string
        start = 0
        # l : number of accumulated left paranthesis, r : number of accumulated right parenthesis
        l, r = 0, 0
        for i, char in enumerate(s):
            if char == '(':
                l += 1
            elif char == ')':
                r += 1
                if l == r:
                    result += s[start + 1: i]
                    start, l, r = i + 1, 0, 0
        return result
