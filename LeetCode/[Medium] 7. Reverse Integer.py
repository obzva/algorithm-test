class Solution:
    def reverse(self, x: int) -> int:
        minus = False

        if x < 0:
            x = -x
            minus = True

        ans = 0
        for _ in range(len(str(x))):
            ans = ans * 10 + x % 10
            x //= 10

        if minus:
            ans = -ans

        if -2 ** 31 > ans or ans > 2 ** 31 - 1:
            return 0
        else:
            return ans
