from typing import *


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # TIME COMPLEXITY NOT O(N)
        #
        # nums.sort()
        # if len(nums) == 1:
        #     return nums[0]
        # i = 0
        # for j in range(1, len(nums)):
        #     if nums[i] != nums[j]:
        #         if j - i == 1:
        #             return nums[i]
        #         i = j
        # return nums[i]

        # BIT OPERATION XOR
        #
        for i in range(1, len(nums)):
            nums[0] ^= nums[i]
        return nums[0]
