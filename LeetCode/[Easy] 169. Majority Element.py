from typing import *


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # MY SOLUTION
        #
        # length = len(nums)
        # counter = collections.Counter(nums)
        # for num in counter:
        #     if counter[num] > length / 2:
        #         return num

        # SORT METHOD

        nums.sort()
        return nums[len(nums) // 2]
