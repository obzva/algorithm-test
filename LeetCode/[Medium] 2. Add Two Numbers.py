from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # MY SOLUTION
        #
        # ans = ListNode(None)
        # head = ans
        # carry = 0
        # while l1 or l2 or carry:
        #     if l1 and l2:
        #         tmp_sum = l1.val + l2.val + carry
        #     elif l1 and not l2:
        #         tmp_sum = l1.val + carry
        #     elif not l1 and l2:
        #         tmp_sum = l2.val + carry
        #     else:
        #         tmp_sum = carry
        #     if carry:
        #         carry = 0
        #     if tmp_sum > 9:
        #         tmp_sum %= 10
        #         carry = 1
        #     head.next = ListNode(tmp_sum)
        #     head = head.next
        #     if l1:
        #         l1 = l1.next
        #     if l2:
        #         l2 = l2.next
        # return ans.next

        # BETTER ONE

        ans = head = ListNode(None)
        carry = 0
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, val = divmod(v1 + v2 + carry, 10)
            head.next = ListNode(val)
            head = head.next
        return ans.next
