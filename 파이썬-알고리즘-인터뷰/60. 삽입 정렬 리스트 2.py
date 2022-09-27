"""
Insertion Sort - revised
"""

from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 추가된 조건문에서 cur.val 비교시 오류 발생하므로, ListNode(None) -> ListNode(0)으로 수정
        cur = parent = ListNode(0)
        while head:
            while cur.next and cur.next.val < head.val:
                cur = cur.next
            cur.next, head.next, head = head, cur.next, head.next
            # 필요할 때만 cur 포인터를 초기화
            if head and cur.val > head.val:
                cur = parent
        # 마지막엔 cur 포인터가 초기화되어 있지 않을 수도 있으니까 parent.next를 리턴
        return parent.next
