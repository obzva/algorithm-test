import sys
from typing import *


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # BFS - TIME LIMIT EXCEED

        # if amount == 0:
        #     return 0
        #
        # amount_set = set()
        # amount_set.add(amount)
        # count = 0
        # while amount_set:
        #     count += 1
        #     new_amount_set = set()
        #     for remainder in amount_set:
        #         if remainder in coins:
        #             return count
        #         for coin in coins:
        #             if remainder >= coin:
        #                 new_amount_set.add(remainder - coin)
        #         amount_set = new_amount_set
        # return -1

        # MEMOIZATION

        if amount == 0:
            return 0

        memo = [sys.maxsize] * (amount + 1)
        memo[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin:
                    memo[i] = min(memo[i], memo[i - coin] + 1)
        return -1 if memo[-1] == sys.maxsize else memo[-1]
