"""
to list
"""

import functools
from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 연결 리스트 뒤집기
    def reverse_list(self, head: ListNode) -> ListNode:
        node, prev = head, None
        while node:
            next, node.next = node.next, prev
            node, prev = next, node
        return prev

    def to_list(self, node: ListNode) -> List:
        list: List = []
        while node:
            list.append(node.val)
            node = node.next
        return list

    def to_reversed_linked_list(self, result: str) -> ListNode:
        prev: ListNode = None
        for r in result:
            node = ListNode(r)
            node.next = prev
            prev = node
        return node

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a = self.to_list(self.reverse_list(l1))
        b = self.to_list(self.reverse_list(l2))

        # result_str = str(int(''.join(str(e) for e in a)) + int(''.join(str(e) for e in b)))
        # result_str = str(int(''.join(map(str, a))) + int(''.join(map(str, b))))
        result_str = str(
            functools.reduce(lambda x, y: 10 * x + y, a, 0) + functools.reduce(lambda x, y: 10 * x + y, b, 0))

        return self.to_reversed_linked_list(result_str)
