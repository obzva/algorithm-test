from typing import *


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # BRUTE FORCE - TIME LIMIT EXCEED

        # n = len(heights)
        # if n == 1:
        #     return heights[0]
        # ans = -sys.maxsize
        # for i in range(n):
        #     h = heights[i]
        #     for j in range(n):
        #         w = j - i + 1
        #         h = min(h, heights[j])
        #         ans = max(ans, w * h)
        # return ans

        # MEMOIZATION - TIME LIMIT EXCEED

        # memo = dict()
        #
        # def dp(start: int, end: int):
        #     if (start, end) not in memo:
        #         height = min(h for h in heights[start: end + 1])
        #         width = end - start + 1
        #         memo[start, end] = height * width
        #     if end + 1 < len(heights):
        #         dp(start + 1, end + 1)
        #         dp(start, end + 1)
        #
        # dp(0, 0)
        # return max(memo.values())

        # BACKTRACKING - TIME LIMIT EXCEED

        # memo = dict()
        #
        # def dp(start: int, end: int) -> int:
        #     if end == len(heights):
        #         memo[start, end] = -sys.maxsize
        #         return memo[start, end]
        #
        #     if (start, end) not in memo:
        #         curr_area = (end - start + 1) * min(h for h in heights[start: end + 1])
        #         next_area1 = dp(start + 1, end + 1)
        #         next_area2 = dp(start, end + 1)
        #         ans = max(curr_area, next_area1, next_area2)
        #         memo[start, end] = ans
        #     return memo[start, end]
        #
        # return dp(0, 0)

        # DIVIDE AND CONQUER - TIME LIMIT EXCEED

        # def get_min_index(start: int, end: int) -> int:
        #     min_index = start
        #     for i in range(start, end + 1):
        #         if heights[i] < heights[min_index]:
        #             min_index = i
        #     return min_index
        #
        # def dnc(start: int, end: int) -> int:
        #     if start > end:
        #         return 0
        #     min_index = get_min_index(start, end)
        #     return max(
        #         (end - start + 1) * heights[min_index],
        #         dnc(start, min_index - 1),
        #         dnc(min_index + 1, end)
        #     )
        #
        # return dnc(0, len(heights) - 1)

        # USING STACK

        """
        1	Idea is, we will consider every element a[i] to be a candidate for the area calculation. That is, if a[i] is the minimum element then what is the maximum area possible for all such rectangles? We can easily figure out that it's a[i]*(R-L+1-2) or a[i] * (R-L-1), where a[R] is first subsequent element(R>i) in the array just smaller than a[i], similarly a[L] is first previous element just smaller than a[i]. makes sense? (or take a[i] as a center and expand it to left and i and stop when first just smaller elements are found on both the sides). But how to implement it efficiently?
	    2	We add the element a[i] directly to the stack if it's greater than the peak element (or a[i-1] ), because we are yet to find R for this. Can you tell what's L for this? Exactly, it's just the previous element in stack. (We will use this information later when we will pop it out).
	    3	What if we get an element a[i] which is smaller than the peak value, it is the R value for all the elements present in stack which are greater than a[i]. Pop out the elements greater than a[i], we have their R value and L value(point 2). and now push a[i] and repeat..
        """

        stack = [-1]
        answer = 0
        for i, height in enumerate(heights):
            while stack[-1] != -1 and height <= heights[stack[-1]]:
                current_height = heights[stack.pop()]
                current_width = i - stack[-1] - 1
                answer = max(answer,
                             current_height * current_width
                             )
            stack.append(i)
        while stack[-1] != -1:
            current_height = heights[stack.pop()]
            current_width = len(heights) - stack[-1] - 1
            answer = max(answer, current_height * current_width)
        return answer
