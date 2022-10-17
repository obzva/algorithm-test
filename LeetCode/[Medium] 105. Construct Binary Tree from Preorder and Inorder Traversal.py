from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # '파이썬 알고리즘 인터뷰'
        # if inorder:
        #     idx = inorder.index(preorder.pop(0))
        #     node = TreeNode(inorder[idx])
        #     node.left = self.buildTree(preorder, inorder[:idx])
        #     node.right = self.buildTree(preorder, inorder[idx + 1:])
        #     return node

        # LEETCODE SOLUTION
        preorder_idx = 0
        inorder_idx_map = {}
        for i, value in enumerate(inorder):
            inorder_idx_map[value] = i

        def recursive(left, right):
            nonlocal preorder_idx
            if left > right:
                return None
            node_val = preorder[preorder_idx]
            node = TreeNode(node_val)
            preorder_idx += 1
            node.left = recursive(left, inorder_idx_map[node_val] - 1)
            node.right = recursive(inorder_idx_map[node_val] + 1, right)
            return node

        return recursive(0, len(preorder) - 1)
