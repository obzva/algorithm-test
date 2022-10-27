from typing import *


class Solution:
    # nums[i] != nums[i + 1] for all 'i'
    def findPeakElement(self, nums: List[int]) -> int:
        # ITERATIVE
        # left, right = 0, len(nums) - 1
        # while left < right:
        #     mid = (left + right) // 2
        #     if nums[mid] < nums[mid + 1]:
        #         left = mid + 1
        #     elif nums[mid] > nums[mid + 1]:
        #         right = mid
        # return left

        # RECURSIVE
        def find_peak_element(left: int, right: int) -> int:
            if left == right:
                return left
            mid = (left + right) // 2
            if nums[mid] < nums[mid + 1]:
                return find_peak_element(mid + 1, right)
            elif nums[mid] > nums[mid + 1]:
                return find_peak_element(left, mid)

        return find_peak_element(0, len(nums) - 1)
