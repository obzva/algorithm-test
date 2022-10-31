from typing import *


class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.count = 0
        self.idx = 0
        self.items = list()
        for item_list in vec:
            for item in item_list:
                self.items.append(item)
                self.count += 1

    def next(self) -> int:
        next_item = self.items[self.idx]
        self.idx += 1
        return next_item

    def hasNext(self) -> bool:
        if self.idx < self.count:
            return True
        else:
            return False

# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()
