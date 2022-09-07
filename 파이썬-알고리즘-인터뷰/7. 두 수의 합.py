from typing import *


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(nums)
        N = len(nums)

        start = 0
        end = N - 1

        while start < end:
            tmp = sorted_nums[start] + sorted_nums[end]
            if tmp == target:
                i = nums.index(sorted_nums[start])
                j = nums.index(sorted_nums[end])
                if i == j:
                    j = nums[i + 1:].index(sorted_nums[end]) + (i + 1)
                return [i, j]
            elif tmp < target:
                start += 1
            else:
                end -= 1
