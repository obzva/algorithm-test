from typing import *


class Solution:
    ROW = 0
    COL = 0

    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0

        self.ROW, self.COL = len(grid), len(grid[0])

        def dfs(row: int, col: int):
            if not (0 <= row < self.ROW and 0 <= col < self.COL) or grid[row][col] != '1':
                return
            grid[row][col] = '#'
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                dfs(row + dr, col + dc)

        for i in range(self.ROW):
            for j in range(self.COL):
                if grid[i][j] == '1':
                    ans += 1
                    dfs(i, j)

        return ans