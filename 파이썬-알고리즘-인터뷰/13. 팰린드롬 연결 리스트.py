from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        if not head:
            return False

        q = []
        while head:
            q.append(head.val)
            head = head.next

        if q == q[::-1]:
            return True
        else:
            return False
