import sys
from typing import *


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # BRUTE FORCE
        # max_sub_array = -sys.maxsize
        # for i in range(len(nums)):
        #     current_sub_array = 0
        #     for j in range(i, len(nums)):
        #         current_sub_array += nums[j]
        #         max_sub_array = max(max_sub_array, current_sub_array)
        # return max_sub_array

        # KADANE
        # current_sub_array = max_sub_array = nums[0]
        # for i in range(1, len(nums)):
        #     if current_sub_array < 0:
        #         current_sub_array = nums[i]
        #     else:
        #         current_sub_array += nums[i]
        #     max_sub_array = max(max_sub_array, current_sub_array)
        # return max_sub_array

        # DIVIDE AND CONQUER
        left, right = 0, len(nums) - 1

        if left > right:
            return -sys.maxsize

        mid = (left + right) // 2
        curr = best_left = best_right = 0

        for i in range(mid - 1, left - 1, -1):
            curr += nums[i]
            best_left = max(best_left, curr)

        curr = 0
        for i in range(mid + 1, right + 1):
            curr += nums[i]
            best_right = max(best_right, curr)

        best_combined_sum = nums[mid] + best_left + best_right

        left_half = self.maxSubArray(nums[:mid])
        right_half = self.maxSubArray(nums[mid + 1:])

        return max(left_half, best_combined_sum, right_half)

