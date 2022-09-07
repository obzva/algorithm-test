from typing import *


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res, left, right = [], [], []
        N = len(nums)

        p = 1
        for i in range(N):
            left.append(p)
            p *= nums[i]

        p = 1
        for i in range(N - 1, -1, -1):
            right.append(p)
            p *= nums[i]
        right.reverse()

        for i in range(N):
            res.append(left[i] * right[i])

        return res


