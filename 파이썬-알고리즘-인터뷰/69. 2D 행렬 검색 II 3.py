"""
Pythonic
"""

from typing import *


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return any(target in row for row in matrix)
        # (target in row)         for (row)                         in (matrix)
        # (row 안에 target이 있는가?) for (matrix라는 list의 elem.인 row) in (matrix)
