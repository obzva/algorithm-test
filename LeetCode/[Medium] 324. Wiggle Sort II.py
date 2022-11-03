import heapq
from typing import *


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
        if len(nums) % 2 == 0:
            for i in range(len(nums)):
                new_num = heapq.heappop(heap)
                if i < len(nums) // 2:
                    nums[len(nums) - 2 - 2 * i] = new_num
                else:
                    nums[len(nums) - 1 - 2 * (i - (len(nums) // 2))] = new_num
        else:
            for i in range(len(nums)):
                new_num = heapq.heappop(heap)
                if i <= len(nums) // 2:
                    nums[len(nums) - 1 - 2 * i] = new_num
                else:
                    nums[len(nums) - 2 - 2 * (i - 1 - (len(nums) // 2))] = new_num
