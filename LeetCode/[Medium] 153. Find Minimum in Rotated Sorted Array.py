# Binary Search

# Time complexity: O(logN)
# Space complexity: const

class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        if nums[lo] < nums[hi]:
            return nums[lo]

        while lo < hi:
            mid = (hi - lo) // 2 + lo
            if lo == mid:
                # if you don't understand this part, think about two cases that can reach this state
                lo = mid + 1
            elif nums[lo] > nums[mid] and nums[mid] < nums[hi]:
                hi = mid
            elif nums[lo] < nums[mid] and nums[mid] > nums[hi]:
                lo = mid
        return nums[lo]