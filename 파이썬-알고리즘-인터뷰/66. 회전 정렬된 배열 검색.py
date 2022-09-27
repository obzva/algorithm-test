from typing import *


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        sorted_nums = sorted(nums)
        offset = nums.index(sorted_nums[0])

        def binary_search(left, right):
            if left <= right:
                # mid = (left + right) // 2
                # 오버플로 발생 가능성이 있으므로, 아래와 같이 수정
                mid = left + (right - left) // 2
                if sorted_nums[mid] < target:
                    return binary_search(mid + 1, right)
                elif target < sorted_nums[mid]:
                    return binary_search(left, mid - 1)
                else:
                    return mid
            else:
                return -1

        binary_search_result = binary_search(0, len(sorted_nums) - 1)

        if binary_search_result == -1:
            return -1
        else:
            return (binary_search_result + offset) % len(nums)
