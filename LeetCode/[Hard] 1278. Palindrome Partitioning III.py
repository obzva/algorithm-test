from functools import cache


class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        n = len(s)

        # costs of making substring[i, j] into palindrome
        @cache
        def get_cost(start: int, end: int) -> int:
            res = 0
            while start < end:
                if s[start] != s[end]:
                    res += 1
                start += 1
                end -= 1
            return res

        # answer of m partitioning for s[i:]
        @cache
        def dp(i: int, m: int) -> int:
            # base case, each partition just have one character
            if n - i == m:
                return 0
            # base case, s[i:] should be a palindrome string
            if m == 1:
                return get_cost(i, n - 1)
            res = n
            for j in range(i + 1, n - m + 2):
                res = min(res, get_cost(i, j - 1) + dp(j, m - 1))
            return res

        return dp(0, k)

    # Time complexity
    ## get_cost -> O(N) at worst
    ## dp -> O(N * k) for unique (i, m) pair and get_cost function call for each pair -> O(N^2 * k)
    ### O(N^2 * k)

    # Space complexity
    ## recursion call stack -> O(k) at most
    ## get_cost cache -> O(N^2) at worst
    ## dp cache -> O(N * k) at worst
    ### O(N^2)
