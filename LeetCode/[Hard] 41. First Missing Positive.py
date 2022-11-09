from typing import *


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        if 1 not in nums:
            return 1

        for i, num in enumerate(nums):
            if num <= 0 or num > n:
                nums[i] = 1

        nums[0] *= -1

        for num in nums:
            abs_num = abs(num)
            nums[abs_num - 1] = - abs(nums[abs_num - 1])

        for i in range(1, n):
            if nums[i] > 0:
                return i + 1
        return n + 1
