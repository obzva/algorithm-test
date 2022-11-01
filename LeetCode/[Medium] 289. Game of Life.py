import collections
from typing import *


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
        m, n = len(board), len(board[0])

        # WITH EXTRA SPACE O(mn)

        # directions = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
        # m, n = len(board), len(board[0])
        # near_live_cells = [[0] * n for _ in range(m)]
        # for row in range(m):
        #     for col in range(n):
        #         if board[row][col]:
        #             for dr, dc in directions:
        #                 if 0 <= row + dr < m and 0 <= col + dc < n:
        #                     near_live_cells[row + dr][col + dc] += 1
        # for row in range(m):
        #     for col in range(n):
        #         if board[row][col]:
        #             if near_live_cells[row][col] < 2:
        #                 board[row][col] = 0
        #             elif near_live_cells[row][col] > 3:
        #                 board[row][col] = 0
        #         else:
        #             if near_live_cells[row][col] == 3:
        #                 board[row][col] = 1

        # IN-PLACE

        # for row in range(m):
        #     for col in range(n):
        #         count = 0
        #         for dr, dc in directions:
        #             if 0 <= row + dr < m and 0 <= col + dc < n and abs(board[row + dr][col + dc]) == 1:
        #                 count += 1
        #         if board[row][col] == 1 and (count < 2 or count > 3):
        #             board[row][col] = -1  # DEAD NEXT BUT LIVE NOW
        #         elif board[row][col] == 0 and count == 3:
        #             board[row][col] = 2  # LIVE NEXT BUT DEAD NOW
        # for row in range(m):
        #     for col in range(n):
        #         if board[row][col] == -1:
        #             board[row][col] = 0
        #         elif board[row][col] == 2:
        #             board[row][col] = 1

        # CHECK ONLY LIVE CELLS

        live = {(i, j)
                for i, row in enumerate(board)
                for j, cell in enumerate(row)
                if cell}

        def get_new_coord_set(coord_set: set) -> set:
            new_coord_cand_set = collections.Counter((ni, nj)
                                                     for i, j in coord_set
                                                     for ni in range(i - 1, i + 2)
                                                     for nj in range(j - 1, j + 2)
                                                     if ni != i or nj != j
                                                     )
            return {coord
                    for coord in new_coord_cand_set
                    if new_coord_cand_set[coord] == 3 or new_coord_cand_set[coord] == 2 and coord in coord_set}

        live = get_new_coord_set(live)

        for row in range(m):
            for col in range(n):
                board[row][col] = int((row, col) in live)
