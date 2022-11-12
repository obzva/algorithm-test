class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # RECURSIVE
        memo = dict()

        def dp(i: int, j: int) -> bool:
            if (i, j) not in memo:
                if j == len(p):
                    ans = i == len(s)
                else:
                    if p[j] == '*':
                        ans = dp(i, j + 1) or i < len(s) and dp(i + 1, j)
                    else:
                        ans = i < len(s) and p[j] in {s[i], '?'} and dp(i + 1, j + 1)
                memo[i, j] = ans
            return memo[i, j]

        return dp(0, 0)
       