from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        ans = 0
        add_odd = True
        cnt = Counter(s)
        for char in cnt:
            num = cnt[char]
            if num % 2 == 0:
                ans += num
            else:
                if add_odd:
                    ans += 1
                    add_odd = not add_odd
                while num > 2:
                    ans += 2
                    num -= 2
        return ans

        # Time complexity
        ## building Counter -> O(N)
        ## iteration -> const
        ## while -> O(N/2) at worst
        ### O(N)

        # Space complexity
        ### const
