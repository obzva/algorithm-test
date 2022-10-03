from typing import *


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # SOLUTION 1
        #
        # dp = collections.defaultdict(list)
        # i = 0
        # while i < numRows:
        #     i += 1
        #     for j in range(i):
        #         if i == 1:
        #             dp[i].append(1)
        #         else:
        #             left = dp[i - 1][j - 1] if j > 0 else 0
        #             right = dp[i - 1][j] if j < i - 1 else 0
        #             dp[i].append(left + right)
        # return list(dp.values())

        # SOLUTION 2

        rows = [[1]]
        for _ in range(1, numRows):
            left = [0] + rows[-1]
            right = rows[-1] + [0]
            rows.append([x + y for x, y in zip(left, right)])
        return rows
