from typing import *


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def bin_left() -> int:
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        def bin_right() -> int:
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right

        left, right = bin_left(), bin_right()
        return [left, right] if len(nums) >= right >= left >= 0 else [-1, -1]
   