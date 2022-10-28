from typing import *


class DoubleLinkedNode:
    def __init__(self, val: int = None):
        self.prev = None
        self.next = None
        self.val = val


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # BUILT-IN
        # for _ in range(k):
        #     node = nums.pop()
        #     nums.insert(0, node)

        # USING DLN
        # head = DoubleLinkedNode()
        # tail = DoubleLinkedNode()
        # head.next = tail
        # tail.prev = head
        #
        # for num in nums:
        #     node = DoubleLinkedNode(num)
        #     node.prev = tail.prev
        #     node.next = tail
        #     tail.prev.next = node
        #     tail.prev = node
        #
        # for _ in range(k):
        #     popped = tail.prev
        #     popped.prev.next, popped.next.prev = popped.next, popped.prev
        #     popped.prev = head
        #     popped.next = head.next
        #     head.next.prev = popped
        #     head.next = popped
        #
        # head = head.next
        # for i in range(len(nums)):
        #     nums[i] = head.val
        #     head = head.next

        # REVERSE
        # def reverse(arr, start, end):
        #     while start < end:
        #         arr[start], arr[end] = arr[end], arr[start]
        #         start += 1
        #         end -= 1
        #
        # n, k = len(nums) - 1, k % len(nums)
        # reverse(nums, 0, n)
        # reverse(nums, 0, k - 1)
        # reverse(nums, k, n)

        # ITERATIVE
        n = len(nums)
        k %= n
        count = start = 0
        while count < n:
            current_idx = start
            prev = nums[current_idx]
            while True:
                next_idx = (current_idx + k) % n
                prev, nums[next_idx] = nums[next_idx], prev
                count += 1
                if next_idx == start:
                    break
                current_idx = next_idx
            start += 1
