class Solution:
    def mySqrt(self, x: int) -> int:
        def binary(left, right):
            mid = left + (right - left) // 2
            if mid ** 2 <= x < (mid + 1) ** 2:
                return mid
            elif x < mid ** 2:
                return binary(left, mid - 1)
            else:
                return binary(mid + 1, right)

        return binary(0, x)
