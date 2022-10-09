from typing import *


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # BINARY SEARCH TWO TIMES
        # searching pivot
        # left, right = 0, len(nums) - 1
        # while left < right:
        #     mid = left + (right - left) // 2
        #     if nums[mid] > nums[right]: # pivot is to the right of mid
        #         left = mid + 1
        #     else: # pivot is to the left of mid
        #         right = mid
        # pivot = left
        #
        # left, right = 0, len(nums) - 1
        # length = len(nums)
        # while left <= right:
        #     mid = left + (right - left) // 2
        #     mid_pivot = (mid + pivot) % length
        #     if nums[mid_pivot] < target:
        #         left = mid + 1
        #     elif nums[mid_pivot] > target:
        #         right = mid - 1
        #     else:
        #         return mid_pivot
        # return -1

        # BINARY SEARCH ONCE
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:  # pivot is to the right of mid, meaning values from [left:mid] are ascending
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:  # pivot is to the left of mid, meaning values from [mid:right] are ascending
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1
