class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next


class Stack:
    def __init__(self):
        self.last = None

    def push(self, item):
        self.last = Node(item, self.last)

    def pop(self):
        item = self.last
        self.last = self.last.next
        return item


stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

print(stack.pop().item)
print(stack.pop().item)
print(stack.pop().item)
