from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = []
        current_level = [root]
        i = True  # False for 'left -> right', True for reverse
        while current_level:
            next_level = []
            ans.append([node.val for node in current_level] if i else [node.val for node in current_level][::-1])
            for node in current_level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            current_level = next_level
            i = not i
        return ans
