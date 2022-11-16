import collections


class TreeNode:
    def __init__(self, x: int = None):
        self.val = x
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.ROOT = None

    def _get_bal(self, node: TreeNode) -> int:
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def _get_height(self, node: TreeNode) -> int:
        if not node:
            return 0
        return node.height

    def _r_rotate(self, node: TreeNode):
        y = node
        x = node.left
        beta = x.right
        x.right = y
        y.left = beta
        x.height = max(self._get_height(x.left), self._get_height(x.right)) + 1
        y.height = max(self._get_height(y.left), self._get_height(y.right)) + 1
        return x

    def _l_rotate(self, node: TreeNode):
        x = node
        y = node.right
        beta = y.left
        y.left = x
        x.right = beta
        x.height = max(self._get_height(x.left), self._get_height(x.right)) + 1
        y.height = max(self._get_height(y.left), self._get_height(y.right)) + 1
        return y

    def _insert(self, node: TreeNode, x: int):
        if not node:
            return TreeNode(x)
        elif node.val < x:
            node.right = self._insert(node.right, x)
        else:
            node.left = self._insert(node.left, x)

        node.height = max(self._get_height(node.left), self._get_height(node.right)) + 1

        b_factor = self._get_bal(node)

        if b_factor > 1:
            if self._get_bal(node.left) >= 0:
                return self._r_rotate(node)
            else:
                node.left = self._l_rotate(node.left)
                return self._r_rotate(node)
        if b_factor < -1:
            if self._get_bal(node.right) <= 0:
                return self._l_rotate(node)
            else:
                node.right = self._l_rotate(node.right)
                return self._r_rotate(node)
        return node

    def insert(self, x: int):
        self.ROOT = self._insert(self.ROOT, x)

    def show(self):
        queue = collections.deque()
        queue.append(self.ROOT)
        level = 0
        while queue:
            level += 1
            iter_no = len(queue)
            out = []
            for _ in range(iter_no):
                popped = queue.popleft()
                if popped:
                    out.append(popped.val)
                    queue.append(popped.left)
                    queue.append(popped.right)
                else:
                    out.append(None)
            print('----level%d----' % level)
            print(out)


avl = AVLTree()

print(avl.ROOT)

for i in [1, 3, 4, 5, 2, 7, 9]:
    avl.insert(i)

avl.show()
