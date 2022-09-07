"""
dictionary
improved for short-coding
but not performance
"""

from typing import *


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in nums_map:
                return [i, nums_map[complement]]
            nums_map[num] = i
