class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        if n == 1:
            return ""
        i = 0
        while i < n // 2:
            char = palindrome[i]
            if char == "a":
                i += 1
            else:
                return palindrome[:i] + "a" + palindrome[i + 1 :]
        return palindrome[:-1] + "b"

    # Time complexity
    ## iteration -> O(N / 2)
    ## return -> O(N)
    ### O(N)

    # Space complexity
    ### const
