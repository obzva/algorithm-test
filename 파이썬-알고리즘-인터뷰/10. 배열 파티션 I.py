from typing import *


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        for num in nums[::2]:
            res += num
        return res
