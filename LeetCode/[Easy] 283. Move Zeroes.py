from typing import *


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = j = 0
        while i < len(nums) - 1 and j < len(nums) - 1:
            if nums[j] != 0:
                j += 1
                continue
            if nums[i] == 0 and nums[i + 1] != 0:
                nums[j], nums[i + 1] = nums[i + 1], 0
                i += 1
                j += 1
            else:
                i += 1
