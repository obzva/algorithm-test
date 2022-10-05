import collections
from typing import *


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # (these methods are possible because judge doesn't care the order of the answer in this problem)
        # TWO POINTER
        #
        # nums1, nums2 = sorted(nums1), sorted(nums2)
        # p = q = 0
        # ans = []
        # while p < len(nums1) and q < len(nums2):
        #     if nums1[p] > nums2[q]:
        #         q += 1
        #     elif nums1[p] < nums2[q]:
        #         p += 1
        #     else:
        #         ans.append(nums1[p])
        #         p += 1
        #         q += 1
        # return ans

        # COUNTER

        counts = collections.Counter(nums1)
        ans = []
        for num in nums2:
            if counts[num] > 0:
                ans.append(num)
                counts[num] -= 1
        return ans
