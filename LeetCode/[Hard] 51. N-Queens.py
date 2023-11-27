class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        answer = []
        queens = set()
        cols = [True] * n
        hill_dia = [True] * (2 * n - 1)
        dale_dia = [True] * (2 * n - 1)

        def check_place(row, col):
            return (
                True
                if cols[col] and hill_dia[row + col] and dale_dia[row - col]
                else False
            )

        def place_queen(row, col):
            cols[col] = False
            hill_dia[row + col] = False
            dale_dia[row - col] = False
            queens.add((row, col))

        def add_answer():
            board = []
            for _, col in sorted(queens, key=lambda x: x[0]):
                board.append("." * col + "Q" + "." * (n - 1 - col))
            answer.append(board)

        def remove_queen(row, col):
            queens.remove((row, col))
            cols[col] = True
            hill_dia[row + col] = True
            dale_dia[row - col] = True

        def backtrack(row):
            for col in range(n):
                if check_place(row, col):
                    place_queen(row, col)
                    if row + 1 == n:
                        add_answer()
                    else:
                        backtrack(row + 1)
                    remove_queen(row, col)

        backtrack(0)
        return answer
