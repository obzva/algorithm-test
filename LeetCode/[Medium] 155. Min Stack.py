# MY SOLUTION
# class DoubleLinkedNode:
#     def __init__(self, value: int = None):
#         self.prev = None
#         self.next = None
#         self.val = value
#
#
# class MinStack:
#
#     def __init__(self):
#         self.head = DoubleLinkedNode()
#         self.tail = DoubleLinkedNode()
#         self.head.next = self.tail
#         self.tail.prev = self.head
#         self.hashmap = {}
#
#     def push(self, val: int) -> None:
#         new_node = DoubleLinkedNode(val)
#         new_node.prev = self.tail.prev
#         new_node.next = self.tail
#         self.tail.prev.next = new_node
#         self.tail.prev = new_node
#         self.hashmap[new_node] = val
#
#     def pop(self) -> None:
#         node = self.tail.prev
#         node.prev.next = node.next
#         node.next.prev = node.prev
#         del self.hashmap[node]
#
#     def top(self) -> int:
#         return self.tail.prev.val
#
#     def getMin(self) -> int:
#         return min(self.hashmap.values())


class Node:
    def __init__(self):
        self.val = None
        self.next = None
        self.min_val = None


class MinStack:
    def __init__(self):
        self.head = Node()

    def push(self, val: int):
        node = Node()
        node.val = val
        if self.head.next:
            self.head.next, node.next = node, self.head.next
            node.min_val = min(node.val, node.next.min_val)
        else:
            self.head.next = node
            node.min_val = node.val

    def pop(self):
        self.head.next = self.head.next.next

    def top(self) -> int:
        return self.head.next.val

    def getMin(self) -> int:
        return self.head.next.min_val
