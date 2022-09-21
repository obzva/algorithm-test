from typing import *


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(index, subset):
            result.append(subset)

            for i in range(index, len(nums)):
                dfs(i + 1, subset + [nums[i]])

        dfs(0, [])
        return result
