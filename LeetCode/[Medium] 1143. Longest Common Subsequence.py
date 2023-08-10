from functools import cache

# class Solution:
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         n, m = len(text1) , len(text2)
#         @cache
#         def dp(i: int, j: int) -> int:
#             if i < 0 or j < 0:
#                 return 0
#             if text1[i] == text2[j]:
#                 return dp(i - 1, j - 1) + 1
#             else:
#                 return max(dp(i, j - 1), dp(i - 1, j))

#         return dp(n - 1, m - 1)

#         # Time complexity
#         ## O(NM) at worst
#         ### O(NM)

#         # Space complexity
#         ## recursion -> O(max(N, M)) at worst
#         ## cache -> O(NM) at worst
#         ### O(NM)

# https://leetcode.com/problems/longest-common-subsequence/editorial/

# 1. Recursion
# class Solution:
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         n, m = len(text1) , len(text2)
#         @cache
#         def dp(i: int, j: int) -> int:
#             if i == n or j == m: # end of searching
#                 return 0

#             case1 = dp(i + 1, j) # not including the first character of text1 in next search

#             first_occurence = text2.find(text1[i], j)
#             case2 = 0
#             if first_occurence != -1: # text1[i] in text2
#                 case2 = 1 + dp(i + 1, first_occurence + 1)

#             return max(case1, case2)

#         return dp(0, 0)

#     # Time complexity
#     ## dp -> O(NM) at worst
#     ## finding first_occurence -> O(M)
#     ### O(N*M^2)

#     # Space complexity
#     ## recursion -> O(max(N, M)) at worst
#     ## cache -> O(NM) at worst
#     ### O(NM)

# 2. Iteration (In many programming languages, iteration is faster than recursion because of overhead)
# class Solution:
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         n, m = len(text1), len(text2)
#         memo = [[0] * (n + 1) for _ in range(m + 1)]
#         for i in reversed(range(m)):
#             for j in reversed(range(n)):
#                 if text2[i] == text1[j]:
#                     memo[i][j] = memo[i + 1][j + 1] + 1
#                 else:
#                     memo[i][j] = max(memo[i][j + 1], memo[i + 1][j])
#         return memo[0][0]

#     # Time complexity
#     ## constructing memo -> O((N + 1) * (M + 1))
#     ## iteration -> O(N * M)
#     ### O(N * M)

#     # Space complexity
#     ## memo -> O((N + 1) * (M + 1))
#     ### O(N * M)


# 2'. Space-Optimized Iteration
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        memo, prev_memo = [0] * (n + 1), [0] * (n + 1)
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                if text2[i] == text1[j]:
                    memo[j] = prev_memo[j + 1] + 1
                else:
                    memo[j] = max(memo[j + 1], prev_memo[j])
            prev_memo = memo[:]
        return memo[0]

    # Time complexity
    ## constructing memo -> O((N + 1) * 2)
    ## iteration -> O(N * M)
    ## re-assigning prev_memo -> O(N + 1)
    ## O(2 * (N + 1) + O(M * (2 * N + 1)))
    ### O(N * M)

    # Space complexity
    ## memo -> O(2 * (N + 1))
    ### O(N)
