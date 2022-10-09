import collections
from typing import *


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # RECURSIVE
        # ans = []
        #
        # def rec(x, remains):
        #     if not remains:
        #         ans.append(x)
        #         return
        #     for j, num in enumerate(remains):
        #         rec(x + [num], remains[:j] + remains[j + 1:])
        #
        # for i, num in enumerate(nums):
        #     rec([num], nums[:i] + nums[i + 1:])
        #
        # return ans

        # ITERATIVE
        queue = collections.deque()
        queue.append([])
        ans = []
        for num in nums:
            for _ in range(len(queue)):
                old_permutation = queue.popleft()
                for i in range(len(old_permutation) + 1):
                    item = old_permutation[:]
                    item.insert(i, num)
                    if len(item) == len(nums):
                        ans.append(item)
                    else:
                        queue.append(item)
        return ans


sol = Solution()
a = [1, 2, 3]
sol.permute(a)
