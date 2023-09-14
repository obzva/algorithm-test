class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)
        i, j = 0, 0
        while 0 <= i < n and 0 <= j < m:
            if i == n:
                return True
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == n

        # Time complexity
        ### O(max(N, M))

        # Space complexity
        ### constant
