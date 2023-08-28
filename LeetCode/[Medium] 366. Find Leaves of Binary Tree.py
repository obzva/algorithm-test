# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
#         def is_leaf(node, pocket):
#             if not node.left and not node.right:
#                 pocket.append(node.val)
#                 return True
#             if node.left:
#                 if is_leaf(node.left, pocket):
#                     node.left = None
#             if node.right:
#                 if is_leaf(node.right, pocket):
#                     node.right = None
#             return False

#         res = []
#         while root:
#             tmp = []
#             is_last = is_leaf(root, tmp)
#             res.append(tmp)
#             if is_last:
#                 break

#         return res


class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        heights = {}

        def save(val, height):
            if height not in heights:
                heights[height] = []
            heights[height].append(val)

        def dfs(node):
            if not node:
                return -1
            height_left = dfs(node.left)
            height_right = dfs(node.right)
            height = max(height_left, height_right) + 1
            save(node.val, height)
            return height

        dfs(root)
        return list(heights.values())
