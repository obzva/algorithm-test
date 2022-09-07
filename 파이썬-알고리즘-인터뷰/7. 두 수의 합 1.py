"""
brute force
"""

from typing import *


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                tmp = nums[i] + nums[j]
                if tmp == target:
                    return [i, j]
