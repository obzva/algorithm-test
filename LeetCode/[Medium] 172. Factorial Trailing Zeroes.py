class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n < 5:
            return 0

        result = 0
        denominator = 5
        quotient = n // denominator
        while quotient:
            result += quotient
            denominator *= 5
            quotient = n // denominator

        return result
