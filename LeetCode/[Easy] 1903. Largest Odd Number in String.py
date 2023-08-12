class Solution:
    def largestOddNumber(self, num: str) -> str:
        i = len(num) - 1
        while i >= 0:
            digit = int(num[i])
            if digit % 2 == 0:
                i -= 1
            else:
                break
        return "" if i < 0 else num[: i + 1]

        # Time complexity
        ## iteration -> O(N) at worst
        ### O(N)

        # Space complexity
        ### constant
