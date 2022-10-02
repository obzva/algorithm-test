class Solution:
    def hammingWeight(self, n: int) -> int:
        # bin(n ^ 0b00000000000000000000000000000000).count('1')
        # => bin(n ^ 0).count('1')
        # => bin(n).count('1')
        return bin(n).count('1')
