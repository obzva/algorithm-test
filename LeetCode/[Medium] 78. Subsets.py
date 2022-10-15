from typing import *


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # MY SOLUTION
        # n = len(nums)
        # ans = []
        #
        # def func(prev, cnt):
        #     ans.append(prev)
        #     if cnt == n:
        #         return
        #     for i in range(cnt + 1, n):
        #         func(prev + [nums[i]], i)
        #
        # func([], -1)
        # return ans

        # CLEANER ONE
        # ans = []
        # n = len(nums)
        #
        # def dfs(i, prev):
        #     ans.append(prev)
        #     for j in range(i, n):
        #         dfs(j + 1, prev + [nums[j]])
        #
        # dfs(0, [])
        # return ans

        # BIT MANIPULATION
        # n = len(nums)
        # ans = []
        # for i in range(1 << n):
        #     tmp = []
        #     for j in range(n):
        #         if i & (1 << j):
        #             tmp.append(nums[j])
        #     ans.append(tmp)
        # return ans

        # ITERATIVE
        ans = [[]]
        for num in nums:
            ans += [[num] + item for item in ans]
        return ans