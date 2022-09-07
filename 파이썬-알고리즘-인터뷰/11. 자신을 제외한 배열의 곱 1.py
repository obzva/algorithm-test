"""
directly multiply right value to res resay
"""

from typing import *


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        N = len(nums)

        p = 1
        for i in range(N):
            res.append(p)
            p *= nums[i]

        p = 1
        for i in range(N - 1, -1, -1):
            res[i] *= p
            p *= nums[i]

        return res
