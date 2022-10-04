from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # CONCATENATE
        last = headA
        while last.next:
            last = last.next
        last.next = headB
        # FIND LOOP
        slow, fast = headA, headA
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                fast = headA
                while slow != fast:
                    slow, fast = slow.next, fast.next
                last.next = None
                return slow
        # NO LOOP FOUND
        last.next = None
        return None
