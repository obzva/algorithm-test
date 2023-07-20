import collections

class Solution:
    def sortString(self, s: str) -> str:
        ans = ''
        count = collections.Counter(s)
        asc = True
        while count:
            for c in sorted(count) if asc else reversed(sorted(count)):
                ans += c
                count[c] -= 1
                if count[c] == 0:
                    del count[c]
            asc = not asc
        return ans
