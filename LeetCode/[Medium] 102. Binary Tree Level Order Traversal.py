from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # MY SOLUTION
        # ans = []
        # queue = collections.deque()
        # queue.append(root)
        # while queue:
        #     level_node_count = len(queue)
        #     tmp = []
        #     while level_node_count:
        #         node = queue.popleft()
        #         level_node_count -= 1
        #         if node:
        #             tmp.append(node.val)
        #             queue.append(node.left)
        #             queue.append(node.right)
        #     if tmp:
        #         ans.append(tmp)
        # return ans

        # MY SOLUTION - REVISE
        # if not root:
        #     return []
        # ans = []
        # level_nodes = [root]
        # while level_nodes:
        #     ans.append([node.val for node in level_nodes])
        #     next_level_nodes = []
        #     for node in level_nodes:
        #         if node.left:
        #             next_level_nodes.append(node.left)
        #         if node.right:
        #             next_level_nodes.append(node.right)
        #     level_nodes = next_level_nodes
        # return ans

        # RECURSIVE
        if not root:
            return []

        levels = []

        def recursive(node, level):
            if len(levels) == level:
                levels.append([])
            levels[level].append(node.val)
            if node.left:
                recursive(node.left, level + 1)
            if node.right:
                recursive(node.right, level + 1)

        recursive(root, 0)
        return levels
