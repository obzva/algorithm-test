import collections
import sys


class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # BRUTE FORCE

        # if len(t) == 1:
        #     return t if t in s else ""
        # for i in range(2, len(s) + 1):
        #     for start in range(len(s) - i + 1):
        #         if all(char in s[start: start + i] for char in t):
        #             return s[start: start + i]
        # return ""

        # SLIDING WINDOW

        if not t or not s:
            return ""

        dict_t = collections.Counter(t)
        required = len(dict_t)

        left = right = 0
        formed = 0
        window_counts = collections.Counter()
        ans = (sys.maxsize, None, None)

        while right < len(s):
            char = s[right]
            window_counts[char] += 1

            if char in dict_t and window_counts[char] == dict_t[char]:
                formed += 1

            while left <= right and formed == required:
                char = s[left]
                if right - left + 1 < ans[0]:
                    ans = (right - left + 1, left, right)

                window_counts[char] -= 1
                if char in dict_t and window_counts[char] < dict_t[char]:
                    formed -= 1

                left += 1
            right += 1
        return "" if ans[0] == sys.maxsize else s[ans[1]:ans[2] + 1]
