class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        answer = 0
        for i in range(2, len(bin(x ^ y))):
            answer += int(bin(x ^ y)[i])
        return answer
