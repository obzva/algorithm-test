import sys
from typing import *


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # SOLUTION 1
        #
        # max_price = prices[-1]
        # margin = [0]
        # for i in range(1, len(prices)):
        #     max_price = max(max_price, prices[-i - 1])
        #     margin.append(max_price - prices[-i - 1])
        # margin.sort(reverse=True)
        # return max(margin)

        # SOLUTION 2

        profit = 0
        min_price = sys.maxsize

        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)

        return profit
