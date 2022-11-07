# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

# RECURSIVE FLATTENER

# class NestedIterator:
#     def __init__(self, nestedList: [NestedInteger]):
#         def flatten(items):
#             for item in items:
#                 if item.isInteger():
#                     self.list.append(item.getInteger())
#                 else:
#                     flatten(item.getList())
#         self.list = []
#         self.idx = -1
#         flatten(nestedList)

#     def next(self) -> int:
#         self.idx += 1
#         return self.list[self.idx]


#     def hasNext(self) -> bool:
#         if self.idx >= len(self.list) - 1:
#             return False
#         return True

# USING STACK

# class NestedIterator:
#     def __init__(self, nestedList: [NestedInteger]):
#         self.stack = nestedList[::-1]
#
#     def make_top_an_integer(self):
#         while self.stack and not self.stack[-1].isInteger():
#             self.stack.extend(self.stack.pop().getList()[::-1])
#
#     def next(self) -> int:
#         self.make_top_an_integer()
#         return self.stack.pop().getInteger()
#
#     def hasNext(self) -> bool:
#         self.make_top_an_integer()
#         return len(self.stack) > 0

# USING TWO STACKS

# class NestedIterator:
#     def __init__(self, nestedList: [NestedInteger]):
#         self.stack = [[nestedList, 0]]
#
#     def _make_top_an_integer(self):
#         while self.stack:
#             curr_list = self.stack[-1][0]
#             curr_idx = self.stack[-1][1]
#
#             if len(curr_list) == curr_idx:
#                 self.stack.pop()
#                 continue
#
#             if curr_list[curr_idx].isInteger():
#                 break
#
#             new_list = curr_list[curr_idx].getList()
#             self.stack[-1][1] += 1
#             self.stack.append([new_list, 0])
#
#     def next(self) -> int:
#         self._make_top_an_integer()
#         curr_list = self.stack[-1][0]
#         curr_idx = self.stack[-1][1]
#         self.stack[-1][1] += 1
#         return curr_list[curr_idx].getInteger()
#
#     def hasNext(self) -> bool:
#         self._make_top_an_integer()
#         return len(self.stack) > 0

# USING GENERATOR

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self._peeked = None
        self._generator = self._int_generator(nestedList)

    def _int_generator(self, nested_list) -> "Generator[int]":
        for nested in nested_list:
            if nested.isInteger():
                yield nested.getInteger()
            else:
                yield from self._int_generator(nested.getList())

    def next(self) -> int:
        if not self.hasNext():
            return None
        next_integer, self._peeked = self._peeked, None
        return next_integer
    
    def hasNext(self) -> bool:
        if self._peeked is not None:
            return True
        try:
            self._peeked = next(self._generator)
            return True
        except:
            return False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
