# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        queue = [root]
        while queue:
            print('--------')
            curr_q_length = len(queue)
            for i in range(curr_q_length):
                node = queue.pop(0)
                if node:
                    queue.append(node.left)
                    queue.append(node.right)
            queue_vals = list(map(lambda x: x.val if x else None, queue))
            if queue_vals != queue_vals[::-1]:
                return False
        return True