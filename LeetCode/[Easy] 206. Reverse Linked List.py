from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # MY SOLUTION
        #
        # if not head:
        #     return head
        # root = ListNode(None)
        # root.next = head
        # p = head
        # q = r = p.next
        # while q:
        #     r = q.next
        #     p.next = None
        #     q.next = root.next
        #     p.next = r
        #     root.next = q
        #     q = r
        # return root.next

        # BETTER SOLUTION
        #
        # ITERATIVE
        #
        # prev = None
        # curr = head
        # while curr:
        #     post = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = post
        # return prev

        # RECURSIVE

        def reverse_link(curr, prev=None):
            if not curr:
                return prev
            post = curr.next
            curr.next = prev
            return reverse_link(post, curr)

        return reverse_link(head)
