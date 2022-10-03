from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # RECURSIVE
        #
        # if not root:
        #     return True
        #
        # def isSym(left: TreeNode, right: TreeNode) -> bool:
        #     if left and right and left.val == right.val:
        #         return isSym(left.left, right.right) and isSym(left.right, right.left)
        #     return left == right
        #
        # return isSym(root.left, root.right)

        # ITERATIVE

        if not root:
            return True
        stack = [(root.left, root.right)]
        while stack:
            left, right = stack.pop()
            if not left and not right:
                continue
            if not left or not right or left.val != right.val:
                return False
            stack.append((left.left, right.right))
            stack.append((left.right, right.left))
        return True
