from typing import *


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # MEMOIZATION

        # memo = [0] * (10 ** 5)
        # for num in nums:
        #     if memo[num - 1]:
        #         return num
        #     memo[num - 1] = 1

        # FLOYD'S TORTOISE AND HARE METHOD
        slow = fast = nums[0]
        while True:
            slow, fast = nums[slow], nums[nums[fast]]
            if slow == fast:
                break
        slow = nums[0]
        while slow != fast:
            slow, fast = nums[slow], nums[fast]
        return slow
