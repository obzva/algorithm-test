# class MedianFinder:
#
#     def __init__(self):
#         self.nums = []
#
#     def addNum(self, num: int) -> None:
#         # IMPLEMENTING BINARY SEARCH
#
#         if not self.nums:
#             self.nums.append(num)
#         else:
#             left, right = 0, len(self.nums) - 1
#             while left < right:
#                 mid = (left + right) // 2
#                 if self.nums[mid] < num:
#                     left = mid + 1
#                 else:
#                     right = mid
#             if self.nums[left] < num:
#                 self.nums.insert(left + 1, num)
#             else:
#                 self.nums.insert(left, num)
#
#     def findMedian(self) -> float:
#         n = len(self.nums)
#         if n % 2 == 0:
#             return (self.nums[n // 2] + self.nums[n // 2 - 1]) / 2
#         else:
#             return float(self.nums[n // 2])


# import heapq
#
#
# # USING TWO HEAPS
#
# class MedianFinder:
#
#     def __init__(self):
#         self.hi = []
#         self.lo = []
#
#     def addNum(self, num: int) -> None:
#         heapq.heappush(self.lo, -num)
#         heapq.heappush(self.hi, -heapq.heappop(self.lo))
#         if len(self.hi) > len(self.lo):
#             heapq.heappush(self.lo, -heapq.heappop(self.hi))
#
#     def findMedian(self) -> float:
#         return (self.hi[0] - self.lo[0]) / 2 if len(self.lo) == len(self.hi) else float(-self.lo[0])
#
# # Your MedianFinder object will be instantiated and called as such:
# # obj = MedianFinder()
# # obj.addNum(num)
# param_2 = obj.findMedian()

class TreeNode:
    def __init__(self, x: int = None):
        self.val = x
        self.left = None
        self.right = None
        self.height = 1
        self.l_size = 0
        self.r_size = 0


class AVLTree:
    def __init__(self):
        self.ROOT = None

    def _get_left_size(self, node: TreeNode) -> int:
        if not node.left:
            return 0
        return self._get_left_size(node.left) + self._get_right_size(node.left) + 1

    def _get_right_size(self, node: TreeNode) -> int:
        if not node.right:
            return 0
        return self._get_left_size(node.right) + self._get_right_size(node.right) + 1

    def _get_bal(self, node: TreeNode) -> int:
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def _get_height(self, node: TreeNode) -> int:
        if not node:
            return 0
        return node.height

    def _r_rotate(self, node: TreeNode):
        y = node
        x = node.left
        beta = x.right
        x.right = y
        y.left = beta
        x.height = max(self._get_height(x.left), self._get_height(x.right)) + 1
        y.height = max(self._get_height(y.left), self._get_height(y.right)) + 1
        x.l_size = self._get_left_size(x)
        x.r_size = self._get_right_size(x)
        y.l_size = self._get_left_size(y)
        y.r_size = self._get_right_size(y)
        return x

    def _l_rotate(self, node: TreeNode):
        x = node
        y = node.right
        beta = y.left
        y.left = x
        x.right = beta
        x.height = max(self._get_height(x.left), self._get_height(x.right)) + 1
        y.height = max(self._get_height(y.left), self._get_height(y.right)) + 1
        x.l_size = self._get_left_size(x)
        x.r_size = self._get_right_size(x)
        y.l_size = self._get_left_size(y)
        y.r_size = self._get_right_size(y)
        return y

    def _insert(self, node: TreeNode, x: int):
        if not node:
            return TreeNode(x)
        elif node.val < x:
            node.right = self._insert(node.right, x)
        else:
            node.left = self._insert(node.left, x)

        node.height = max(self._get_height(node.left), self._get_height(node.right)) + 1
        node.l_size = self._get_left_size(node)
        node.r_size = self._get_right_size(node)

        b_factor = self._get_bal(node)

        if b_factor > 1:
            if self._get_bal(node.left) >= 0:
                return self._r_rotate(node)
            else:
                node.left = self._l_rotate(node.left)
                return self._r_rotate(node)
        if b_factor < -1:
            if self._get_bal(node.right) <= 0:
                return self._l_rotate(node)
            else:
                node.right = self._r_rotate(node.right)
                return self._l_rotate(node)
        return node

    def insert(self, x: int):
        self.ROOT = self._insert(self.ROOT, x)

    def select_median(self, node: TreeNode, k: int):
        left_size = node.l_size
        if left_size >= k:
            return self.select_median(node.left, k)
        elif k == left_size + 1:
            return node.val
        else:
            return self.select_median(node.right, k - left_size - 1)


class MedianFinder:

    def __init__(self):
        self.avl = AVLTree()
        self.count = 0

    def addNum(self, num: int) -> None:
        self.avl.insert(num)
        self.count += 1

    def findMedian(self) -> float:
        if self.count % 2 == 0:
            return (self.avl.select_median(self.avl.ROOT, self.count // 2) + self.avl.select_median(self.avl.ROOT,
                                                                                                    self.count // 2 + 1)) / 2
        else:
            return float(self.avl.select_median(self.avl.ROOT, self.count // 2 + 1))

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
