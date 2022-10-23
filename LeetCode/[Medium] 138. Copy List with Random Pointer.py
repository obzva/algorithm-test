# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    visited_hash = {}

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # GRAPH
        # REC
        # if not head:
        #     return None
        #
        # if head in self.visited_hash:
        #     return self.visited_hash[head]
        #
        # node = Node(head.val)
        # self.visited_hash[head] = node
        #
        # node.next = self.copyRandomList(head.next)
        # node.random = self.copyRandomList(head.random)
        #
        # return node

        # ITERATIVE
        if not head:
            return None

        def get_cloned_node(node: Node) -> Node:
            if not node:
                return None

            if node in self.visited_hash:
                return self.visited_hash[node]
            else:
                self.visited_hash[node] = Node(node.val)
                return self.visited_hash[node]

        old_node = head
        new_node = Node(old_node.val)
        self.visited_hash[old_node] = new_node

        while old_node:
            new_node.random, new_node.next = get_cloned_node(old_node.random), get_cloned_node(old_node.next)
            old_node, new_node = old_node.next, new_node.next

        return self.visited_hash[head]
