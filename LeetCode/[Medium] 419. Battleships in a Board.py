# class Solution:
#     def countBattleships(self, board: List[List[str]]) -> int:
#         directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
#         m, n = len(board), len(board[0])
#         visited = set()
#         res = 0
#         def is_battleship(input: str) -> bool:
#             return True if input == 'X' else False
#         def search_linearly(r: int, c: int, dr: int, dc: int):
#             new_r, new_c = r + dr, c + dc
#             if 0 <= new_r < m and 0 <= new_c < n:
#                 if (new_r, new_c) in visited:
#                     return
#                 else:
#                     visited.add((new_r, new_c))
#                     if is_battleship(board[new_r][new_c]):
#                         search_linearly(new_r, new_c, dr, dc)

#         for row in range(m):
#             for col in range(n):
#                 if (row, col) in visited:
#                     continue
#                 else:
#                     visited.add((row, col))
#                     if is_battleship(board[row][col]):
#                         res += 1
#                         for direction in directions:
#                             dr, dc = direction
#                             search_linearly(row, col, dr, dc)
#         return res

#         # Time complexity
#         ## Iteration -> O(NM)
#         ### O(NM)

#         # Space complexity
#         ## visited -> O(NM)


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        m, n = len(board), len(board[0])
        res = 0

        def is_topleft_X(r: int, c: int) -> bool:
            if board[r][c] == "X":
                if 0 <= c - 1 and board[r][c - 1] == "X":
                    return False
                if 0 <= r - 1 and board[r - 1][c] == "X":
                    return False
                return True
            return False

        for row in range(m):
            for col in range(n):
                if is_topleft_X(row, col):
                    res += 1
        return res

        # Time complexity
        ## Iteration -> O(NM)
        ### O(NM)

        # Space complexity
        ### constant
