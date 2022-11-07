from typing import *


class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.board = [[0] * n for _ in range(n)]
        self.dia_left_to_right = [[i, i] for i in range(self.n)]
        self.dia_right_to_left = [[i, self.n - 1 - i] for i in range(self.n)]

    def _check_win(self, player: int, line: List[List[int]]) -> bool:
        for row, col in line:
            if self.board[row][col] != player:
                return False
        return True

    def move(self, row: int, col: int, player: int) -> int:
        self.board[row][col] = player
        if self._check_win(player, [[row, i] for i in range(self.n)]):
            return player
        if self._check_win(player, [[i, col] for i in range(self.n)]):
            return player
        if [row, col] in self.dia_right_to_left and self._check_win(player, self.dia_right_to_left):
            return player
        if [row, col] in self.dia_left_to_right and self._check_win(player, self.dia_left_to_right):
            return player
        return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
