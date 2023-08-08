# from functools import cache

# class Solution:
#     def longestPalindromeSubseq(self, s: str) -> int:
#         @cache
#         def LPS(start: int, end: int) -> int:
#             if start > end:
#                 return 0
#             elif start == end:
#                 return 1
#             elif s[start] == s[end]:
#                 return 2 + LPS(start + 1, end - 1)
#             else:
#                 return max(LPS(start + 1, end), LPS(start, end - 1))
#         return LPS(0, len(s) - 1)

#     # Time complexity:
#     ## for the worst case, we should call the function LPS for every (start, end) -> O(N^2)
#     ### O(N^2)

#     # Space complexity:
#     ## cache -> O(N^2)
#     ## for the worst case, recursive call stack -> O(N)
#     ### O(N^2)


# class Solution:
#     def longestPalindromeSubseq(self, s: str) -> int:
#         n = len(s)
#         memo = [[0] * n for _ in range(n)]
#         for i in reversed(range(n)):
#             memo[i][i] = 1
#             for j in range(i + 1, n):
#                 if s[i] == s[j]:
#                     memo[i][j] = 2 + memo[i + 1][j - 1]
#                 else:
#                     memo[i][j] = max(memo[i + 1][j], memo[i][j - 1])
#         return memo[0][n - 1]

#     # Time complexity:
#     ## iteration -> O(N^2)
#     ### O(N^2)

#     # Space complexity:
#     ## memo list -> O(N^2)
#     ### O(N^2)

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        memo, memo_prev = [0] * n, [0] * n
        for i in reversed(range(n)):
            memo[i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    memo[j] = 2 + memo_prev[j - 1]
                else:
                    memo[j] = max(memo_prev[j], memo[j - 1])
            memo_prev = memo[:]
        return memo[n - 1]

    # Time complexity:
    ## for i -> O(N)
    ## for j -> O(N)
    ## shallow copying -> O(N)
    ### O(N^2)

    # Space complexity:
    ## memo list -> O(N^2)
    ## memo_prev list -> O(N^2)
    ### O(N^2)