from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not (head and head.next):
            return head

        p = head
        q = p.next

        while q and q.next:
            r = q.next

            q.next = r.next
            r.next = p.next
            p.next = r

            p = p.next
            q = q.next

        return head
