"""
heapq
"""

import heapq
from typing import *


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = list()
        for n in nums:
            heapq.heappush(heap, -n)

        for _ in range(k - 1):
            heapq.heappop(heap)

        return -heapq.heappop(heap)
