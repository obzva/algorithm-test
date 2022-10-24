class DoubleListNode:
    def __init__(self):
        self.key = 0
        self.val = 0
        self.prev = self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.hashmap = {}
        self.head = DoubleListNode()
        self.tail = DoubleListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    # SUPPORT METHODS
    def _add_node(self, node: DoubleListNode) -> None:
        node.prev = self.head
        node.next = self.head.next
        # 순서 중요함.. 
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node: DoubleListNode) -> None:
        pre = node.prev
        post = node.next
        pre.next = post
        post.prev = pre

    def _move_to_head(self, node: DoubleListNode) -> None:
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self) -> DoubleListNode:
        popped_node = self.tail.prev
        self._remove_node(popped_node)
        return popped_node

    def get(self, key: int) -> int:
        node = self.hashmap.get(key, None)
        if not node:
            return -1
        self._move_to_head(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        node = self.hashmap.get(key, None)
        if node:
            node.val = value
            self._move_to_head(node)
        else:
            new_node = DoubleListNode()
            new_node.key = key
            new_node.val = value

            self.hashmap[key] = new_node
            self._add_node(new_node)
            self.size += 1

            if self.size > self.capacity:
                popped_node = self._pop_tail()
                del self.hashmap[popped_node.key]
                self.size -= 1
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
