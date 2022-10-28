from typing import *


class Solution:
    def rob(self, nums: List[int]) -> int:
        # RECURSIVE - TIME LIMIT EXCEED
        # ans = 0
        #
        # def rob_func(acc, num_list):
        #     if not num_list:
        #         nonlocal ans
        #         ans = max(ans, acc)
        #         return
        #     rob_func(acc + num_list[0], num_list[2:])
        #     if len(num_list) > 1:
        #         rob_func(acc + num_list[1], num_list[3:])
        #
        # rob_func(0, nums)
        # return ans

        # MEMO
        memo = [0] * (len(nums) + 1)
        memo[1] = nums[0]
        for i in range(1, len(nums)):
            memo[i + 1] = max(memo[i - 1] + nums[i], memo[i])
        return memo.pop()
