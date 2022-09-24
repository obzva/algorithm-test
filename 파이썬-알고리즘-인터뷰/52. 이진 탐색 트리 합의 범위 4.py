"""
loop BFS
"""
import collections
from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        result = 0
        queue = collections.deque([root])
        while queue:
            node = queue.popleft()
            if node:
                if low <= node.val <= high:
                    result += node.val
                    queue.append(node.left)
                    queue.append(node.right)
                if node.val < low:
                    queue.append(node.right)
                if node.val > high:
                    queue.append(node.left)
        return result
