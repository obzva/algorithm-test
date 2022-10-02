"""
dictionary
"""

from typing import *


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for i, num in enumerate(nums):
            nums_map[num] = i

        for i, num in enumerate(nums):
            complement = target - num
            if complement in nums_map and i != nums_map[complement]:
                # 'i != nums_map[complement]'가 없다면 해의 고유성을 보장할 수 없음
                # ex: [3, 2, 4] , 6
                return [i, nums_map[complement]]
