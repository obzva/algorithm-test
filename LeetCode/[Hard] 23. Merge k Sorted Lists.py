import heapq
from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i, lst in enumerate(lists):
            if lst:
                heapq.heappush(heap, (lst.val, i))
        head = ListNode()
        node = head
        while heap:
            value, idx = heapq.heappop(heap)
            lists[idx] = lists[idx].next
            node.next = ListNode(value)
            node = node.next
            if lists[idx]:
                heapq.heappush(heap, (lists[idx].val, idx))
        return head.next
