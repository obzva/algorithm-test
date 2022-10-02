"""
deque
"""
import collections
from typing import *


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = collections.deque()
        c_max = float('-inf')
        result = []
        for i, v in enumerate(nums):
            window.append(v)
            if i < k - 1:
                continue

            if c_max == float('-inf'):
                c_max = max(window)
            elif v > c_max:
                c_max = v

            result.append(c_max)

            if window.popleft() == c_max:
                c_max = float('-inf')
        return result
