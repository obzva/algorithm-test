import collections
import itertools
from typing import *


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # m, n = len(board), len(board[0])
        #
        # def func(row, col):
        #     if not (0 <= row < m and 0 <= col < n):
        #         return True
        #     if board[row][col] != 'O':
        #         return False
        #     board[row][col] = 'X'
        #     is_surrounded = not func(row, col + 1) and not func(row + 1, col) and not func(row, col - 1) and not func(
        #         row - 1, col)
        #     if not is_surrounded:
        #         board[row][col] = 'O'
        #     return not is_surrounded
        #
        # for i in range(m):
        #     for j in range(n):
        #         func(i, j)

        # DFS, BFS
        if not board or not board[0]:
            return

        m, n = len(board), len(board[0])

        def dfs(row, col):
            if not (0 <= row < m and 0 <= col < n):
                return
            if board[row][col] != 'O':
                return
            board[row][col] = 'E'
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            for dr, dc in directions:
                dfs(row + dr, col + dc)

        def bfs(row, col):
            queue = collections.deque()
            queue.append((row, col))
            while queue:
                row, col = queue.popleft()
                if not (0 <= row < m and 0 <= col < n) or board[row][col] != 'O':
                    continue
                board[row][col] = 'E'
                for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    queue.append((row + dr, col + dc))

        borders = list(itertools.product(range(m), [0, n - 1])) + list(itertools.product([0, m - 1], range(1, n - 1)))
        for row, col in borders:
            dfs(row, col)  # or use 'bfs(row, col)'

        for row in range(m):
            for col in range(n):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                elif board[row][col] == 'E':
                    board[row][col] = 'O'
