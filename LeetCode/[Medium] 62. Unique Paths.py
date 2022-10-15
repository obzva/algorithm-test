class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # MY SOLUTION
        # memo = [[1] * n]
        # for _ in range(m - 1):
        #     memo.append([1] + [0] * (n - 1))
        #
        # for r in range(1, m):
        #     for c in range(1, n):
        #         memo[r][c] = memo[r - 1][c] + memo[r][c - 1]
        #
        # return memo[m - 1][n - 1]
        #
        # O(N) SPACE
        memo = [1] * n
        for _ in range(1, m):
            for j in range(1, n):
                memo[j] += memo[j - 1]
        return memo[n - 1]
