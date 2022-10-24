from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # MERGE SORT
        if not (head and head.next):
            return head

        def merge_sort(l1: ListNode, l2: ListNode) -> ListNode:
            if l1.val > l2.val:
                merge_sort(l2, l1)
            l1.next = l2
            return l1

        half = None
        slow = fast = head
        while fast and fast.next:
            half, slow, fast = slow, slow.next, fast.next.next
        half.next = None

        l1 = self.sortList(head)
        l2 = self.sortList(slow)

        return merge_sort(l1, l2)
