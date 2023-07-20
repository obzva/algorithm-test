class Solution:
    def removePalindromeSub(self, s: str) -> int:
        # if s is empty string: 0
        # else if s is palindromic string : 1
        # else : 2
        return 0 if s == "" else 1 if s == s[::-1] else 2