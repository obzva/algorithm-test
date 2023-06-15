class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        dict = {s[0]: 0}
        i, j = 0, 0
        ans = 1
        while j < n - 1:
            j += 1
            if s[j] in dict and dict[s[j]] >= i:
                i = dict[s[j]] + 1
            dict[s[j]] = j
            ans = max(ans, j - i + 1)
        return ans
