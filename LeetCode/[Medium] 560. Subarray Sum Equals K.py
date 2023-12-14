# Hashmap

# Time complexity: O(N), for iteration
# Space complexity: O(N), for subtotals


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap = {}
        hashmap[0] = 1

        acc, cnt = 0, 0
        for num in nums:
            acc += num
            if acc - k in hashmap:
                cnt += hashmap[acc - k]
            hashmap[acc] = hashmap.get(acc, 0) + 1

        return cnt
