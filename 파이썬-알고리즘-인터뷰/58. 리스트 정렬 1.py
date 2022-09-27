"""
Merge-sort
"""

from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def merge_two_lists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = self.merge_two_lists(l1.next, l2)
        return l1 or l2

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 예외 처리
        if not (head and head.next):
            return head

        # 중앙 분할
        half, slow, fast = None, head, head
        while fast and fast.next:
            half, slow, fast = slow, slow.next, fast.next.next
        half.next = None

        # 분할하여 재귀 호출 진행
        l1 = self.sortList(head)
        l2 = self.sortList(slow)

        return self.merge_two_lists(l1, l2)
