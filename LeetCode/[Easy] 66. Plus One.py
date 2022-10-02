from typing import *


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        reverse = digits[::-1]
        reverse[0] += 1
        for i in range(len(reverse)):
            if reverse[i] == 10:
                reverse[i] = 0
                if i == len(reverse) - 1:
                    reverse.append(1)
                else:
                    reverse[i + 1] += 1
            else:
                return reverse[::-1]
        return reverse[::-1]


class Solution1:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        for i in range(len(digits) - 1, 0, -1):
            if digits[i] != 10:
                break
            digits[i] = 0
            digits[i - 1] += 1

        if digits[0] == 10:
            digits[0] = 0
            return [1] + digits
        return digits
