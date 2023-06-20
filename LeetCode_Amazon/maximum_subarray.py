class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # kadane
        # current = nums[0]
        # res = nums[0]
        # for num in nums[1:]:
        #     if current < 0:
        #         current = 0
        #     current += num
        #     res = max(res, current)
        # return res

        # divide and conquer
        def rec(left, right):
            if left > right:
                return -math.inf
            mid = (left + right) // 2
            curr = best_left_sum = best_right_sum = 0
            for i in range(mid - 1, left - 1, -1):
                curr += nums[i]
                best_left_sum = max(best_left_sum, curr)
            curr = 0
            for i in range(mid + 1, right + 1):
                curr += nums[i]
                best_right_sum = max(best_right_sum, curr)
            best_combined_sum = nums[mid] + best_left_sum + best_right_sum
            left_half = rec(left, mid - 1)
            right_half = rec(mid + 1, right)
            return max(best_combined_sum, left_half, right_half)

        return rec(0, len(nums) - 1)
