"""
simple full-adder
"""


class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        INT_MAX = 0x7FFFFFFF

        while b != 0:
            a, b = (a ^ b) & MASK, ((a & b) << 1) & MASK
            #      자리 올림 제외 합  , 자리 올림만 체크

        if a > INT_MAX:
            a = ~(MASK ^ a)

        return a
