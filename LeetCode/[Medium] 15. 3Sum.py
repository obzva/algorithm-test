from typing import *


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # TIME COMPLEXITY O(N^2)
        nums.sort()
        ans = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            start, end = i + 1, len(nums) - 1
            while start < end:
                if nums[i] + nums[start] + nums[end] == 0:
                    ans.append([nums[i], nums[start], nums[end]])
                    while start < end and nums[start] == nums[start + 1]:
                        start += 1
                    while start < end and nums[end] == nums[end - 1]:
                        end -= 1
                    start += 1
                    end -= 1
                elif nums[i] + nums[start] + nums[end] < 0:
                    while start < end and nums[start] == nums[start + 1]:
                        start += 1
                    start += 1
                else:
                    while start < end and nums[end] == nums[end - 1]:
                        end -= 1
                    end -= 1
        return ans
