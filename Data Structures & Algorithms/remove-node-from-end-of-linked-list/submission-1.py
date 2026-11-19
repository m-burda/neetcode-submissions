# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0

        node = head
        while node:
            size += 1
            node = node.next

        k = 0
        dummy = ListNode(next=head)
        node = dummy
        while k < size - n:
            node = node.next
            k += 1

        node.next = node.next.next

        return dummy.next