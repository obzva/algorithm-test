import sys
from typing import *


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m < n:
            return self.findMedianSortedArrays(nums2, nums1)
        low, high = 0, 2 * n
        while low <= high:
            mid2 = (low + high) // 2
            mid1 = m + n - mid2

            left1 = -sys.maxsize if mid1 == 0 else nums1[(mid1 - 1) // 2]
            left2 = -sys.maxsize if mid2 == 0 else nums2[(mid2 - 1) // 2]
            right1 = sys.maxsize if mid1 == 2 * m else nums1[mid1 // 2]
            right2 = sys.maxsize if mid2 == 2 * n else nums2[mid2 // 2]

            if left1 > right2:
                low = mid2 + 1
            elif right1 < left2:
                high = mid2 - 1
            else:
                return (max(left1, left2) + min(right1, right2)) / 2
