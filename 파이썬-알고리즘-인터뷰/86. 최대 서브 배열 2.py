"""
Kadane
"""
import sys
from typing import *


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = 0
        best_sum = -sys.maxsize
        for num in nums:
            current_sum = max(num, current_sum + num)
            best_sum = max(best_sum, current_sum)
        return best_sum
