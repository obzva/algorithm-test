"""
Binary-search with bisect module
"""
import bisect
from typing import *


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, number in enumerate(numbers):
            expected = target - number
            j = bisect.bisect_left(numbers, expected, i + 1)
            if j < len(numbers) and numbers[j] == expected:
                return [i + 1, j + 1]
