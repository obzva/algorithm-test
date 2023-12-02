# My solution - iteration

# Time complexity: O(N), the number of iteration is less or equal than N
# Space complexity: O(1), it uses constant number of pointers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def count(self, root: Optional[ListNode]) -> int:
        res = 0
        while root:
            res += 1
            root = root.next
        return res

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = self.count(head)

        repeat = n // k

        root = ListNode()

        root.next = head

        tmp_head = root
        node = head
        for _i in range(repeat):
            for _j in range(k - 1):
                next_node = node.next
                next_next_node = node.next.next

                node.next = next_next_node
                next_node.next = tmp_head.next
                tmp_head.next = next_node

            tmp_head = node
            node = tmp_head.next

        return root.next
