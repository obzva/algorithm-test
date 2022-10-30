from typing import *


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # ITERATIVE
        # row = 0
        # col = len(matrix[0]) - 1
        # while row < len(matrix) and col >= 0:
        #     if matrix[row][col] == target:
        #         return True
        #     elif matrix[row][col] < target:
        #         row += 1
        #     else:
        #         col -= 1
        # return False

        # RECURSIVE
        # def recursive_func(row: int, col: int) -> bool:
        #     if not (row < len(matrix) and col >= 0):
        #         return False
        #     if matrix[row][col] == target:
        #         return True
        #     elif matrix[row][col] > target:
        #         return recursive_func(row, col - 1)
        #     else:
        #         return recursive_func(row + 1, col)
        #
        # return recursive_func(0, len(matrix[0]) - 1)

        # PYTHONIC
        return any(target in row for row in matrix)
