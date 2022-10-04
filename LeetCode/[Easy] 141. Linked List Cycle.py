from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # MY SOLUTION
        #
        # stack = []
        # while head:
        #     if head in stack:
        #         return True
        #     stack.append(head)
        #     head = head.next
        # return False

        # RUNNER METHOD

        try:
            slow, fast = head, head.next
            while slow != fast:
                slow, fast = slow.next, fast.next.next
            return True
        except AttributeError:
            return False
