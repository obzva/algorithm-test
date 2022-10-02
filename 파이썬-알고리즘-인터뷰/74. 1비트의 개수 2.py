"""
bitwise operation
EX: bin(0b1000 & (0b1000 - 1)) = 0b0
EX: bin(0b1010 & (0b1010 - 1)) = 0b1000
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        one = 0
        while n != 0:
            n &= n - 1
            one += 1
        return one
