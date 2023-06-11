class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        if m == 0 or n == 0:
            return max(m, n)
        if m < n:
            return self.minDistance(word2, word1)
        
        dp = [i for i in range(m + 1)]
        for j in range(n):
            next = [0] * (m + 1)
            next[0] = dp[0] + 1
            for k in range(1,m + 1):
                if word1[k - 1] == word2[j]:
                    next[k] = dp[k - 1]
                else:
                    next[k] = min(dp[k - 1], dp[k], next[k - 1]) + 1
            dp = next
        return dp[m]
        
