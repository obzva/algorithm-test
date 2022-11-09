class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        # DIVIDE AND CONQUER

        # if not s:
        #     return 0
        #
        # count = collections.Counter(s)
        #
        # if all(count[char] >= k for char in s):
        #     return len(s)
        #
        # mid = None
        # for char in count:
        #     if count[char] < k:
        #         mid = s.index(char)
        #         break
        #
        # left = self.longestSubstring(s[:mid], k)
        # right = self.longestSubstring(s[mid + 1:], k)
        #
        # return max(left, right)

        # DIVIDE AND CONQUER - SPLIT

        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(t, k) for t in s.split(c))
        return len(s)
