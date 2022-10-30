from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # ITERATIVE SOLUTION USING STACK
        # stack = []
        # nums = []
        # while root or stack:
        #     while root:
        #         stack.append(root)
        #         root = root.left
        #     root = stack.pop()
        #     if len(nums) == k - 1:
        #         return root.val
        #     nums.append(root.val)
        #     root = root.right

        # RECURSIVE SOLUTION
        answer = 0

        def dfs(node: TreeNode):
            if not node:
                return
            dfs(node.left)
            nonlocal k
            k -= 1
            if k == 0:
                nonlocal answer
                answer = node.val
                return
            dfs(node.right)

        dfs(root)
        return answer
