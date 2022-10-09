class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        is_negative = (dividend < 0) != (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)

        quotient = 0
        tmp_sum = divisor

        while dividend - divisor >= 0:
            current_q = 1
            while dividend - (tmp_sum << 1) >= 0:
                tmp_sum <<= 1
                current_q <<= 1
            dividend -= tmp_sum
            tmp_sum = divisor
            quotient += current_q

        return min(2147483647, max(-quotient if is_negative else quotient, -2147483648))
