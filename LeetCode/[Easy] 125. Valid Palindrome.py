class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_alnum = [ch.lower() for ch in s if ch.isalnum()]
        return s_alnum == s_alnum[::-1]
