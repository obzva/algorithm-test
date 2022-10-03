class Solution:
    def climbStairs(self, n: int) -> int:
        # MEMOIZATION
        #
        dic = {1: 1, 2: 2}
        for i in range(3, n + 1):
            dic[i] = dic[i - 1] + dic[i - 2]
        return dic[n]

        # RECURSIVE -> Time Limit Exceeded
        #
        # if n <= 2:
        #     return n
        # return self.climbStairs(n - 1) + self.climbStairs(n - 2)
