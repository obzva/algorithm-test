from typing import *


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(nums)
        left, right = 0, len(nums) - 1
        while left < right:
            sum = sorted_nums[left] + sorted_nums[right]
            if sum > target:
                right -= 1
            elif sum < target:
                left += 1
            else:
                if sorted_nums[left] == sorted_nums[right]:
                    index1 = nums.index(sorted_nums[left])
                    index2 = nums[index1 + 1:].index(sorted_nums[left]) + index1 + 1
                    return [index1, index2]
                else:
                    return [nums.index(sorted_nums[left]), nums.index(sorted_nums[right])]
