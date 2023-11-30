# My solution - BFS with two queue

# Time complexity: O(N), for every node
# Space compexity: O(logN), for leaf level queue size

from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        current_level = deque([root])
        next_level = deque()
        answer = []
        while current_level:
            node = current_level.popleft()
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
            if not current_level:
                answer.append(node.val)
                current_level, next_level = next_level, current_level
        return answer
