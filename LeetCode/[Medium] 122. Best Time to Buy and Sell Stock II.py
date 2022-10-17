from typing import *


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        prev_price = prices[0]
        for i in range(1, len(prices)):
            if prices[i] > prev_price:
                profit += prices[i] - prev_price
            prev_price = prices[i]
        return profit
