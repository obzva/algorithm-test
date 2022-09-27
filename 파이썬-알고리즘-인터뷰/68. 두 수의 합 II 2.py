"""
Binary-search
"""
from typing import *


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, number in enumerate(numbers):
            left, right, residual = i + 1, len(numbers) - 1, target - number
            while left <= right:
                mid = left + (right - left) // 2
                if numbers[mid] > residual:
                    right = mid - 1
                elif numbers[mid] < residual:
                    left = mid + 1
                else:
                    return [i + 1, mid + 1]
