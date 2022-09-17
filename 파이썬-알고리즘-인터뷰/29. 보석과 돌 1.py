class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freq = {}
        for stone in stones:
            if stone not in freq:
                freq[stone] = 1
            else:
                freq[stone] += 1

        count = 0
        for jewel in jewels:
            if jewel in freq:
                count += freq[jewel]

        return count
