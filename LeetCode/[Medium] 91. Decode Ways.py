class Solution:
    def numDecodings(self, s: str) -> int:
        # MY SOLUTION - TIME LIMIT EXCEED
        # def func(code):
        #     if len(code) == 0:
        #         return 1
        #     if code[0] == '0':
        #         return 0
        #     if len(code) > 1 and ((code[0] == '1') or (code[0] == '2' and int(code[1]) < 7)):
        #         return func(code[1:]) + func(code[2:])
        #     else:
        #         return func(code[1:])
        #
        # return func(s)

        # MY SOLUTION - REVISED BUT TIME LIMIT EXCEED
        # def func(code):
        #     if len(code) == 0:
        #         return 1
        #     if code[0] == '0':
        #         return 0
        #     if len(code) == 1:
        #         return 1
        #     result = func(code[1:])
        #     if 0 < int(code[0:2]) <= 26:
        #         result += func(code[2:])
        #     return result
        #
        # return func(s)

        # MY SOLUTION - WITH INDEX BUT TIME LIMIT EXCEED
        # def func(idx):
        #     if idx == len(s):
        #         return 1
        #     if s[idx] == '0':
        #         return 0
        #     if idx == len(s) - 1:
        #         return 1
        #     result = func(idx + 1)
        #     if 0 < int(s[idx: idx + 2]) <= 26:
        #         result += func(idx + 2)
        #     return result
        #
        # return func(0)

        # DP
        if s[0] == '0':
            return 0
        memo = [0] * (len(s) + 1)
        memo[0] = memo[1] = 1
        for i in range(2, len(s) + 1):
            if s[i - 1] != '0':
                memo[i] += memo[i - 1]
            if 10 <= int(s[i - 2: i]) <= 26:
                memo[i] += memo[i - 2]
        return memo[-1]
