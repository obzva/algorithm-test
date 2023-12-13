# Using hashmap

# Time complexity: O(M + N), for M = len(s1) and N = len(s2)
# Space complexity: const, maximum 26 for each map

from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1map = Counter(s1)

        def check(hash):
            for key in s1map:
                if key not in hash or hash[key] != s1map[key]:
                    return False
            return True

        substrmap = {}
        for i in range(len(s1)):
            char = s2[i]
            if char not in substrmap:
                substrmap[char] = 1
            else:
                substrmap[char] += 1
        if check(substrmap):
            return True

        for i in range(len(s1), len(s2)):
            new_char, old_char = s2[i], s2[i - len(s1)]

            substrmap[old_char] -= 1
            if substrmap[old_char] == 0:
                del substrmap[old_char]

            if new_char not in substrmap:
                substrmap[new_char] = 1
            else:
                substrmap[new_char] += 1

            if check(substrmap):
                return True

        return False
