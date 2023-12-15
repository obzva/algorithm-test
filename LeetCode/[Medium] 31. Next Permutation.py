# My solution - find gradient change

# Time complexity: O(N + NlogN)
# Space complexity: O(N)


# class Solution:
#     def nextPermutation(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         n = len(nums)
#         index = -1
#         for i in range(n - 1):
#             num1, num2 = nums[n - i - 2], nums[n - i - 1]
#             if num1 >= num2:
#                 continue
#             else:
#                 index = n - i - 2
#                 break
#         if index == -1:
#             nums.sort()
#         else:
#             nums_to_reorder = sorted(nums[index:])
#             for i in range(len(nums_to_reorder)):
#                 num = nums_to_reorder[i]
#                 if num > nums[index]:
#                     del nums_to_reorder[i]
#                     nums_to_reorder = [num] + nums_to_reorder
#                     break

#             nums[index:] = nums_to_reorder

# Another implementation

# Time complexity: O(N)
# Space complexity: const

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        if n == 1:
            return

        index = -1

        for i in range(n - 1):
            num1, num2 = nums[n - i - 2], nums[n - i - 1]
            if num1 >= num2:
                continue
            else:
                index = n - i - 2
                break

        # there was no decreasing
        if index == -1:
            nums.sort()
            return

        for i in reversed(range(index + 1, n)):
            if nums[i] > nums[index]:
                nums[index], nums[i] = nums[i], nums[index]
                nums[index + 1 :] = nums[index + 1 :][::-1]
                return
