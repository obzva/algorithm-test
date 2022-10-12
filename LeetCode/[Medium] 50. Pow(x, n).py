class Solution:
    def myPow(self, x: float, n: int) -> float:
        # TIME LIMIT EXCEED
        # if n == 0:
        #     return 1
        # elif n < 0:
        #     n, x = -n, 1 / x
        # ans = 1
        # for _ in range(n):
        #     ans *= x
        #
        # return ans

        # USING RECURSION
        # x ^ n = (x ^ 2) ^ (n / 2) [if even]
        #         x * (x ^ 2) ^ (n // 2) [if odd]
        # def func(base, exponent):
        #     if exponent == 0:
        #         return 1
        #     elif exponent % 2 == 0:
        #         return func(base * base, exponent / 2)
        #     else:
        #         return base * func(base * base, exponent // 2)
        #
        # if n == 0:
        #     return 1
        # elif n < 0:
        #     n, x = -n, 1 / x
        #
        # return func(x, n)

        # ANOTHER RECURSION
        # if n == 0:
        #     return 1
        # elif n < 0:
        #     n, x = -n, 1 / x
        #
        # def rec(base, exponent):
        #     if exponent == 0:
        #         return 1
        #     half = rec(base, exponent // 2)
        #     if exponent % 2 == 0:
        #         return half * half
        #     else:
        #         return base * half * half
        #
        # return rec(x, n)

        # ITERATIVE
        # bit representation
        # n = 0b[bm, bm-1, ... , b2, b1]
        #   = 2 ^ bm + 2 ^ bm-1 + ... + 2 ^ b2 + 2 ^ b1
        # therefore, answer = x ^ (2 ^ bm + 2 ^ bm-1 + ... + 2 ^ b2 + 2 ^ b1)
        #                   = x ^ (2 ^ bm) * x ^ (2 ^ bm-1) * ... * x ^ (2 ^ b2) * x ^ (2 ^ b1)
        if n == 0:
            return 1
        if n < 0:
            n, x = -n, 1 / x
        ans, multi = 1, x
        while n:
            if n & 1:
                ans *= multi
            multi *= multi
            n >>= 1
        return ans
