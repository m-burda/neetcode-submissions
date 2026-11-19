# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # reach half of the list using fast and slow pointers
        # reverse one half of the list
        # merge two lists

        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        node2 = slow.next
        slow.next = None
        while node2:
            temp = node2.next
            node2.next = prev
            prev = node2
            node2 = temp

        node1 = head
        while node1 and prev:
            temp = node1.next
            node1.next = prev
            node1 = prev
            prev = temp

        
