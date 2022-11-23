import collections
from typing import *


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        answer = 0
        cache = collections.defaultdict(int)

        def dfs(row: int, col: int):
            if cache[row, col]:
                return cache[row, col]
            else:
                for dr, dc in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < m and 0 <= nc < n and matrix[nr][nc] > matrix[row][col]:
                        cache[row, col] = max(cache[row, col], dfs(nr, nc))
                cache[row, col] += 1
                return cache[row, col]

        for i in range(m):
            for j in range(n):
                answer = max(answer, dfs(i, j))

        return answer
