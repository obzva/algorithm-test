class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0
        # 1. READ IN AND IGNORE ANY LEADING WHITESPACE
        w = 0
        while s[w] == ' ':
            w += 1
            if w == len(s):
                return 0
        s = s[w:]

        # 2. CHECK THE SIGN
        sign = 1
        if s[0] == '+':
            s = s[1:]
        elif s[0] == '-':
            sign *= -1
            s = s[1:]

        # 3, 4. READ IN UNTIL THE NEXT NO DIGIT CHARACTER OR THE END OF THE INPUT IS REACHED
        ans = 0
        i = 0
        while i < len(s):
            if 48 <= ord(s[i]) <= 57:
                ans = ans * 10 + (ord(s[i]) - 48)
                i += 1
            else:
                break
        ans *= sign

        # 5. CLAMP
        if ans < -2 ** 31:
            ans = -2 ** 31
        if ans > 2 ** 31 - 1:
            ans = 2 ** 31 - 1

        return ans
