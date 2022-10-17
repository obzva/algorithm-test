from typing import *


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # MY SOLUTION
        # if not root:
        #     return root
        # level = collections.deque()
        # level.append(root)
        # while level:
        #     next_level = collections.deque()
        #     for node in level:
        #         if node.left:
        #             next_level.append(node.left)
        #         if node.right:
        #             next_level.append(node.right)
        #     level = next_level
        #     for i in range(len(level) - 1):
        #         level[i].next = level[i + 1]
        # return root

        # SPATIAL REVISE
        # if not root:
        #     return root
        # queue = collections.deque([root])
        # while queue:
        #     level_size = len(queue)
        #     for i in range(level_size):
        #         node = queue.popleft()
        #         if i < level_size - 1:
        #             node.next = queue[0]
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
        # return root

        # NOT USING QUEUE
        if not root:
            return root
        leftmost = root
        while leftmost.left:
            head = leftmost
            while head:
                head.left.next = head.right
                if head.next:
                    head.right.next = head.next.left
                head = head.next
            leftmost = leftmost.left
        return root
