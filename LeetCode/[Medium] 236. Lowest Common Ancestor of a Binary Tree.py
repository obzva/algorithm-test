# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # DFS
        # answer = None
        #
        # def dfs(node: TreeNode) -> bool:
        #     if not node:
        #         return False
        #     left = dfs(node.left)
        #     right = dfs(node.right)
        #     mid = node == p or node == q
        #     if left + mid + right >= 2:
        #         nonlocal answer
        #         answer = node
        #     return mid or left or right
        #
        # dfs(root)
        # return answer

        # DFS2
        # if not root:
        #     return None
        # if root == p or root == q:
        #     return root
        # left = self.lowestCommonAncestor(root.left, p, q)
        # right = self.lowestCommonAncestor(root.right, p, q)
        # if not left:
        #     return right
        # if not right:
        #     return left
        # return root

        # DFS3
        if root in (None, p, q):
            return root
        left, right = (self.lowestCommonAncestor(kid, p, q) for kid in (root.left, root.right))
        return root if left and right else left or right
