class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 1:
            return s
        dp = [[False for i in range(n)] for j in range(n)]
        start, end = 0, 0
        for i in range(n):
            dp[i][i] = True
            if i < n - 1 and s[i] == s[i + 1]:
                dp[i][i + 1] = True
                start, end = i, i + 1
        for diff in range(2, n):
            for i in range(0, n - diff):
                if s[i] == s[i + diff] and dp[i + 1][i + diff - 1]:
                    dp[i][i + diff] = True
                    if end - start < diff:
                        start, end = i, i + diff
        return s[start : end + 1]
