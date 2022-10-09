class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1]:
            return s

        def sliding_window(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        ans = ''
        for i in range(len(s) - 1):
            ans = max(ans, sliding_window(i, i + 1), sliding_window(i, i + 2), key=len)
        return ans
