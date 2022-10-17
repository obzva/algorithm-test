from typing import *


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])

        def func(row, col):
            if not (0 <= row < m and 0 <= col < n):
                return True
            if board[row][col] != 'O':
                return False
            board[row][col] = 'X'
            is_surrounded = not func(row, col + 1) and not func(row + 1, col) and not func(row, col - 1) and not func(
                row - 1, col)
            if not is_surrounded:
                board[row][col] = 'O'
            return not is_surrounded

        for i in range(m):
            for j in range(n):
                func(i, j)

