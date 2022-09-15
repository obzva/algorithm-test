from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


head = ListNode(1)
p = head
p.next = ListNode(2)
p = p.next
p.next = ListNode(3)
p = p.next
p.next = ListNode(4)
p = p.next
p.next = ListNode(5)


def print_head(head: ListNode) -> None:
    if head:
        print(head.val, end='->')
        if head.next:
            print(head.next.val, end='->')
            if head.next.next:
                print(head.next.next.val, end='->')
                if head.next.next.next:
                    print(head.next.next.next.val, end='->')
                    if head.next.next.next.next:
                        print(head.next.next.next.next.val)
                    else:
                        print('None')
                else:
                    print('None')
            else:
                print('None')
        else:
            print('None')
    else:
        print('None')


def odd_even_list(head: Optional[ListNode]) -> Optional[ListNode]:
    # 예외 처리
    if not head:
        return None

    odd = head
    even = head.next
    even_head = head.next

    print('-----before loop-----')
    print(head.val, end='->')
    print(head.next.val, end='->')
    print(head.next.next.val, end='->')
    print(head.next.next.next.val, end='->')
    print(head.next.next.next.next.val)

    i = 0
    # 반복하면서 홀짝 노드 처리
    while even and even.next:
        i += 1
        print(f'-----in loop {i}-----')

        odd.next = odd.next.next
        print('~~~process I~~~')
        print('-head')
        print_head(head)
        print('-odd')
        print_head(odd)
        print('-even')
        print_head(even)
        print('-even_head')
        print_head(even_head)

        odd = odd.next
        print('~~~process II~~~')
        print('-head')
        print_head(head)
        print('-odd')
        print_head(odd)
        print('-even')
        print_head(even)
        print('-even_head')
        print_head(even_head)

        even.next = even.next.next
        print('~~~process III~~~')
        print('-head')
        print_head(head)
        print('-odd')
        print_head(odd)
        print('-even')
        print_head(even)
        print('-even_head')
        print_head(even_head)

        even = even.next
        print('~~~process IV~~~')
        print('-head')
        print_head(head)
        print('-odd')
        print_head(odd)
        print('-even')
        print_head(even)
        print('-even_head')
        print_head(even_head)

    # 홀수 노드의 마지막을 짝수 헤드로 연결
    odd.next = even_head
    print('$$$$$$$$$$RESULT$$$$$$$$$$$$$')
    print_head(head)
    return head


func_p = odd_even_list(head)
