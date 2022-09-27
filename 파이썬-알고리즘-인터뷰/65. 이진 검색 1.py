"""
recursive
"""

from typing import *


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(left, right):
            if left <= right:
                # mid = (left + right) // 2
                # 오버플로 발생 가능성이 있으므로, 아래와 같이 수정
                mid = left + (right - left) // 2
                if nums[mid] < target:
                    return binary_search(mid + 1, right)
                elif target < nums[mid]:
                    return binary_search(left, mid - 1)
                else:
                    return mid
            else:
                return -1

        return binary_search(0, len(nums) - 1)
