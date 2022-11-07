import heapq
from typing import *


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # PYTHONIC (I THINK) - SPACE COMPLEXITY NOT MET
        #
        # heap = []
        #
        # for row in matrix:
        #     for num in row:
        #         heapq.heappush(heap, num)
        #
        # return heapq.nsmallest(k, heap)[-1]

        # USE HEAP FOR ROWS

        heap = []
        for i, row in enumerate(matrix):
            heapq.heappush(heap, (row[0], i, 0))
        i = 0
        while i < k:
            i += 1
            value, row, col = heapq.heappop(heap)
            if col < len(matrix[0]) - 1:
                heapq.heappush(heap, (matrix[row][col + 1], row, col + 1))
        return value
