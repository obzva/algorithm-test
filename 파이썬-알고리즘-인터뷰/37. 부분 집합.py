from typing import *


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]

        def dfs(index, subset):
            for i in range(index, len(nums)):
                new_subset = subset[:]
                new_subset.append(nums[i])
                result.append(new_subset)
                dfs(i + 1, new_subset)

        dfs(0, [])
        return result
