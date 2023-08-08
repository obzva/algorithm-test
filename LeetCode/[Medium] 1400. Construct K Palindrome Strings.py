class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) == k:
            return True
        cnt = collections.Counter(s)
        number_of_odds = 0
        for char in cnt:
            if cnt[char] % 2 == 1:
                number_of_odds += 1
        return number_of_odds <= k <= len(s)


# Time complexity:
## len(s) -> O(1)
## constructing Counter -> O(N)
## iteration over Counter -> O(N)
### O(N)

# Space complexity
## Counter -> O(N)
## number_of_odds -> O(1)
### O(N)
