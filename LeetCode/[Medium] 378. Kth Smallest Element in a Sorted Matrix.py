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

        # heap = []
        # for i, row in enumerate(matrix):
        #     heapq.heappush(heap, (row[0], i, 0))
        # i = 0
        # while i < k:
        #     i += 1
        #     value, row, col = heapq.heappop(heap)
        #     if col < len(matrix[0]) - 1:
        #         heapq.heappush(heap, (matrix[row][col + 1], row, col + 1))
        # return value

        # BINARY SEARCH

        def binary(mid: int, smaller: int, larger: int):
            n = len(matrix)
            count = 0
            row, col = 0, n - 1
            while row < n and col >= 0:
                if matrix[row][col] > mid:
                    larger = min(larger, matrix[row][col])
                    col -= 1
                else:
                    smaller = max(smaller, matrix[row][col])
                    count += col + 1
                    row += 1
            return (count, smaller, larger)

        start, end = matrix[0][0], matrix[-1][-1]
        while start < end:
            mid = (start + end) // 2
            smaller, larger = matrix[0][0], matrix[-1][-1]
            count, smaller, larger = binary(mid, smaller, larger)
            if count == k:
                return smaller
            elif count < k:
                start = larger
            else:
                end = smaller
        return start
