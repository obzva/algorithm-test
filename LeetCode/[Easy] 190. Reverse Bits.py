class Solution:
    def reverseBits(self, n: int) -> int:
        # MY SOLUTION
        #
        # mask = 0xFFFFFFFF - 1
        # answer = 0
        # for _ in range(32):
        #     tmp = (mask | n) ^ mask
        #     answer = answer * 2 + tmp
        #     n >>= 1
        # return answer

        # OPTIMIZATION OF MY SOLUTION

        answer = 0
        for _ in range(32):
            answer = (answer << 1) + (n & 1)
            n >>= 1
        return answer
