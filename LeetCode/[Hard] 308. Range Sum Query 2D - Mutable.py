from typing import *


# class NumMatrix:
#
#     def __init__(self, matrix: List[List[int]]):
#         self.A = matrix
#
#     def update(self, row: int, col: int, val: int) -> None:
#         self.A[row][col] = val
#
#     def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
#         ans = 0
#         for row in self.A[row1:row2 + 1]:
#             ans += sum(row[col1: col2 + 1])
#         return ans
#
# # Your NumMatrix object will be instantiated and called as such:
# # obj = NumMatrix(matrix)
# # obj.update(row,col,val)
# # param_2 = obj.sumRegion(row1,col1,row2,col2)

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.m = len(self.A)
        self.n = len(self.A[0])
        self.A = [[0] * self.n for _ in range(self.m)]
        self.bi_tree = [[0] * (self.n + 1) for _ in range(self.m + 1)]
        for row in range(self.m):
            for col in range(self.n):
                self.update(row, col, matrix[row][col])

    def _lsb(self, x):
        return x & -x

    def update(self, row: int, col: int, val: int) -> None:
        diff = val - self.A[row][col]
        row += 1
        col += 1
        while row <= self.m:
            j = col
            while j <= self.n:
                self.bi_tree[row][j] += diff
                j += self._lsb(j)
            row += self._lsb(row)

    def _query(self, row: int, col: int) -> int:
        row += 1
        col += 1
        result = 0
        while row > 0:
            j = col
            while j > 0:
                result += self.bi_tree[row][j]
                j -= self._lsb(j)
            row -= self._lsb(row)
        return result

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self._query(row2, col2) - self._query(row1 - 1, col2) - self._query(row2, col1 - 1) + self._query(
            row1 - 1, col1 - 1)

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)
