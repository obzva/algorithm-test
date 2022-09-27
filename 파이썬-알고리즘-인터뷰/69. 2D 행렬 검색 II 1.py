"""
loop
"""

from typing import *


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # exception
        if not matrix:
            return False

        # the last elem. of the first row
        row = 0
        col = len(matrix[0]) - 1

        while row <= len(matrix) - 1 and col >= 0:
            if target == matrix[row][col]:
                return True
            # if smaller than target then move left
            elif target < matrix[row][col]:
                col -= 1
            # if larger than target then move down
            else:
                row += 1
        return False
