from typing import *


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # MY SOLUTION
        # m = len(matrix)
        # n = len(matrix[0])
        # curr_dir = 'right'
        # i = j = 0
        # cnt = 1
        # ans = []
        # while True:
        #     ans.append(matrix[i][j])
        #     if cnt == m * n:
        #         break
        #     matrix[i][j] = '#'
        #     if curr_dir == 'right':
        #         if j < n - 1 and matrix[i][j + 1] != '#':
        #             j += 1
        #         else:
        #             curr_dir = 'down'
        #             i += 1
        #     elif curr_dir == 'down':
        #         if i < m - 1 and matrix[i + 1][j] != '#':
        #             i += 1
        #         else:
        #             curr_dir = 'left'
        #             j -= 1
        #     elif curr_dir == 'left':
        #         if j > 0 and matrix[i][j - 1] != '#':
        #             j -= 1
        #         else:
        #             curr_dir = 'up'
        #             i -= 1
        #     elif curr_dir == 'up':
        #         if i > 0 and matrix[i - 1][j] != '#':
        #             i -= 1
        #         else:
        #             curr_dir = 'right'
        #             j += 1
        #     cnt += 1
        # return ans

        # RESETTING BOUNDARIES
        # m, n = len(matrix), len(matrix[0])
        # up = left = 0
        # down, right = m - 1, n - 1
        # ans = []
        # while len(ans) < m * n:
        #     for i in range(left, right + 1):
        #         ans.append(matrix[up][i])
        #     for i in range(up + 1, down + 1):
        #         ans.append(matrix[i][right])
        #     if up != down:
        #         for i in range(right - 1, left - 1, -1):
        #             ans.append(matrix[down][i])
        #         if left != right:
        #             for i in range(down - 1, up, -1):
        #                 ans.append(matrix[i][left])
        #     up += 1
        #     right -= 1
        #     down -= 1
        #     left += 1
        # return ans

        # RESETTING BOUNDARIES OPTIMIZED
        # m, n = len(matrix), len(matrix[0])
        # i, j = 0, -1
        # direction = 1
        # ans = []
        # while m * n > 0:
        #     for _ in range(n):
        #         j += direction
        #         ans.append(matrix[i][j])
        #     m -= 1
        #     for _ in range(m):
        #         i += direction
        #         ans.append(matrix[i][j])
        #     n -= 1
        #     direction *= -1
        # return ans

        # MARK AS READ
        m, n = len(matrix), len(matrix[0])
        di = [0, 1, 0, -1]
        dj = [1, 0, -1, 0]
        direction = 0
        i = j = 0
        ans = [matrix[i][j]]
        matrix[0][0] = '#'
        while len(ans) < m * n:
            ni = i + di[direction]
            nj = j + dj[direction]
            if not (0 <= ni < m and 0 <= nj < n) or matrix[ni][nj] == '#':
                direction = (direction + 1) % 4
            else:
                i, j = ni, nj
                ans.append(matrix[i][j])
                matrix[i][j] = '#'
        return ans
