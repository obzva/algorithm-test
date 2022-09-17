"""
defaultdict
"""

import collections


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freq = collections.defaultdict(int)
        count = 0

        for stone in stones:
            freq[stone] += 1

        for jewel in jewels:
            count += freq[jewel]

        return count
