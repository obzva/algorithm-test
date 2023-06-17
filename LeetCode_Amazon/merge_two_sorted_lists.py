# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        head = ListNode()
        node = head
        while list1 or list2:
            if not list1:
                node.next = list2
                return head.next
            elif not list2:
                node.next = list1
                return head.next
            if list1.val < list2.val:
                node.next = ListNode(list1.val)
                list1, node = list1.next, node.next
            else:
                node.next = ListNode(list2.val)
                list2, node = list2.next, node.next
