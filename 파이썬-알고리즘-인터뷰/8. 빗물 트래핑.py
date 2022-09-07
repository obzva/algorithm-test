from typing import *


class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = [], []
        left_max, right_max = 0, 0
        for i in range(len(height)):
            if height[i] > left_max:
                left_max = height[i]
            if height[len(height) - 1 - i] > right_max:
                right_max = height[len(height) - 1 - i]
            right.append(right_max)
            left.append(left_max)
        right.reverse()

        water = 0
        for i in range(len(height)):
            water += min(left[i], right[i]) - height[i]

        return water
