# BFS

# Time complexity: O(MN)
# Space complexity: O(MN)

from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        fresh_orange = 0

        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh_orange += 1

        if fresh_orange == 0 and not queue:
            return 0

        minute = -1

        tmp_queue = deque()
        while queue:
            rot_row, rot_col = queue.popleft()
            for dr, dc in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                nr, nc = rot_row + dr, rot_col + dc
                if 0 <= nr < m and 0 <= nc < n:
                    if grid[nr][nc] == 1:
                        fresh_orange -= 1
                        grid[nr][nc] = 2
                        tmp_queue.append((nr, nc))

            if not queue:
                minute += 1
                queue = tmp_queue
                tmp_queue = deque()

        return minute if fresh_orange == 0 else -1


# BFS - with in-place modification

# Time Complexity: O(MN)
# Space Complexity: const


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def rot_orange(timestamp: int) -> bool:
            to_be_continued = False
            for r in range(m):
                for c in range(n):
                    if grid[r][c] == timestamp:
                        for dr, dc in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < m and 0 <= nc < n:
                                if grid[nr][nc] == 1:
                                    grid[nr][nc] = timestamp + 1
                                    to_be_continued = True
            return to_be_continued

        timestamp = 2

        while rot_orange(timestamp):
            timestamp += 1

        for row in grid:
            for cell in row:
                if cell == 1:
                    return -1

        return timestamp - 2
