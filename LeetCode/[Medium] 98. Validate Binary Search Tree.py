import sys
from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    min_val = -sys.maxsize

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # RECURSIVE
        # def validate(node, low, high):
        #     if not node:
        #         return True
        #     if node.val <= low or node.val >= high:
        #         return False
        #     return validate(node.left, low, node.val) and validate(node.right, node.val, high)
        #
        # return validate(root, -sys.maxsize, sys.maxsize)

        # ITERATIVE
        # if not root:
        #     return True
        # stack = [(root, -sys.maxsize, sys.maxsize)]
        # while stack:
        #     node, min_val, max_val = stack.pop()
        #     if not node:
        #         continue
        #     if node.val <= min_val or max_val <= node.val:
        #         return False
        #     stack.append((node.left, min_val, node.val))
        #     stack.append((node.right, node.val, max_val))
        # return True

        # RECURSIVE - IN ORDER
        # def in_order(node):
        #     if not node:
        #         return True
        #     if not in_order(node.left):
        #         return False
        #     if node.val <= self.min_val:
        #         return False
        #     self.min_val = node.val
        #     return in_order(node.right)
        #
        # return in_order(root)

        # ITERATIVE - IN ORDER
        stack, prev = [], -sys.maxsize
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= prev:
                return False
            prev = root.val
            root = root.right
        return True
