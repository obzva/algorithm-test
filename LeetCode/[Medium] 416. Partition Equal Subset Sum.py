# from typing import Tuple
# from functools import cache

# Recursion(DFS) with Cache

# Time complexity: O(NM), N is length of nums and M is target of subset sum
# Space complexity: O(NM), because we cached for lengths (N) and subset sums (M)

# class Solution:
#     def canPartition(self, nums: List[int]) -> bool:
#         total_sum = sum(nums)

#         if total_sum % 2 != 0:
#             return False

#         target = total_sum // 2

#         @cache
#         def dfs(length: int, total: int) -> bool:
#             if total == 0:
#                 return True
#             if length == 0 or total < 0:
#                 return False
#             return dfs(length - 1, total - nums[length - 1]) or dfs(length - 1, total)

#         return dfs(len(nums), target)


# Memoization with 2D array

# Big O notation is same as the previous approach

# class Solution:
#     def canPartition(self, nums: List[int]) -> bool:
#         total_sum = sum(nums)

#         if total_sum % 2 != 0:
#             return False

#         target = total_sum // 2

#         memo = [[False] * (target + 1) for _ in range(len(nums) + 1)]
#         memo[0][0] = True

#         for i in range(1, len(nums) + 1):
#             num = nums[i - 1]
#             for j in range(target + 1):
#                 if j < num:
#                     memo[i][j] = memo[i - 1][j]
#                 else:
#                     memo[i][j] = memo[i - 1][j] or memo[i - 1][j - num]

#         return memo[len(nums)][target]


# Memoization with 1D array

# Time complexity: O(NM), N is length of nums and M is target of subset sum
# Space complexity: O(M), memo array size of M


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)

        if total_sum % 2 != 0:
            return False

        target = total_sum // 2

        memo = [False] * (target + 1)
        memo[0] = True

        for num in nums:
            for i in reversed(range(target + 1)):
                if i >= num:
                    memo[i] = memo[i] or memo[i - num]

        return memo[target]
