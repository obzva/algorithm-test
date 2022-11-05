from typing import *


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # MY SOLUTION

        # sub = [nums[0]]
        # for i in range(1, len(nums)):
        #     num = nums[i]
        #     if num <= sub[-1]:
        #         if sub[0] >= num:
        #             sub[0] = num
        #         else:
        #             sub[1] = num
        #     else:
        #         sub.append(num)
        #     if len(sub) == 3:
        #         return True
        # return False

        # MAXRIGHT AND MINLEFT

        max_rights = [0] * len(nums)
        max_rights[-1] = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            max_rights[i] = max(max_rights[i + 1], nums[i + 1])

        min_left = nums[0]
        for i in range(1, len(nums) - 1):
            if min_left < nums[i] < max_rights[i]:
                return True
            min_left = min(min_left, nums[i])
        return False
