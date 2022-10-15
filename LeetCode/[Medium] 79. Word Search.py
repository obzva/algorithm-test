from typing import *


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        m = len(board)
        n = len(board[0])

        def back_track(row: int, col: int, suffix: str) -> bool:
            if len(suffix) == 0:
                return True
            if not (0 <= row < m and 0 <= col < n) or board[row][col] != suffix[0]:
                return False

            board[row][col] = '#'
            for dr, dc in directions:
                if back_track(row + dr, col + dc, suffix[1:]):
                    return True

            board[row][col] = suffix[0]
            return False

            # IN THIS WAY, WE CAN PRESERVE THE ORIGINAL VALUES OF THE MATRIX
            # board[row][col] = '#'
            # return_value = False
            # for dr, dc in directions:
            #     if back_track(row + dr, col + dc, suffix[1:]):
            #         return_value = True
            #         break
            #
            # board[row][col] = suffix[0]
            # return return_value

        for i in range(m):
            for j in range(n):
                if back_track(i, j, word):
                    return True
        return False
