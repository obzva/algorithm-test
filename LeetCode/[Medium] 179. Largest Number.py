from typing import *


class Compare(str):
    def __lt__(self, other):
        return self + other > other + self


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # BRUTE FORCE - TIME LIMIT EXCEED
        # combinations = []
        #
        # def combination(path: str, num_list: List[int]):
        #     if not num_list:
        #         nonlocal combinations
        #         combinations.append(int(path))
        #         return
        #
        #     for i in range(len(num_list)):
        #         num = num_list[i]
        #         combination(path + str(num), num_list[:i] + num_list[i + 1:])
        #
        # combination('', nums)
        # return str(max(combinations))

        # SORT OPERATING - WITH ITERATIVE FUNCTION
        # def have_to_swap(n1: int, n2: int):
        #     return int(str(n1) + str(n2)) < int(str(n2) + str(n1))
        #
        # i = 1
        # while i < len(nums):
        #     j = i
        #     while j > 0 and have_to_swap(nums[j - 1], nums[j]):
        #         nums[j - 1], nums[j] = nums[j], nums[j - 1]
        #         j -= 1
        #     i += 1
        #
        # return str(int(''.join([str(num) for num in nums])))

        # SORT OPERATING WITH MAGIC OPERATOR
        nums_str = list(map(str, nums))
        nums_str.sort(key=Compare)
        return str(int(''.join(nums_str)))
