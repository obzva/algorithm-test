"""
dictionary
"""

from typing import *


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for i, num in enumerate(nums):
            nums_map[num] = i

        for i, num in enumerate(nums):
            complement = target - num
            if complement in nums_map and i != nums_map[complement]:
                return [i, nums_map[complement]]
