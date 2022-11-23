from typing import *


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        out = []

        def dfs(node: TreeNode):
            if not node:
                return out.append('#')
            out.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return '.'.join(out)

    def _make_tree(self, data: List[str]):
        if data[-1] == '#':
            data.pop()
            return None
        node = TreeNode(int(data.pop()))
        node.left = self._make_tree(data)
        node.right = self._make_tree(data)
        return node

    def deserialize(self, data: str):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data = data.split('.')[::-1]
        return self._make_tree(data)


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
f = TreeNode(6)

a.left, a.right = b, c
c.left, c.right = d, e
e.left = f

ser = Codec()
deser = Codec()
print(ser.serialize(a))
node = deser.deserialize(ser.serialize(a))
print(node.val)
