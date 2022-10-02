class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n & 0xFFFFFFFF).count('1')
