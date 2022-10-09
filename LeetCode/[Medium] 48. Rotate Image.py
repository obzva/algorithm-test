from typing import *


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # PYTHONIC
        # matrix[:] = map(list, zip(*matrix[::-1]))

        # SWITCH
        n = len(matrix)
        for i in range(n // 2):
            for j in range(n - n // 2):
                matrix[i][j], matrix[~j][i], matrix[~i][~j], matrix[j][~i] = matrix[~j][i], matrix[~i][~j], matrix[j][
                    ~i], matrix[i][j]
