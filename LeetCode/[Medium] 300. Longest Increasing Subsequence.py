from typing import *


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # DP - TIME LIMIT EXCEED

        # answer = 1
        # memo = [1] * len(nums) # memo[i] := longest subsequence length ends with nums[i]
        # for i in range(len(nums)):
        #     for j in range(i):
        #         if nums[i] <= nums[j]:
        #             continue
        #         memo[i] = max(memo[i], memo[j] + 1)
        #     answer = max(answer, memo[i])
        # return answer

        # INTELLIGENTLY BUILD SUBSEQUENCE

        # sub = [nums[0]]
        # for i in range(1, len(nums)):
        #     if nums[i] > sub[-1]:
        #         sub.append(nums[i])
        #     else:
        #         j = 0
        #         while sub[j] < nums[i]:
        #             j += 1
        #         sub[j] = nums[i]
        # return len(sub)

        # INTELLIGENTLY BUILD SUBSEQUENCE WITH BINARY SEARCH

        sub = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] > sub[-1]:
                sub.append(nums[i])
            else:
                left, right = 0, len(sub) - 1
                while left < right:
                    mid = (left + right) // 2
                    if sub[mid] < nums[i]:
                        left = mid + 1
                    else:
                        right = mid
                sub[left] = nums[i]

        return len(sub)
