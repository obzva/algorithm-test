class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0

        def onion(lo: int, hi: int) -> int:
            res = 0
            while 0 <= lo and hi < len(s):
                if s[lo] != s[hi]:
                    break
                lo -= 1
                hi += 1
                res += 1
            return res

        for i in range(len(s)):
            ans += onion(i, i)
            ans += onion(i, i + 1)
        return ans

        # time complexity: O(N^2)
        # space complexity: O(1)
