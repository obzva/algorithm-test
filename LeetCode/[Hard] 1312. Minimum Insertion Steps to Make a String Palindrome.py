from functools import cache


class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        if n == 1:
            return 0

        @cache
        def dp(r: int, c: int) -> int:
            if r >= c:
                return 0
            elif s[r] == s[c]:
                return dp(r + 1, c - 1)
            else:
                return min(dp(r + 1, c), dp(r, c - 1)) + 1

        return dp(0, n - 1)
