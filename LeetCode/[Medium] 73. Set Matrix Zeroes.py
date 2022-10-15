from typing import *


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row, col = len(matrix), len(matrix[0])
        zero_row, zero_col = set(), set()

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    zero_row.add(i)
                    zero_col.add(j)

        for r in zero_row:
            for j in range(col):
                matrix[r][j] = 0

        for c in zero_col:
            for i in range(row):
                matrix[i][c] = 0
