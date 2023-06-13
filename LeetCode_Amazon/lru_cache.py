class ListNode:
    
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.dict = dict()
        self.head = ListNode(None, None)
        self.tail = ListNode(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        node = self.dict[key]
        self._remove(node)
        self._add(node)
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self._remove(self.dict[key])
            self.length -= 1
        node = ListNode(key, value)
        self._add(node)
        self.dict[key] = node
        self.length += 1
        if self.length > self.capacity:
            node = self.head.next
            self._remove(node)
            del self.dict[node.key]
            self.length -= 1
        
        
    def _add(self, node: ListNode) -> None:
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.prev = p
        node.next = self.tail
        
    def _remove(self, node: ListNode) -> None:
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)