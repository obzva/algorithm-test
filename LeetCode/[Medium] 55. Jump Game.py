from typing import *


class Solution:
    # RECURSIVE: TIME LIMIT EXCEED
    # ans: bool = False
    #
    # def canJump(self, nums: List[int]) -> bool:
    #     # RECURSIVE
    #     def func(idx: int):
    #         if idx == len(nums) - 1:
    #             self.ans = True
    #         if idx >= len(nums) or nums[idx] == 0:
    #             return
    #         else:
    #             for num in range(1, nums[idx] + 1):
    #                 func(idx + num)
    #
    #     func(0)
    #     return self.ans
    def canJump(self, nums: List[int]) -> bool:
        # ITERATIVE: TIME LIMIT EXCEED
        # if len(nums) == 1:
        #     return True
        # queue = collections.deque()
        # queue.append(0)
        # while queue:
        #     idx = queue.popleft()
        #     max_jump = nums[idx]
        #     if max_jump == 0:
        #         continue
        #     for jump in range(1, max_jump + 1):
        #         if idx + jump == len(nums) - 1:
        #             return True
        #         if idx + jump not in queue and idx + jump < len(nums):
        #             queue.append(idx + jump)
        # return False

        # MEMOIZATION TOP-DOWN: TIME LIMIT EXCEED
        # memo = ['u'] * len(nums)
        # memo[-1] = 'g'
        #
        # def func(position: int) -> bool:
        #     if memo[position] != 'u':
        #         return memo[position] == 'g'
        #
        #     furthest_jump = min(position + nums[position], len(nums) - 1)
        #     for next_position in range(position + 1, furthest_jump + 1):
        #         if func(next_position):
        #             memo[position] = 'g'
        #             return True
        #     memo[position] = 'b'
        #     return False
        #
        # return func(0)

        # MEMOIZATION BOTTOM-UP
        # memo = ['u'] * len(nums)
        # memo[-1] = 'g'
        # for i in range(len(nums) - 2, -1, -1):
        #     furthest_jump = min(i + nums[i], len(nums) - 1)
        #     for j in range(i + 1, furthest_jump + 1):
        #         if memo[j] == 'g':
        #             memo[i] = 'g'
        #             break
        # return memo[0] == 'g'

        # GREEDY
        # last_position = len(nums) - 1
        # for i in range(len(nums) - 1, -1, -1):
        #     if i + nums[i] >= last_position:
        #         last_position = i
        # return last_position == 0

        # GOING FORWARD
        furthest = i = 0
        while i <= furthest:
            furthest = max(furthest, i + nums[i])
            if furthest >= len(nums) - 1:
                return True
            i += 1
        return False
