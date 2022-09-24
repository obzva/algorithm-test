"""
loop
"""

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
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                if low <= node.val <= high:
                    result += node.val
                    stack.append(node.left)
                    stack.append(node.right)
                if node.val < low:
                    stack.append(node.right)
                if node.val > high:
                    stack.append(node.left)
        return result
