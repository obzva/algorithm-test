class MinStack:

    def __init__(self):
        self.stack = []
        
    def push(self, val: int) -> None:
        min_val = val if len(self.stack) == 0 else min(self.stack[-1][1], val)
        self.stack.append([val, min_val])
        

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
        
        
# linked list

# class ListNode:
    
#     def __init__(self, val):
#         self.val = val
#         self.prev = None
#         self.next= None
#         self.min = math.inf

# class MinStack:

#     def __init__(self):
#         self.head = ListNode(None)
#         self.tail = ListNode(None)
#         self.head.next = self.tail
#         self.tail.prev = self.head
        
#     def push(self, val: int) -> None:
#         node = ListNode(val)
#         node.next = self.head.next
#         node.prev = self.head
#         self.head.next.prev = node
#         self.head.next = node
#         node.min = min(node.val, node.next.min)
        

#     def pop(self) -> None:
#         node = self.head.next
#         self.head.next = node.next
#         node.next.prev = self.head
        

#     def top(self) -> int:
#         return self.head.next.val

#     def getMin(self) -> int:
#         return self.head.next.min
