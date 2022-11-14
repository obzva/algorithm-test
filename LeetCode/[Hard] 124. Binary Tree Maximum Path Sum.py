from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # MY SOLUTION

        # ans = root.val
        #
        # def rec(node: Optional[TreeNode]):
        #     if not node:
        #         return None
        #
        #     n = node.val
        #     l = rec(node.left)
        #     r = rec(node.right)
        #
        #     up = [n] if n > 0 else []
        #     tmp = [n]
        #     if l:
        #         tmp.extend([n, n + l])
        #         if n + l > 0:
        #             up.append(n + l)
        #     if r:
        #         tmp.extend([n, n + r])
        #         if n + r > 0:
        #             up.append(n + r)
        #     if l and r:
        #         tmp.append(n + l + r)
        #     nonlocal ans
        #     ans = max(ans, max(tmp))
        #
        #     return max(up) if up else None
        #
        # rec(root)
        # return ans

        # REFACTORING OF MY SOLUTION

        ans = root.val

        def get_max_gain(node: Optional[TreeNode]):
            if not node:
                return 0
            left_gain = max(get_max_gain(node.left), 0)
            right_gain = max(get_max_gain(node.right), 0)
            current_max_gain = node.val + left_gain + right_gain
            nonlocal ans
            ans = max(ans, current_max_gain)
            return node.val + max(left_gain, right_gain)

        get_max_gain(root)
        return ans

