import math


class Solution:
    def numSquares(self, n: int) -> int:
        # BRUTE FORCE RECURSION
        # squares = [num * num for num in range(1, int(math.sqrt(n)) + 1)]
        #
        # def get_min_num_squares(m: int) -> int:
        #     if m in squares:
        #         return 1
        #     min_num = sys.maxsize
        #     for square in squares:
        #         if m < square:
        #             break
        #         num = get_min_num_squares(m - square) + 1
        #         min_num = min(min_num, num)
        #     return min_num
        #
        # return get_min_num_squares(n)

        # BOTTOM-UP MEMOIZATION
        # if n < 4:
        #     return n
        # squares = [num * num for num in range(1, int(math.sqrt(n)) + 1)]
        # memo = [sys.maxsize] * (n + 1)
        # memo[0:4] = [0, 1, 2, 3]
        #
        # for i in range(4, n + 1):
        #     for square in squares:
        #         if i < square:
        #             break
        #         memo[i] = min(memo[i], memo[i - square] + 1)
        # return memo[-1]

        # GREEDY
        # squares = [num * num for num in range(1, int(math.sqrt(n)) + 1)]
        #
        # def can_divided_by(m: int, count: int) -> bool:
        #     if count == 1:
        #         return m in squares
        #     for square in squares:
        #         if m <= square:
        #             break
        #         if can_divided_by(m - square, count - 1):
        #             return True
        #     return False
        #
        # for i in range(1, n + 1):
        #     if can_divided_by(n, i):
        #         return i

        # GREEDY BFS
        squares = [num * num for num in range(1, int(math.sqrt(n)) + 1)]
        remainders = set()
        remainders.add(n)
        level = 0
        while True:
            level += 1
            new_remainders = set()
            for remainder in remainders:
                if remainder in squares:
                    return level
                for square in squares:
                    if remainder < square:
                        break
                    new_remainders.add(remainder - square)
            remainders = new_remainders
