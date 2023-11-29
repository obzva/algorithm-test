# brute force

# Time complexity: O((M + N)!/(M!*N!)), for all unique paths
# Space complexity: O(M + N), for recursion stack


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        delta = [[1, 0], [0, 1]]
        answer = 200 * (2 * 200 - 1)

        def dfs(row, col, acc):
            nonlocal answer
            if row == m - 1 and col == n - 1:
                answer = min(answer, acc)
            for dr, dc in delta:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < m and 0 <= new_col < n:
                    dfs(new_row, new_col, acc + grid[new_row][new_col])

        dfs(0, 0, grid[0][0])

        return answer


# memoization

# Time complexity: O(MN), for each coordinates
# Space complexity: O(MN), for additional memoization list


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        memo = [[0] * n for _ in range(m)]
        memo[0][0] = grid[0][0]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                if i == 0:
                    memo[i][j] = memo[i][j - 1] + grid[i][j]
                elif j == 0:
                    memo[i][j] = memo[i - 1][j] + grid[i][j]
                else:
                    memo[i][j] = grid[i][j] + min(memo[i][j - 1], memo[i - 1][j])

        return memo[m - 1][n - 1]


# memoization, but 1D

# Time complexity: O(MN), for every coordinate
# Space complexity: O(N), for memoization list


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        memo = grid[0][:]

        for j in range(1, n):
            memo[j] += memo[j - 1]

        for i in range(1, m):
            for j in range(n):
                if j == 0:
                    memo[j] += grid[i][j]
                else:
                    memo[j] = grid[i][j] + min(memo[j], memo[j - 1])

        return memo[n - 1]
