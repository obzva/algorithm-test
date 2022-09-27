"""
recursive
"""

from typing import *


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # exception
        if not matrix:
            return False

        def check(row: int, col: int) -> bool:
            if row <= len(matrix) - 1 and col >= 0:
                if target == matrix[row][col]:
                    return True
                elif target < matrix[row][col]:
                    return check(row, col - 1)
                else:
                    return check(row + 1, col)
            else:
                return False

        return check(0, len(matrix[0]) - 1)
