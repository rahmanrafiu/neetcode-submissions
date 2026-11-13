# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        start = dummy
        pos = head

        for _ in range(n):
            pos = pos.next

        while pos:
            start = start.next
            pos = pos.next
        
        start.next = start.next.next
        return dummy.next
        