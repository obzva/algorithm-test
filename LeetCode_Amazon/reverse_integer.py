class Solution:
    def reverse(self, x: int) -> int:
        ans = 0
        if x < 0:
            sign = -1
            x *= -1
        else:
            sign = 1
        while x > 0:
            ans = ans * 10 + x % 10
            x //= 10
        return (
            ans * sign if -math.pow(2, 31) <= ans * sign <= math.pow(2, 31) - 1 else 0
        )
