import collections


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # SOLUTION 1
        #
        # return sorted(s) == sorted(t)

        # SOLUTION 2

        check = collections.Counter(s)
        for char in t:
            if char not in check:
                return False
            check[char] -= 1
        return max(check.values()) == 0