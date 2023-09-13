# class Solution:
#     def swimInWater(self, grid: List[List[int]]) -> int:
#         n = len(grid)
#         visited = {(0, 0)}
#         # (elevation, row, column)[]
#         heap = [(grid[0][0], 0, 0)]
#         ans = 0
#         directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
#         while heap:
#             elevation, row, col = heapq.heappop(heap)
#             ans = max(ans, elevation)
#             if row == col == n - 1:
#                 return ans
#             for dr, dc in directions:
#                 new_row, new_col = row + dr, col + dc
#                 if 0 <= new_row < n and 0 <= new_col < n and (new_row, new_col) not in visited:
#                     heapq.heappush(heap, (grid[new_row][new_col], new_row, new_col))
#                     visited.add((new_row, new_col))

#         # Time complexity
#         ## iteration -> O(N^2) for worst case
#         ## heappop -> O(logN)
#         ## heappush -> O(logN)
#         ### O(N^2logN)

#         # Space complexity
#         ### O(N^2) for the worst case


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        def check(t: int) -> bool:
            stack = [(0, 0)]
            visited = {(0, 0)}
            while stack:
                row, col = stack.pop()
                if row == col == n - 1:
                    return True
                for new_row, new_col in [
                    (row, col + 1),
                    (row + 1, col),
                    (row, col - 1),
                    (row - 1, col),
                ]:
                    if (
                        0 <= new_row < n
                        and 0 <= new_col < n
                        and grid[new_row][new_col] <= t
                        and (new_row, new_col) not in visited
                    ):
                        stack.append((new_row, new_col))
                        visited.add((new_row, new_col))
            return False

        lo, hi = grid[0][0], n * n
        while lo < hi:
            mid = (lo + hi) // 2
            if not check(mid):
                lo = mid + 1
            else:
                hi = mid
        return lo

        # Time complexity
        ## iteration -> O(logN)
        ## check -> O(N^2)
        ### O(N^2logN)

        # Space complexity
        ### O(N^2)
