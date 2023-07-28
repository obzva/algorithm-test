import collections


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        cnt = collections.Counter(s)
        ans = ""
        for o in order:
            ans = ans + o * cnt[o]
            cnt[o] = 0
        for c in cnt:
            ans = ans + c * cnt[c]
        return ans

# time complexity

# let n and m = len(order) and len(s)
# O(n + m)

# space complexity

# O(m)