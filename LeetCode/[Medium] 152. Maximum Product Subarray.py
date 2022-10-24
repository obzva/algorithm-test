from typing import *


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # BRUTE FORCE
        # max_product = -sys.maxsize
        # for i in range(len(nums)):
        #     current_product = nums[i]
        #     max_product = max(max_product, current_product)
        #     for j in range(i + 1, len(nums)):
        #         current_product *= nums[j]
        #         max_product = max(max_product, current_product)
        # return max_product

        # DYNAMIC PROGRAMMING
        max_so_far = min_so_far = result = nums[0]
        for i in range(1, len(nums)):
            current = nums[i]
            max_so_far, min_so_far = max(current, current * max_so_far, current * min_so_far), min(current,
                                                                                                   current * max_so_far,
                                                                                                   current * min_so_far)
            result = max(max_so_far, result)
        return result
