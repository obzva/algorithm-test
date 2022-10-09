from typing import *


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            nums_row = [x for x in board[i] if x != '.']
            if len(nums_row) != len(set(nums_row)):
                return False

            nums_col = []
            for j in range(9):
                if board[j][i] != '.':
                    nums_col.append(board[j][i])
            if len(nums_col) != len(set(nums_col)):
                return False

            nums_box = []
            q = i // 3
            r = i % 3
            for k in range(3 * q, 3 * (q + 1)):
                for l in range(r * 3, 3 * (r + 1)):
                    if board[k][l] != '.':
                        nums_box.append(board[k][l])
            if len(nums_box) != len(set(nums_box)):
                return False
        return True
