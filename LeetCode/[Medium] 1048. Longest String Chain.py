from functools import cache

# class Solution:
#     def longestStrChain(self, words: List[str]) -> int:
#         s_words = sorted(words, key=len)
#         n = len(s_words)

#         def check(short: str, long: str) -> bool:
#             if len(short) + 1 != len(long):
#                 return False
#             i, j = 0, 0
#             while i < len(short) and j < len(long):
#                 if short[i] == long[j]:
#                     i += 1
#                     if i == len(short):
#                         return True
#                 j += 1
#             return False

#         ans = 1
#         memo = [1] * len(s_words)

#         for i in reversed(range(n - 1)):
#             res = 1
#             for j in range(i + 1, n):
#                 if check(s_words[i], s_words[j]):
#                     res = max(res, memo[j] + 1)
#             memo[i] = res
#             ans = max(ans, res)

#         return ans

#         # Time complexity
#         ## sorted -> O(NlogN)
#         ## check -> O(m) at worst for a long word whose length is m
#         ## iteration -> O(N^2)
#         ### O(N^2*m)

#         # Space complexity
#         ## s_words -> O(N)
#         ## memo -> O(N)
#         ### O(N)


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words_set = set(words)

        @cache
        def dfs(word: str) -> int:
            res = 1
            for i in range(len(word)):
                new_word = word[:i] + word[i + 1 :]
                if new_word in words_set:
                    curr = 1 + dfs(new_word)
                    res = max(res, curr)
            return res

        ans = 0
        for word in words:
            ans = max(ans, dfs(word))

        return ans

    # Time complexity
    ## constructing set -> O(N)
    ## iteration -> O(N)
    ## dfs -> O(L^2) (for word length L, recursion depth O(L) at most and iteration in dfs O(L))
    ### O(N*L^2)

    # Space complexity
    ## set -> O(N)