from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        apres = avant = head
        for _ in range(n):
            avant = avant.next
        if not avant:  # means that we need to delete second element from the head
            return head.next

        while avant.next:
            apres, avant = apres.next, avant.next
        apres.next = apres.next.next
        return head
