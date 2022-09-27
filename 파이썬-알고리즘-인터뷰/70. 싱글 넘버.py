"""
XOR
"""

from typing import *


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        mask = 0xFFFF
        for i, num in enumerate(nums):
            mask = mask ^ num
            if i % 2 == 1 and mask != 0xFFFF:
                return nums[i - 1]
            elif i == len(nums) - 1 and mask != 0xFFFF:
                return nums[i]
