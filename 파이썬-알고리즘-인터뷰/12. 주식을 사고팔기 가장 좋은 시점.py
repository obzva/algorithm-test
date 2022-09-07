from typing import *


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)

        right_max = prices[N - 1]
        res = 0
        for i in range(N - 2, -1, -1):
            right_max = max(right_max, prices[i])
            res = max(res, right_max - prices[i])

        return res
