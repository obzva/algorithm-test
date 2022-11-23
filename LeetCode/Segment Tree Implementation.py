from typing import *


class SegmentTree:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.size = len(nums)
        self.tree = [0] * (2 * self.size)
        self._build_tree()

    def _merge(self, a, b):
        # in this case merge means sum
        # return a + b

        # in this case merge means min
        return min(a, b)

    def _build_tree(self):
        for i in range(self.size):
            self.tree[i + self.size] = self.nums[i]
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = self._merge(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, index: int, val: int) -> None:
        index += self.size
        self.tree[index] = val
        while index > 0:
            if index % 2 == 0:
                left, right = index, index + 1
            else:
                left, right = index - 1, index
            self.tree[index // 2] = self._merge(self.tree[left], self.tree[right])
            index //= 2

    def sumRange(self, left: int, right: int) -> int:
        left, right = left + self.size, right + self.size
        result = 0
        while left <= right:
            if left % 2 == 1:
                result = self._merge(result, self.tree[left])
                left += 1
            if right % 2 == 0:
                result = self._merge(result, self.tree[right])
                right -= 1
            left, right = left // 2, right // 2
        return result


tree = SegmentTree([5, 2, 6, 1, 3, 4])
print(tree.tree)
