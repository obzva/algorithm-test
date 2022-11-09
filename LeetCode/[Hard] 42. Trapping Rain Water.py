from typing import *


class Solution:
    def trap(self, height: List[int]) -> int:
        # MY SOLUTION ; ITERATION TWICE

        # water = []
        # max_height = -sys.maxsize
        # for h in height:
        #     max_height = max(max_height, h)
        #     water.append(max_height)
        # max_height = -sys.maxsize
        # for i in range(len(water) - 1, - 1, -1):
        #     max_height = max(max_height, height[i])
        #     water[i] = min(water[i], max_height)
        # return sum(water) - sum(height)

        # OPTIMIZATION TO ITERATION ONCE WITH TWO POINTER

        # water = 0
        # left, right = 0, len(height) - 1
        # left_max, right_max = height[left], height[right]
        # while left < right:
        #     left_max, right_max = max(left_max, height[left]), max(right_max, height[right])
        #     if left_max <= right_max:
        #         water += left_max - height[left]
        #         left += 1
        #     else:
        #         water += right_max - height[right]
        #         right -= 1
        # return water

        # STACK AND INFLECTION POINT

        stack = []
        answer = 0
        for i, h in enumerate(height):
            while stack and h > height[stack[-1]]:
                bottom = height[stack.pop()]
                if len(stack) == 0:
                    break
                answer += (i - stack[-1] - 1) * (min(height[stack[-1]], h) - bottom)

            stack.append(i)
        return answer
