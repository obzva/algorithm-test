# My solution

# Time complexity: O(N), we call dfs for every node
# Space complexity: O(N), for recursion call stack


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def dfs(node):
            tail = node
            if node:
                L, L_tail = dfs(node.left)
                R, R_tail = dfs(node.right)
                node.left, node.right = None, None
                if L:
                    node.right = L
                    tail = L_tail
                if R:
                    tail.right = R
                    tail = R_tail
            return node, tail

        dfs(root)


# Similar to my solution, but it returns just its tail

# Time complexity: O(N), we call dfs for every node
# Space complexity: O(N), for recursion call stack


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def dfs(node):
            if not node:
                return None

            if not node.left and not node.right:
                return node

            left_tail = dfs(node.left)
            right_tail = dfs(node.right)

            if left_tail:
                left_tail.right = node.right
                node.right = node.left
                node.left = None

            return right_tail if right_tail else left_tail

        dfs(root)


# Iterative one

# Time Complexity: O(N) for every node
# Space Complexity: O(N) occupied by stack


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None

        stack = []
        START, END = 1, 0
        tail = None

        stack.append((root, START))

        while stack:
            node, state = stack.pop()

            if not node.left and not node.right:
                tail = node
                continue

            if state == START:
                if node.left:
                    stack.append((node, END))
                    stack.append((node.left, START))
                elif node.right:
                    stack.append((node.right, START))
            else:
                right_node = node.right
                if tail:
                    tail.right = node.right
                    node.right = node.left
                    node.left = None
                if right_node:
                    stack.append((right_node, START))


# Using Morris Traversal

# Time Complexity: O(N), for every node
# Space Complexity: const, no additional space used


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None

        node = root
        while node:
            if node.left:
                tail = node.left
                while tail.right:
                    tail = tail.right

                node.left, node.right, tail.right = None, node.left, node.right

            node = node.right
