"""
Counter
"""
import collections
import heapq
from typing import *


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = collections.Counter(nums)
        freqs_heap = []
        for freq in freqs:
            heapq.heappush(freqs_heap, (-freqs[freq], freq))

        top_k = list()

        for _ in range(k):
            top_k.append(heapq.heappop(freqs_heap)[1])

        return top_k
