from typing import *


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        writing_index = 1
        for i in range(len(nums) - 1):
            if nums[i] != nums[i + 1]:
                nums[writing_index] = nums[i + 1]
                writing_index += 1
        return writing_index
