class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        ans = -1
        memo = {}
        for i, char in enumerate(s):
            if char in memo:
                ans = max(ans, i - 1 - memo[char])
            else:
                memo[char] = i
        return ans

        # Time complexity
        ## iteration -> O(N)
        ### O(N)

        # Space complexity
        ## memo -> 26 at worst
        ### constant
