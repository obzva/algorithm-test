class Solution:
    def hammingWeight(self, n: int) -> int:
        answer = 0
        for _ in range(32):
            answer += n & 1 == 1
            n >>= 1
        return answer
