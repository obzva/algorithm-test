"""
Counter
"""

import collections


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freq = collections.Counter(stones)
        count = 0

        for jewel in jewels:
            count += freq[jewel]
            # Counter는 존재하지 않는 키의 경우 KeyError를 발생하는 게 아니라 0을 출력해 준

        return count
